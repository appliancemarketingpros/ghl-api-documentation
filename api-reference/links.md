# Trigger Links API

Documentation for links API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Trigger Links](#trigger-links)
- [Trigger Links Search](#trigger-links-search)

## Trigger Links

### GET `/links/id/{linkId}`

**Get Link by ID**

Get a single link by its ID

**Operation ID:** `get-link-by-id`

**Tags:** Trigger Links

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | query | string | Yes | Location Id |
| `linkId` | path | string | Yes | Link Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `link` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/links/{linkId}`

**Update Link**

Update Link

**Operation ID:** `update-link`

**Tags:** Trigger Links

**Required Scopes:** `links.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `linkId` | path | string | Yes | Link Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `redirectTo` | string | Yes |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `link` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/links/{linkId}`

**Delete Link**

Delete Link

**Operation ID:** `delete-link`

**Tags:** Trigger Links

**Required Scopes:** `links.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `linkId` | path | string | Yes | Link Id |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/links/`

**Get Links**

Get Links

**Operation ID:** `get-links`

**Tags:** Trigger Links

**Required Scopes:** `links.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `links` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/links/`

**Create Link**

Create Link

**Operation ID:** `create-link`

**Tags:** Trigger Links

**Required Scopes:** `links.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `redirectTo` | string | Yes |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `link` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Trigger Links Search

### GET `/links/search`

**Search Trigger Links**

Get list of links by searching

**Operation ID:** `search-trigger-links`

**Tags:** Trigger Links Search

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | query | string | Yes | Location Id |
| `query` | query | string | No | Search query as a string |
| `skip` | query | number | No | Numbers of query results to skip |
| `limit` | query | number | No | Limit on number of search results |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `links` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Schemas

### DeleteLinksSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### GetLinkSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `link` | object | No |  |

### GetLinksSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `links` | array of object | No |  |

### LinkSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `redirectTo` | string | No |  |
| `fieldKey` | string | No |  |
| `locationId` | string | No |  |

### LinkUpdateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `redirectTo` | string | Yes |  |

### LinksDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `redirectTo` | string | Yes |  |
