# Campaigns API

Documentation for campaigns API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Campaigns](#campaigns)

## Campaigns

### GET `/campaigns/`

**Get Campaigns**

Get Campaigns

**Operation ID:** `get-campaigns`

**Tags:** Campaigns

**Required Scopes:** `campaigns.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `status` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaigns` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### CampaignsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaigns` | array of object | No |  |

### campaignsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `status` | string | No |  |
| `locationId` | string | No |  |
