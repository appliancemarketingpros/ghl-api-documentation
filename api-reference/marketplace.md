# Marketplace API

Documentation for Marketplace API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Wallet Charges](#wallet-charges)
- [App Management](#app-management)
- [App Billing Management](#app-billing-management)
- [External Auth Migration](#external-auth-migration)

## Wallet Charges

### POST `/marketplace/billing/charges`

**Create a new wallet charge**

Create a new wallet charge

**Operation ID:** `charge`

**Tags:** Wallet Charges

**Required Scopes:** `charges.write`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `appId` | string | Yes | App ID of the App |
| `meterId` | string | Yes | Billing Meter ID (you can find this on your app's pricing page) |
| `eventId` | string | Yes | Event ID / Transaction ID on your server's side. This will help you maintain the reference of the event/transaction on your end that you charged the customer for. |
| `userId` | string | No | User ID |
| `locationId` | string | Yes | ID of the Sub-Account to be charged |
| `companyId` | string | Yes | ID of the Agency the Sub-account belongs to |
| `description` | string | Yes | Description of the charge |
| `price` | number | No | Price per unit to charge |
| `units` | number | Yes | Number of units to charge |
| `eventTime` | string | No | The timestamp when the event/transaction was performed. If blank, the billing timestamp will be set as the event time. ISO8601 Format. |

#### Responses

**`201` - Charge created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Indicates whether the charge was created successfully |
| `chargeId` | string | No | Unique identifier of the created charge |

**`400` - Bad request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No | Error message describing the bad request |
| `statusCode` | number | No | HTTP status code |

**`422` - Unprocessable Entity**

---

### GET `/marketplace/billing/charges`

**Get all wallet charges**

Get all wallet charges

**Operation ID:** `getCharges`

**Tags:** Wallet Charges

**Required Scopes:** `charges.readonly`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `meterId` | query | string | No | Billing Meter ID (you can find this on your app's pricing page on the developer portal) |
| `eventId` | query | string | No | Event ID / Transaction ID |
| `userId` | query | string | No | Filter results by User ID that your server passed via API when the charge was created |
| `startDate` | query | string | No | Filter results AFTER a specific date. Use this in combination with endDate to filter results in a specific time window. |
| `endDate` | query | string | No | Filter results BEFORE a specific date. Use this in combination with startDate to filter results in a specific time window. |
| `skip` | query | number | No | Number of records to skip |
| `limit` | query | number | No | Maximum number of records to return |

#### Responses

**`200` - Returns list of wallet charges**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of object | No | List of wallet charges |
| `count` | number | No | Total number of charges |
| `pagination` | object | No | Pagination metadata for the charges list |

**`422` - Unprocessable Entity**

---

### DELETE `/marketplace/billing/charges/{chargeId}`

**Delete a wallet charge**

Delete a wallet charge

**Operation ID:** `deleteCharge`

**Tags:** Wallet Charges

**Required Scopes:** `charges.write`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `chargeId` | path | string | Yes | ID of the charge to delete |

#### Responses

**`200` - Charge deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Indicates whether the charge was deleted successfully |

**`404` - Charge not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No | Error message describing why the charge was not found |
| `statusCode` | number | No | HTTP status code |

**`422` - Unprocessable Entity**

---

### GET `/marketplace/billing/charges/{chargeId}`

**Get specific wallet charge details**

Get specific wallet charge details

**Operation ID:** `getSpecificCharge`

**Tags:** Wallet Charges

**Required Scopes:** `charges.readonly`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `chargeId` | path | string | Yes | ID of the charge to retrieve |

#### Responses

**`200` - Returns charge details**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `refunded` | boolean | No | Value is 'true' if the charge has subsequently been refunded. |
| `currency` | string | No | Currency of the transaction. We currently support USD only. |
| `appId` | string | No | App ID |
| `meterId` | string | No | Billing Meter ID (you can find this on your app's pricing page) |
| `chargeId` | string | No | Charge ID |
| `entityType` | string | No | Indicates who was charged? Currently, we support charges for 'location' only |
| `entityId` | string | No | If the entityType is Location, entityld would be locationld. |
| `amountCharged` | number | No | Total amount charged |
| `pricePerUnit` | number | No | Price per unit for the charge |
| `transactionType` | string | No | This can be one of two values - 'charge' or 'refund' |
| `units` | number | No | Number of units that the sub-account was charged for |
| `meta` | object | No | meta object contains details that were sent while creating the charge via the API - eventID, description, eventTime, userld |
| `createdAt` | string | No | Timestamp when the charge was created in our system |
| `updatedAt` | string | No | Timestamp when the charge was last updated in our system |

**`404` - Charge not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No | Error message describing why the charge was not found |
| `statusCode` | number | No | HTTP status code |

**`422` - Unprocessable Entity**

---

### GET `/marketplace/billing/charges/has-funds`

**Check if account has sufficient funds**

Check if account has sufficient funds

**Operation ID:** `hasFunds`

**Tags:** Wallet Charges

**Required Scopes:** `charges.readonly`

#### Responses

**`200` - Returns fund availability status**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `hasFunds` | boolean | No | Indicates whether the sub-account has sufficient funds to be charged |

**`422` - Unprocessable Entity**

---

## App Management

### DELETE `/marketplace/app/{appId}/installations`

**Uninstall an application**

Uninstalls an application from your company or a specific location. This will remove the application`s access and stop all its functionalities

**Operation ID:** `uninstall-application`

**Tags:** App Management

**Required Scopes:** `oauth.write`, `oauth.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `appId` | path | string | Yes | The application id which is to be uninstalled. |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | No | The company id from which the application is to be uninstalled. If you pass agency token, then companyId is required. It will uninstall application from agency as well as all sub-accounts. |
| `locationId` | string | No | The location id from which the application is to be uninstalled. If you pass location token, then locationId is required. It will uninstall application from that location only. |
| `reason` | string | No | The reason for uninstalling the application. Reason is required if you are uninstalling the application as a developer. |

#### Responses

**`200` - Successfully uninstalled the application**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | The status of the uninstallation of the application |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/marketplace/app/{appId}/installations`

**Get Installer Details**

Fetches installer details for the authenticated user. This endpoint returns information about the company, location, user, and installation details associated with the current OAuth token.

**Operation ID:** `get-installer-details`

**Tags:** App Management

**Required Scopes:** `marketplace-installer-details.readonly`, `marketplace-installer-details.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `appId` | path | string | Yes | ID of the app to get installer details |

#### Responses

**`200` - Successfully retrieved installer details. Returns company, location, user, and installation information.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `installationDetails` | object | Yes |  |

**`400` - Bad Request. Invalid request parameters or missing required data.**

**`403` - Forbidden. The client does not have necessary permissions to access installer details.**

---

## App Billing Management

### GET `/marketplace/app/{appId}/rebilling-config/location/{locationId}`

**Get rebilling config for an app subscription and usage plans**

Get rebilling config for an app subscription and usage plans for the authenticated sub-account. This endpoint returns the subscription and usage plans for an app.

**Operation ID:** `get-rebilling-config-for-app`

**Tags:** App Billing Management

**Required Scopes:** `oauth.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `appId` | path | string | Yes | ID of the app to get rebilling config |
| `locationId` | path | string | Yes | ID of the Sub-Account location to get rebilling config for |

#### Responses

**`200` - Successfully retrieved rebilling config for the app**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `plans` | object | Yes |  |

**`400` - Bad Request. Invalid request parameters or missing required data.**

**`403` - Forbidden. The client does not have necessary permissions to access installer details.**

---

## External Auth Migration

### POST `/marketplace/external-auth/migration`

**Migrate external authentication connection**

Migrates an external authentication connection credentials (basic or oauth2) for a specific app and location. This endpoint validates the app configuration, stores credentials safely in CRM's native encrypted storage. With this the lifecycle of the token is managed by CRM.

**Operation ID:** `migrateConnection`

**Tags:** External Auth Migration

**Required Scopes:** `marketplace-external-auth-migration.write`, `marketplace-external-auth-migration.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `oauth2`, `basic`) | Yes | Type of authentication - basic or oauth2 |
| `locationId` | string | Yes | Location ID |
| `appId` | string | Yes | App ID |
| `appVersionId` | string | Yes | App Version ID |
| `accountId` | string | Yes | Connection identifier |
| `apiKey` | string | No | API Key (supported when type is basic) |
| `basicCredentials` | object | No | Basic auth credentials as key/value pairs (supported when type is basic). Keys are validated against the app version externalAuthConfig.fields. |
| `accessToken` | string | No | Access token (required when type is oauth2) |
| `refreshToken` | string | No | Refresh token (required when type is oauth2) |
| `expiryIn` | number | No | Access token expiry time in milliseconds (optional for oauth2) |
| `expiryAt` | number | No | Timestamp for access token expiry (optional for oauth2) |
| `scopes` | array of string | No | OAuth2 scopes (optional for oauth2) |
| `displayName` | string | No | Display name for the connection (optional, defaults to accountId) |
| `isDefault` | boolean | No | Whether this is the default connection for the location (optional, defaults to false) |

#### Responses

**`201` - Connection migrated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the migration was successful |
| `identifier` | string | Yes | Unique identifier for the migrated connection |
| `message` | string | No | Message describing the result |

**`400` - Bad request - invalid input or auth type mismatch**

**`401` - Unauthorized - invalid or missing token**

**`404` - App not found**

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | HTTP status code |
| `message` | string | No | Error message describing the internal server error |

---

## Schemas

### DeleteIntegrationBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | No | The company id from which the application is to be uninstalled. If you pass agency token, then companyId is required. It will uninstall application from agency as well as all sub-accounts. |
| `locationId` | string | No | The location id from which the application is to be uninstalled. If you pass location token, then locationId is required. It will uninstall application from that location only. |
| `reason` | string | No | The reason for uninstalling the application. Reason is required if you are uninstalling the application as a developer. |

### DeleteIntegrationResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | The status of the uninstallation of the application |

### GetInstallerDetailsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `installationDetails` | object | Yes |  |

### GetRebillingConfigResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `plans` | object | Yes |  |

### InstallerDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes | Company ID |
| `locationId` | string | No | Location ID (if applicable) |
| `companyName` | string | Yes | Company name |
| `relationshipNumber` | string | Yes | Company relationship number |
| `companyEmail` | string | No | Company email. Will be null for sub-account installations due to PII concerns. |
| `companyOwnerFullName` | string | No | Company owner full name. Will be null for sub-account installations due to PII concerns. |
| `userId` | string | Yes | User ID who installed the app |
| `isWhitelabelCompany` | boolean | Yes | Whether the company is a whitelabel company |
| `companyPlan` | string | No | Company plan. Will be null for sub-account installations due to business sensitivity. |
| `companyHighLevelPlan` | string | No | Company plan. Will be null for sub-account installations due to business sensitivity. |
| `marketplaceAppPlanId` | string | No | Marketplace app plan ID for paid apps |
| `whitelabelDetails` | object | No |  |

### InternalServerErrorDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | HTTP status code |
| `message` | string | No | Error message describing the internal server error |

### MigrateConnectionDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `oauth2`, `basic`) | Yes | Type of authentication - basic or oauth2 |
| `locationId` | string | Yes | Location ID |
| `appId` | string | Yes | App ID |
| `appVersionId` | string | Yes | App Version ID |
| `accountId` | string | Yes | Connection identifier |
| `apiKey` | string | No | API Key (supported when type is basic) |
| `basicCredentials` | object | No | Basic auth credentials as key/value pairs (supported when type is basic). Keys are validated against the app version externalAuthConfig.fields. |
| `accessToken` | string | No | Access token (required when type is oauth2) |
| `refreshToken` | string | No | Refresh token (required when type is oauth2) |
| `expiryIn` | number | No | Access token expiry time in milliseconds (optional for oauth2) |
| `expiryAt` | number | No | Timestamp for access token expiry (optional for oauth2) |
| `scopes` | array of string | No | OAuth2 scopes (optional for oauth2) |
| `displayName` | string | No | Display name for the connection (optional, defaults to accountId) |
| `isDefault` | boolean | No | Whether this is the default connection for the location (optional, defaults to false) |

### MigrateConnectionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the migration was successful |
| `identifier` | string | Yes | Unique identifier for the migrated connection |
| `message` | string | No | Message describing the result |

### PlansDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `subscription` | array of object | Yes | Subscription plans |
| `usage` | array of object | Yes | Usage-based plans |

### RaiseChargeBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `appId` | string | Yes | App ID of the App |
| `meterId` | string | Yes | Billing Meter ID (you can find this on your app's pricing page) |
| `eventId` | string | Yes | Event ID / Transaction ID on your server's side. This will help you maintain the reference of the event/transaction on your end that you charged the customer for. |
| `userId` | string | No | User ID |
| `locationId` | string | Yes | ID of the Sub-Account to be charged |
| `companyId` | string | Yes | ID of the Agency the Sub-account belongs to |
| `description` | string | Yes | Description of the charge |
| `price` | number | No | Price per unit to charge |
| `units` | number | Yes | Number of units to charge |
| `eventTime` | string | No | The timestamp when the event/transaction was performed. If blank, the billing timestamp will be set as the event time. ISO8601 Format. |

### SubscriptionPlanDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `resellingAmount` | number | Yes | The reselling amount |
| `baseAmount` | number | Yes | The base amount |
| `planId` | string | Yes | The plan id |
| `features` | array of string | Yes | The features |
| `paymentType` | string | Yes | The payment time |
| `name` | string | Yes | The plan name |
| `paymentTime` | string | Yes | The payment time |

### UsagePlanDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `productType` | string | Yes | The product type |
| `productName` | string | Yes | The product name |
| `usageUnit` | string | Yes | The usage unit for the meter |
| `meterId` | string | Yes | The meter id |
| `meterName` | string | Yes | The meter name |
| `fixedPricePerUnit` | number | Yes | The fixed price per unit, applicable for fixed price type |
| `priceType` | string (enum: `fixed`, `dynamic`) | Yes | The price type |
| `minPricePerUnit` | string | Yes | The min price per unit, applicable for dynamic price type |
| `maxPricePerUnit` | string | Yes | The max price per unit, applicable for dynamic price type |
| `executionLimitPerCycle` | number | Yes | The execution limit per cycle |

### WhitelabelDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `domain` | string | Yes | Domain of the whitelabel company |
| `logoUrl` | string | Yes | Logo URL of the whitelabel company |
