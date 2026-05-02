# Opportunities API

Documentation for Opportunities API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Lost reason](#lost-reason)
- [Search](#search)
- [Pipelines](#pipelines)
- [Opportunities](#opportunities)
- [Followers](#followers)

## Lost reason

### GET `/opportunities/lost-reason`

**Get lost reason**

Get lost reason

**Operation ID:** `get-lost-reason`

**Tags:** Lost reason

**Required Scopes:** `opportunities.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `name` | query | string | No | lost reason name |
| `deleted` | query | boolean | No | deleted |
| `query` | query | string | No | search query |
| `skip` | query | number | No | skip |
| `limit` | query | number | No | limit |
| `getCount` | query | boolean | No | get count |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `lostReasons` | array of object | No |  |
| `total` | number | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Search

### GET `/opportunities/search`

**Search Opportunity**

Search Opportunity

**Operation ID:** `search-opportunity`

**Tags:** Search

**Required Scopes:** `opportunities.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `q` | query | string | No |  |
| `location_id` | query | string | Yes | Location Id |
| `pipeline_id` | query | string | No | Pipeline Id |
| `pipeline_stage_id` | query | string | No | stage Id |
| `contact_id` | query | string | No | Contact Id |
| `status` | query | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | No |  |
| `assigned_to` | query | string | No |  |
| `campaignId` | query | string | No | Campaign Id |
| `id` | query | string | No | Opportunity Id |
| `order` | query | string | No |  |
| `endDate` | query | string | No | End date |
| `startAfter` | query | string | No | Start After |
| `startAfterId` | query | string | No | Start After Id |
| `date` | query | string | No | Start date |
| `country` | query | string | No |  |
| `page` | query | number | No |  |
| `limit` | query | number | No | Limit Per Page records count. will allow maximum up to 100 and default will be 20 |
| `getTasks` | query | boolean | No | get Tasks in contact |
| `getNotes` | query | boolean | No | get Notes in contact |
| `getCalendarEvents` | query | boolean | No | get Calender event in contact |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunities` | array of object | No |  |
| `meta` | object | No |  |
| `aggregations` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/opportunities/search`

**Search Opportunities**

Search Opportunities based on combinations of advanced filters. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-424216/7bf11bc9b94f80f

**Operation ID:** `search-opportunities-advanced`

**Tags:** Search

**Required Scopes:** `opportunities.readonly`

**External Documentation:** [Click here for more information](https://doc.clickup.com/8631005/d/h/87cpx-424216/7bf11bc9b94f80f)

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `query` | string | Yes |  |
| `limit` | number | Yes |  |
| `page` | number | Yes |  |
| `searchAfter` | array of string | Yes |  |
| `additionalDetails` | object | Yes |  |

**`additionalDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notes` | boolean | Yes |  |
| `tasks` | boolean | Yes |  |
| `calendarEvents` | boolean | Yes |  |
| `unReadConversations` | boolean | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunities` | array of object | No |  |
| `total` | number | Yes |  |
| `aggregations` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Pipelines

### GET `/opportunities/pipelines`

**Get Pipelines**

Get Pipelines

**Operation ID:** `get-pipelines`

**Tags:** Pipelines

**Required Scopes:** `opportunities.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pipelines` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Opportunities

### GET `/opportunities/{id}`

**Get Opportunity**

Get Opportunity

**Operation ID:** `get-opportunity`

**Tags:** Opportunities

**Required Scopes:** `opportunities.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Opportunity Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunity` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/opportunities/{id}`

**Delete Opportunity**

Delete Opportunity

**Operation ID:** `delete-opportunity`

**Tags:** Opportunities

**Required Scopes:** `opportunities.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Opportunity Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/opportunities/{id}`

**Update Opportunity**

Update Opportunity

**Operation ID:** `update-opportunity`

**Tags:** Opportunities

**Required Scopes:** `opportunities.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Opportunity Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pipelineId` | string | No | pipeline Id |
| `name` | string | No |  |
| `pipelineStageId` | string | No |  |
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | No |  |
| `monetaryValue` | number | No |  |
| `assignedTo` | string | No |  |
| `customFields` | array of object | object | object | No | Update custom fields to opportunities. |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunity` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/opportunities/{id}/status`

**Update Opportunity Status**

Update Opportunity Status

**Operation ID:** `update-opportunity-status`

**Tags:** Opportunities

**Required Scopes:** `opportunities.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Opportunity Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | Yes |  |
| `lostReasonId` | string | No | lost reason Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/opportunities/upsert`

**Upsert Opportunity**

Upsert Opportunity

**Operation ID:** `Upsert-opportunity`

**Tags:** Opportunities

**Required Scopes:** `opportunities.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | opportunityId |
| `pipelineId` | string | Yes | pipeline Id |
| `locationId` | string | Yes | locationId |
| `followers` | array of string | Yes | contactId |
| `isRemoveAllFollowers` | boolean | Yes | isRemoveAllFollowers |
| `followersActionType` | string (enum: `add`, `remove`) | Yes | followers action type |
| `name` | string | No | name |
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | No |  |
| `pipelineStageId` | string | No |  |
| `monetaryValue` | object | No |  |
| `assignedTo` | string | No |  |
| `lostReasonId` | string | No | lost reason Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunity` | object | Yes | Updated / New Opportunity |
| `new` | boolean | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/opportunities/`

**Create Opportunity**

Create Opportunity

**Operation ID:** `create-opportunity`

**Tags:** Opportunities

**Required Scopes:** `opportunities.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pipelineId` | string | Yes | pipeline Id |
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `pipelineStageId` | string | No |  |
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | Yes |  |
| `contactId` | string | Yes |  |
| `monetaryValue` | number | No |  |
| `assignedTo` | string | No |  |
| `customFields` | array of object | object | object | No | Add custom fields to opportunities. |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunity` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Followers

### POST `/opportunities/{id}/followers`

**Add Followers**

Add Followers

**Operation ID:** `add-followers-opportunity`

**Tags:** Followers

**Required Scopes:** `opportunities.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Opportunity Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | Yes |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersAdded` | array of string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/opportunities/{id}/followers`

**Remove Followers**

Allows removal of one or all followers from an opportunity.

**Operation ID:** `remove-followers-opportunity`

**Tags:** Followers

**Required Scopes:** `opportunities.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Opportunity Id |
| `isRemoveAllFollowers` | query | boolean | No |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | Yes |  |

#### Responses

**`200` - Followers successfully removed.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersRemoved` | array of string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AdditionalDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notes` | boolean | Yes |  |
| `tasks` | boolean | Yes |  |
| `calendarEvents` | boolean | Yes |  |
| `unReadConversations` | boolean | Yes |  |

### CreateAddFollowersSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersAdded` | array of string | No |  |

### CreateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pipelineId` | string | Yes | pipeline Id |
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `pipelineStageId` | string | No |  |
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | Yes |  |
| `contactId` | string | Yes |  |
| `monetaryValue` | number | No |  |
| `assignedTo` | string | No |  |
| `customFields` | array of object | object | object | No | Add custom fields to opportunities. |

### CustomFieldResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `fieldValue` | string | object | array of string | array of object | Yes | The value of the custom field |

### DeleteFollowersSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersRemoved` | array of string | No |  |

### DeleteUpdateOpportunitySuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### FollowersDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | Yes |  |

### GetPipelinesSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pipelines` | array of object | No |  |

### GetPostOpportunitySuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunity` | object | No |  |

### LostReasonResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | lost reason id |
| `name` | string | No | lost reason name |
| `locationId` | string | No | location id |
| `updatedAt` | string | No | updated at |
| `createdAt` | string | No | created at |

### LostReasonsResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `lostReasons` | array of object | No |  |
| `total` | number | No |  |

### OpportunitySearchBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `query` | string | Yes |  |
| `limit` | number | Yes |  |
| `page` | number | Yes |  |
| `searchAfter` | array of string | Yes |  |
| `additionalDetails` | object | Yes |  |

### PipelinesResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `stages` | array of array of any | No |  |
| `showInFunnel` | boolean | No |  |
| `showInPieChart` | boolean | No |  |
| `locationId` | string | No |  |
| `colorRenderMode` | string (enum: `dot`, `bg-tint`, `none`) | No | How pipeline/stage colors are rendered |

### PostSearchSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunities` | array of object | No |  |
| `total` | number | Yes |  |
| `aggregations` | object | No |  |

### SearchMetaResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | No |  |
| `nextPageUrl` | string | No |  |
| `startAfterId` | string | No |  |
| `startAfter` | number | No |  |
| `currentPage` | number | No |  |
| `nextPage` | number | No |  |
| `prevPage` | number | No |  |

### SearchOpportunitiesContactResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `companyName` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `tags` | array of string | No |  |

### SearchOpportunitiesResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `monetaryValue` | number | No |  |
| `pipelineId` | string | No |  |
| `pipelineStageId` | string | No |  |
| `assignedTo` | string | No |  |
| `status` | string | No |  |
| `source` | string | No |  |
| `lastStatusChangeAt` | string | No |  |
| `lastStageChangeAt` | string | No |  |
| `lastActionDate` | string | No |  |
| `indexVersion` | string | No |  |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |
| `contactId` | string | No |  |
| `locationId` | string | No |  |
| `contact` | object | No |  |
| `notes` | array of array of any | No |  |
| `tasks` | array of array of any | No |  |
| `calendarEvents` | array of array of any | No |  |
| `lostReasonId` | string | No |  |
| `customFields` | array of object | No |  |
| `followers` | array of array of any | No |  |
| `externalObjectId` | string | No |  |

### SearchSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunities` | array of object | No |  |
| `meta` | object | No |  |
| `aggregations` | object | No |  |

### UpdateOpportunityDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pipelineId` | string | No | pipeline Id |
| `name` | string | No |  |
| `pipelineStageId` | string | No |  |
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | No |  |
| `monetaryValue` | number | No |  |
| `assignedTo` | string | No |  |
| `customFields` | array of object | object | object | No | Update custom fields to opportunities. |

### UpdateStatusDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | Yes |  |
| `lostReasonId` | string | No | lost reason Id |

### UpsertOpportunityDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | opportunityId |
| `pipelineId` | string | Yes | pipeline Id |
| `locationId` | string | Yes | locationId |
| `followers` | array of string | Yes | contactId |
| `isRemoveAllFollowers` | boolean | Yes | isRemoveAllFollowers |
| `followersActionType` | string (enum: `add`, `remove`) | Yes | followers action type |
| `name` | string | No | name |
| `status` | string (enum: `open`, `won`, `lost`, `abandoned`, `all`) | No |  |
| `pipelineStageId` | string | No |  |
| `monetaryValue` | object | No |  |
| `assignedTo` | string | No |  |
| `lostReasonId` | string | No | lost reason Id |

### UpsertOpportunitySuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `opportunity` | object | Yes | Updated / New Opportunity |
| `new` | boolean | Yes |  |

### customFieldsInputArraySchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | array of string | No |  |

### customFieldsInputObjectSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | object | No |  |

### customFieldsInputStringSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Pass either `id` or `key` of custom field |
| `key` | string | No | Pass either `id` or `key` of custom field |
| `field_value` | string | No |  |
