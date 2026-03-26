# Marketplace API

Documentation for Marketplace API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Wallet Charges](#wallet-charges)
- [App Management](#app-management)

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
| `units` | string | Yes | Number of units to charge |
| `eventTime` | string | No | The timestamp when the event/transaction was performed. If blank, the billing timestamp will be set as the event time. ISO8601 Format. |

#### Responses

**`201` - Charge created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No |  |
| `chargeId` | string | No |  |

**`400` - Bad request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No |  |
| `statusCode` | number | No |  |

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
| `charges` | array of object | No |  |
| `total` | number | No |  |

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
| `success` | boolean | No |  |

**`404` - Charge not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | No |  |
| `statusCode` | number | No |  |

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
| `message` | string | No |  |
| `statusCode` | number | No |  |

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
| `hasFunds` | boolean | No |  |

**`422` - Unprocessable Entity**

---

## App Management

### DELETE `/marketplace/app/{appId}/installations`

**Uninstall an application**

Uninstalls an application from your company or a specific location. This will remove the application`s access and stop all its functionalities

**Operation ID:** `uninstall-application`

**Tags:** App Management

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

### InstallerDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes | Company ID |
| `locationId` | string | No | Location ID (if applicable) |
| `companyName` | string | Yes | Company name |
| `companyEmail` | string | Yes | Company email |
| `companyOwnerFullName` | string | No | Company owner full name |
| `userId` | string | Yes | User ID who installed the app |
| `isWhitelabelCompany` | boolean | Yes | Whether the company is a whitelabel company |
| `companyHighLevelPlan` | string | No | Company plan |
| `marketplaceAppPlanId` | string | No | Marketplace app plan ID for paid apps |
| `whitelabelDetails` | object | No |  |

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
| `units` | string | Yes | Number of units to charge |
| `eventTime` | string | No | The timestamp when the event/transaction was performed. If blank, the billing timestamp will be set as the event time. ISO8601 Format. |

### WhitelabelDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `domain` | string | Yes | Domain of the whitelabel company |
| `logoUrl` | string | Yes | Logo URL of the whitelabel company |
