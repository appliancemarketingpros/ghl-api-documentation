# Affiliate Manager API

Documentation for Affiliate Manager API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Affiliates](#affiliates)
- [Payouts](#payouts)
- [Commissions](#commissions)

## Affiliates

### GET `/affiliate-manager/{locationId}/affiliates`

**List Affiliates**

Retrieve the list of affiliates for a location.

**Operation ID:** `list-affiliates`

**Tags:** Affiliates

**Required Scopes:** `affiliate-manager.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `query` | query | string | No |  |
| `active` | query | string | No |  |
| `campaignId` | query | string | No |  |
| `skip` | query | number | No |  |
| `limit` | query | number | No | Maximum number of records to return. Maximum allowed value is 100. |
| `fromDate` | query | string | No |  |
| `toDate` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `affiliates` | array of object | Yes | Affiliate list |
| `meta` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/affiliate-manager/{locationId}/affiliates/{affiliateId}`

**Get Affiliate**

Retrieve a single affiliate by id for a location.

**Operation ID:** `get-affiliate`

**Tags:** Affiliates

**Required Scopes:** `affiliate-manager.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `affiliateId` | path | string | Yes | Affiliate Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Affiliate id |
| `firstName` | string | No | Affiliate first name |
| `lastName` | string | No | Affiliate last name |
| `phone` | string | No | Affiliate phone number |
| `deleted` | boolean | No | Whether the affiliate is deleted |
| `locationId` | string | Yes | Location id |
| `active` | boolean | No | Whether the affiliate is active |
| `address` | string | No | Affiliate address |
| `avatar` | string | No | Affiliate avatar URL |
| `createdAt` | string | No | Created at timestamp |
| `createdBy` | object | No | Created by audit info |
| `facebookUrl` | string | No | Facebook URL |
| `instagramUrl` | string | No | Instagram URL |
| `linkedInUrl` | string | No | LinkedIn URL |
| `twitterUrl` | string | No | Twitter URL |
| `youtubeUrl` | string | No | YouTube URL |
| `websiteUrl` | string | No | Website URL |
| `contactId` | string | No | Contact id associated with the affiliate |
| `campaignIds` | array of string | No | Campaign ids |
| `vatId` | string | No | VAT ID |
| `updatedAt` | string | No | Updated at timestamp |
| `w8Form` | string | No | W8 form URL |
| `w9Form` | string | No | W9 form URL |
| `lastUpdatedBy` | object | No | Last updated by audit info |
| `email` | string | Yes | Affiliate email |
| `revenue` | number | No | Affiliate revenue |
| `customer` | number | No | Customer count |
| `lead` | number | No | Lead count |
| `droppedCustomer` | number | No | Dropped customer count |
| `clickCount` | number | No | Click count |
| `paid` | number | No | Paid amount |
| `currency` | string | No | Currency code |
| `owned` | number | No | Owned amount |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Payouts

### GET `/affiliate-manager/{locationId}/payouts`

**List Payouts**

Retrieve the list of payouts for a location.

**Operation ID:** `list-payouts`

**Tags:** Payouts

**Required Scopes:** `affiliate-manager.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `status` | query | string | No | Payout status |
| `query` | query | string | No | query |
| `affiliateId` | query | string | No | Affiliate Id |
| `campaignId` | query | string | No | Campaign Id |
| `skip` | query | number | No |  |
| `limit` | query | number | No |  |
| `start` | query | string | No |  |
| `end` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `payouts` | array of object | Yes | Payout list |
| `meta` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Commissions

### GET `/affiliate-manager/{locationId}/commissions`

**List Commissions**

Retrieve the list of commissions for a location.

**Operation ID:** `list-commissions`

**Tags:** Commissions

**Required Scopes:** `affiliate-manager.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `campaignId` | query | string | No | Campaign Id |
| `affiliateId` | query | string | No | Affiliate Id |
| `status` | query | string | No | Status |
| `query` | query | string | No | Query |
| `skip` | query | number | No |  |
| `limit` | query | number | No | Maximum number of records to return. Maximum allowed value is 100. |
| `fromDate` | query | string | No |  |
| `toDate` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `commissions` | array of object | Yes | Commission list |
| `meta` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AffiliateListMetaResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Total affiliates matching the applied filters |

### CommissionAffiliateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No | Affiliate id |
| `name` | string | No | Affiliate display name |
| `email` | string | No | Affiliate email |

### CommissionCampaignResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Campaign id |
| `name` | string | No | Campaign name |
| `liveMode` | boolean | No | Whether the campaign is in live mode |

### CommissionCustomerResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No | Customer id |
| `firstName` | string | No | Customer first name |
| `lastName` | string | No | Customer last name |
| `email` | string | No | Customer email |
| `type` | string | No | Customer type |

### CommissionListItemResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Commission id |
| `productId` | string | No | Product id |
| `productName` | string | No | Product name |
| `qty` | number | No | Quantity |
| `productCommission` | number | No | Product commission amount |
| `commissionAmount` | number | No | Commission amount |
| `amount` | number | No | Base amount |
| `unitDiscount` | number | No | Unit discount |
| `campaignName` | string | No | Campaign name |
| `commission` | number | No | Commission percentage or value |
| `commissionType` | string | No | Commission type |
| `transactionAt` | string | No | Transaction time |
| `transactionId` | string | No | Transaction id |
| `affiliateId` | string | No | Affiliate id |
| `payoutId` | string | No | Payout id |
| `status` | string | No | Commission status |
| `currency` | string | No | Currency |
| `isTrial` | boolean | No | Whether the item is a trial commission |
| `customer` | object | No |  |
| `createdAt` | string | No | Created at |
| `eventId` | string | No | Event id |
| `campaign` | object | No |  |
| `affiliate` | object | No |  |
| `dueAt` | string | No | Due date |
| `liveMode` | boolean | No | Whether the commission is in live mode |
| `tier` | number | No | Commission tier |

### CommissionListMetaResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Total commissions matching the filters |

### GetAffiliateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Affiliate id |
| `firstName` | string | No | Affiliate first name |
| `lastName` | string | No | Affiliate last name |
| `phone` | string | No | Affiliate phone number |
| `deleted` | boolean | No | Whether the affiliate is deleted |
| `locationId` | string | Yes | Location id |
| `active` | boolean | No | Whether the affiliate is active |
| `address` | string | No | Affiliate address |
| `avatar` | string | No | Affiliate avatar URL |
| `createdAt` | string | No | Created at timestamp |
| `createdBy` | object | No | Created by audit info |
| `facebookUrl` | string | No | Facebook URL |
| `instagramUrl` | string | No | Instagram URL |
| `linkedInUrl` | string | No | LinkedIn URL |
| `twitterUrl` | string | No | Twitter URL |
| `youtubeUrl` | string | No | YouTube URL |
| `websiteUrl` | string | No | Website URL |
| `contactId` | string | No | Contact id associated with the affiliate |
| `campaignIds` | array of string | No | Campaign ids |
| `vatId` | string | No | VAT ID |
| `updatedAt` | string | No | Updated at timestamp |
| `w8Form` | string | No | W8 form URL |
| `w9Form` | string | No | W9 form URL |
| `lastUpdatedBy` | object | No | Last updated by audit info |
| `email` | string | Yes | Affiliate email |
| `revenue` | number | No | Affiliate revenue |
| `customer` | number | No | Customer count |
| `lead` | number | No | Lead count |
| `droppedCustomer` | number | No | Dropped customer count |
| `clickCount` | number | No | Click count |
| `paid` | number | No | Paid amount |
| `currency` | string | No | Currency code |
| `owned` | number | No | Owned amount |

### GetCommissionListResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `commissions` | array of object | Yes | Commission list |
| `meta` | object | No |  |

### GetPayoutListResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `payouts` | array of object | Yes | Payout list |
| `meta` | object | No |  |

### ListAffiliatesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `affiliates` | array of object | Yes | Affiliate list |
| `meta` | object | Yes |  |

### OAuthAffiliateListItemResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Affiliate id |
| `firstName` | string | No | Affiliate first name |
| `lastName` | string | No | Affiliate last name |
| `phone` | string | No | Affiliate phone number |
| `deleted` | boolean | No | Whether the affiliate is deleted |
| `locationId` | string | Yes | Location id |
| `active` | boolean | No | Whether the affiliate is active |
| `address` | string | No | Affiliate address |
| `avatar` | string | No | Affiliate avatar URL |
| `createdAt` | string | No | Created at timestamp |
| `createdBy` | object | No | Created by audit info |
| `facebookUrl` | string | No | Facebook URL |
| `instagramUrl` | string | No | Instagram URL |
| `linkedInUrl` | string | No | LinkedIn URL |
| `twitterUrl` | string | No | Twitter URL |
| `youtubeUrl` | string | No | YouTube URL |
| `websiteUrl` | string | No | Website URL |
| `contactId` | string | No | Contact id associated with the affiliate |
| `campaignIds` | array of string | No | Campaign ids |
| `vatId` | string | No | VAT ID |
| `updatedAt` | string | No | Updated at timestamp |
| `w8Form` | string | No | W8 form URL |
| `w9Form` | string | No | W9 form URL |
| `lastUpdatedBy` | object | No | Last updated by audit info |
| `email` | string | Yes | Affiliate email |
| `revenue` | number | No | Affiliate revenue |
| `customer` | number | No | Customer count |
| `lead` | number | No | Lead count |
| `droppedCustomer` | number | No | Dropped customer count |
| `clickCount` | number | No | Click count |
| `paid` | number | No | Paid amount |
| `currency` | string | No | Currency code |
| `owned` | number | No | Owned amount |

### PayoutListItemResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Payout id |
| `locationId` | string | Yes | Location id |
| `affiliateId` | string | Yes | Affiliate id |
| `campaignId` | string | No | Campaign id |
| `currency` | string | Yes | Payout currency |
| `amount` | number | Yes | Payout amount |
| `status` | string | No | Payout status |
| `payoutMonth` | string | No | Payout month |
| `dueAt` | string | No | Payout due date |
| `paidAt` | string | No | Payout paid date |
| `paidMeta` | object | No | Payout metadata |
| `paidMethod` | string | No | Payout paid method |
| `altId` | string | No | Alternate id |
| `deleted` | boolean | No | Whether the payout is deleted |
| `isMigrated` | boolean | No | Whether the payout is migrated |
| `createdAt` | string | No | Created at timestamp |
| `updatedAt` | string | No | Updated at timestamp |
| `campaign` | string | No | Campaign name |
| `affiliateName` | string | No | Affiliate display name |
| `affiliateEmail` | string | No | Affiliate email |
| `payoutMethod` | string | No | Primary payout method |
| `affiliate` | object | No |  |

### PayoutListMetaResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Total payouts matching the filters |
