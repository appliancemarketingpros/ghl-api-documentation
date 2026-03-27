#!/usr/bin/env python3
"""
Convert GoHighLevel API OpenAPI JSON specs and markdown docs to organized markdown documentation.
This script is run by the GitHub Actions sync workflow to keep documentation current.
"""

import json
import os
import re
import shutil
import glob
import sys

# Paths are relative to the repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCE_DIR = os.path.join(REPO_ROOT, "_upstream")
OUTPUT_DIR = REPO_ROOT

# Mapping of JSON file names to human-readable titles
API_TITLES = {
    "agencies": "Agencies",
    "associations": "Associations",
    "blogs": "Blogs",
    "businesses": "Businesses",
    "calendars": "Calendars",
    "campaigns": "Campaigns",
    "companies": "Companies",
    "contacts": "Contacts",
    "conversations": "Conversations",
    "courses": "Courses",
    "custom-fields": "Custom Fields V2",
    "custom-menus": "Custom Menus",
    "email-isv": "LC Email",
    "emails": "Emails",
    "forms": "Forms",
    "funnels": "Funnels",
    "invoices": "Invoices",
    "links": "Trigger Links",
    "locations": "Sub-Accounts (Locations)",
    "marketplace": "Marketplace",
    "medias": "Media Library",
    "oauth": "OAuth 2.0",
    "objects": "Objects",
    "opportunities": "Opportunities",
    "payments": "Payments",
    "phone-system": "Phone System",
    "products": "Products",
    "proposals": "Proposals & Estimates",
    "saas-api": "SaaS API",
    "snapshots": "Snapshots",
    "social-media-posting": "Social Media Posting",
    "store": "Store",
    "surveys": "Surveys",
    "users": "Users",
    "voice-ai": "Voice AI",
    "workflows": "Workflows",
}


def resolve_ref(ref, spec):
    """Resolve a $ref pointer in the OpenAPI spec."""
    if not ref or not ref.startswith("#/"):
        return None
    parts = ref[2:].split("/")
    obj = spec
    for part in parts:
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(obj, dict) and part in obj:
            obj = obj[part]
        else:
            return None
    return obj


def resolve_schema(schema, spec, depth=0):
    """Recursively resolve a schema, following $ref pointers."""
    if depth > 10:
        return schema
    if schema is None:
        return {}
    if "$ref" in schema:
        resolved = resolve_ref(schema["$ref"], spec)
        if resolved:
            return resolve_schema(resolved, spec, depth + 1)
        return schema
    if "allOf" in schema:
        merged = {}
        merged_props = {}
        merged_required = []
        for sub in schema["allOf"]:
            resolved_sub = resolve_schema(sub, spec, depth + 1)
            if "properties" in resolved_sub:
                merged_props.update(resolved_sub["properties"])
            if "required" in resolved_sub:
                merged_required.extend(resolved_sub["required"])
            merged.update(resolved_sub)
        if merged_props:
            merged["properties"] = merged_props
        if merged_required:
            merged["required"] = list(set(merged_required))
        return merged
    if "oneOf" in schema:
        return schema
    if "anyOf" in schema:
        return schema
    return schema


def format_schema_type(schema, spec, depth=0):
    """Get a human-readable type string from a schema."""
    if not schema:
        return "any"
    schema = resolve_schema(schema, spec, depth)
    if "oneOf" in schema:
        types = []
        for s in schema["oneOf"]:
            types.append(format_schema_type(s, spec, depth + 1))
        return " | ".join(types)
    if "anyOf" in schema:
        types = []
        for s in schema["anyOf"]:
            types.append(format_schema_type(s, spec, depth + 1))
        return " | ".join(types)
    t = schema.get("type", "any")
    if t == "array":
        items = schema.get("items", {})
        item_type = format_schema_type(items, spec, depth + 1)
        return f"array of {item_type}"
    if t == "object":
        return "object"
    if "enum" in schema:
        enum_vals = ", ".join([f"`{v}`" for v in schema["enum"]])
        return f"{t} (enum: {enum_vals})"
    return t


def schema_to_properties_table(schema, spec, depth=0):
    """Convert a schema's properties to a markdown table."""
    if depth > 5:
        return ""
    schema = resolve_schema(schema, spec, depth)
    if not schema or "properties" not in schema:
        return ""

    required_fields = set(schema.get("required", []))
    props = schema["properties"]

    lines = []
    lines.append("| Property | Type | Required | Description |")
    lines.append("|----------|------|----------|-------------|")

    for prop_name, prop_schema in props.items():
        resolved_prop = resolve_schema(prop_schema, spec, depth + 1)
        prop_type = format_schema_type(resolved_prop, spec, depth + 1)
        is_required = "Yes" if prop_name in required_fields else "No"
        description = resolved_prop.get("description", "").replace("\n", " ").replace("|", "\\|")
        if len(description) > 200:
            description = description[:200] + "..."

        if "enum" in resolved_prop and "enum:" not in prop_type:
            enum_vals = ", ".join([f"`{v}`" for v in resolved_prop["enum"]])
            if description:
                description += f" Possible values: {enum_vals}"
            else:
                description = f"Possible values: {enum_vals}"

        if "default" in resolved_prop:
            description += f" Default: `{resolved_prop['default']}`"

        lines.append(f"| `{prop_name}` | {prop_type} | {is_required} | {description} |")

    return "\n".join(lines)


def format_example(example, indent=0):
    """Format an example value as JSON."""
    if example is None:
        return ""
    try:
        return json.dumps(example, indent=2)
    except (TypeError, ValueError):
        return str(example)


def generate_endpoint_markdown(path, method, operation, spec):
    """Generate markdown for a single API endpoint."""
    lines = []

    summary = operation.get("summary", "")
    description = operation.get("description", "")
    operation_id = operation.get("operationId", "")
    tags = operation.get("tags", [])
    deprecated = operation.get("deprecated", False)

    lines.append(f"### {method.upper()} `{path}`")
    lines.append("")

    if summary:
        lines.append(f"**{summary}**")
        lines.append("")

    if deprecated:
        lines.append("> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.")
        lines.append("")

    if description:
        desc = description.replace("<br/>", "\n").replace("<br>", "\n")
        desc = re.sub(r'<[^>]+>', '', desc)
        lines.append(desc)
        lines.append("")

    if operation_id:
        lines.append(f"**Operation ID:** `{operation_id}`")
        lines.append("")

    if tags:
        lines.append(f"**Tags:** {', '.join(tags)}")
        lines.append("")

    security = operation.get("security", [])
    if security:
        scopes = []
        for sec in security:
            for key, vals in sec.items():
                scopes.extend(vals)
        if scopes:
            lines.append(f"**Required Scopes:** {', '.join([f'`{s}`' for s in scopes])}")
            lines.append("")

    ext_docs = operation.get("externalDocs", {})
    if ext_docs and ext_docs.get("url"):
        lines.append(f"**External Documentation:** [{ext_docs.get('description', 'More info')}]({ext_docs['url']})")
        lines.append("")

    parameters = operation.get("parameters", [])
    non_version_params = [p for p in parameters if not (p.get("name") == "Version" and p.get("in") == "header")]
    version_params = [p for p in parameters if p.get("name") == "Version" and p.get("in") == "header"]

    if version_params:
        vp = version_params[0]
        version_val = vp.get("schema", {}).get("enum", [""])[0] if "schema" in vp else ""
        if version_val:
            lines.append(f"**API Version:** `{version_val}`")
            lines.append("")

    if non_version_params:
        lines.append("#### Parameters")
        lines.append("")
        lines.append("| Parameter | In | Type | Required | Description |")
        lines.append("|-----------|-----|------|----------|-------------|")

        for param in non_version_params:
            p_name = param.get("name", "")
            p_in = param.get("in", "")
            p_required = "Yes" if param.get("required", False) else "No"
            p_desc = param.get("description", "").replace("\n", " ").replace("|", "\\|")
            p_schema = param.get("schema", {})
            p_type = format_schema_type(p_schema, spec)

            if len(p_desc) > 200:
                p_desc = p_desc[:200] + "..."

            lines.append(f"| `{p_name}` | {p_in} | {p_type} | {p_required} | {p_desc} |")

        lines.append("")

    request_body = operation.get("requestBody", {})
    if request_body:
        lines.append("#### Request Body")
        lines.append("")
        rb_required = request_body.get("required", False)
        rb_desc = request_body.get("description", "")
        if rb_desc:
            lines.append(rb_desc)
            lines.append("")
        if rb_required:
            lines.append("**Required:** Yes")
            lines.append("")

        content = request_body.get("content", {})
        for content_type, content_schema in content.items():
            lines.append(f"**Content Type:** `{content_type}`")
            lines.append("")

            schema = content_schema.get("schema", {})
            resolved = resolve_schema(schema, spec)

            if resolved:
                table = schema_to_properties_table(resolved, spec)
                if table:
                    lines.append(table)
                    lines.append("")

                if "properties" in resolved:
                    for prop_name, prop_schema in resolved["properties"].items():
                        resolved_prop = resolve_schema(prop_schema, spec)
                        if resolved_prop.get("type") == "object" and "properties" in resolved_prop:
                            lines.append(f"**`{prop_name}` object properties:**")
                            lines.append("")
                            nested_table = schema_to_properties_table(resolved_prop, spec, depth=1)
                            if nested_table:
                                lines.append(nested_table)
                                lines.append("")
                        elif resolved_prop.get("type") == "array":
                            items = resolve_schema(resolved_prop.get("items", {}), spec)
                            if items and items.get("type") == "object" and "properties" in items:
                                lines.append(f"**`{prop_name}` array item properties:**")
                                lines.append("")
                                nested_table = schema_to_properties_table(items, spec, depth=1)
                                if nested_table:
                                    lines.append(nested_table)
                                    lines.append("")

            example = content_schema.get("example")
            if example:
                lines.append("**Example:**")
                lines.append("")
                lines.append("```json")
                lines.append(format_example(example))
                lines.append("```")
                lines.append("")

    responses = operation.get("responses", {})
    if responses:
        lines.append("#### Responses")
        lines.append("")

        for status_code, response in sorted(responses.items()):
            resp_desc = response.get("description", "")
            lines.append(f"**`{status_code}` - {resp_desc}**")
            lines.append("")

            resp_content = response.get("content", {})
            for content_type, content_schema in resp_content.items():
                schema = content_schema.get("schema", {})
                resolved = resolve_schema(schema, spec)

                if resolved and "properties" in resolved:
                    table = schema_to_properties_table(resolved, spec)
                    if table:
                        lines.append(table)
                        lines.append("")

                example = content_schema.get("example")
                if not example:
                    examples = content_schema.get("examples", {})
                    if examples:
                        for ex_name, ex_val in examples.items():
                            example = ex_val.get("value")
                            break

                if example:
                    lines.append("**Response Example:**")
                    lines.append("")
                    lines.append("```json")
                    lines.append(format_example(example))
                    lines.append("```")
                    lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def convert_openapi_to_markdown(json_path, api_name):
    """Convert an OpenAPI JSON spec file to markdown."""
    with open(json_path, "r") as f:
        spec = json.load(f)

    title = API_TITLES.get(api_name, api_name.replace("-", " ").title())

    lines = []
    lines.append(f"# {title} API")
    lines.append("")

    info = spec.get("info", {})
    if info:
        if info.get("description"):
            lines.append(info["description"])
            lines.append("")
        if info.get("version"):
            lines.append(f"**API Version:** {info['version']}")
            lines.append("")

    servers = spec.get("servers", [])
    if servers:
        lines.append("## Base URL")
        lines.append("")
        for server in servers:
            lines.append(f"- `{server.get('url', '')}`")
            if server.get("description"):
                lines.append(f"  {server['description']}")
        lines.append("")

    paths = spec.get("paths", {})
    tag_endpoints = {}
    untagged = []

    for path, methods in paths.items():
        for method, operation in methods.items():
            if method in ("get", "post", "put", "patch", "delete", "options", "head"):
                tags = operation.get("tags", [])
                if tags:
                    for tag in tags:
                        if tag not in tag_endpoints:
                            tag_endpoints[tag] = []
                        tag_endpoints[tag].append((path, method, operation))
                else:
                    untagged.append((path, method, operation))

    lines.append("## Table of Contents")
    lines.append("")
    for tag in tag_endpoints:
        anchor = tag.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "")
        lines.append(f"- [{tag}](#{anchor})")
    if untagged:
        lines.append("- [Other Endpoints](#other-endpoints)")
    lines.append("")

    for tag, endpoints in tag_endpoints.items():
        lines.append(f"## {tag}")
        lines.append("")
        for path, method, operation in endpoints:
            lines.append(generate_endpoint_markdown(path, method, operation, spec))

    if untagged:
        lines.append("## Other Endpoints")
        lines.append("")
        for path, method, operation in untagged:
            lines.append(generate_endpoint_markdown(path, method, operation, spec))

    components = spec.get("components", {})
    schemas = components.get("schemas", {})

    if schemas:
        lines.append("## Schemas")
        lines.append("")
        for schema_name, schema_def in sorted(schemas.items()):
            resolved = resolve_schema(schema_def, spec)
            lines.append(f"### {schema_name}")
            lines.append("")
            if resolved.get("description"):
                lines.append(resolved["description"])
                lines.append("")
            if resolved.get("type"):
                lines.append(f"**Type:** `{resolved['type']}`")
                lines.append("")
            if "enum" in resolved:
                lines.append("**Possible Values:**")
                lines.append("")
                for val in resolved["enum"]:
                    lines.append(f"- `{val}`")
                lines.append("")
            table = schema_to_properties_table(resolved, spec)
            if table:
                lines.append(table)
                lines.append("")

    return "\n".join(lines)


def copy_existing_markdown(src_path, dest_path):
    """Copy and optionally clean up an existing markdown file."""
    with open(src_path, "r") as f:
        content = f.read()
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(content)


def generate_main_readme(api_files, doc_sections):
    """Generate the main README.md with table of contents."""
    lines = []
    lines.append("# GoHighLevel API Documentation")
    lines.append("")
    lines.append("Comprehensive API documentation for the GoHighLevel (HighLevel) platform, converted to Markdown format for easy reference and integration.")
    lines.append("")
    lines.append("> **Source:** This documentation is automatically synced from the [official GoHighLevel API V2 documentation](https://marketplace.gohighlevel.com/docs/) and the [GoHighLevel API docs repository](https://github.com/GoHighLevel/highlevel-api-docs). It is checked for updates daily via GitHub Actions.")
    lines.append("")

    lines.append("## Table of Contents")
    lines.append("")

    lines.append("### Authentication & OAuth")
    lines.append("")
    for title, path in doc_sections.get("oauth", []):
        lines.append(f"- [{title}]({path})")
    lines.append("")

    lines.append("### API Reference")
    lines.append("")
    lines.append("| API | Description | Documentation |")
    lines.append("|-----|-------------|---------------|")
    for api_name, rel_path, endpoint_count in sorted(api_files, key=lambda x: x[0]):
        title = API_TITLES.get(api_name, api_name.replace("-", " ").title())
        lines.append(f"| {title} | {endpoint_count} endpoints | [{title} API]({rel_path}) |")
    lines.append("")

    lines.append("### Webhook Events")
    lines.append("")
    for title, path in doc_sections.get("webhooks", []):
        lines.append(f"- [{title}]({path})")
    lines.append("")

    lines.append("### Marketplace Modules")
    lines.append("")
    for title, path in doc_sections.get("marketplace_modules", []):
        lines.append(f"- [{title}]({path})")
    lines.append("")

    if doc_sections.get("other"):
        lines.append("### Other Documentation")
        lines.append("")
        for title, path in doc_sections.get("other", []):
            lines.append(f"- [{title}]({path})")
        lines.append("")

    lines.append("## Quick Start")
    lines.append("")
    lines.append("### Base URL")
    lines.append("")
    lines.append("All API requests should be made to:")
    lines.append("")
    lines.append("```")
    lines.append("https://services.leadconnectorhq.com")
    lines.append("```")
    lines.append("")
    lines.append("### Authentication")
    lines.append("")
    lines.append("The GoHighLevel API uses **OAuth 2.0** for authentication. See the [OAuth Overview](docs/oauth/Overview.md) for details.")
    lines.append("")
    lines.append("### Example Request")
    lines.append("")
    lines.append("```bash")
    lines.append('curl -X GET \\')
    lines.append('  https://services.leadconnectorhq.com/contacts/ \\')
    lines.append('  -H "Authorization: Bearer YOUR_TOKEN" \\')
    lines.append('  -H "Content-Type: application/json" \\')
    lines.append('  -H "Version: 2021-07-28"')
    lines.append("```")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("This documentation is maintained by [Appliance Marketing Pros](https://github.com/appliancemarketingpros). For official API issues, please refer to the [GoHighLevel API docs repository](https://github.com/GoHighLevel/highlevel-api-docs).")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("This documentation is provided for reference purposes. GoHighLevel and HighLevel are trademarks of HighLevel Inc.")
    lines.append("")

    return "\n".join(lines)


def main():
    """Main conversion function."""
    if not os.path.exists(SOURCE_DIR):
        print(f"ERROR: Source directory not found: {SOURCE_DIR}")
        sys.exit(1)

    api_dir = os.path.join(OUTPUT_DIR, "api-reference")
    docs_dir = os.path.join(OUTPUT_DIR, "docs")
    oauth_dir = os.path.join(docs_dir, "oauth")
    webhook_dir = os.path.join(docs_dir, "webhook-events")
    marketplace_dir = os.path.join(docs_dir, "marketplace-modules")
    other_dir = os.path.join(docs_dir, "other")

    for d in [api_dir, oauth_dir, webhook_dir, marketplace_dir, other_dir]:
        os.makedirs(d, exist_ok=True)

    api_files = []
    doc_sections = {
        "oauth": [],
        "webhooks": [],
        "marketplace_modules": [],
        "other": [],
    }

    # 1. Convert all OpenAPI JSON specs to markdown
    print("Converting OpenAPI JSON specs to markdown...")
    apps_dir = os.path.join(SOURCE_DIR, "apps")
    if os.path.exists(apps_dir):
        for json_file in sorted(glob.glob(os.path.join(apps_dir, "*.json"))):
            api_name = os.path.basename(json_file).replace(".json", "")
            print(f"  Processing: {api_name}")
            try:
                md_content = convert_openapi_to_markdown(json_file, api_name)
                md_filename = f"{api_name}.md"
                md_path = os.path.join(api_dir, md_filename)
                with open(md_path, "w") as f:
                    f.write(md_content)
                with open(json_file) as f:
                    spec = json.load(f)
                endpoint_count = 0
                for path, methods in spec.get("paths", {}).items():
                    for method in methods:
                        if method in ("get", "post", "put", "patch", "delete"):
                            endpoint_count += 1
                rel_path = f"api-reference/{md_filename}"
                api_files.append((api_name, rel_path, endpoint_count))
                print(f"    -> {md_filename} ({endpoint_count} endpoints)")
            except Exception as e:
                print(f"    ERROR: {e}")

    # 2. Copy OAuth documentation
    print("\nCopying OAuth documentation...")
    oauth_files = [
        ("Overview.md", "Overview"),
        ("Scopes.md", "Scopes"),
        ("Authorization.md", "Authorization"),
        ("Billing.md", "External Billing"),
        ("ExternalAuthentication.md", "External Authentication"),
        ("WebhookAuthentication.md", "Webhook Authentication"),
        ("Faqs.md", "FAQs"),
    ]
    for filename, title in oauth_files:
        src = os.path.join(SOURCE_DIR, "docs", "oauth", filename)
        if os.path.exists(src):
            dest = os.path.join(oauth_dir, filename)
            copy_existing_markdown(src, dest)
            doc_sections["oauth"].append((title, f"docs/oauth/{filename}"))
            print(f"  Copied: {filename}")

    # 3. Copy webhook event documentation
    print("\nCopying webhook event documentation...")
    webhook_src_dir = os.path.join(SOURCE_DIR, "docs", "webhook events")
    if os.path.exists(webhook_src_dir):
        for md_file in sorted(glob.glob(os.path.join(webhook_src_dir, "*.md"))):
            filename = os.path.basename(md_file)
            title = filename.replace(".md", "")
            dest = os.path.join(webhook_dir, filename)
            copy_existing_markdown(md_file, dest)
            doc_sections["webhooks"].append((title, f"docs/webhook-events/{filename}"))
            print(f"  Copied: {filename}")

    # 4. Copy marketplace module documentation
    print("\nCopying marketplace module documentation...")
    marketplace_src_dir = os.path.join(SOURCE_DIR, "docs", "marketplace modules")
    if os.path.exists(marketplace_src_dir):
        for md_file in sorted(glob.glob(os.path.join(marketplace_src_dir, "*.md"))):
            filename = os.path.basename(md_file)
            title = filename.replace(".md", "")
            dest = os.path.join(marketplace_dir, filename)
            copy_existing_markdown(md_file, dest)
            doc_sections["marketplace_modules"].append((title, f"docs/marketplace-modules/{filename}"))
            print(f"  Copied: {filename}")

    # 5. Copy country list
    print("\nCopying other documentation...")
    country_src = os.path.join(SOURCE_DIR, "docs", "country list", "Country.md")
    if os.path.exists(country_src):
        dest = os.path.join(other_dir, "Country.md")
        copy_existing_markdown(country_src, dest)
        doc_sections["other"].append(("Country List", "docs/other/Country.md"))
        print("  Copied: Country.md")

    # 6. Generate main README
    print("\nGenerating main README.md...")
    readme_content = generate_main_readme(api_files, doc_sections)
    with open(os.path.join(OUTPUT_DIR, "README.md"), "w") as f:
        f.write(readme_content)
    print("  Generated: README.md")

    # 7. Common schemas
    common_src = os.path.join(SOURCE_DIR, "common", "common-schemas.json")
    if os.path.exists(common_src):
        os.makedirs(os.path.join(OUTPUT_DIR, "schemas"), exist_ok=True)
        with open(common_src) as f:
            common = json.load(f)
        schema_lines = ["# Common Schemas", "", "Shared schema definitions used across multiple GoHighLevel API endpoints.", ""]
        schemas = common.get("components", {}).get("schemas", {})
        if not schemas:
            schemas = common.get("schemas", {})
        for name, schema_def in sorted(schemas.items()):
            schema_lines.append(f"## {name}")
            schema_lines.append("")
            if schema_def.get("description"):
                schema_lines.append(schema_def["description"])
                schema_lines.append("")
            if schema_def.get("type"):
                schema_lines.append(f"**Type:** `{schema_def['type']}`")
                schema_lines.append("")
            if "properties" in schema_def:
                required = set(schema_def.get("required", []))
                schema_lines.append("| Property | Type | Required | Description |")
                schema_lines.append("|----------|------|----------|-------------|")
                for prop_name, prop_def in schema_def["properties"].items():
                    p_type = prop_def.get("type", "any")
                    p_req = "Yes" if prop_name in required else "No"
                    p_desc = prop_def.get("description", "").replace("\n", " ")
                    schema_lines.append(f"| `{prop_name}` | {p_type} | {p_req} | {p_desc} |")
                schema_lines.append("")
            if "enum" in schema_def:
                schema_lines.append("**Possible Values:**")
                for val in schema_def["enum"]:
                    schema_lines.append(f"- `{val}`")
                schema_lines.append("")
        with open(os.path.join(OUTPUT_DIR, "schemas", "common-schemas.md"), "w") as f:
            f.write("\n".join(schema_lines))
        print("  Generated: schemas/common-schemas.md")

    # Summary
    total_endpoints = sum(c for _, _, c in api_files)
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  API reference files: {len(api_files)}")
    print(f"  OAuth docs: {len(doc_sections['oauth'])}")
    print(f"  Webhook event docs: {len(doc_sections['webhooks'])}")
    print(f"  Marketplace module docs: {len(doc_sections['marketplace_modules'])}")
    print(f"  Other docs: {len(doc_sections['other'])}")
    print(f"  Total API endpoints documented: {total_endpoints}")


if __name__ == "__main__":
    main()
