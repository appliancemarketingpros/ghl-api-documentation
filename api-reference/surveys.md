# Surveys API

Documentation for surveys API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Surveys](#surveys)

## Surveys

### GET `/surveys/submissions`

**Get Surveys Submissions**

Get Surveys Submissions

**Operation ID:** `get-surveys-submissions`

**Tags:** Surveys

**Required Scopes:** `surveys.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `page` | query | number | No | Page No. By default it will be 1 |
| `limit` | query | number | No | Limit Per Page records count. will allow maximum up to 100 and default will be 20 |
| `surveyId` | query | string | No | Filter submission by survey id |
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

### GET `/surveys/`

**Get Surveys**

Get Surveys

**Operation ID:** `get-surveys`

**Tags:** Surveys

**Required Scopes:** `surveys.readonly`

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
| `surveys` | array of object | No |  |
| `total` | number | No | Number of surveys |

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

### GetSurveysSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `locationId` | string | No |  |

### GetSurveysSubmissionSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `submissions` | array of object | No |  |
| `meta` | object | No |  |

### GetSurveysSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `surveys` | array of object | No |  |
| `total` | number | No | Number of surveys |

### PageDetailsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | No |  |
| `title` | string | No |  |

### SubmissionSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `contactId` | string | No |  |
| `createdAt` | string | No |  |
| `surveyId` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `others` | object | No |  |

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
