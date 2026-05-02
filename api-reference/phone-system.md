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

### GET `/phone-system/numbers/location/{locationId}/available`

**List available phone numbers**

Search for available phone numbers to purchase for a specific location. Supports filtering by number pattern, type, and capabilities.

**Operation ID:** `available-numbers`

**Tags:** Phone Numbers

**Required Scopes:** `phonenumbers.read`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | The unique identifier of the location |
| `countryCode` | query | string | Yes | ISO 3166-1 alpha-2 country code for which to search available numbers |
| `numberTypes` | query | string | No | Comma-separated list of phone number types to search for (e.g. local, tollFree, mobile) |
| `firstPart` | query | string | No | Filter numbers that begin with this digit pattern |
| `lastPart` | query | string | No | Filter numbers that end with this digit pattern |
| `anywhere` | query | string | No | Filter numbers that contain this digit pattern anywhere |
| `smsEnabled` | query | boolean | No | Filter for numbers with SMS capability |
| `mmsEnabled` | query | boolean | No | Filter for numbers with MMS capability |
| `voiceEnabled` | query | boolean | No | Filter for numbers with voice capability |

#### Responses

**`200` - Successfully retrieved list of available phone numbers**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fingerprintId` | string | Yes | Unique fingerprint ID for this search result, required when purchasing one of the returned numbers |
| `numbers` | array of object | Yes | List of available phone numbers matching the search criteria |

**Response Example:**

```json
{
  "fingerprintId": "1773314252953",
  "numbers": [
    {
      "phoneNumber": "+18705871861",
      "friendlyName": "(870) 587-1861",
      "lata": "528",
      "locality": "Wynne",
      "rateCenter": "WYNNE",
      "latitude": "35.241800",
      "longitude": "-90.846000",
      "region": "AR",
      "postalCode": "72396",
      "isoCountry": "US",
      "addressRequirements": "none",
      "beta": false,
      "capabilities": {
        "MMS": true,
        "SMS": true,
        "voice": true
      },
      "price": {
        "number_type": "local",
        "price": 1.15,
        "price_unit": "USD"
      }
    }
  ]
}
```

**`400` - Bad request - Invalid parameters**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No |  |
| `error` | string | No |  |
| `statusCode` | number | No |  |

**`401` - Unauthorized**

**`500` - Internal server error**

---

### POST `/phone-system/numbers/location/{locationId}/purchase`

**Purchase a phone number**

Purchase a phone number for a specific location.

**Operation ID:** `purchase-phone-number`

**Tags:** Phone Numbers

**Required Scopes:** `phonenumbers.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | The unique identifier of the location |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `phoneNumber` | string | Yes | The phone number to purchase |
| `countryCode` | string | No | ISO 3166-1 alpha-2 country code of the number |
| `numberType` | string (enum: `local`, `tollFree`, `mobile`) | No | Type of phone number |
| `addressSid` | string | No | Twilio address SID for compliance |
| `bundleSid` | string | No | Twilio bundle SID for regulatory compliance |
| `locality` | string | No | Locality where the number is being purchased |
| `region` | string | No | Region where the number is being purchased |
| `fingerprintId` | string | No | Unique request ID for idempotency (fingerprint of the purchase request) |
| `skipLocationKYC` | boolean | No | Skip location-level KYC verification if agency-level compliance has already been verified |

#### Responses

**`201` - Phone number successfully purchased. Returns the updated Twilio account state for the location.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the Twilio account record |
| `account_sid` | string | Yes | Twilio Account SID |
| `under_ghl_account` | boolean | Yes | Whether this location is under a GHL-managed Twilio account |
| `validate_sms` | boolean | Yes | Whether SMS validation is enabled |
| `location_id` | string | Yes | The location ID this Twilio account belongs to |
| `migration_status` | string | No | Current migration status of the account |
| `migration_numbers` | array of string | No | List of numbers being migrated |
| `assigned_to_numbers` | object | No | Map of phone numbers to assigned user IDs |
| `numbers` | object | Yes | Map of phone numbers to their service type (e.g. 'conversation') |
| `number_name` | object | No | Map of phone numbers to their friendly names |
| `new_account_sid` | string | No | New account SID if the account has been migrated to new credentials |

**Response Example:**

```json
{
  "id": "8xMPW85D2z5jgcTa5L1p",
  "account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "under_ghl_account": true,
  "validate_sms": true,
  "location_id": "aa4PBpxnPc9bs4LSdiW7",
  "migration_numbers": [],
  "assigned_to_numbers": {},
  "numbers": {
    "+18705871861": "conversation"
  },
  "number_name": {
    "+18705871861": "My Number"
  },
  "new_account_sid": ""
}
```

**`400` - Bad request - Invalid parameters or number unavailable**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No |  |
| `error` | string | No |  |
| `statusCode` | number | No |  |

**`401` - Unauthorized**

**`500` - Internal server error - An unexpected error occurred while purchasing the phone number**

---

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

### AvailableNumbersResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fingerprintId` | string | Yes | Unique fingerprint ID for this search result, required when purchasing one of the returned numbers |
| `numbers` | array of object | Yes | List of available phone numbers matching the search criteria |

### AvailablePhoneNumberDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `phoneNumber` | string | Yes | E.164 formatted phone number |
| `friendlyName` | string | Yes | Human-readable formatted phone number |
| `isoCountry` | string | Yes | ISO 3166-1 alpha-2 country code |
| `lata` | string | No | Local Access and Transport Area code |
| `locality` | string | No | City or locality of the number |
| `rateCenter` | string | No | Rate center of the number |
| `latitude` | string | No | Latitude coordinate of the number's location |
| `longitude` | string | No | Longitude coordinate of the number's location |
| `region` | string | No | State or region abbreviation |
| `postalCode` | string | No | Postal code of the number |
| `addressRequirements` | string (enum: `none`, `any`, `local`, `foreign`) | Yes | Address requirements for purchasing this number |
| `beta` | boolean | Yes | Whether this is a beta number |
| `capabilities` | object | Yes | Communication capabilities supported by this number |
| `price` | object | No | Pricing information for this number |

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

### PurchasePhoneNumberBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `phoneNumber` | string | Yes | The phone number to purchase |
| `countryCode` | string | No | ISO 3166-1 alpha-2 country code of the number |
| `numberType` | string (enum: `local`, `tollFree`, `mobile`) | No | Type of phone number |
| `addressSid` | string | No | Twilio address SID for compliance |
| `bundleSid` | string | No | Twilio bundle SID for regulatory compliance |
| `locality` | string | No | Locality where the number is being purchased |
| `region` | string | No | Region where the number is being purchased |
| `fingerprintId` | string | No | Unique request ID for idempotency (fingerprint of the purchase request) |
| `skipLocationKYC` | boolean | No | Skip location-level KYC verification if agency-level compliance has already been verified |

### TwilioAccountResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the Twilio account record |
| `account_sid` | string | Yes | Twilio Account SID |
| `under_ghl_account` | boolean | Yes | Whether this location is under a GHL-managed Twilio account |
| `validate_sms` | boolean | Yes | Whether SMS validation is enabled |
| `location_id` | string | Yes | The location ID this Twilio account belongs to |
| `migration_status` | string | No | Current migration status of the account |
| `migration_numbers` | array of string | No | List of numbers being migrated |
| `assigned_to_numbers` | object | No | Map of phone numbers to assigned user IDs |
| `numbers` | object | Yes | Map of phone numbers to their service type (e.g. 'conversation') |
| `number_name` | object | No | Map of phone numbers to their friendly names |
| `new_account_sid` | string | No | New account SID if the account has been migrated to new credentials |
