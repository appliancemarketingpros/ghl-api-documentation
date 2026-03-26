# Forms API

Documentation for forms API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Forms](#forms)

## Forms

### GET `/forms/submissions`

**Get Forms Submissions**

Get Forms Submissions

**Operation ID:** `get-forms-submissions`

**Tags:** Forms

**Required Scopes:** `forms.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `page` | query | number | No | Page No. By default it will be 1 |
| `limit` | query | number | No | Limit Per Page records count. will allow maximum up to 100 and default will be 20 |
| `formId` | query | string | No | Filter submission by form id |
| `q` | query | string | No | Filter by contactId, name, email or phone no. |
| `startAt` | query | string | No | Get submission by starting of this date. By default it will be same date of last month(YYYY-MM-DD). |
| `endAt` | query | string | No | Get submission by ending of this date. By default it will be current date(YYYY-MM-DD). |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `submissions` | array of object | No |  |
| `meta` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/forms/upload-custom-files`

**Upload files to custom fields**

Post the necessary fields for the API to upload files. The files need to be a buffer with the key "_".  Here custom field id is the ID of your custom field and file id is a randomly generated id (or uuid)  There is support for multiple file uploads as well. Have multiple fields in the format mentioned.File size is limited to 50 MB. The allowed file types are: 
 PDFDOCXDOCJPGJPEGPNGGIFCSVXLSXXLSMP4MPEGZIPRARTXTSVG  The API will return the updated contact object.

**Operation ID:** `upload-to-custom-fields`

**Tags:** Forms

**Required Scopes:** `forms.write`, `forms.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | query | string | Yes | Contact ID to upload the file to. |
| `locationId` | query | string | Yes | Location ID of the contact. |

#### Request Body

**Required:** Yes

**Content Type:** `multipart/form-data`

#### Responses

**`200` - Successful response**

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/forms/`

**Get Forms**

Get Forms

**Operation ID:** `get-forms`

**Tags:** Forms

**Required Scopes:** `forms.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `skip` | query | number | No |  |
| `limit` | query | number | No | Limit Per Page records count. will allow maximum up to 50 and default will be 10 |
| `type` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `forms` | array of object | No |  |
| `total` | number | No | Total number of forms |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Schemas

### ContactSessionIds

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ids` | array of string | No |  |

### EventDataSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fbc` | string | No |  |
| `fbp` | string | No |  |
| `page` | object | No |  |
| `type` | string | No |  |
| `domain` | string | No |  |
| `medium` | string | No |  |
| `source` | string | No |  |
| `version` | string | No |  |
| `adSource` | string | No |  |
| `mediumId` | string | No |  |
| `parentId` | string | No |  |
| `referrer` | string | No |  |
| `fbEventId` | string | No |  |
| `timestamp` | number | No |  |
| `parentName` | string | No |  |
| `fingerprint` | string | No |  |
| `pageVisitType` | string | No |  |
| `contactSessionIds` | object | No |  |

### FormsParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `locationId` | string | No |  |

### FormsSubmissionsSubmissionsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `contactId` | string | No |  |
| `createdAt` | string | No |  |
| `formId` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `others` | object | No |  |

### FormsSubmissionsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `submissions` | array of object | No |  |
| `meta` | object | No |  |

### FormsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `forms` | array of object | No |  |
| `total` | number | No | Total number of forms |

### PageDetailsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | No |  |
| `title` | string | No |  |

### metaSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | No |  |
| `currentPage` | number | No |  |
| `nextPage` | number | No |  |
| `prevPage` | number | No |  |

### othersSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `__submissions_other_field__` | string | No |  |
| `__custom_field_id__` | string | No |  |
| `eventData` | object | No |  |
| `fieldsOriSequance` | array of string | No |  |
