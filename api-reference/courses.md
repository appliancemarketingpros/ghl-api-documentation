# Courses API

API Service for Courses and Memberships

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Other Endpoints](#other-endpoints)

## Other Endpoints

### POST `/courses/courses-exporter/public/import`

**Import Courses**

Import Courses through public channels

**Operation ID:** `import-courses`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `userId` | string | No |  |
| `products` | array of object | Yes |  |

**`products` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `description` | string | Yes |  |
| `imageUrl` | string | No |  |
| `categories` | array of object | Yes |  |
| `instructorDetails` | object | No |  |

#### Responses

**`201` - **

---

## Schemas

### CategoryInterface

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `visibility` | string (enum: `published`, `draft`) | Yes |  |
| `thumbnailUrl` | string | No |  |
| `posts` | array of object | No |  |
| `subCategories` | array of object | No |  |

### InstructorDetails

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `description` | string | Yes |  |

### PostInterface

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `visibility` | string (enum: `published`, `draft`) | Yes |  |
| `thumbnailUrl` | string | No |  |
| `contentType` | string (enum: `video`, `assignment`, `quiz`) | Yes |  |
| `description` | string | Yes |  |
| `bucketVideoUrl` | string | No |  |
| `postMaterials` | array of object | No |  |

### PostMaterialInterface

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `type` | string (enum: `pdf`, `image`, `docx`, `pptx`, `xlsx`, `html`, `dotx`, `epub`, `webp`, `gdoc`, `mp3`, `doc`, `txt`, `zip`, `ppt`, `key`, `htm`, `xls`, `odp`, `odt`, `rtf`, `m4a`, `ods`, `mp4`, `ai`, `avi`, `mov`, `wmv`, `mkv`, `wav`, `flac`, `ogg`, `png`, `jpeg`, `jpg`, `gif`, `bmp`, `tiff`, `svg`, `odg`, `sxw`, `sxc`, `sxi`, `rar`, `7z`, `json`, `xml`, `csv`, `md`, `obj`, `stl`, `woff`, `ttf`) | Yes |  |
| `url` | string | Yes |  |

### ProductInterface

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `description` | string | Yes |  |
| `imageUrl` | string | No |  |
| `categories` | array of object | Yes |  |
| `instructorDetails` | object | No |  |

### PublicExporterPayload

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `userId` | string | No |  |
| `products` | array of object | Yes |  |

### SubCategoryInterface

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `visibility` | string (enum: `published`, `draft`) | Yes |  |
| `thumbnailUrl` | string | No |  |
| `posts` | array of object | No |  |

### contentType

**Type:** `string`

**Possible Values:**

- `video`
- `assignment`
- `quiz`

### type

**Type:** `string`

**Possible Values:**

- `pdf`
- `image`
- `docx`
- `pptx`
- `xlsx`
- `html`
- `dotx`
- `epub`
- `webp`
- `gdoc`
- `mp3`
- `doc`
- `txt`
- `zip`
- `ppt`
- `key`
- `htm`
- `xls`
- `odp`
- `odt`
- `rtf`
- `m4a`
- `ods`
- `mp4`
- `ai`
- `avi`
- `mov`
- `wmv`
- `mkv`
- `wav`
- `flac`
- `ogg`
- `png`
- `jpeg`
- `jpg`
- `gif`
- `bmp`
- `tiff`
- `svg`
- `odg`
- `sxw`
- `sxc`
- `sxi`
- `rar`
- `7z`
- `json`
- `xml`
- `csv`
- `md`
- `obj`
- `stl`
- `woff`
- `ttf`

### visibility

**Type:** `string`

**Possible Values:**

- `published`
- `draft`
