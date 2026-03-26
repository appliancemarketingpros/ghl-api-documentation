# Proposals & Estimates API

Documentation for Documents and Contracts API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Documents](#documents)
- [Templates](#templates)

## Documents

### GET `/proposals/document`

**List documents**

List documents for a location

**Operation ID:** `list-documents-contracts`

**Tags:** Documents

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | query | string | Yes | Location Id |
| `status` | query | string (enum: `draft`, `sent`, `viewed`, `completed`, `accepted`) | No | Document status, pass as comma separated values |
| `paymentStatus` | query | string (enum: `waiting_for_payment`, `paid`, `no_payment`) | No | Payment status, pass as comma separated values |
| `limit` | query | number | No | Limit to fetch number of records |
| `skip` | query | number | No | Skip number of records |
| `query` | query | string | No | Search string |
| `dateFrom` | query | string | No | Date start from (ISO 8601), dateFrom & DateTo must be provided together |
| `dateTo` | query | string | No | Date to (ISO 8601), dateFrom & DateTo must be provided together |

#### Responses

**`200` - Document fetched successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `documents` | array of object | Yes | List of documents |
| `total` | number | Yes | Total records available |
| `whiteLabelBaseUrl` | number | No | WhiteLabel url for document |
| `whiteLabelBaseUrlForInvoice` | number | No | WhiteLabel url for invoice |

**`400` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/proposals/document/send`

**Send document**

Send document to a client

**Operation ID:** `send-documents-contracts`

**Tags:** Documents

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `documentId` | string | Yes | Document Id |
| `documentName` | string | No | Document Name |
| `medium` | string (enum: `link`, `email`) | No | Medium to be used for sending the document |
| `ccRecipients` | array of object | No | CC Recipient |
| `notificationSettings` | object | No |  |
| `sentBy` | string | Yes | Sent ByUser Id |

**`ccRecipients` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | string | Yes | Email |
| `id` | string | Yes | Contact ID |
| `imageUrl` | string | Yes | Contact Image URL |
| `contactName` | string | Yes | Contact Name |
| `firstName` | string | Yes | First Name |
| `lastName` | string | Yes | Last Name |

**`notificationSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `receive` | object | Yes |  |
| `sender` | object | Yes |  |

#### Responses

**`200` - Document sent successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `links` | array of object | Yes | Links for all recipients |

**`400` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

## Templates

### GET `/proposals/templates`

**List templates**

List document contract templates for a location

**Operation ID:** `list-documents-contracts-templates`

**Tags:** Templates

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | query | string | Yes | Location Id |
| `dateFrom` | query | string | No | Date start from (ISO 8601) |
| `dateTo` | query | string | No | Date to (ISO 8601) |
| `type` | query | string | No | Comma-separated template types. Valid values: proposal, estimate, contentLibrary |
| `name` | query | string | No | Template Name |
| `isPublicDocument` | query | boolean | No | If the docForm is a DocForm |
| `userId` | query | string | No | User Id, required when isPublicDocument is true |
| `limit` | query | string | No | Limit |
| `skip` | query | string | No | Skip |

#### Responses

**`200` - Templates fetched successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes | Array of templates |
| `total` | number | Yes | Total number of templates |
| `traceId` | string | No | Trace ID for request tracking |

**`400` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/proposals/templates/send`

**Send template**

Send template to a client

**Operation ID:** `send-documents-contracts-template`

**Tags:** Templates

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `templateId` | string | Yes | Template Id |
| `userId` | string | Yes | User Id |
| `sendDocument` | boolean | No | Send Document |
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `opportunityId` | string | No | Opportunity Id |

#### Responses

**`200` - Document sent successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `links` | array of object | Yes | Links for all recipients |

**`400` - Unprocessable Entity**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

## Schemas

### BadRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

### CCRecipientItem

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | string | Yes | Email |
| `id` | string | Yes | Contact ID |
| `imageUrl` | string | Yes | Contact Image URL |
| `contactName` | string | Yes | Contact Name |
| `firstName` | string | Yes | First Name |
| `lastName` | string | Yes | Last Name |

### DiscountDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the discount |
| `value` | number | Yes | Discount value (either a percentage or custom amount) |
| `type` | string (enum: `percentage`, `custom_amount`) | Yes | Type of discount |

### DocumentDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `documentId` | string | Yes | Document Id |
| `_id` | string | Yes | Unique identifier |
| `name` | string | Yes | Name of the document |
| `type` | string | Yes | Type of the document |
| `deleted` | boolean | Yes | Whether the document is deleted |
| `isExpired` | boolean | Yes | Whether the document is expired |
| `documentRevision` | number | Yes | Number of times document is moved to draft state |
| `fillableFields` | array of object | Yes | Fillable fields |
| `grandTotal` | object | Yes |  |
| `locale` | string | Yes | Locale of the location |
| `status` | array of string (enum: `draft`, `sent`, `viewed`, `completed`, `accepted`) | Yes | Document status |
| `paymentStatus` | array of string (enum: `waiting_for_payment`, `paid`, `no_payment`) | Yes | Payment status |
| `recipients` | array of object | Yes | Recipients |
| `links` | array of object | Yes | Links for the document if its sent |
| `updatedAt` | string | Yes | Date start from (ISO 8601) |
| `createdAt` | string | Yes | Date to (ISO 8601) |

### DocumentListResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `documents` | array of object | Yes | List of documents |
| `total` | number | Yes | Total records available |
| `whiteLabelBaseUrl` | number | No | WhiteLabel url for document |
| `whiteLabelBaseUrlForInvoice` | number | No | WhiteLabel url for invoice |

### ELEMENTS_LOOKUP

Element type

**Type:** `string`

**Possible Values:**

- `Page`
- `Text`
- `Image`
- `Video`
- `Table`
- `ProductList`
- `PageBreak`
- `Signature`
- `PaymentDetails`
- `TextField`
- `DateField`
- `InitialsField`
- `Checkbox`
- `Row`
- `Column`

### EntityReference

Entity type

**Type:** `string`

**Possible Values:**

- `contacts`
- `users`

### FillableFieldsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fieldId` | string | Yes | Field Id |
| `isRequired` | boolean | Yes | Is the field required |
| `hasCompleted` | boolean | Yes | Has the field been completed |
| `recipient` | string | Yes | Recipient |
| `entityType` | string (enum: `contacts`, `users`) | Yes | Entity type |
| `id` | string | Yes | Id |
| `type` | string (enum: `Page`, `Text`, `Image`, `Video`, `Table`, `ProductList`, `PageBreak`, `Signature`, `PaymentDetails`, `TextField`, `DateField`, `InitialsField`, `Checkbox`, `Row`, `Column`) | Yes | Element type |
| `value` | string | Yes | Value of the field |

### GrandTotalDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | number | Yes | Total amount before discounts |
| `currency` | string | Yes | Currency of the total amount |
| `discountPercentage` | number | Yes | Total discount percentage applied |
| `discounts` | array of object | Yes | List of applied discounts |

### NotificationSendSettingDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `templateId` | string | Yes |  |
| `subject` | string | Yes |  |

### NotificationSenderSettingDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fromEmail` | string | Yes |  |
| `fromName` | string | Yes |  |

### NotificationSettingsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `receive` | object | Yes |  |
| `sender` | object | Yes |  |

### ProposalEstimateLinksDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `referenceId` | string | Yes | Reference ID |
| `documentId` | string | Yes | Document ID |
| `recipientId` | string | Yes | Recipient ID |
| `entityName` | string (enum: `contacts`, `users`) | Yes | Entity name that the recipient belongs to |
| `recipientCategory` | string (enum: `recipient`, `cc`, `bcc`) | Yes | Recipient category (recipient, cc, or bcc) |
| `documentRevision` | number | Yes | Document revision number |
| `createdBy` | string | Yes | Created by user ID |
| `deleted` | boolean | Yes | Whether the document is deleted |

### RecipientItem

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Recipient Id |
| `firstName` | string | No | Recipient First Name |
| `lastName` | string | No | Recipient Last Name |
| `email` | string | Yes | Recipient Email |
| `phoneNumber` | string | No | Recipient Phone Number |
| `phone` | string | No | Recipient Phone |
| `hasCompleted` | boolean | Yes | Recipient has completed the document |
| `role` | string (enum: `user`, `signer`) | Yes | Recipient role |
| `isPrimary` | boolean | Yes | Recipient is primary |
| `signingOrder` | number | Yes | Recipient signing order |
| `imgUrl` | string | No | Recipient image url |
| `ip` | string | No | Recipient ip |
| `userAgent` | string | No | Recipient user agent |
| `signedDate` | string | No | Recipient signed date |
| `contactName` | string | No | Recipient contact name |
| `country` | string | No | Recipient country |
| `entityName` | string | No | Recipient entity name |
| `initialsImgUrl` | string | No | Recipient initials image url |
| `lastViewedAt` | string | No | Recipient last viewed date |
| `shareLink` | string | No | Share link |

### SendDocumentDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `documentId` | string | Yes | Document Id |
| `documentName` | string | No | Document Name |
| `medium` | string (enum: `link`, `email`) | No | Medium to be used for sending the document |
| `ccRecipients` | array of object | No | CC Recipient |
| `notificationSettings` | object | No |  |
| `sentBy` | string | Yes | Sent ByUser Id |

### SendDocumentFromPublicApiBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `templateId` | string | Yes | Template Id |
| `userId` | string | Yes | User Id |
| `sendDocument` | boolean | No | Send Document |
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `opportunityId` | string | No | Opportunity Id |

### SendDocumentResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `links` | array of object | Yes | Links for all recipients |

### SendTemplateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `links` | array of object | Yes | Links for all recipients |

### TemplateListPaginationResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes | Array of templates |
| `total` | number | Yes | Total number of templates |
| `traceId` | string | No | Trace ID for request tracking |

### TemplateListResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template ID |
| `deleted` | boolean | Yes | Whether the template is deleted |
| `version` | number | Yes | Template version |
| `name` | string | Yes | Template name |
| `locationId` | string | Yes | Location ID |
| `type` | string (enum: `proposal`, `estimate`, `contentLibrary`) | Yes | Template type |
| `updatedBy` | string | Yes | User ID who last updated the template |
| `isPublicDocument` | boolean | Yes | Whether the template is a public document |
| `createdAt` | string | Yes | Template creation date |
| `updatedAt` | string | Yes | Template last update date |
| `id` | string | Yes | Template ID (alias for _id) |
| `documentCount` | number | No | Document count (only present when isPublicDocument is true) |
| `docFormUrl` | string | No | Document form URL (only present when isPublicDocument is true) |

### UnauthorizedDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |
