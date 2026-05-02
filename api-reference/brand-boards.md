# Brand Boards API

Documentation for Brand Boards API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Brand Boards](#brand-boards)

## Brand Boards

### GET `/brand-boards/{locationId}`

**Get Brand Boards**

Retrieves all Brand Boards for a specific location

**Operation ID:** `getBrandBoardsByLocation`

**Tags:** Brand Boards

**Required Scopes:** `brand-boards/design-kit.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |
| `limit` | query | number | No | Maximum number of brand boards to return |
| `offset` | query | number | No | Number of brand boards to skip for pagination |
| `search` | query | string | No | Search term to filter brand boards by name |
| `deleted` | query | boolean | No | Include deleted brand boards in results |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `brandBoards` | array of object | Yes | Array of brand boards for the location |
| `totalCount` | number | Yes | Total number of brand boards matching the query |

**`400` - Bad Request**

**`401` - Unauthorized**

**`403` - The token does not have access to this location**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`422` - Unprocessable Entity**

---

### GET `/brand-boards/{locationId}/{id}`

**Get Brand Board**

Retrieves a specific Brand Board by its ID

**Operation ID:** `getBrandBoardById`

**Tags:** Brand Boards

**Required Scopes:** `brand-boards/design-kit.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID where the brand board exists |
| `id` | path | string | Yes | Brand board ID to update, retrieve, or delete |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Brand board ID |
| `locationId` | string | Yes | Location ID |
| `name` | string | Yes | Brand board name |
| `logos` | array of object | No | Array of logos |
| `colors` | array of object | No | Array of brand colors |
| `fonts` | array of object | No | Array of brand fonts |
| `default` | boolean | Yes | Whether this is the default brand board for the location |
| `deleted` | boolean | Yes | Whether the brand board has been soft deleted |
| `parentId` | string | No | Parent folder ID in media library |
| `folderId` | string | No | Media library folder ID for this brand board |
| `originId` | string | No | Original brand board ID if cloned from snapshot |
| `meta` | object | No |  |
| `createdAt` | string | No | Creation timestamp |
| `updatedAt` | string | No | Last update timestamp |

**`400` - Bad Request**

**`401` - Unauthorized**

**`403` - The token does not have access to this location**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`404` - Not Found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

---

### PATCH `/brand-boards/{locationId}/{id}`

**Update a Brand Board**

Updates an existing Brand Board

**Operation ID:** `updateBrandBoard`

**Tags:** Brand Boards

**Required Scopes:** `brand-boards/design-kit.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID where the brand board exists |
| `id` | path | string | Yes | Brand board ID to update, retrieve, or delete |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the brand board |
| `logos` | array of object | No | Array of logos for the brand board |
| `colors` | array of object | No | Array of colors for the brand board |
| `fonts` | array of object | No | Array of fonts for the brand board |
| `default` | boolean | No | Set as the default brand board for this location |
| `parentId` | string | No | Parent folder ID in media library (reserved for future use) |

**`logos` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the logo |
| `url` | string | Yes | Public URL of the logo image. Used for uploading to the brand board folder in media library |
| `label` | string | Yes | Display label for the logo (e.g., Primary, Secondary) |
| `path` | string | Yes | Storage path of the logo in the media library |

**`colors` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the color |
| `hexa` | string | Yes | Color in HEXA format (with alpha) |
| `rgba` | string | Yes | Color in RGBA format |
| `hex` | string | Yes | Color in HEX format |
| `rgb` | string | Yes | Color in RGB format |
| `label` | string | Yes | Display label for the color |

**`fonts` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the font |
| `font` | string | Yes | Font family name |
| `fallback` | string | Yes | Fallback font family |
| `label` | string | Yes | Display label for the font |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Brand board ID |
| `locationId` | string | Yes | Location ID |
| `name` | string | Yes | Brand board name |
| `logos` | array of object | No | Array of logos |
| `colors` | array of object | No | Array of brand colors |
| `fonts` | array of object | No | Array of brand fonts |
| `default` | boolean | Yes | Whether this is the default brand board for the location |
| `deleted` | boolean | Yes | Whether the brand board has been soft deleted |
| `parentId` | string | No | Parent folder ID in media library |
| `folderId` | string | No | Media library folder ID for this brand board |
| `originId` | string | No | Original brand board ID if cloned from snapshot |
| `meta` | object | No |  |
| `createdAt` | string | No | Creation timestamp |
| `updatedAt` | string | No | Last update timestamp |

**`400` - Bad Request**

**`401` - Unauthorized**

**`403` - The token does not have access to this location**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`404` - Not Found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

---

### DELETE `/brand-boards/{locationId}/{id}`

**Delete a Brand Board**

Deletes a Brand Board

**Operation ID:** `deleteBrandBoard`

**Tags:** Brand Boards

**Required Scopes:** `brand-boards/design-kit.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID where the brand board exists |
| `id` | path | string | Yes | Brand board ID to update, retrieve, or delete |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Brand board ID |
| `locationId` | string | Yes | Location ID |
| `name` | string | Yes | Brand board name |
| `logos` | array of object | No | Array of logos |
| `colors` | array of object | No | Array of brand colors |
| `fonts` | array of object | No | Array of brand fonts |
| `default` | boolean | Yes | Whether this is the default brand board for the location |
| `deleted` | boolean | Yes | Whether the brand board has been soft deleted |
| `parentId` | string | No | Parent folder ID in media library |
| `folderId` | string | No | Media library folder ID for this brand board |
| `originId` | string | No | Original brand board ID if cloned from snapshot |
| `meta` | object | No |  |
| `createdAt` | string | No | Creation timestamp |
| `updatedAt` | string | No | Last update timestamp |

**`400` - Bad Request**

**`401` - Unauthorized**

**`403` - The token does not have access to this location**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`404` - Not Found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

---

### POST `/brand-boards/`

**Create a new brand board**

Creates a new brand board with logos, colors, and fonts

**Operation ID:** `createBrandBoard`

**Tags:** Brand Boards

**Required Scopes:** `brand-boards/design-kit.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID where the brand board will be created |
| `name` | string | Yes | Name of the brand board |
| `logos` | array of object | No | Array of logos for the brand board |
| `colors` | array of object | No | Array of colors for the brand board |
| `fonts` | array of object | No | Array of fonts for the brand board |
| `default` | boolean | No | Set as the default brand board for this location |
| `brandBoardId` | string | No | Source brand board ID to copy from (creates a new brand board based on this template) |
| `parentId` | string | No | Parent folder ID in media library for organizing brand boards |
| `type` | string (enum: `template`, `blank`, `snapshot`) | No | Source type indicating how the brand board was created |

**`logos` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the logo |
| `url` | string | Yes | Public URL of the logo image. Used for uploading to the brand board folder in media library |
| `label` | string | Yes | Display label for the logo (e.g., Primary, Secondary) |
| `path` | string | Yes | Storage path of the logo in the media library |

**`colors` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the color |
| `hexa` | string | Yes | Color in HEXA format (with alpha) |
| `rgba` | string | Yes | Color in RGBA format |
| `hex` | string | Yes | Color in HEX format |
| `rgb` | string | Yes | Color in RGB format |
| `label` | string | Yes | Display label for the color |

**`fonts` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the font |
| `font` | string | Yes | Font family name |
| `fallback` | string | Yes | Fallback font family |
| `label` | string | Yes | Display label for the font |

#### Responses

**`201` - Created**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Brand board ID |
| `locationId` | string | Yes | Location ID |
| `name` | string | Yes | Brand board name |
| `logos` | array of object | No | Array of logos |
| `colors` | array of object | No | Array of brand colors |
| `fonts` | array of object | No | Array of brand fonts |
| `default` | boolean | Yes | Whether this is the default brand board for the location |
| `deleted` | boolean | Yes | Whether the brand board has been soft deleted |
| `parentId` | string | No | Parent folder ID in media library |
| `folderId` | string | No | Media library folder ID for this brand board |
| `originId` | string | No | Original brand board ID if cloned from snapshot |
| `meta` | object | No |  |
| `createdAt` | string | No | Creation timestamp |
| `updatedAt` | string | No | Last update timestamp |

**`400` - Bad Request**

**`401` - Unauthorized**

**`403` - The token does not have access to this location**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`422` - Unprocessable Entity**

---

## Schemas

### BrandBoardListItemDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Brand board ID |
| `name` | string | Yes | Brand board name |
| `updatedAt` | string | Yes | Last update timestamp |
| `default` | boolean | No | Whether this is the default brand board for the location |
| `meta` | object | No |  |

### Color

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the color |
| `hexa` | string | Yes | Color in HEXA format (with alpha) |
| `rgba` | string | Yes | Color in RGBA format |
| `hex` | string | Yes | Color in HEX format |
| `rgb` | string | Yes | Color in RGB format |
| `label` | string | Yes | Display label for the color |

### CreateBrandBoardParam

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID where the brand board will be created |
| `name` | string | Yes | Name of the brand board |
| `logos` | array of object | No | Array of logos for the brand board |
| `colors` | array of object | No | Array of colors for the brand board |
| `fonts` | array of object | No | Array of fonts for the brand board |
| `default` | boolean | No | Set as the default brand board for this location |
| `brandBoardId` | string | No | Source brand board ID to copy from (creates a new brand board based on this template) |
| `parentId` | string | No | Parent folder ID in media library for organizing brand boards |
| `type` | string (enum: `template`, `blank`, `snapshot`) | No | Source type indicating how the brand board was created |

### Font

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the font |
| `font` | string | Yes | Font family name |
| `fallback` | string | Yes | Fallback font family |
| `label` | string | Yes | Display label for the font |

### GetBrandBoardSuccessDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Brand board ID |
| `locationId` | string | Yes | Location ID |
| `name` | string | Yes | Brand board name |
| `logos` | array of object | No | Array of logos |
| `colors` | array of object | No | Array of brand colors |
| `fonts` | array of object | No | Array of brand fonts |
| `default` | boolean | Yes | Whether this is the default brand board for the location |
| `deleted` | boolean | Yes | Whether the brand board has been soft deleted |
| `parentId` | string | No | Parent folder ID in media library |
| `folderId` | string | No | Media library folder ID for this brand board |
| `originId` | string | No | Original brand board ID if cloned from snapshot |
| `meta` | object | No |  |
| `createdAt` | string | No | Creation timestamp |
| `updatedAt` | string | No | Last update timestamp |

### GetBrandBoardsByLocationSuccessDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `brandBoards` | array of object | Yes | Array of brand boards for the location |
| `totalCount` | number | Yes | Total number of brand boards matching the query |

### InvalidLocationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

### Logo

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the logo |
| `url` | string | Yes | Public URL of the logo image. Used for uploading to the brand board folder in media library |
| `label` | string | Yes | Display label for the logo (e.g., Primary, Secondary) |
| `path` | string | Yes | Storage path of the logo in the media library |

### MetaData

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updatedBy` | string | No | User ID who last updated the brand board |
| `lastAction` | string | No | Last action performed on the brand board |
| `sourceId` | string | No | Source brand board ID if created from a template |
| `sourceType` | string (enum: `template`, `blank`, `snapshot`) | No | How the brand board was created |

### NotFoundDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

### UpdateBrandBoardBody

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the brand board |
| `logos` | array of object | No | Array of logos for the brand board |
| `colors` | array of object | No | Array of colors for the brand board |
| `fonts` | array of object | No | Array of fonts for the brand board |
| `default` | boolean | No | Set as the default brand board for this location |
| `parentId` | string | No | Parent folder ID in media library (reserved for future use) |
