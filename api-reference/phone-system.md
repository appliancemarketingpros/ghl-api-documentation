# Phone System API

Documentation for Phone System API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Number Pools](#number-pools)
- [Phone Numbers](#phone-numbers)

## Number Pools

### GET `/phone-system/number-pools`

**List Number Pools**

Get list of number pools

**Operation ID:** `getNumberPoolList`

**Tags:** Number Pools

**Required Scopes:** `numberpools.read`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | No | Location ID to filter pools |

#### Responses

**`200` - Successfully retrieved number pools list**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Indicates if the request was successful |
| `data` | array of object | No | Array of number pool objects |
| `total` | number | No | Total number of pools returned |

**Response Example:**

```json
{
  "success": true,
  "data": [
    {
      "id": "ve9EPM428h8vShlRW1KT",
      "name": "Sales Team Pool",
      "locationId": "loc123",
      "numbers": [
        {
          "phoneNumber": "+14155552671",
          "friendlyName": "Sales Line 1"
        }
      ],
      "forwardingNumber": "+14155552671",
      "whisper": true,
      "whisperMessage": "Incoming call from sales line",
      "callRecording": true,
      "isActive": true,
      "inboundCallService": {
        "type": "voice_ai",
        "value": "68e381b296a83800a27cd1"
      }
    }
  ],
  "total": 1
}
```

**`400` - Bad request - Invalid location ID or parameters**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No |  |
| `error` | string | No |  |
| `statusCode` | number | No |  |

**`401` - Unauthorized - Invalid or missing authentication token**

**`403` - Forbidden - Insufficient permissions for this location**

---

## Phone Numbers

### GET `/phone-system/numbers/location/{locationId}`

**List active numbers**

Retrieve a paginated list of active phone numbers for a specific location. Supports filtering, pagination, and optional exclusion of number pool assignments.

**Operation ID:** `active-numbers`

**Tags:** Phone Numbers

**Required Scopes:** `phonenumbers.read`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | The unique identifier of the location |
| `pageSize` | query | number | No | How many resources to return in each list page. The default is 50, and the maximum is 1000. |
| `page` | query | number | No | The page index for pagination. The default is 0. |
| `searchFilter` | query | string | No | Filter numbers by phone number pattern. Supports partial matching (e.g., "+91" to find all Indian numbers). |
| `skipNumberPool` | query | boolean | No | Whether to exclude numbers that are assigned to number pools. Default is true. |

#### Responses

**`200` - Successfully retrieved list of active numbers**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `numbers` | array of object | Yes | Array of phone number objects with detailed configuration |
| `isUnderGhl` | boolean | Yes | Whether this account is manged by LeadconnectorHQ |
| `pageSize` | number | Yes | Number of items requested per page |
| `page` | number | Yes | Current page index (0-based) |
| `accountStatus` | string (enum: `active`, `suspended`, `closed`) | Yes | Current status of the account |

**Response Example:**

```json
{
  "numbers": [
    {
      "phoneNumber": "+14155552671",
      "friendlyName": "Sales Line 1",
      "sid": "PN1234567890abcdef1234567890abcde",
      "countryCode": "US",
      "capabilities": {
        "voice": true,
        "sms": true,
        "mms": true,
        "fax": false
      },
      "type": "local",
      "isDefaultNumber": true,
      "linkedUser": "user_123456789",
      "linkedRingAllUsers": [
        "user_123",
        "user_456"
      ],
      "inboundCallService": {
        "type": "voice_ai",
        "value": "68e381b296a83800a27cd1"
      },
      "forwardingNumber": "+14155552672",
      "isGroupConversationEnabled": true,
      "addressSid": "AD1234567890abcdef1234567890abcde",
      "bundleSid": "BU1234567890abcdef1234567890abcde",
      "dateAdded": "2023-01-15T10:30:00Z",
      "dateUpdated": "2023-02-20T14:45:00Z",
      "origin": "twilio"
    },
    {
      "phoneNumber": "+18005551234",
      "friendlyName": "Support Toll-Free",
      "sid": "PN9876543210fedcba9876543210fedcb",
      "countryCode": "US",
      "capabilities": {
        "voice": true,
        "sms": false,
        "mms": false,
        "fax": false
      },
      "type": "toll-free",
      "isDefaultNumber": false,
      "linkedUser": null,
      "linkedRingAllUsers": [
        "user_789",
        "user_101"
      ],
      "inboundCallService": null,
      "forwardingNumber": null,
      "isGroupConversationEnabled": false,
      "addressSid": null,
      "bundleSid": null,
      "dateAdded": "2023-01-16T14:20:00Z",
      "dateUpdated": "2023-01-16T14:20:00Z",
      "origin": "twilio"
    }
  ],
  "isUnderGhl": true,
  "pageSize": 100,
  "page": 0,
  "accountStatus": "active"
}
```

**`400` - Bad request - Invalid parameters**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No |  |
| `error` | string | No |  |
| `statusCode` | number | No |  |

**`401` - Unauthorized**

**`404` - Phone system not connected**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No |  |
| `statusCode` | number | No |  |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `msg` | string | No |  |
| `accountStatus` | string | No | Account status when error occurs |

---

## Schemas

### DetailedPhoneNumberDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `phoneNumber` | string | Yes | E.164 formatted phone number |
| `friendlyName` | string | No | Human-readable name assigned to the number |
| `sid` | string | Yes | Phone number SID (unique identifier) |
| `countryCode` | string | Yes | ISO 3166-1 alpha-2 country code |
| `capabilities` | object | Yes | Communication capabilities supported by this number |
| `type` | string (enum: `local`, `toll-free`, `mobile`, `national`) | Yes | Type of phone number (local, toll-free, mobile, etc.) |
| `isDefaultNumber` | boolean | Yes | Whether this is the default outbound number for the location |
| `linkedUser` | string | No | User ID of the user assigned to this number |
| `linkedRingAllUsers` | array of string | Yes | Array of user IDs that should ring when this number is called |
| `inboundCallService` | object | No | Configuration for inbound call handling service |
| `forwardingNumber` | string | No | Phone number to forward calls to |
| `isGroupConversationEnabled` | boolean | Yes | Whether group conversations are enabled for this number (US/CA numbers with SMS/MMS only) |
| `addressSid` | string | No | Address SID for compliance purposes |
| `bundleSid` | string | No | Bundle SID for regulatory compliance |
| `dateAdded` | string | No | When the number was originally purchased/added |
| `dateUpdated` | string | No | When the number configuration was last updated |
| `origin` | string (enum: `twilio`, `hosted`, `ported`) | No | Source or origin of the phone number |

### NumberPoolDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Unique identifier for the number pool |
| `name` | string | No | Human-readable name of the number pool |
| `locationId` | string | No | Location ID this pool belongs to |
| `numbers` | array of object | No | Phone numbers in this pool |
| `forwardingNumber` | string | No | Number to forward calls to |
| `whisper` | boolean | No | Whether whisper is enabled |
| `whisperMessage` | string | No | Message played during whisper |
| `callRecording` | boolean | No | Whether call recording is enabled |
| `isActive` | boolean | No | Whether the number pool is active |
| `inboundCallService` | object | No | Inbound call service configuration |
