# Businesses API

Documentation for business API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Businesses](#businesses)

## Businesses

### PUT `/businesses/{businessId}`

**Update Business**

Update Business

**Operation ID:** `update-business`

**Tags:** Businesses

**Required Scopes:** `businesses.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `businessId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No |  |
| `phone` | string | No |  |
| `email` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `address` | string | No |  |
| `state` | string | No |  |
| `city` | string | No |  |
| `country` | string | No |  |
| `description` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success Value |
| `buiseness` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/businesses/{businessId}`

**Delete Business**

Delete Business

**Operation ID:** `delete-Business`

**Tags:** Businesses

**Required Scopes:** `businesses.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `businessId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success value |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/businesses/{businessId}`

**Get Business**

Get Business

**Operation ID:** `get-business`

**Tags:** Businesses

**Required Scopes:** `businesses.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `businessId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `business` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/businesses/`

**Get Businesses by Location**

Get Businesses by Location

**Operation ID:** `get-businesses-by-location`

**Tags:** Businesses

**Required Scopes:** `businesses.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `limit` | query | string | No |  |
| `skip` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `businesses` | array of object | Yes | Business Response |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/businesses/`

**Create Business**

Create Business

**Operation ID:** `create-business`

**Tags:** Businesses

**Required Scopes:** `businesses.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `locationId` | string | Yes |  |
| `phone` | string | No |  |
| `email` | string | No |  |
| `website` | string | No |  |
| `address` | string | No |  |
| `city` | string | No |  |
| `postalCode` | string | No |  |
| `state` | string | No |  |
| `country` | string | No |  |
| `description` | string | No |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success Value |
| `buiseness` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### BusinessCreatedByOrUpdatedBy

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### BusinessDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Business Id |
| `name` | string | Yes | Business Name |
| `phone` | string | No | phone number |
| `email` | string | No | email |
| `website` | string | No | website |
| `address` | string | No | address |
| `city` | string | No | city |
| `description` | string | No | description |
| `state` | string | No | state |
| `postalCode` | string | No | postal code |
| `country` | string | No | country |
| `updatedBy` | object | No |  |
| `locationId` | string | Yes | locaitonId |
| `createdBy` | object | No |  |
| `createdAt` | string | No | Creation Time |
| `updatedAt` | string | No | Last updation time |

### CreateBusinessDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `locationId` | string | Yes |  |
| `phone` | string | No |  |
| `email` | string | No |  |
| `website` | string | No |  |
| `address` | string | No |  |
| `city` | string | No |  |
| `postalCode` | string | No |  |
| `state` | string | No |  |
| `country` | string | No |  |
| `description` | string | No |  |

### DeleteBusinessResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success value |

### GetBusinessByIdResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `business` | object | Yes |  |

### GetBusinessByLocationResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `businesses` | array of object | Yes | Business Response |

### UpdateBusinessDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No |  |
| `phone` | string | No |  |
| `email` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `address` | string | No |  |
| `state` | string | No |  |
| `city` | string | No |  |
| `country` | string | No |  |
| `description` | string | No |  |

### UpdateBusinessResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success Value |
| `buiseness` | object | Yes |  |
