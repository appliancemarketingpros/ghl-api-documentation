# Emails API

Documentation for emails API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Campaigns](#campaigns)
- [Templates](#templates)

## Campaigns

### GET `/emails/schedule`

**Get Campaigns**

Get Campaigns

**Operation ID:** `fetch-campaigns`

**Tags:** Campaigns

**Required Scopes:** `emails/schedule.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location ID to fetch campaigns from |
| `limit` | query | number | No | Maximum number of campaigns to return. Defaults to 10, maximum is 100 |
| `offset` | query | number | No | Number of campaigns to skip for pagination |
| `status` | query | string (enum: `active`, `pause`, `complete`, `cancelled`, `retry`, `draft`, `resend-scheduled`) | No | Filter by schedule status |
| `emailStatus` | query | string (enum: `all`, `not-started`, `paused`, `cancelled`, `processing`, `resumed`, `next-drip`, `complete`, `success`, `error`, `waiting`, `queued`, `queueing`, `reading`, `scheduled`) | No | Filter by email delivery status |
| `name` | query | string | No | Filter campaigns by name |
| `parentId` | query | string | No | Filter campaigns by parent folder ID |
| `limitedFields` | query | boolean | No | When true, returns only essential campaign fields like id, templateDataDownloadUrl, updatedAt, type, templateType, templateId, downloadUrl and isPlainText. When false, returns complete campaign data i... |
| `archived` | query | boolean | No | Filter archived campaigns |
| `campaignsOnly` | query | boolean | No | Return only campaigns, excluding folders |
| `showStats` | query | boolean | No | When true, returns campaign statistics including delivered count, opened count, clicked count and revenue if available for the campaign. When false, returns campaign data without statistics. |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedules` | array of object | Yes | The list of campaigns |
| `total` | array of string | Yes | The total number of campaigns |
| `traceId` | string | Yes | Trace Id |

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

## Templates

### POST `/emails/builder`

**Create a new template**

Create a new template

**Operation ID:** `create-template`

**Tags:** Templates

**Required Scopes:** `emails/builder.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `title` | string | No |  |
| `type` | string (enum: `html`, `folder`, `import`, `builder`, `blank`) | Yes |  |
| `updatedBy` | string | No |  |
| `builderVersion` | string (enum: `1`, `2`) | No |  Default: `2` |
| `name` | string | No |  |
| `parentId` | string | No |  |
| `templateDataUrl` | string | No |  |
| `importProvider` | string (enum: `mailchimp`, `active_campaign`, `kajabi`) | Yes |  |
| `importURL` | string | No |  |
| `templateSource` | string | No |  |
| `isPlainText` | boolean | No |  |

#### Responses

**`201` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `redirect` | string | Yes | template id |
| `traceId` | string | Yes | trace id |

**`400` - Bad Request**

**`401` - Unauthorized**

**`404` - Not Found**

**`422` - Unprocessable Entity**

---

### GET `/emails/builder`

**Fetch email templates**

Fetch email templates by location id

**Operation ID:** `fetch-template`

**Tags:** Templates

**Required Scopes:** `emails/builder.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `limit` | query | string | No |  |
| `offset` | query | string | No |  |
| `search` | query | string | No |  |
| `sortByDate` | query | string | No |  |
| `archived` | query | string | No |  |
| `builderVersion` | query | string (enum: `1`, `2`) | No |  |
| `name` | query | string | No |  |
| `parentId` | query | string | No |  |
| `originId` | query | string | No |  |
| `templatesOnly` | query | string | No |  |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | template name |
| `updatedBy` | string | No | updated by |
| `isPlainText` | boolean | No | plain text based template |
| `lastUpdated` | string | No | last updated |
| `dateAdded` | string | No | date added |
| `previewUrl` | string | No | preview url |
| `id` | string | No | id |
| `version` | string | No | version |
| `templateType` | string | No | type |

**`400` - Bad Request**

**`401` - Unauthorized**

**`404` - Not Found**

**`422` - Unprocessable Entity**

---

### DELETE `/emails/builder/{locationId}/{templateId}`

**Delete a template**

Delete a template

**Operation ID:** `delete-template`

**Tags:** Templates

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |
| `templateId` | path | string | Yes |  |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ok` | string | No | ok |
| `traceId` | string | No | trace id |

**`400` - Bad Request**

**`401` - Unauthorized**

**`404` - Not Found**

**`422` - Unprocessable Entity**

---

### POST `/emails/builder/data`

**Update a template**

Update a template

**Operation ID:** `update-template`

**Tags:** Templates

**Required Scopes:** `emails/builder.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `templateId` | string | Yes |  |
| `updatedBy` | string | Yes |  |
| `dnd` | object | Yes |  |
| `html` | string | Yes |  |
| `editorType` | string (enum: `html`, `builder`) | Yes |  |
| `previewText` | string | No |  |
| `isPlainText` | boolean | No |  |

**`dnd` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `elements` | array of string | Yes |  |
| `attrs` | object | Yes |  |
| `templateSettings` | object | Yes |  |

#### Responses

**`201` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ok` | string | No | ok |
| `traceId` | string | No | trace id |
| `previewUrl` | string | No | preview url |
| `templateDownloadUrl` | string | No | template data download url |

**`400` - Bad Request**

**`401` - Unauthorized**

**`404` - Not Found**

**`422` - Unprocessable Entity**

---

## Schemas

### BuilderUpdateSuccessfulDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ok` | string | No | ok |
| `traceId` | string | No | trace id |
| `previewUrl` | string | No | preview url |
| `templateDownloadUrl` | string | No | template data download url |

### CreateBuilderDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `title` | string | No |  |
| `type` | string (enum: `html`, `folder`, `import`, `builder`, `blank`) | Yes |  |
| `updatedBy` | string | No |  |
| `builderVersion` | string (enum: `1`, `2`) | No |  Default: `2` |
| `name` | string | No |  |
| `parentId` | string | No |  |
| `templateDataUrl` | string | No |  |
| `importProvider` | string (enum: `mailchimp`, `active_campaign`, `kajabi`) | Yes |  |
| `importURL` | string | No |  |
| `templateSource` | string | No |  |
| `isPlainText` | boolean | No |  |

### CreateBuilderSuccesfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `redirect` | string | Yes | template id |
| `traceId` | string | Yes | trace id |

### DeleteBuilderSuccesfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ok` | string | No | ok |
| `traceId` | string | No | trace id |

### FetchBuilderSuccesfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | template name |
| `updatedBy` | string | No | updated by |
| `isPlainText` | boolean | No | plain text based template |
| `lastUpdated` | string | No | last updated |
| `dateAdded` | string | No | date added |
| `previewUrl` | string | No | preview url |
| `id` | string | No | id |
| `version` | string | No | version |
| `templateType` | string | No | type |

### IBuilderJsonMapper

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `elements` | array of string | Yes |  |
| `attrs` | object | Yes |  |
| `templateSettings` | object | Yes |  |

### InvalidLocationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

### NotFoundDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

### SaveBuilderDataDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `templateId` | string | Yes |  |
| `updatedBy` | string | Yes |  |
| `dnd` | object | Yes |  |
| `html` | string | Yes |  |
| `editorType` | string (enum: `html`, `builder`) | Yes |  |
| `previewText` | string | No |  |
| `isPlainText` | boolean | No |  |

### ScheduleDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `repeatAfter` | string | Yes |  |
| `id` | string | Yes |  |
| `parentId` | string | Yes |  |
| `childCount` | number | Yes |  |
| `campaignType` | string | Yes |  |
| `bulkActionVersion` | string | Yes |  |
| `_id` | string | Yes |  |
| `status` | string | Yes |  |
| `sendDays` | array of string | Yes |  |
| `deleted` | boolean | Yes |  |
| `migrated` | boolean | Yes |  |
| `archived` | boolean | Yes |  |
| `hasTracking` | boolean | Yes |  |
| `isPlainText` | boolean | Yes |  |
| `hasUtmTracking` | boolean | Yes |  |
| `enableResendToUnopened` | boolean | Yes |  |
| `locationId` | string | Yes |  |
| `templateId` | string | Yes |  |
| `templateType` | string | Yes |  |
| `createdAt` | string | Yes |  |
| `updatedAt` | string | Yes |  |
| `__v` | number | Yes |  |
| `documentId` | string | Yes |  |
| `downloadUrl` | string | Yes |  |
| `templateDataDownloadUrl` | string | Yes |  |
| `child` | array of string | Yes |  |

### ScheduleFetchSuccessfulDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedules` | array of object | Yes | The list of campaigns |
| `total` | array of string | Yes | The total number of campaigns |
| `traceId` | string | Yes | Trace Id |

### TemplateSettings

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
