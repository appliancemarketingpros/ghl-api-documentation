# Knowledge Base API

Documentation for Knowledge Base API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Faqs](#faqs)
- [Web Crawler](#web-crawler)
- [Knowledge Base](#knowledge-base)

## Faqs

### GET `/knowledge-bases/faqs`

**Get all FAQs by knowledge base with pagination support**

Retrieves FAQs for a knowledge base. Supports pagination using limit and lastFaqId parameters.

**Operation ID:** `list`

**Tags:** Faqs

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `knowledgeBaseId` | query | string | Yes | knowledge base ID as string |
| `locationId` | query | string | Yes | location ID as string |
| `limit` | query | number | No | Limit the number of FAQs returned |
| `lastFaqId` | query | string | No | Last FAQ ID for pagination (cursor-based) |

#### Responses

**`200` - FAQs retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Total count of all FAQs in the knowledge base |
| `faqs` | array of object | Yes | Array of FAQ objects |
| `lastFaqId` | string | No | Last FAQ ID for pagination (use as lastFaqId in next request) |
| `hasMore` | boolean | No | Whether there are more FAQs available |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/knowledge-bases/faqs`

**Create a new FAQ inside knowledge base**

**Operation ID:** `create`

**Tags:** Faqs

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | location ID as string |
| `question` | string | Yes | faq question as a string |
| `answer` | string | Yes | faq answer as a string |
| `knowledgeBaseId` | string | Yes | knowledge base ID as string |

#### Responses

**`201` - FAQ created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `faq` | object | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### PUT `/knowledge-bases/faqs/{id}`

**Update an existing knowledge base FAQ**

**Operation ID:** `update`

**Tags:** Faqs

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `id` | path | string | Yes | faq ID as string |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `question` | string | Yes | faq question as a string |
| `answer` | string | Yes | faq answer as a string |

#### Responses

**`200` - FAQ updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the update operation |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### DELETE `/knowledge-bases/faqs/{id}`

**Delete an existing knowledge base FAQ**

**Operation ID:** `delete`

**Tags:** Faqs

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `id` | path | string | Yes | faq ID as string |

#### Responses

**`200` - FAQ deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the delete operation |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

## Web Crawler

### GET `/knowledge-bases/crawler`

**Get all trained page links by knowledge base**

**Operation ID:** `getAllWebsiteUrlsDataByKnowledgeBase`

**Tags:** Web Crawler

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `knowledgeBaseId` | query | string | Yes | knowledge base ID as string |
| `locationId` | query | string | Yes | location ID as string |
| `page` | query | number | No | Page number |
| `pageLength` | query | number | No | Records per page |
| `query` | query | string | No | query to filter on url links |

#### Responses

**`200` - Trained page links retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Total count of URLs in the knowledge base |
| `urls` | array of object | Yes | Array of crawled URLs with their details |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/knowledge-bases/crawler`

**Start crawling and discover pages for training**

**Operation ID:** `discoverWebsite`

**Tags:** Web Crawler

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `url` | string | Yes | Website URL as string |
| `option` | string (enum: `Exact`, `Path`, `Domain`) | Yes | Mode as string |
| `knowledgeBaseId` | string | Yes | knowledge base ID as string |

#### Responses

**`201` - Crawling and discovery started successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |
| `data` | object | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### DELETE `/knowledge-bases/crawler`

**Delete trained pages**

**Operation ID:** `deleteTrainedUrlsForKnowledgeBase`

**Tags:** Web Crawler

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `knowledgeBaseId` | string | Yes | knowledge base ID as string |
| `locationId` | string | Yes | location ID as string |
| `urlIds` | array of string | Yes | List of trained urls ids ( fetched from the Get all trained page links by knowledge base endpoint) |

#### Responses

**`200` - Selected pages deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### GET `/knowledge-bases/crawler/status`

**Get crawling status for the latest operation**

**Operation ID:** `getCrawlingStatusForLatestOperation`

**Tags:** Web Crawler

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | query | string | Yes | Location ID as string |
| `operationId` | query | string | Yes | operation id as string |
| `knowledgeBaseId` | query | string | Yes | knowledge base id |

#### Responses

**`200` - Operation status fetched successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |
| `data` | object | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/knowledge-bases/crawler/train`

**Train discovered website pages and ingest into the knowledge base**

**Operation ID:** `trainDiscoveredUrls`

**Tags:** Web Crawler

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `urlIds` | array of string | Yes | List of Object ids of the discovered urls |
| `knowledgeBaseId` | string | Yes | knowledge base id |
| `operationId` | string | Yes | operation id as string |

#### Responses

**`201` - Pages trained successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

**`422` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

## Knowledge Base

### GET `/knowledge-bases/{knowledgeBaseId}`

**Get knowledge base by ID**

**Operation ID:** `getKnowledgeBaseById`

**Tags:** Knowledge Base

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `knowledgeBaseId` | path | string | Yes |  |

#### Responses

**`200` - Knowledge base by ID retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `data` | object | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

---

### DELETE `/knowledge-bases/{knowledgeBaseId}`

**Delete a knowledge base**

**Operation ID:** `deleteKnowledgeBase`

**Tags:** Knowledge Base

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `knowledgeBaseId` | path | string | Yes |  |

#### Responses

**`200` - Knowledge base deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

---

### PUT `/knowledge-bases/{id}`

**Update a knowledge base**

**Operation ID:** `updateKnowledgeBase`

**Tags:** Knowledge Base

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `id` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | field to update the name of the knowledge base |
| `description` | string | No | field to update the description of the knowledge base |

#### Responses

**`200` - Knowledge base updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

---

### GET `/knowledge-bases/`

**Get all knowledge bases for a location by location Id (paginated)**

**Operation ID:** `listAllKnowledgeBasesPaginated`

**Tags:** Knowledge Base

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | query | string | Yes |  |
| `query` | query | string | No | search query for knowledge base name |
| `limit` | query | number | No | Maximum number of knowledge bases to return |
| `lastKnowledgeBaseId` | query | string | No | ID of the last knowledge base from the previous page (for pagination) |

#### Responses

**`200` - Paginated knowledge bases retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `data` | object | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

---

### POST `/knowledge-bases/`

**Create a new knowledge base (max 15 knowledge bases per location)**

**Operation ID:** `createKnowledgeBase`

**Tags:** Knowledge Base

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `description` | string | No |  |
| `locationId` | string | Yes |  |

#### Responses

**`201` - Knowledge base created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `data` | object | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

---

## Schemas

### AddFaqDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | location ID as string |
| `question` | string | Yes | faq question as a string |
| `answer` | string | Yes | faq answer as a string |
| `knowledgeBaseId` | string | Yes | knowledge base ID as string |

### BadRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

### CrawledUrlDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the URL |
| `url` | string | Yes | The actual URL that was crawled |
| `title` | string | Yes | Title of the webpage |
| `status` | string (enum: `Pending`, `Processing`, `Successful`, `Failed`, `Existing`, `Restricted`, `Cancelled`, `Aborted`, `Training`) | Yes | Current processing status of the URL |
| `locationId` | string | Yes | Location ID associated with this URL |
| `knowledgeBaseId` | string | Yes | Knowledge base ID this URL belongs to |
| `content` | string | Yes | URL to the stored content file |
| `contentEditedByUser` | boolean | Yes | Whether the content was edited by user |
| `updatedAt` | string | Yes | Last updated timestamp |

### CrawlingAggregateDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string (enum: `Pending`, `Processing`, `Successful`, `Failed`, `Existing`, `Restricted`, `Cancelled`, `Aborted`, `Training`) | Yes | Status grouping identifier |
| `records` | array of object | Yes | Array of records for this status |

### CrawlingRecordDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes | URL being crawled |
| `id` | string | Yes | Unique record identifier |
| `title` | string | No | Page title (for successful/pending records) |
| `error` | object | No |  |

### CrawlingStatusDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `aggregate` | array of object | Yes | Aggregated crawling results by status |
| `operationDetails` | object | Yes |  |

### CrawlingStatusResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |
| `data` | object | Yes |  |

### CreateFaqResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `faq` | object | Yes |  |

### CreateKnowledgeBaseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `description` | string | No |  |
| `locationId` | string | Yes |  |

### CreateKnowledgeBaseResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `data` | object | Yes |  |

### DeleteFaqResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the delete operation |

### DeleteKnowledgeBaseResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |

### DeleteWebsiteUrlRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `knowledgeBaseId` | string | Yes | knowledge base ID as string |
| `locationId` | string | Yes | location ID as string |
| `urlIds` | array of string | Yes | List of trained urls ids ( fetched from the Get all trained page links by knowledge base endpoint) |

### DeleteWebsiteUrlResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |

### DiscoverWebsiteDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operationId` | string | Yes | Operation ID for tracking the discovery process |
| `status` | string (enum: `Pending`, `Processing`, `Successful`, `Failed`, `Existing`, `Restricted`, `Cancelled`, `Aborted`, `Training`) | Yes | Current status of the website discovery operation |
| `url` | string | Yes | The URL being discovered/crawled |

### DiscoverWebsiteRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `url` | string | Yes | Website URL as string |
| `option` | string (enum: `Exact`, `Path`, `Domain`) | Yes | Mode as string |
| `knowledgeBaseId` | string | Yes | knowledge base ID as string |

### DiscoverWebsiteResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |
| `data` | object | Yes |  |

### ErrorDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stack` | string | Yes | Error stack trace |
| `response` | string | Yes | Error response message |
| `status` | number | Yes | HTTP status code |
| `options` | object | No | Additional options (nullable) |
| `message` | string | Yes | Error message |
| `name` | string | Yes | Error name/type |

### FaqResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | FAQ ID as string |
| `question` | string | Yes | FAQ question |
| `questionLowerCase` | string | Yes | FAQ question in lowercase |
| `answer` | string | Yes | FAQ answer |
| `knowledgeBaseId` | string | Yes | Knowledge base ID |
| `locationId` | string | Yes | Location ID |
| `trainedUrlId` | string | Yes | Trained URL ID |
| `deleted` | boolean | Yes | Whether the FAQ is deleted |
| `createdAt` | string | Yes | Date when FAQ was created |
| `updatedAt` | string | Yes | Date when FAQ was last updated |

### GetAllKnowledgeBasesPaginatedDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `knowledgeBases` | array of object | Yes | Array of knowledge bases |
| `activeCount` | number | Yes | Total count of all active knowledge bases |
| `hasMore` | boolean | Yes | Whether there are more knowledge bases available |
| `lastKnowledgeBaseId` | string | No | ID of the last knowledge base in this page (use for next page request) |

### GetAllKnowledgeBasesPaginatedResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `data` | object | Yes |  |

### GetAllUrlsByKnowledgeBaseResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Total count of URLs in the knowledge base |
| `urls` | array of object | Yes | Array of crawled URLs with their details |

### GetKnowledgeBaseByIdDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Knowledge base ID |
| `name` | string | Yes | Knowledge base name |
| `nameLowerCase` | string | Yes | Knowledge base name in lowercase |
| `locationId` | string | Yes | Location ID |
| `deleted` | boolean | Yes | Whether the knowledge base is deleted |
| `createdAt` | string | Yes | Date when knowledge base was created |
| `updatedAt` | string | Yes | Date when knowledge base was last updated |
| `kbMetadata` | object | Yes |  |
| `isDefault` | boolean | No | Whether the knowledge base is default or not |

### GetKnowledgeBaseByIdResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the operation |
| `data` | object | Yes |  |

### InternalServerErrorDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

### KnowledgeBaseDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Knowledge base ID |
| `name` | string | Yes | Knowledge base name |
| `nameLowerCase` | string | Yes | Knowledge base name in lowercase |
| `locationId` | string | Yes | Location ID |
| `kbMetadata` | object | Yes | Knowledge base metadata |
| `deleted` | boolean | Yes | Whether the knowledge base is deleted |
| `createdAt` | string | Yes | Date when knowledge base was created |
| `updatedAt` | string | Yes | Date when knowledge base was last updated |

### KnowledgeBaseListItemDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Knowledge base ID |
| `name` | string | Yes | Knowledge base name |
| `createdAt` | string | Yes | Date when knowledge base was created |

### KnowledgeBaseMetadataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `faqs` | number | Yes | Number of FAQs in the knowledge base |
| `urls` | number | Yes | Number of URLs in the knowledge base |
| `richText` | number | Yes | Number of rich text documents in the knowledge base |
| `files` | number | Yes | Number of files in the knowledge base |
| `webSearches` | number | Yes | Number of web searche configs in the knowledge base |
| `tables` | number | Yes | Number of tables in the knowledge base |

### ListFaqsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Total count of all FAQs in the knowledge base |
| `faqs` | array of object | Yes | Array of FAQ objects |
| `lastFaqId` | string | No | Last FAQ ID for pagination (use as lastFaqId in next request) |
| `hasMore` | boolean | No | Whether there are more FAQs available |

### OperationDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `discoveredUrlsCount` | number | Yes | Number of URLs discovered |
| `trainedUrlsCount` | number | Yes | Number of URLs successfully trained |
| `_id` | string | Yes | Operation unique identifier |
| `locationId` | string | Yes | Associated location ID |
| `status` | string (enum: `Pending`, `Processing`, `Successful`, `Failed`, `Existing`, `Restricted`, `Cancelled`, `Aborted`, `Training`) | Yes | Current operation status |
| `url` | string | Yes | Base URL being crawled |
| `mode` | string (enum: `Exact`, `Path`, `Domain`) | Yes | Crawling mode used |
| `knowledgeBaseId` | string | Yes | Knowledge base ID |
| `createdAt` | string | Yes | Operation creation timestamp |
| `updatedAt` | string | Yes | Last update timestamp |
| `__v` | number | Yes | Version field |
| `robotsFileData` | string | No | Robots.txt file content |

### TrainDiscoveredUrlsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `urlIds` | array of string | Yes | List of Object ids of the discovered urls |
| `knowledgeBaseId` | string | Yes | knowledge base id |
| `operationId` | string | Yes | operation id as string |

### TrainDiscoveredUrlsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the operation was successful |

### UnauthorizedDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

### UnprocessableDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array of string | No |  |
| `error` | string | No |  |

### UpdateFaqBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `question` | string | Yes | faq question as a string |
| `answer` | string | Yes | faq answer as a string |

### UpdateFaqResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the update operation |

### UpdateKnowledgeBaseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | field to update the name of the knowledge base |
| `description` | string | No | field to update the description of the knowledge base |

### UpdateKnowledgeBaseResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |
