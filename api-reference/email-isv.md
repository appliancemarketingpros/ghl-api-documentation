# LC Email API

Documentation for Email ISV API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Email Verification](#email-verification)

## Email Verification

### POST `/email/verify`

**Email Verification**

Verify Email

**Operation ID:** `verify-email`

**Tags:** Email Verification

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id, The email verification charges will be deducted from this location (if rebilling is enabled) / company wallet |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `email`, `contact`) | Yes | Email Verification type |
| `verify` | string | Yes | Email Verification recepient (email address / contactId) |

#### Responses

**`201` - Successful response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### EmailNotVerifiedResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verified` | boolean | Yes | Email verification not processed |
| `message` | string | No | Email verification failure message |
| `address` | string | No | Email address |

### EmailVerifiedResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `reason` | array of string | No | Reason for email verification failure |
| `result` | string (enum: `deliverable`, `undeliverable`, `do_not_send`, `unknown`, `catch_all`) | Yes | Email verification result |
| `risk` | string (enum: `high`, `low`, `medium`, `unknown`) | Yes | Risk level of email sending to bounce |
| `address` | string | Yes | Email address |
| `leadconnectorRecomendation` | object | Yes |  |

### LeadConnectorRecomandationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEmailValid` | boolean | No | Email verification status |

### VerificationBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `email`, `contact`) | Yes | Email Verification type |
| `verify` | string | Yes | Email Verification recepient (email address / contactId) |
