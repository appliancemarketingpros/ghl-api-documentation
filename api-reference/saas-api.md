# SaaS API API

API Service for SaaS

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Saas](#saas)

## Saas

### GET `/saas-api/public-api/locations`

**Get locations by stripeId with companyId**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Get locations by stripeCustomerId or stripeSubscriptionId with companyId

**Operation ID:** `locations-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `customerId` | query | string | No | Stripe customer ID to find locations for |
| `subscriptionId` | query | string | No | Stripe subscription ID to find locations for |
| `companyId` | query | string | Yes | Company ID to filter locations |

#### Responses

**`200` - Locations retrieved successfully**

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### PUT `/saas-api/public-api/update-saas-subscription/{locationId}`

**Update SaaS subscription**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Update SaaS subscription for given locationId and customerId

**Operation ID:** `update-saas-subscription-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID to update subscription for |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `subscriptionId` | string | Yes | Subscription ID |
| `customerId` | string | Yes | Customer ID |
| `companyId` | string | Yes | Company ID |

#### Responses

**`200` - SaaS subscription updated successfully**

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### POST `/saas-api/public-api/bulk-disable-saas/{companyId}`

**Disable SaaS for locations**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Disable SaaS for locations for given locationIds

**Operation ID:** `bulk-disable-saas-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `companyId` | path | string | Yes | Company ID to disable SaaS for |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationIds` | array of string | Yes | Location IDs |

#### Responses

**`200` - SaaS disabled successfully for locations**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Response data from the bulk disable SaaS operation |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### POST `/saas-api/public-api/enable-saas/{locationId}`

**Enable SaaS for Sub-Account (Formerly Location)**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.


                  Enable SaaS for Sub-Account (Formerly Location) based on the data provided
                  
                    
                                !
                      
                      
                        
                          This feature is only available on Agency Pro ($497) plan.
                        
                      
                  
                
    

**Operation ID:** `enable-saas-location-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID to enable SaaS for |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripeAccountId` | string | No | Stripe account id(Required only for SaaS V1) |
| `name` | string | No | Name of the stripe customer(Required only for SaaS V1) |
| `email` | string | No | Email of the stripe customer(Required only for SaaS V1) |
| `stripeCustomerId` | string | No | Stripe customer id if exists(Required only for SaaS V1) |
| `companyId` | string | Yes |  |
| `isSaaSV2` | boolean | Yes | Denotes if it is a saas v2 or v1 sub-account |
| `contactId` | string | No | Agency subaccount used for payment provider integration(Required Only for SaaS V2) |
| `providerLocationId` | string | No | Agency Subaccount ID |
| `description` | string | No | Description |
| `saasPlanId` | string | No | Required only while pre-configuring saas subscription |
| `priceId` | string | No | Required only while pre-configuring saas subscription |

#### Responses

**`200` - SaaS enabled successfully for location**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Response data from the enable SaaS operation |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### POST `/saas-api/public-api/pause/{locationId}`

**Pause location**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Pause Sub account for given locationId

**Operation ID:** `pause-location-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID to pause/unpause |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `paused` | boolean | Yes | Paused |
| `companyId` | string | Yes | Company ID |

#### Responses

**`200` - Location paused/unpaused successfully**

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### POST `/saas-api/public-api/update-rebilling/{companyId}`

**Update Rebilling**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Bulk update rebilling for given locationIds

**Operation ID:** `update-rebilling-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `companyId` | path | string | Yes | Company ID to update rebilling for |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `product` | string (enum: `contentAI`, `workflow_premium_actions`, `workflow_ai`, `conversationAI`, `EmailNotification`, `whatsApp`, `reviewsAI`, `VERIFIED_CALLER_ID`, `WALLET_SALES_TAX`, `NOTIFICATION_SMS`, `EmailSmtp`, `EmailVerification`, `autoCompleteAddress`, `funnelAI`, `domainPurchase`, `Phone`, `Email`) | Yes | The product to update rebilling for |
| `locationIds` | array of string | Yes | Array of location IDs to update rebilling for |
| `config` | object | Yes | Configuration for rebilling settings |

**`config` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `optIn` | boolean | No | Enable the product for the locations |
| `enabled` | boolean | No | Enable the rebilling for the locations |
| `markup` | number | No | Additional value to be added in terms of percentage. For example, if the product price is $100 and the markup is 5, the amount charged to will be $105. |

#### Responses

**`200` - Rebilling updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the rebilling update was successful |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### GET `/saas-api/public-api/agency-plans/{companyId}`

**Get Agency Plans**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Fetch all agency subscription plans for a given company ID

**Operation ID:** `get-agency-plans-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes | Company ID to get agency plans for |

#### Responses

**`200` - Agency plans retrieved successfully**

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### GET `/saas-api/public-api/get-saas-subscription/{locationId}`

**Get Location Subscription Details**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Fetch subscription details for a specific location from location metadata

**Operation ID:** `get-location-subscription-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | path | string | Yes | Location ID to get subscription details for |
| `companyId` | query | string | Yes | Company ID to filter subscription details |

#### Responses

**`200` - Location subscription details retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID |
| `isSaaSV2` | boolean | Yes | Indicates if the SaaS is V2 |
| `companyId` | string | Yes | Company ID |
| `saasMode` | string | No | SaaS mode |
| `subscriptionId` | string | No | Subscription ID |
| `customerId` | string | No | Customer ID |
| `productId` | string | No | Product ID |
| `priceId` | string | No | Price ID |
| `saasPlanId` | string | No | SaaS plan ID |
| `subscriptionStatus` | string | No | Subscription status |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### POST `/saas-api/public-api/bulk-enable-saas/{companyId}`

**Bulk Enable SaaS**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Enable SaaS mode for multiple locations with support for both SaaS v1 and v2

**Operation ID:** `bulk-enable-saas-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes | Company ID to enable SaaS for |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationIds` | array of string | Yes | Array of location IDs to enable SaaS for |
| `isSaaSV2` | boolean | Yes | Indicates if the SaaS is V2 |
| `actionPayload` | object | Yes |  |

**`actionPayload` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceId` | string | No | Price ID for the SaaS plan |
| `stripeAccountId` | string | No | Stripe account ID |
| `saasPlanId` | string | Yes | SaaS plan ID |
| `providerLocationId` | string | No | Provider location ID |

#### Responses

**`200` - Bulk SaaS enable operation completed successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the bulk enable SaaS operation was successful |
| `message` | string | Yes | Message indicating the bulk enable SaaS operation |
| `bulkActionUrl` | string | No | URL for the bulk enable SaaS operation |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### GET `/saas-api/public-api/saas-locations/{companyId}`

**Get SaaS Locations**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Fetch all SaaS-activated locations for a company with pagination

**Operation ID:** `get-saas-locations-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes | Company ID to get SaaS locations for |
| `page` | query | number | No | Page number for pagination |

#### Responses

**`200` - SaaS locations retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locations` | array of object | Yes | Array of SaaS locations |
| `pagination` | object | Yes |  |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### GET `/saas-api/public-api/saas-plan/{planId}`

**Get SaaS Plan**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Fetch a specific SaaS plan by plan ID

**Operation ID:** `get-saas-plan-deprecated`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `planId` | path | string | Yes | Plan ID to get SaaS plan details for |
| `companyId` | query | string | Yes | Company ID to filter SaaS plan |

#### Responses

**`200` - SaaS plan retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `planId` | string | Yes | Unique identifier for the SaaS plan |
| `companyId` | string | Yes | Company ID associated with the SaaS plan |
| `title` | string | Yes | Title of the SaaS plan |
| `description` | string | Yes | Description of the SaaS plan |
| `saasProducts` | array of string | Yes | Array of SaaS products included in the plan |
| `addOns` | array of string | No | Array of add-ons included in the plan |
| `planLevel` | number | Yes | Level of the plan (0-4) |
| `trialPeriod` | number | Yes | Trial period in days |
| `setupFee` | number | No | Setup fee for the plan |
| `userLimit` | number | No | User limit for the plan |
| `contactLimit` | number | No | Contact limit for the plan |
| `prices` | array of object | Yes | Prices for the plan |
| `categoryId` | string | No | Category ID for the plan |
| `snapshotId` | string | No | Snapshot ID for the plan |
| `providerLocationId` | string | No | Provider location ID |
| `productId` | string | No | Product ID for the plan |
| `isSaaSV2` | boolean | Yes | Indicates if this is a SaaS V2 plan |
| `createdAt` | string | Yes | Creation timestamp |
| `updatedAt` | string | Yes | Last update timestamp |

**`400` - Bad Request**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`401` - Unauthorized**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

**`404` - Resource not found**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

**`500` - Internal server error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

---

### GET `/saas/locations`

**Get locations by stripeId with companyId**

Get locations by stripeCustomerId or stripeSubscriptionId with companyId

**Operation ID:** `locations`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `customerId` | query | string | Yes |  |
| `subscriptionId` | query | string | Yes |  |
| `companyId` | query | string | Yes |  |

#### Responses

**`200` - **

---

### PUT `/saas/update-saas-subscription/{locationId}`

**Update SaaS subscription**

Update SaaS subscription for given locationId and customerId

**Operation ID:** `generate-payment-link`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `subscriptionId` | string | Yes | Subscription ID |
| `customerId` | string | Yes | Customer ID |
| `companyId` | string | Yes | Company ID |

#### Responses

**`200` - **

---

### POST `/saas/bulk-disable-saas/{companyId}`

**Disable SaaS for locations**

Disable SaaS for locations for given locationIds

**Operation ID:** `bulk-disable-saas`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationIds` | array of string | Yes | Location IDs |

#### Responses

**`201` - **

---

### POST `/saas/enable-saas/{locationId}`

**Enable SaaS for Sub-Account (Formerly Location)**


                  Enable SaaS for Sub-Account (Formerly Location) based on the data provided
                  
                    
                                !
                      
                      
                        
                          This feature is only available on Agency Pro ($497) plan.
                        
                      
                  
                
    

**Operation ID:** `enable-saas-location`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripeAccountId` | string | No | Stripe account id(Required only for SaaS V1) |
| `name` | string | No | Name of the stripe customer(Required only for SaaS V1) |
| `email` | string | No | Email of the stripe customer(Required only for SaaS V1) |
| `stripeCustomerId` | string | No | Stripe customer id if exists(Required only for SaaS V1) |
| `companyId` | string | Yes |  |
| `isSaaSV2` | boolean | Yes | Denotes if it is a saas v2 or v1 sub-account |
| `contactId` | string | No | Agency subaccount used for payment provider integration(Required Only for SaaS V2) |
| `providerLocationId` | string | No | Agency Subaccount ID |
| `description` | string | No | Description |
| `saasPlanId` | string | No | Required only while pre-configuring saas subscription |
| `priceId` | string | No | Required only while pre-configuring saas subscription |

#### Responses

**`201` - **

---

### POST `/saas/pause/{locationId}`

**Pause location**

Pause Sub account for given locationId

**Operation ID:** `pause-location`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `paused` | boolean | Yes | Paused |
| `companyId` | string | Yes | Company ID |

#### Responses

**`201` - **

---

### POST `/saas/update-rebilling/{companyId}`

**Update Rebilling**

Bulk update rebilling for given locationIds

**Operation ID:** `update-rebilling`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `product` | string (enum: `contentAI`, `workflow_premium_actions`, `workflow_ai`, `conversationAI`, `EmailNotification`, `whatsApp`, `reviewsAI`, `VERIFIED_CALLER_ID`, `WALLET_SALES_TAX`, `NOTIFICATION_SMS`, `EmailSmtp`, `EmailVerification`, `autoCompleteAddress`, `funnelAI`, `domainPurchase`, `Phone`, `Email`) | Yes | The product to update rebilling for |
| `locationIds` | array of string | Yes | Array of location IDs to update rebilling for |
| `config` | object | Yes | Configuration for rebilling settings |

**`config` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `optIn` | boolean | No | Enable the product for the locations |
| `enabled` | boolean | No | Enable the rebilling for the locations |
| `markup` | number | No | Additional value to be added in terms of percentage. For example, if the product price is $100 and the markup is 5, the amount charged to will be $105. |

#### Responses

**`201` - **

---

### GET `/saas/agency-plans/{companyId}`

**Get Agency Plans**

Fetch all agency subscription plans for a given company ID

**Operation ID:** `get-agency-plans`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes |  |

#### Responses

**`200` - **

---

### GET `/saas/get-saas-subscription/{locationId}`

**Get Location Subscription Details**

Fetch subscription details for a specific location from location metadata

**Operation ID:** `get-location-subscription`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `locationId` | path | string | Yes |  |
| `companyId` | query | string | Yes |  |

#### Responses

**`200` - **

---

### POST `/saas/bulk-enable-saas/{companyId}`

**Bulk Enable SaaS**

Enable SaaS mode for multiple locations with support for both SaaS v1 and v2

**Operation ID:** `bulk-enable-saas`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationIds` | array of string | Yes | Array of location IDs to enable SaaS for |
| `isSaaSV2` | boolean | Yes | Indicates if the SaaS is V2 |
| `actionPayload` | object | Yes |  |

**`actionPayload` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceId` | string | No | Price ID for the SaaS plan |
| `stripeAccountId` | string | No | Stripe account ID |
| `saasPlanId` | string | Yes | SaaS plan ID |
| `providerLocationId` | string | No | Provider location ID |

#### Responses

**`201` - **

---

### GET `/saas/saas-locations/{companyId}`

**Get SaaS Locations**

Fetch all SaaS-activated locations for a company with pagination

**Operation ID:** `get-saas-locations`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `companyId` | path | string | Yes |  |
| `page` | query | number | Yes |  |

#### Responses

**`200` - **

---

### GET `/saas/saas-plan/{planId}`

**Get SaaS Plan**

Fetch a specific SaaS plan by plan ID

**Operation ID:** `get-saas-plan`

**Tags:** Saas

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `planId` | path | string | Yes |  |
| `companyId` | query | string | Yes |  |

#### Responses

**`200` - **

---

## Schemas

### AgencyPlanResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `planId` | string | Yes | Unique identifier for the plan |
| `title` | string | Yes | Title of the plan |
| `description` | string | Yes | Description of the plan |
| `saasProducts` | array of string | Yes | Array of SaaS products included in the plan |
| `addOns` | array of string | No | Array of add-ons included in the plan |
| `planLevel` | number | Yes | Level of the plan (0-4) |
| `trialPeriod` | number | Yes | Trial period in days |
| `userLimit` | number | No | User limit for the plan |
| `contactLimit` | number | No | Contact limit for the plan |
| `prices` | array of object | Yes | Pricing information for the plan |
| `categoryId` | string | No | Category ID for the plan |
| `snapshotId` | string | No | Snapshot ID for the plan |
| `productId` | string | No | Product ID for the plan |
| `isSaaSV2` | boolean | Yes | Indicates if this is a SaaS V2 plan |
| `providerLocationId` | string | No | Provider location ID |
| `createdAt` | string | Yes | Creation timestamp |
| `updatedAt` | string | Yes | Last update timestamp |

### BadRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

### BulkDisableSaasDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationIds` | array of string | Yes | Location IDs |

### BulkDisableSaasResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Response data from the bulk disable SaaS operation |

### BulkEnableSaasActionPayloadDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceId` | string | No | Price ID for the SaaS plan |
| `stripeAccountId` | string | No | Stripe account ID |
| `saasPlanId` | string | Yes | SaaS plan ID |
| `providerLocationId` | string | No | Provider location ID |

### BulkEnableSaasRequestDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationIds` | array of string | Yes | Array of location IDs to enable SaaS for |
| `isSaaSV2` | boolean | Yes | Indicates if the SaaS is V2 |
| `actionPayload` | object | Yes |  |

### BulkEnableSaasResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the bulk enable SaaS operation was successful |
| `message` | string | Yes | Message indicating the bulk enable SaaS operation |
| `bulkActionUrl` | string | No | URL for the bulk enable SaaS operation |

### EnableSaasDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripeAccountId` | string | No | Stripe account id(Required only for SaaS V1) |
| `name` | string | No | Name of the stripe customer(Required only for SaaS V1) |
| `email` | string | No | Email of the stripe customer(Required only for SaaS V1) |
| `stripeCustomerId` | string | No | Stripe customer id if exists(Required only for SaaS V1) |
| `companyId` | string | Yes |  |
| `isSaaSV2` | boolean | Yes | Denotes if it is a saas v2 or v1 sub-account |
| `contactId` | string | No | Agency subaccount used for payment provider integration(Required Only for SaaS V2) |
| `providerLocationId` | string | No | Agency Subaccount ID |
| `description` | string | No | Description |
| `saasPlanId` | string | No | Required only while pre-configuring saas subscription |
| `priceId` | string | No | Required only while pre-configuring saas subscription |

### EnableSaasResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes | Response data from the enable SaaS operation |

### GetSaasLocationsResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locations` | array of object | Yes | Array of SaaS locations |
| `pagination` | object | Yes |  |

### InternalServerErrorDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

### LocationSubscriptionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID |
| `isSaaSV2` | boolean | Yes | Indicates if the SaaS is V2 |
| `companyId` | string | Yes | Company ID |
| `saasMode` | string | No | SaaS mode |
| `subscriptionId` | string | No | Subscription ID |
| `customerId` | string | No | Customer ID |
| `productId` | string | No | Product ID |
| `priceId` | string | No | Price ID |
| `saasPlanId` | string | No | SaaS plan ID |
| `subscriptionStatus` | string | No | Subscription status |

### PauseLocationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `paused` | boolean | Yes | Paused |
| `companyId` | string | Yes | Company ID |

### ResourceNotFoundDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |

### SaasLocationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID |
| `companyId` | string | Yes | Company ID |
| `saasMode` | string | Yes | SaaS mode |
| `subscriptionId` | string | Yes | Subscription ID |
| `customerId` | string | No | Customer ID |
| `name` | string | No | Name |
| `email` | string | No | Email |
| `providerLocationId` | string | No | Provider location ID |
| `isSaaSV2` | boolean | No | Indicates if the SaaS is V2 |
| `subscriptionInfo` | object | No | Subscription information |

### SaasPlanResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `planId` | string | Yes | Unique identifier for the SaaS plan |
| `companyId` | string | Yes | Company ID associated with the SaaS plan |
| `title` | string | Yes | Title of the SaaS plan |
| `description` | string | Yes | Description of the SaaS plan |
| `saasProducts` | array of string | Yes | Array of SaaS products included in the plan |
| `addOns` | array of string | No | Array of add-ons included in the plan |
| `planLevel` | number | Yes | Level of the plan (0-4) |
| `trialPeriod` | number | Yes | Trial period in days |
| `setupFee` | number | No | Setup fee for the plan |
| `userLimit` | number | No | User limit for the plan |
| `contactLimit` | number | No | Contact limit for the plan |
| `prices` | array of object | Yes | Prices for the plan |
| `categoryId` | string | No | Category ID for the plan |
| `snapshotId` | string | No | Snapshot ID for the plan |
| `providerLocationId` | string | No | Provider location ID |
| `productId` | string | No | Product ID for the plan |
| `isSaaSV2` | boolean | Yes | Indicates if this is a SaaS V2 plan |
| `createdAt` | string | Yes | Creation timestamp |
| `updatedAt` | string | Yes | Last update timestamp |

### UnauthorizedDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No | Status code |
| `message` | string | No | Error message |
| `error` | string | No | Error message |

### UpdateRebillingDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `product` | string (enum: `contentAI`, `workflow_premium_actions`, `workflow_ai`, `conversationAI`, `EmailNotification`, `whatsApp`, `reviewsAI`, `VERIFIED_CALLER_ID`, `WALLET_SALES_TAX`, `NOTIFICATION_SMS`, `EmailSmtp`, `EmailVerification`, `autoCompleteAddress`, `funnelAI`, `domainPurchase`, `Phone`, `Email`) | Yes | The product to update rebilling for |
| `locationIds` | array of string | Yes | Array of location IDs to update rebilling for |
| `config` | object | Yes | Configuration for rebilling settings |

### UpdateRebillingResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the rebilling update was successful |

### UpdateSubscriptionDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `subscriptionId` | string | Yes | Subscription ID |
| `customerId` | string | Yes | Customer ID |
| `companyId` | string | Yes | Company ID |
