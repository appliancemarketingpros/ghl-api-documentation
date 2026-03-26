# Funnels API

Documentation for funnels API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Redirect](#redirect)
- [Funnel](#funnel)

## Redirect

### POST `/funnels/lookup/redirect`

**Create Redirect**

The "Create Redirect" API Allows adding a new url redirect to the system. Use this endpoint to create a url redirect with the specified details. Ensure that the required information is provided in the request payload.

**Operation ID:** `create-redirect`

**Tags:** Redirect

**Required Scopes:** `funnels/redirect.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `domain` | string | Yes |  |
| `path` | string | Yes |  |
| `target` | string | Yes |  |
| `action` | string (enum: `funnel`, `website`, `url`, `all`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |

**`422` - Unprocessable Entity**

---

### PATCH `/funnels/lookup/redirect/{id}`

**Update Redirect By Id**

The "Update Redirect By Id" API Allows updating an existing URL redirect in the system. Use this endpoint to modify a URL redirect with the specified ID using details provided in the request payload.

**Operation ID:** `update-redirect-by-id`

**Tags:** Redirect

**Required Scopes:** `funnels/redirect.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `target` | string | Yes |  |
| `action` | string (enum: `funnel`, `website`, `url`, `all`) | Yes |  |
| `locationId` | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |

**`422` - Unprocessable Entity**

---

### DELETE `/funnels/lookup/redirect/{id}`

**Delete Redirect By Id**

The "Delete Redirect By Id" API Allows deletion of a URL redirect from the system using its unique identifier. Use this endpoint to delete a URL redirect with the specified ID using details provided in the request payload.

**Operation ID:** `delete-redirect-by-id`

**Tags:** Redirect

**Required Scopes:** `funnels/redirect.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |
| `locationId` | query | string | Yes |  |

#### Responses

**`200` - Successful response - URL redirect deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Status of the delete operation |

**`422` - Unprocessable Entity - The provided data is invalid or incomplete**

---

### GET `/funnels/lookup/redirect/list`

**Fetch List of Redirects**

Retrieves a list of all URL redirects based on the given query parameters.

**Operation ID:** `fetch-redirects-list`

**Tags:** Redirect

**Required Scopes:** `funnels/redirect.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `limit` | query | number | Yes |  |
| `offset` | query | number | Yes |  |
| `search` | query | string | No |  |

#### Responses

**`200` - Successful response - List of URL redirects returned**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Object containing the count of redirects and an array of redirect data |

**`422` - Unprocessable Entity - The provided data is invalid or incomplete**

---

## Funnel

### GET `/funnels/funnel/list`

**Fetch List of Funnels**

Retrieves a list of all funnels based on the given query parameters.

**Operation ID:** `getFunnels`

**Tags:** Funnel

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `type` | query | string | No |  |
| `category` | query | string | No |  |
| `offset` | query | string | No |  |
| `limit` | query | string | No |  |
| `parentId` | query | string | No |  |
| `name` | query | string | No |  |

#### Responses

**`200` - Successful response - List of funnels returned**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `funnels` | object | Yes |  |
| `count` | number | Yes |  |
| `traceId` | string | Yes |  |

---

### GET `/funnels/page`

**Fetch list of funnel pages**

Retrieves a list of all funnel pages based on the given query parameters.

**Operation ID:** `getPagesByFunnelId`

**Tags:** Funnel

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `funnelId` | query | string | Yes |  |
| `name` | query | string | No |  |
| `limit` | query | number | Yes |  |
| `offset` | query | number | Yes |  |

#### Responses

**`200` - Successful response - List of funnel pages returned**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes |  |
| `locationId` | string | Yes |  |
| `funnelId` | string | Yes |  |
| `name` | string | Yes |  |
| `stepId` | string | Yes |  |
| `deleted` | string | Yes |  |
| `updatedAt` | string | Yes |  |

---

### GET `/funnels/page/count`

**Fetch count of funnel pages**

Retrieves count of all funnel pages based on the given query parameters.

**Operation ID:** `getPagesCountByFunnelId`

**Tags:** Funnel

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `funnelId` | query | string | Yes |  |
| `name` | query | string | No |  |

#### Responses

**`200` - Successful response - Count of funnel pages returned**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes |  |

---

## Schemas

### CreateRedirectParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `domain` | string | Yes |  |
| `path` | string | Yes |  |
| `target` | string | Yes |  |
| `action` | string (enum: `funnel`, `website`, `url`, `all`) | Yes |  |

### CreateRedirectResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |

### DeleteRedirectResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Status of the delete operation |

### FunnelListResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `funnels` | object | Yes |  |
| `count` | number | Yes |  |
| `traceId` | string | Yes |  |

### FunnelPageCountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes |  |

### FunnelPageResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes |  |
| `locationId` | string | Yes |  |
| `funnelId` | string | Yes |  |
| `name` | string | Yes |  |
| `stepId` | string | Yes |  |
| `deleted` | string | Yes |  |
| `updatedAt` | string | Yes |  |

### RedirectListResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Object containing the count of redirects and an array of redirect data |

### RedirectResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the redirect |
| `locationId` | string | Yes | Identifier of the location associated with the redirect |
| `domain` | string | Yes | Domain where the redirect occurs |
| `path` | string | Yes | Original path that will be redirected |
| `pathLowercase` | string | Yes | Lowercase version of the original path |
| `type` | string | Yes | Type of redirect (e.g., Permanent, Temporary) |
| `target` | string | Yes | Target URL to which the original path will be redirected |
| `action` | string | Yes | Action performed by the redirect |

### UpdateRedirectParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `target` | string | Yes |  |
| `action` | string (enum: `funnel`, `website`, `url`, `all`) | Yes |  |
| `locationId` | string | Yes |  |

### UpdateRedirectResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
