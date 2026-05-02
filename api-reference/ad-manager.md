# Ad Manager API

Documentation for Ad-publishing API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Facebook Reporting](#facebook-reporting)
- [Facebook Integration](#facebook-integration)
- [Facebook Ads](#facebook-ads)
- [Google Reporting](#google-reporting)
- [Google Ads](#google-ads)
- [Google Integration](#google-integration)
- [LinkedIn Integration](#linkedin-integration)
- [LinkedIn Ads](#linkedin-ads)
- [LinkedIn Reporting](#linkedin-reporting)

## Facebook Reporting

### GET `/ad-publishing/facebook/reporting`

**Get reporting data**

Retrieve aggregated Facebook ad reporting metrics for a location

**Operation ID:** `fb-get-reporting`

**Tags:** Facebook Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `groupBy` | query | string (enum: `day`, `week`, `month`) | Yes | Time grouping interval |
| `startDate` | query | string | Yes | Report start date |
| `endDate` | query | string | Yes | Report end date |
| `type` | query | string (enum: `AD_MANAGER`, `INTEGRATION`) | Yes | Integration source type |
| `fields` | query | array of string (enum: `impressions`, `clicks`, `spend`, `cpc`, `cost_per_conversion`, `conversions`, `cpm`, `reach`, `frequency`) | Yes | Comma-separated reporting fields |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/reporting/campaign/{campaignId}`

**Get campaign reporting**

Retrieve reporting metrics for a specific Facebook campaign

**Operation ID:** `fb-get-campaign-reporting`

**Tags:** Facebook Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes | Campaign identifier |
| `locationId` | query | string | Yes | Location identifier |
| `startDate` | query | string | Yes | Report start date |
| `endDate` | query | string | Yes | Report end date |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/reporting/list`

**Get reporting list**

Retrieve a list of Facebook campaigns, adsets, or ads with reporting data

**Operation ID:** `fb-get-reporting-list`

**Tags:** Facebook Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `listType` | query | string | Yes | Reporting list type |
| `startDate` | query | string | Yes | Report start date |
| `endDate` | query | string | Yes | Report end date |
| `campaignId` | query | string | Yes | Campaign identifier |
| `type` | query | string (enum: `AD_MANAGER`, `INTEGRATION`) | Yes | Integration source type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Facebook Integration

### GET `/ad-publishing/facebook/me`

**Get current Facebook user**

Retrieve the authenticated Facebook user profile for a location

**Operation ID:** `fb-get-current-user`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/pages`

**Get Facebook pages**

Retrieve Facebook pages associated with the connected account

**Operation ID:** `fb-get-pages`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `fetchExisting` | query | string | No | Fetch existing pages flag |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/page/{pageId}/instagram`

**Get Instagram accounts for page**

Retrieve Instagram accounts linked to a specific Facebook page

**Operation ID:** `fb-get-instagram-accounts`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `pageId` | path | string | Yes | Facebook page identifier |
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `INTEGRATION`, `AD_MANAGER`) | No | Integration type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/page/{pageId}/forms`

**Get page lead forms**

Retrieve lead gen forms for a specific Facebook page

**Operation ID:** `fb-get-page-lead-forms`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `pageId` | path | string | Yes | Facebook page identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/page/{pageId}/forms`

**Create page lead form**

Create a new lead gen form on a Facebook page

**Operation ID:** `fb-create-page-lead-form`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `pageId` | path | string | Yes | Facebook page identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `MORE_VOLUME`, `HIGHER_INTENT`) | Yes | Lead form type |
| `name` | string | Yes | Lead form name |
| `locationId` | string | Yes | Location identifier |
| `greetingCard` | object | No |  |
| `questions` | array of object | Yes | List of questions displayed on the lead form |
| `questionPageHeadline` | string | No | Question page headline |
| `privacyPolicyLink` | string | Yes | Privacy policy URL |
| `privacyPolicyText` | string | No | Privacy policy text |
| `customDisclaimer` | object | No |  |
| `thankYouPage` | object | Yes |  |

**`greetingCard` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Greeting card title |
| `style` | string | Yes | Greeting card style |
| `content` | array of string | Yes | Greeting card content |

**`questions` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `label` | string | No | Question label text shown to the user |
| `key` | string | Yes | Question key |
| `type` | string (enum: `CUSTOM`, `CITY`, `COMPANY_NAME`, `COUNTRY`, `DATE_OF_BIRTH`, `EMAIL`, `FIRST_NAME`, `FULL_NAME`, `GENDER`, `JOB_TITLE`, `LAST_NAME`, `MARITAL_STATUS`, `MILITARY_STATUS`, `PHONE`, `POST_CODE`, `RELATIONSHIP_STATUS`, `STATE`, `STREET_ADDRESS`, `WORK_EMAIL`, `WORK_PHONE_NUMBER`, `ZIP`, `SHORT_ANSWER`) | Yes | Question input type — use a prefilled type for standard fields or CUSTOM / SHORT_ANSWER for freeform questions |
| `options` | array of object | No | Answer options for multiple-choice questions (only applies to CUSTOM type) |

**`customDisclaimer` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Disclaimer title |
| `body` | string | Yes | Disclaimer body text |
| `checkboxes` | array of object | No | Consent checkboxes the user must agree to before submitting the form |

**`thankYouPage` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Thank you page title |
| `body` | string | Yes | Thank you page body |
| `buttonText` | string | Yes | Button text label |
| `buttonType` | string | Yes | Button action type |
| `buttonLink` | string | No | Button destination link |
| `businessPhone` | string | No | Business phone number |
| `countryCode` | string | No | Phone country code |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/ad-accounts`

**Get ad accounts**

Retrieve Facebook ad accounts available for the connected user

**Operation ID:** `fb-get-ad-accounts`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string | No | Account source type |
| `next` | query | string | No | Pagination cursor |
| `fetchAll` | query | string | No | Fetch all accounts |
| `limit` | query | string | No | Results page limit |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/ad-accounts/{adAccountId}`

**Get ad account details**

Retrieve details of a specific Facebook ad account

**Operation ID:** `fb-get-ad-account`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adAccountId` | path | string | Yes | Ad account identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/ad-accounts/{adAccountId}`

**Delete ad account**

Remove a Facebook ad account connection from a location

**Operation ID:** `fb-delete-ad-account`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adAccountId` | path | string | Yes | Ad account identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/conversation-forms`

**Get conversation forms**

Retrieve Facebook conversation lead forms for a location

**Operation ID:** `fb-get-conversation-forms`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/conversation-forms`

**Create conversation form**

Create a new Facebook conversation lead form

**Operation ID:** `fb-create-conversation-form`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `name` | string | Yes | Conversation form name |
| `text` | string | Yes | Welcome message text |
| `questions` | array of object | Yes | Quick-reply questions shown in the welcome message of the conversation form |

**`questions` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `question` | string | Yes | Question title text |
| `response` | string | No | Auto-response message |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/integration`

**Create Facebook integration**

Create a Facebook ad integration for a location with page and ad account

**Operation ID:** `fb-create-integration`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `pageId` | string | Yes | Facebook page ID |
| `adAccountId` | string | No | Ad account identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/integration`

**Get Facebook integration**

Retrieve the Facebook ad integration details for a location

**Operation ID:** `fb-get-integration`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/integration`

**Delete Facebook integration**

Remove the Facebook ad integration from a location

**Operation ID:** `fb-delete-integration`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/page`

**Delete page connection**

Remove a Facebook page connection from a location

**Operation ID:** `fb-delete-page`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `pageId` | query | string | Yes | Facebook page ID |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/page/default`

**Set default page**

Set the default Facebook page for a location

**Operation ID:** `fb-set-default-page`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pageId` | string | Yes | Facebook page identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/lead-form/{leadFormId}`

**Get lead form by ID**

Retrieve a specific Facebook lead form by its ID

**Operation ID:** `fb-get-lead-form`

**Tags:** Facebook Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `leadFormId` | path | string | Yes | Lead form identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Facebook Ads

### GET `/ad-publishing/facebook/targeting/search`

**Search targeting options**

Search Facebook geo-locations and interests for ad targeting

**Operation ID:** `fb-search-targeting`

**Tags:** Facebook Ads

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `type` | query | string | Yes | Targeting search type |
| `query` | query | string | Yes | Search query string |
| `searchType` | query | string | No | Specific search subtype |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/campaigns/{campaignId}/publish`

**Publish campaign**

Publish a Facebook campaign and push it live to Facebook

**Operation ID:** `fb-publish-campaign`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes | Campaign identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/pixels`

**Get conversion pixels**

Retrieve Facebook conversion pixels for a location

**Operation ID:** `fb-get-pixels`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `channel` | query | string | No | Channel type |
| `pageId` | query | string | No | Facebook page ID |
| `igUserId` | query | string | No | Instagram user ID |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/pixels`

**Upsert conversion pixel**

Create or update a Facebook conversion pixel configuration

**Operation ID:** `fb-upsert-pixel`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `conversionPixelId` | string | No | Conversion pixel ID |
| `name` | string | No | Pixel name |
| `igUserId` | string | No | Instagram user ID |
| `type` | string | Yes | Pixel event type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/custom-audience`

**Get custom audiences**

Retrieve Facebook custom audiences for a location

**Operation ID:** `fb-get-custom-audiences`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `lookalike`, `custom`, `all`) | Yes | Audience list type |
| `source` | query | string (enum: `ad_manager`, `integration`) | No | Audience data source |
| `adAccountId` | query | string | Yes | Ad account identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/custom-audience/{audienceId}`

**Delete custom audience**

Delete a Facebook custom audience by ID

**Operation ID:** `fb-delete-custom-audience`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `audienceId` | path | string | Yes | Custom audience identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/custom-audience/{audienceId}`

**Update custom audience**

Update name or description of a Facebook custom audience

**Operation ID:** `fb-update-custom-audience`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `audienceId` | path | string | Yes | Custom audience identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `name` | string | Yes | Audience name |
| `description` | string | Yes | Audience description |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/custom-audience/{audienceId}`

**Get custom audience by ID**

Retrieve a specific Facebook custom audience by its ID

**Operation ID:** `fb-get-custom-audience-by-id`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `audienceId` | path | string | Yes | Custom audience identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/custom-audience/{audienceId}/member`

**Add custom audience member**

Add a member to a Facebook custom audience

**Operation ID:** `fb-add-custom-audience-member`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `audienceId` | path | string | Yes | Custom audience identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `contactId` | string | Yes | Contact identifier |
| `fbAdAccountId` | string | No | Facebook ad account ID |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/custom-audience/{audienceId}/member`

**Remove custom audience member**

Remove a member from a Facebook custom audience

**Operation ID:** `fb-remove-custom-audience-member`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `audienceId` | path | string | Yes | Custom audience identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `contactId` | string | Yes | Contact identifier |
| `fbAdAccountId` | string | No | Facebook ad account ID |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/custom-audience/{audienceId}/member/batch`

**Batch update audience members**

Add or remove members in bulk from a Facebook custom audience via CSV or smart lists

**Operation ID:** `fb-batch-update-audience-members`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `audienceId` | path | string | Yes | Custom audience identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `csvPath` | string | No | CSV file path |
| `operationType` | string | Yes | Batch operation type |
| `smartlistIds` | array of string | No | Smartlist IDs array |
| `dynamicAudience` | string | No | Dynamic audience flag |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/campaign/{campaignId}`

**Get campaign with linked entities**

Retrieve a Facebook campaign with its linked adsets and ads

**Operation ID:** `fb-get-campaign`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes | Campaign identifier |
| `locationId` | query | string | Yes | Location identifier |
| `fields` | query | string | No | Comma-separated field names |
| `source` | query | string | No | Campaign data source |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/facebook/entity`

**Get entities**

Retrieve Facebook campaigns, adsets, or ads based on entity type

**Operation ID:** `fb-get-entity`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `AD_MANAGER`, `INTEGRATION`) | Yes | Integration source type |
| `next` | query | string | No | Pagination cursor |
| `fetchAll` | query | string | No | Fetch all entities |
| `campaignId` | query | string | No | Campaign identifier |
| `adSetId` | query | string | No | Ad set identifier |
| `entityType` | query | string (enum: `CAMPAIGN`, `ADSET`, `AD`) | Yes | Entity type to fetch |
| `searchId` | query | string | No | Search identifier |
| `selectedAdAccountId` | query | string | No | Selected ad account ID |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/campaigns`

**Upsert campaign**

Create or update a Facebook campaign

**Operation ID:** `fb-upsert-campaign`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Campaign identifier |
| `locationId` | string | Yes | Location identifier |
| `name` | string | No | Campaign name |
| `objective` | string (enum: `OUTCOME_LEADS`, `OUTCOME_TRAFFIC`, `OUTCOME_ENGAGEMENT`, `OUTCOME_SALES`) | No | Campaign objective |
| `specialAdCategories` | string (enum: `EMPLOYMENT`, `CREDIT`, `FINANCIAL_PRODUCTS_SERVICES`, `HOUSING`, `ISSUES_ELECTIONS_POLITICS`, `ONLINE_GAMBLING_AND_GAMING`, `NONE`) | No | Special ad categories |
| `source` | string | No | Campaign data source |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/adsets`

**Upsert adset**

Create or update a Facebook ad set

**Operation ID:** `fb-upsert-adset`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Ad set identifier |
| `locationId` | string | Yes | Location identifier |
| `name` | string | No | Ad set name |
| `pageId` | string | No | Facebook page ID |
| `instagramActorId` | string | No | Instagram actor ID |
| `messagingPlatforms` | string (enum: `WHATSAPP`, `MESSENGER`, `INSTAGRAM_DIRECT`) | No | Messaging platforms |
| `whatsappNumber` | string | No | WhatsApp phone number |
| `audience` | object | No |  |
| `budget` | object | No |  |
| `conversionLocation` | string | No | Conversion location |
| `customEventType` | string | No | Custom event type |
| `pixelId` | string | No | Conversion pixel ID |
| `campaignId` | string | Yes | Parent campaign ID |

**`audience` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `geo_locations` | array of object | Yes | Geographic locations to target or exclude |
| `locales` | array of object | No | Language locales to target |
| `placements` | object | No |  |
| `placementType` | string (enum: `auto`, `manual`) | No | Placement strategy — "auto" lets Facebook choose, "manual" uses the placements config |
| `lookalike` | array of object | No | Lookalike audiences to target |
| `retargeting` | array of object | No | Retargeting custom audiences to target |
| `interests` | array of object | No | Interest-based targeting criteria |
| `age_min` | number | No | Minimum age for targeting |
| `age_max` | number | No | Maximum age for targeting |
| `genders` | array of number | No | Gender targeting (1 = male, 2 = female) |

**`budget` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `budgetType` | string (enum: `DAILY`, `LIFETIME`) | Yes | Budget type |
| `amount` | number | Yes | Budget amount |
| `scheduleStartDate` | string | No | Schedule start date |
| `scheduleEndDate` | string | No | Schedule end date |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/facebook/ads-v2`

**Upsert ad**

Create or update a Facebook ad (v2)

**Operation ID:** `fb-upsert-ad`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Ad identifier |
| `locationId` | string | Yes | Location identifier |
| `name` | string | No | Ad name |
| `primaryText` | string | No | Ad primary text |
| `headline` | string | No | Ad headline text |
| `description` | string | No | Ad description text |
| `imageUrl` | string | No | Ad image URL |
| `mediaType` | string (enum: `SINGLE`, `CAROUSEL`) | No | Ad media type |
| `media` | array of object | No | Media items (images or videos) attached to the ad creative |
| `multiAdvertiserAds` | boolean | No | Enable multi-advertiser ads |
| `campaignId` | string | Yes | Parent campaign ID |
| `adsetId` | string | Yes | Parent ad set ID |
| `cta` | string | No | Call to action type |
| `conversationFormId` | string | No | Conversation form ID |
| `destinationLink` | string | No | Destination link URL |
| `destinationFormId` | string | No | Destination form ID |

**`media` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `src` | string | Yes | Media source URL |
| `thumbnailUrl` | string | No | Thumbnail URL (required when type is video) |
| `selectedPoster` | number | No | Selected poster index (required when type is video) |
| `type` | string (enum: `image`, `video`) | Yes | Media content type |
| `name` | string | No | Media file name |
| `headline` | string | No | Media headline |
| `description` | string | No | Media description |
| `link` | string | No | Media destination link |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/campaigns/{campaignId}/pause`

**Pause campaign**

Pause a running Facebook campaign

**Operation ID:** `fb-pause-campaign`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/campaigns/{campaignId}/resume`

**Resume campaign**

Resume a paused Facebook campaign

**Operation ID:** `fb-resume-campaign`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/campaigns/{campaignId}/duplicate`

**Duplicate campaign**

Duplicate an existing Facebook campaign

**Operation ID:** `fb-duplicate-campaign`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/campaigns/{campaignId}`

**Delete campaign**

Delete a Facebook campaign by ID

**Operation ID:** `fb-delete-campaign`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/adsets/{adsetId}/pause`

**Pause ad set**

Pause a running Facebook ad set

**Operation ID:** `fb-pause-adset`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adsetId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/adsets/{adsetId}/resume`

**Resume ad set**

Resume a paused Facebook ad set

**Operation ID:** `fb-resume-adset`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adsetId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/adsets/{adsetId}/duplicate`

**Duplicate ad set**

Duplicate an existing Facebook ad set

**Operation ID:** `fb-duplicate-adset`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adsetId` | path | string | Yes |  |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/adsets/{adsetId}`

**Delete ad set**

Delete a Facebook ad set by ID

**Operation ID:** `fb-delete-adset`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adsetId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/ads/{adId}/pause`

**Pause ad**

Pause a running Facebook ad

**Operation ID:** `fb-pause-ad`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/ads/{adId}/resume`

**Resume ad**

Resume a paused Facebook ad

**Operation ID:** `fb-resume-ad`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/facebook/ads/{adId}/duplicate`

**Duplicate ad**

Duplicate an existing Facebook ad

**Operation ID:** `fb-duplicate-ad`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes |  |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/facebook/ads/{adId}`

**Delete ad**

Delete a Facebook ad by ID

**Operation ID:** `fb-delete-ad`

**Tags:** Facebook Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Google Reporting

### GET `/ad-publishing/google/reporting`

**Get reporting data**

Retrieve aggregated Google Ads reporting metrics for a location

**Operation ID:** `google-get-reporting`

**Tags:** Google Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `groupBy` | query | string (enum: `date`, `week`, `month`) | No | Group by period |
| `startDate` | query | string | Yes | Report start date |
| `endDate` | query | string | Yes | Report end date |
| `type` | query | string (enum: `AD_MANAGER`, `INTEGRATION`) | Yes | Integration type |
| `fields` | query | array of string (enum: `impressions`, `clicks`, `cost_micros`, `average_cpc`, `conversions`, `average_cpm`, `cost_per_conversion`, `ctr`) | Yes | Comma-separated reporting fields |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/reporting/list`

**Get reporting list**

Retrieve a list of Google campaigns or ad groups with reporting data

**Operation ID:** `google-get-reporting-list`

**Tags:** Google Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `listType` | query | string | Yes | Report list type |
| `startDate` | query | string | Yes | Report start date |
| `endDate` | query | string | Yes | Report end date |
| `campaignId` | query | string | No | Campaign identifier |
| `type` | query | string (enum: `AD_MANAGER`, `INTEGRATION`) | Yes | Integration type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/reporting/campaign/{campaignId}`

**Get campaign reporting**

Retrieve reporting metrics for a specific Google campaign

**Operation ID:** `google-get-campaign-reporting`

**Tags:** Google Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignId` | path | string | Yes | Campaign identifier |
| `locationId` | query | string | Yes | Location identifier |
| `startDate` | query | string | Yes | Report start date |
| `endDate` | query | string | Yes | Report end date |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Google Ads

### GET `/ad-publishing/google/conversions`

**Get conversions**

Retrieve Google Ads conversion actions for a location

**Operation ID:** `google-get-conversions`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `AD_MANAGER`, `AD_WORDS`) | No | Integration type |
| `conversionType` | query | string | No | Conversion type |
| `category` | query | string | No | Conversion category |
| `startDate` | query | string | No | Filter start date |
| `endDate` | query | string | No | Filter end date |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/google/conversions`

**Upsert conversion**

Create or update a Google Ads conversion action

**Operation ID:** `google-upsert-conversion`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `conversionId` | string | No | Conversion identifier |
| `name` | string | Yes | Conversion name |
| `type` | string (enum: `UPLOAD_CLICKS`, `UPLOAD_CALLS`, `WEBPAGE`, `LEAD_FORM_SUBMIT`) | Yes | Conversion type |
| `category` | string | Yes | Conversion category |
| `valueSettings` | object | Yes |  |
| `countingType` | string (enum: `ONE_PER_CLICK`, `MANY_PER_CLICK`) | Yes | How conversions are counted per interaction |
| `attributionModel` | string (enum: `GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN`, `GOOGLE_ADS_LAST_CLICK`) | Yes | Attribution model used to credit conversions |
| `clickThroughWindow` | number | Yes | Click-through conversion window in days |

**`valueSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `defaultValue` | number | Yes | Default monetary value assigned to each conversion |
| `defaultCurrencyCode` | string | Yes | ISO 4217 currency code for the default value |
| `alwaysUseDefaultValue` | boolean | Yes | When true, always uses the default value even if a transaction-specific value is provided |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/conversions/{conversionId}`

**Get conversion by ID**

Retrieve a specific Google Ads conversion action by ID

**Operation ID:** `google-get-conversion-by-id`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `conversionId` | path | string | Yes | Conversion identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/google/conversions/{conversionId}`

**Delete conversion**

Delete a Google Ads conversion action by ID

**Operation ID:** `google-delete-conversion`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `conversionId` | path | string | Yes | Conversion identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/google/ads/{adId}/publish`

**Publish ad**

Publish a Google ad and push it live

**Operation ID:** `google-publish-ad`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes | Ad identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/targeting/search`

**Search targeting options**

Search Google geo-locations for ad targeting

**Operation ID:** `google-search-targeting`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `type` | query | string | Yes | Search type |
| `query` | query | string | No | Search query |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/google/keyword-ideas`

**Get keyword ideas**

Retrieve keyword suggestions for Google Ads campaigns

**Operation ID:** `google-get-keyword-ideas`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes | Target URL |
| `languageCode` | string | No | Language code |
| `locations` | array of string | No | Target locations |
| `keywords` | array of string | No | Seed keywords |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/assets`

**Get assets**

Retrieve Google Ads creative assets for a location

**Operation ID:** `google-get-assets`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `CALL`, `SITELINK`, `LEAD_FORM`, `IMAGE`, `TEXT`) | Yes | Asset type to retrieve |
| `id` | query | string | No | Asset identifier |
| `advertiserOnly` | query | string | No | Advertiser only flag |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/google/assets`

**Upsert assets**

Create or update Google Ads creative assets

**Operation ID:** `google-upsert-assets`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `type` | string (enum: `CALL`, `SITELINK`, `LEAD_FORM`) | Yes | Asset type to create or update |
| `payload` | object | object | object | Yes | Asset payload — shape depends on the type field: CallAssetPayload (CALL), SitelinkAssetPayload (SITELINK), or LeadFormAssetPayload (LEAD_FORM) |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/entity`

**Get entities**

Retrieve Google campaigns, ad groups, or ads based on entity type

**Operation ID:** `google-get-entity`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `AD_MANAGER`, `INTEGRATION`) | Yes | Integration type |
| `campaignId` | query | string | No | Campaign identifier |
| `adGroupId` | query | string | No | Ad group identifier |
| `entityType` | query | string (enum: `CAMPAIGN`, `ADGROUP`, `AD`) | Yes | Entity type |
| `searchId` | query | string | No | Search identifier |
| `startDate` | query | string | No | Filter start date |
| `endDate` | query | string | No | Filter end date |
| `selectedAdAccountId` | query | string | No | Selected ad account ID |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/target-interests`

**Get target interests**

Retrieve affinity and in-market audience options for Google Ads targeting

**Operation ID:** `google-get-target-interests`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `AFFINITY`, `IN_MARKET`) | Yes | Interest type |
| `advertisingChannelType` | query | string | Yes | Channel type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/segments`

**Get segments**

Retrieve Google Ads audience segments for a location

**Operation ID:** `google-get-segments`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string | No | Segment type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/google/segments`

**Upsert segment**

Create or update a Google Ads audience segment

**Operation ID:** `google-upsert-segment`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `CUSTOM_SEGMENTS`, `WEBSITE_VISITOR`, `CUSTOMER_MATCH`, `LOOKALIKE`) | Yes | Segment type |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Segment name |
| `description` | string | No | Segment description |
| `members` | array of object | No | Segment members — keywords, URLs, or apps that define the custom segment |
| `status` | string | No | Segment status |
| `type` | string | No | Segment type |
| `id` | string | No | Segment identifier |
| `membershipStatus` | string | No | Membership status |
| `ruleBasedUserList` | object | No |  |
| `membershipLifeSpan` | number | No | Membership life span |
| `seedUserListIds` | array of string | No | Seed user list IDs |
| `countryCodes` | array of string | No | Country codes |
| `expansionLevel` | string (enum: `BALANCED`, `BROAD`, `NARROW`) | No | Expansion level |

**`members` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `memberType` | string (enum: `KEYWORD`, `URL`, `APP`) | Yes | Member type |
| `keyword` | string | No | Keyword value |
| `url` | string | No | URL value |
| `app` | string | No | App identifier |

**`ruleBasedUserList` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `prepopulationStatus` | string (enum: `REQUESTED`) | No | Prepopulation status |
| `flexibleRuleUserList` | object | Yes |  |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/google/segments/{segmentId}`

**Delete segment**

Delete a Google Ads audience segment by ID

**Operation ID:** `google-delete-segment`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `segmentId` | path | string | Yes | Segment identifier |
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `CUSTOM_SEGMENTS`, `DATA_SEGMENTS`) | Yes | Segment type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/segments/{segmentId}`

**Get segment by ID**

Retrieve a specific Google Ads audience segment by ID

**Operation ID:** `google-get-segment-by-id`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `segmentId` | path | string | Yes | Segment identifier |
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `CUSTOM_SEGMENTS`, `DATA_SEGMENTS`) | Yes | Segment type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/google/segments/offline-user-list-job`

**Create offline user list job**

Create a job to upload users to a Google customer match list

**Operation ID:** `google-create-offline-user-list-job`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `smartListIds` | array of string | No | Smart list IDs |
| `csvPath` | string | No | CSV file path |
| `userListId` | string | No | User list identifier |
| `isDynamic` | boolean | No | Dynamic list flag |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/google/audiences`

**Upsert audience**

Create or update a Google Ads combined audience

**Operation ID:** `google-upsert-audience`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `resourceName` | string | No | Audience resource name |
| `name` | string | Yes | Audience name |
| `dimensions` | object | No |  |
| `exclusionDimension` | object | No |  |

**`dimensions` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAgeUnknown` | boolean | No | Include unknown age |
| `ageRanges` | array of string | No | Age range filters |
| `genders` | array of string | No | Gender targets |
| `parentalStatuses` | array of string | No | Parental status targets |
| `audienceSegments` | object | No |  |

**`exclusionDimension` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAgeUnknown` | boolean | No | Include unknown age |
| `ageRanges` | array of string | No | Age range filters |
| `genders` | array of string | No | Gender targets |
| `parentalStatuses` | array of string | No | Parental status targets |
| `audienceSegments` | object | No |  |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/audiences`

**Get audiences**

Retrieve Google Ads combined audiences for a location

**Operation ID:** `google-get-audiences`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/audiences/{audienceId}`

**Get audience by ID**

Retrieve a specific Google Ads combined audience by ID

**Operation ID:** `google-get-audience-by-id`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `audienceId` | path | string | Yes | Audience identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/google/ads`

**Upsert Google campaign**

Create or update a full Google Ads campaign structure

**Operation ID:** `google-upsert-campaign`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Campaign identifier |
| `name` | string | Yes | Campaign name |
| `locationId` | string | Yes | Location identifier |
| `advertisingChannelType` | string (enum: `SEARCH`, `DISCOVERY`, `DISPLAY`, `HOTEL`, `LOCAL`, `MULTI_CHANNEL`, `PERFORMANCE_MAX`, `DEMAND_GEN`) | Yes | Advertising channel |
| `advertisingChannelSubType` | string (enum: `DEMAND_GEN`) | No | Channel sub type |
| `goalType` | string (enum: `WEBSITE_TRAFFIC`, `LEAD`) | No | Goal type |
| `budget` | object | No |  |
| `audience` | object | No |  |
| `networkSettings` | object | No |  |
| `biddingStrategy` | object | No |  |
| `assets` | object | No |  |
| `isEuPoliticalAds` | boolean | No | EU political ads flag |
| `adGroups` | array of object | No | Campaign ad groups |
| `campaignGoal` | object | No |  |
| `adSchedule` | array of object | No | Ad schedule rules |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No | Publishing status |
| `googleAdAccountId` | string | No | Google Ad account identifier |
| `unpublishedChanges` | boolean | No | Whether the campaign has unpublished changes |
| `maximumCpc` | number | No | Maximum CPC bid in micros |
| `googleCampaignId` | string | No | Google Ads campaign resource ID |
| `source` | string | No | Traffic source |
| `advancedOptions` | object | No | Advanced options |

**`budget` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `budgetType` | string (enum: `DAILY`, `LIFETIME`) | No | Budget type |
| `amount` | number | No | Budget amount in micros |
| `scheduleStartDate` | string | No | Schedule start date |
| `scheduleEndDate` | string | No | Schedule end date |

**`audience` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `geo_locations` | array of object | No | Geo-location targeting |
| `locales` | array of object | No | Language/locale targeting |
| `gender` | array of object | No | Gender targeting |
| `ageRange` | array of object | No | Age range targeting |
| `segments` | array of object | No | Audience segment targeting |
| `targetInterests` | object | No |  |

**`networkSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetSearchNetwork` | boolean | Yes | Target Google Search Network |
| `targetContentNetwork` | boolean | Yes | Target Google Display Network |

**`biddingStrategy` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | No | Bidding strategy type |
| `value` | number | No | Bid value in micros |

**`assets` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calls` | array of string | No | Call extension asset resource names |
| `sitelinks` | array of string | No | Sitelink asset resource names |
| `leadForm` | string | No | Lead form asset resource name |
| `images` | array of object | No | Image assets |
| `businessLogo` | object | No |  |

**`adGroups` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Ad group identifier |
| `adGroupId` | string | No | Google ad group identifier |
| `name` | string | No | Ad group name |
| `adCampaignId` | string | No | Ad campaign identifier |
| `adContent` | array of object | No | Ad content items |
| `keywords` | object | No |  |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No | Ad group publishing status |
| `adGroupError` | string | No | Ad group-level error from Google |
| `googleAdGroupId` | string | No | Google Ads ad group resource ID |
| `customChannels` | boolean | No | Custom channels flag |
| `selectedChannels` | array of string (enum: `GMAIL`, `YOUTUBE_IN_STREAM`, `YOUTUBE_SHORTS`, `YOUTUBE_IN_FEED`, `DISCOVER`, `DISPLAY`) | No | Selected channel placements |
| `googleAudienceId` | string | No | Google audience resource ID |
| `audience` | object | No |  |

**`campaignGoal` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `CONVERSIONS`, `CLICK`, `YOUTUBE_ENGAGEMENT`) | Yes | Campaign goal type |
| `value` | string | No | Goal value (e.g. conversion action resource name) |
| `isCustomConversionGoal` | boolean | No | Whether this is a custom conversion goal |

**`adSchedule` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dayOfWeek` | string (enum: `FRIDAY`, `MONDAY`, `SATURDAY`, `SUNDAY`, `THURSDAY`, `TUESDAY`, `UNKNOWN`, `UNSPECIFIED`, `WEDNESDAY`, `ALL_DAYS`, `MONDAY_TO_FRIDAY`, `SATURDAY_AND_SUNDAY`) | Yes | Day of week |
| `from` | string | Yes | Start time (HH:MM) |
| `to` | string | Yes | End time (HH:MM) |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/ads/{adId}`

**Get Google campaign by ID**

Retrieve a specific Google Ads campaign by ID

**Operation ID:** `google-get-campaign-by-id`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes | Ad identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/conversion-goals`

**Get conversion goals**

Retrieve Google Ads conversion goals for a location

**Operation ID:** `google-get-conversion-goals`

**Tags:** Google Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Google Integration

### GET `/ad-publishing/google/integration`

**Get Google integration**

Retrieve the Google Ads integration details for a location

**Operation ID:** `google-get-integration`

**Tags:** Google Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/google/integration`

**Create Google integration**

Create a Google Ads integration for a location

**Operation ID:** `google-create-integration`

**Tags:** Google Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `adAccountId` | string | Yes | Ad account identifier |
| `mccId` | string | Yes | MCC identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/me`

**Get current Google user**

Retrieve the authenticated Google user info for a location

**Operation ID:** `google-get-current-user`

**Tags:** Google Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/ad-accounts`

**Get Google ad accounts**

Retrieve Google Ads accounts available for the connected user

**Operation ID:** `google-get-ad-accounts`

**Tags:** Google Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `type` | query | string (enum: `INTEGRATION`, `AD_MANAGER`) | No | Account type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/google/ad-accounts/{adAccountId}`

**Get ad account details**

Retrieve details of a specific Google Ads account

**Operation ID:** `google-get-ad-account-details`

**Tags:** Google Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `adAccountId` | path | string | Yes | Ad account identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/google/ad-accounts/{adAccountId}`

**Delete ad account**

Remove a Google Ads account connection from a location

**Operation ID:** `google-delete-ad-account`

**Tags:** Google Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adAccountId` | path | string | Yes | Ad account identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## LinkedIn Integration

### GET `/ad-publishing/linkedin/integration`

**Get LinkedIn integration**

Retrieve the LinkedIn Ads integration details for a location

**Operation ID:** `li-get-integration`

**Tags:** LinkedIn Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/linkedin/integration`

**Create LinkedIn integration**

Create a LinkedIn Ads integration for a location with ad account details

**Operation ID:** `li-create-integration`

**Tags:** LinkedIn Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `adAccountId` | string | Yes | Ad account identifier |
| `adAccountName` | string | Yes | Ad account name |
| `currencyCode` | string | Yes | Currency code |
| `organizationId` | string | Yes | Organization identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/linkedin/ad-accounts`

**Get LinkedIn ad accounts**

Retrieve LinkedIn Ads accounts available for the connected user

**Operation ID:** `li-get-ad-accounts`

**Tags:** LinkedIn Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/linkedin/ad-account`

**Get ad account details**

Retrieve details of a specific LinkedIn ad account

**Operation ID:** `li-get-ad-account-details`

**Tags:** LinkedIn Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `adAccountId` | query | string | Yes | Ad account identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/ad-publishing/linkedin/ad-account`

**Delete ad account**

Remove a LinkedIn ad account connection from a location

**Operation ID:** `li-delete-ad-account`

**Tags:** LinkedIn Integration

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `adAccountId` | query | string | Yes | Ad account identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/linkedin/me`

**Get current LinkedIn user**

Retrieve the authenticated LinkedIn user info for a location

**Operation ID:** `li-get-current-user`

**Tags:** LinkedIn Integration

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## LinkedIn Ads

### GET `/ad-publishing/linkedin/ads/{adId}`

**Get ad campaign group**

Retrieve a LinkedIn ad campaign group by ID

**Operation ID:** `li-get-campaign-group`

**Tags:** LinkedIn Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes | Ad identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/linkedin/ads/{adId}/publish`

**Publish ad campaign group**

Publish a LinkedIn ad campaign group and push it live

**Operation ID:** `li-publish-campaign-group`

**Tags:** LinkedIn Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes | Ad identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/ad-publishing/linkedin/ads`

**Upsert ad campaign group**

Create or update a LinkedIn ad campaign group with campaigns and ads

**Operation ID:** `li-upsert-campaign-group`

**Tags:** LinkedIn Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `locationId` | string | Yes | Location ID |
| `budget` | object | No |  |
| `adCampaigns` | array of object | No |  |
| `adBudgetOptimization` | string (enum: `MAXIMUM_DELIVERY`, `COST_CAP`) | No |  |
| `objectiveType` | string (enum: `LEAD_GENERATION`, `WEBSITE_VISIT`) | No |  |
| `name` | string | No |  |
| `adCampaignGroupId` | string | No |  |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No |  |
| `linkedInAdAccountId` | string | No |  |
| `unpublishedChanges` | boolean | No |  |
| `meta` | object | No |  |
| `linkedInError` | string | No |  |

**`budget` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `budgetType` | string (enum: `DAILY`, `LIFETIME`) | No |  |
| `amount` | number | No |  |
| `scheduleStartDate` | string | No | Schedule start date (ISO 8601) |
| `scheduleEndDate` | string | No | Schedule end date (ISO 8601) |

**`adCampaigns` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `locale` | object | No |  |
| `name` | string | No |  |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No |  |
| `mediaType` | string (enum: `STANDARD_UPDATE`, `SINGLE_VIDEO`, `CAROUSEL`) | No | Campaign audience targeting |
| `audience` | object | No |  |
| `unitCost` | object | No |  |
| `campaignType` | string | No |  |
| `adCampaignGroupId` | string | No |  |
| `adCampaignId` | string | No |  |
| `ads` | array of object | No |  |
| `linkedInError` | string | No | LinkedIn API error message |
| `meta` | object | No |  |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/linkedin/targeting/search`

**Search targeting options**

Search LinkedIn targeting facets such as locations, industries, and job titles

**Operation ID:** `li-search-targeting`

**Tags:** LinkedIn Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |
| `facet` | query | string | Yes | Targeting facet |
| `query` | query | string | No | Search query |
| `q` | query | string | No | Query parameter |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/linkedin/{accountId}/forms`

**Get lead forms**

Retrieve LinkedIn lead gen forms for an ad account

**Operation ID:** `li-get-lead-forms`

**Tags:** LinkedIn Ads

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `accountId` | path | string | Yes | Account identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/ad-publishing/linkedin/{accountId}/form`

**Create lead form**

Create a new LinkedIn lead gen form for an ad account

**Operation ID:** `li-create-lead-form`

**Tags:** LinkedIn Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `owner` | object | Yes |  |
| `creationLocale` | object | Yes |  |
| `name` | string | Yes | Form name |
| `state` | string (enum: `PUBLISHED`) | Yes | Form state |
| `content` | object | Yes |  |
| `hiddenFields` | array of object | No | Hidden fields |

**`owner` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sponsoredAccount` | string | Yes | Sponsored account URN |

**`creationLocale` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `country` | string | Yes | Country code |
| `language` | string | Yes | Language code |

**`content` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `questions` | array of object | Yes | Form questions |
| `description` | object | No |  |
| `headline` | object | Yes |  |
| `postSubmissionInfo` | object | Yes |  |
| `legalInfo` | object | Yes |  |

**`hiddenFields` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Field name |
| `value` | string | Yes | Field value |

#### Responses

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/ad-publishing/linkedin/{adId}/status`

**Update ad status**

Pause or resume a LinkedIn ad, campaign, or ad group

**Operation ID:** `li-update-ad-status`

**Tags:** LinkedIn Ads

**Required Scopes:** `adPublishing.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `adId` | path | string | Yes | Ad identifier |
| `locationId` | query | string | Yes | Location identifier |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operationType` | string (enum: `PAUSED`, `ARCHIVED`, `RESUME`) | Yes | Update operation |
| `type` | string (enum: `adGroup`, `adCampaign`, `ad`) | Yes | Ad object type |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## LinkedIn Reporting

### GET `/ad-publishing/linkedin/reporting`

**Get ad analytics**

Retrieve LinkedIn Ads analytics data with configurable pivot and time grouping

**Operation ID:** `li-get-ad-analytics`

**Tags:** LinkedIn Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location ID |
| `pivot` | query | string (enum: `ACCOUNT`, `CAMPAIGN`, `CAMPAIGN_GROUP`, `CREATIVE`) | No | Analytics pivot type |
| `groupBy` | query | string (enum: `day`, `month`, `year`) | No | Time granularity for analytics |
| `startDate` | query | string | Yes | Start date in yyyy-mm-dd format |
| `endDate` | query | string | Yes | End date in yyyy-mm-dd format |
| `entityUrns` | query | string | No | Comma-separated list of entity URNs |
| `fields` | query | array of string | No | Comma-separated list of fields to retrieve |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/linkedin/reporting/list`

**Get reporting list**

Retrieve a list of LinkedIn campaigns or campaign groups with reporting data

**Operation ID:** `li-get-reporting-list`

**Tags:** LinkedIn Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location ID |
| `listType` | query | string | Yes | List type |
| `campaignId` | query | string | Yes | Campaign ID |
| `campaignGroupId` | query | string | Yes | Campaign group ID |
| `startDate` | query | string | Yes | Start date in yyyy-mm-dd format |
| `endDate` | query | string | Yes | End date in yyyy-mm-dd format |
| `fields` | query | array of string | No | Comma-separated list of fields to retrieve |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/ad-publishing/linkedin/reporting/campaign-group/{campaignGroupId}`

**Get campaign group reporting**

Retrieve reporting metrics for a specific LinkedIn campaign group

**Operation ID:** `li-get-campaign-group-reporting`

**Tags:** LinkedIn Reporting

**Required Scopes:** `adPublishing.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `campaignGroupId` | path | string | Yes | Campaign group identifier |
| `locationId` | query | string | Yes | Location ID |
| `startDate` | query | string | Yes | Start date in yyyy-mm-dd format |
| `endDate` | query | string | Yes | End date in yyyy-mm-dd format |
| `fields` | query | array of string | No | Comma-separated list of fields to retrieve |
| `campaignGroupId` | query | string | No | Campaign group ID |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AdCampaignDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `locale` | object | No |  |
| `name` | string | No |  |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No |  |
| `mediaType` | string (enum: `STANDARD_UPDATE`, `SINGLE_VIDEO`, `CAROUSEL`) | No | Campaign audience targeting |
| `audience` | object | No |  |
| `unitCost` | object | No |  |
| `campaignType` | string | No |  |
| `adCampaignGroupId` | string | No |  |
| `adCampaignId` | string | No |  |
| `ads` | array of object | No |  |
| `linkedInError` | string | No | LinkedIn API error message |
| `meta` | object | No |  |

### AdCampaignGroupDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `locationId` | string | Yes | Location ID |
| `budget` | object | No |  |
| `adCampaigns` | array of object | No |  |
| `adBudgetOptimization` | string (enum: `MAXIMUM_DELIVERY`, `COST_CAP`) | No |  |
| `objectiveType` | string (enum: `LEAD_GENERATION`, `WEBSITE_VISIT`) | No |  |
| `name` | string | No |  |
| `adCampaignGroupId` | string | No |  |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No |  |
| `linkedInAdAccountId` | string | No |  |
| `unpublishedChanges` | boolean | No |  |
| `meta` | object | No |  |
| `linkedInError` | string | No |  |

### AdScheduleTargetDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `startMinute` | string (enum: `ZERO`, `FIFTEEN`, `THIRTY`, `FORTY_FIVE`) | Yes | Minute mark the schedule starts at |
| `endMinute` | string (enum: `ZERO`, `FIFTEEN`, `THIRTY`, `FORTY_FIVE`) | Yes | Minute mark the schedule ends at |
| `dayOfWeek` | string (enum: `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`) | Yes | Day of the week for this schedule |
| `startHour` | number | Yes | Start hour in 24h format (0-23) |
| `endHour` | number | Yes | End hour in 24h format (0-23) |

### AudienceCustomAudienceItemDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Custom audience ID |
| `name` | string | Yes | Custom audience name |

### AudienceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `geo_locations` | array of object | No | Geographic location targets |
| `targetAudience` | object | No |  |

### AudienceDimensionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAgeUnknown` | boolean | No | Include unknown age |
| `ageRanges` | array of string | No | Age range filters |
| `genders` | array of string | No | Gender targets |
| `parentalStatuses` | array of string | No | Parental status targets |
| `audienceSegments` | object | No |  |

### AudienceInterestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Interest ID |
| `name` | string | Yes | Interest name |
| `type` | string | No | Interest category type (defaults to "interests" if omitted) |

### AudienceLocaleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Locale display name |
| `key` | number | Yes | Facebook locale key |

### AudienceLocationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | string | Yes | Facebook location key |
| `name` | string | Yes | Location display name |
| `type` | string (enum: `country`, `city`, `region`, `country_group`, `geo_market`, `large_geo_area`, `medium_geo_area`, `small_geo_area`, `subcity`, `neighborhood`, `zip`, `address`) | Yes | Geographic location type |
| `selectionType` | string (enum: `include`, `exclude`) | Yes | Whether the location is included or excluded from targeting |
| `radius` | number | No | Targeting radius around the location (for city/address types) |
| `radiusUnit` | string (enum: `km`, `mi`) | No | Unit for the targeting radius |
| `geometry` | object | No |  |

### AudienceLocationGeometry

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `location` | object | Yes | Geographic coordinates |
| `location_type` | string | Yes | Geocoding result type |

### AudiencePlacementsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facebook` | array of string | No | Facebook placement positions |
| `instagram` | array of string | No | Instagram placement positions |
| `messenger` | array of string | No | Messenger placement positions |

### AudienceSegmentsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customAudiences` | array of string | No | Resource names of custom audience segments |
| `userLists` | array of string | No | Resource names of user lists (remarketing lists, customer match lists, etc.) |
| `userInterests` | array of string | No | Resource names of user interest segments (in-market or affinity audiences) |

### Budget

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `budgetType` | string (enum: `DAILY`, `LIFETIME`) | Yes | Budget type |
| `amount` | number | Yes | Budget amount |
| `scheduleStartDate` | string | No | Schedule start date |
| `scheduleEndDate` | string | No | Schedule end date |

### CallAssetPayloadDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `phoneNumber` | string | Yes | Phone number for call ads |
| `countryCode` | string | Yes | Two-letter ISO country code |
| `callConversionAction` | string | No | Call conversion action resource name |
| `adScheduleTargets` | array of object | No | Ad schedule targets restricting when the call asset is shown |
| `resourceName` | string | No | Google Ads resource name for an existing call asset |

### CampaignDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Campaign identifier |
| `name` | string | Yes | Campaign name |
| `locationId` | string | Yes | Location identifier |
| `advertisingChannelType` | string (enum: `SEARCH`, `DISCOVERY`, `DISPLAY`, `HOTEL`, `LOCAL`, `MULTI_CHANNEL`, `PERFORMANCE_MAX`, `DEMAND_GEN`) | Yes | Advertising channel |
| `advertisingChannelSubType` | string (enum: `DEMAND_GEN`) | No | Channel sub type |
| `goalType` | string (enum: `WEBSITE_TRAFFIC`, `LEAD`) | No | Goal type |
| `budget` | object | No |  |
| `audience` | object | No |  |
| `networkSettings` | object | No |  |
| `biddingStrategy` | object | No |  |
| `assets` | object | No |  |
| `isEuPoliticalAds` | boolean | No | EU political ads flag |
| `adGroups` | array of object | No | Campaign ad groups |
| `campaignGoal` | object | No |  |
| `adSchedule` | array of object | No | Ad schedule rules |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No | Publishing status |
| `googleAdAccountId` | string | No | Google Ad account identifier |
| `unpublishedChanges` | boolean | No | Whether the campaign has unpublished changes |
| `maximumCpc` | number | No | Maximum CPC bid in micros |
| `googleCampaignId` | string | No | Google Ads campaign resource ID |
| `source` | string | No | Traffic source |
| `advancedOptions` | object | No | Advanced options |

### ConsentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `checkRequired` | boolean | Yes | Whether consent checkbox is required |
| `id` | number | Yes | Consent identifier |
| `consent` | object | Yes |  |

### ConversionValueSettings

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `defaultValue` | number | Yes | Default monetary value assigned to each conversion |
| `defaultCurrencyCode` | string | Yes | ISO 4217 currency code for the default value |
| `alwaysUseDefaultValue` | boolean | Yes | When true, always uses the default value even if a transaction-specific value is provided |

### CreateConversationFormDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `name` | string | Yes | Conversation form name |
| `text` | string | Yes | Welcome message text |
| `questions` | array of object | Yes | Quick-reply questions shown in the welcome message of the conversation form |

### CreateGoogleIntegrationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `adAccountId` | string | Yes | Ad account identifier |
| `mccId` | string | Yes | MCC identifier |

### CreateIntegrationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `pageId` | string | Yes | Facebook page ID |
| `adAccountId` | string | No | Ad account identifier |

### CreateLeadFormDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `MORE_VOLUME`, `HIGHER_INTENT`) | Yes | Lead form type |
| `name` | string | Yes | Lead form name |
| `locationId` | string | Yes | Location identifier |
| `greetingCard` | object | No |  |
| `questions` | array of object | Yes | List of questions displayed on the lead form |
| `questionPageHeadline` | string | No | Question page headline |
| `privacyPolicyLink` | string | Yes | Privacy policy URL |
| `privacyPolicyText` | string | No | Privacy policy text |
| `customDisclaimer` | object | No |  |
| `thankYouPage` | object | Yes |  |

### CreateLinkedinIntegrationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `adAccountId` | string | Yes | Ad account identifier |
| `adAccountName` | string | Yes | Ad account name |
| `currencyCode` | string | Yes | Currency code |
| `organizationId` | string | Yes | Organization identifier |

### CreateOfflineUserListJobDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `smartListIds` | array of string | No | Smart list IDs |
| `csvPath` | string | No | CSV file path |
| `userListId` | string | No | User list identifier |
| `isDynamic` | boolean | No | Dynamic list flag |

### CreationLocaleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `country` | string | Yes | Country code |
| `language` | string | Yes | Language code |

### CustomDisclaimer

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Disclaimer title |
| `body` | string | Yes | Disclaimer body text |
| `checkboxes` | array of object | No | Consent checkboxes the user must agree to before submitting the form |

### CustomDisclaimerCheckbox

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `is_required` | boolean | Yes | Checkbox required flag |
| `text` | string | Yes | Checkbox text label |
| `key` | string | Yes | Checkbox unique key |

### CustomQuestionFieldDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customQuestionText` | string | Yes | Custom question text shown to the user |
| `singleChoiceAnswers` | array of string | Yes | Answer choices for the custom question |

### FacebookAudienceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `geo_locations` | array of object | Yes | Geographic locations to target or exclude |
| `locales` | array of object | No | Language locales to target |
| `placements` | object | No |  |
| `placementType` | string (enum: `auto`, `manual`) | No | Placement strategy — "auto" lets Facebook choose, "manual" uses the placements config |
| `lookalike` | array of object | No | Lookalike audiences to target |
| `retargeting` | array of object | No | Retargeting custom audiences to target |
| `interests` | array of object | No | Interest-based targeting criteria |
| `age_min` | number | No | Minimum age for targeting |
| `age_max` | number | No | Maximum age for targeting |
| `genders` | array of number | No | Gender targeting (1 = male, 2 = female) |

### FbSetDefaultPageBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pageId` | string | Yes | Facebook page identifier |

### FbUpdateAudienceBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `name` | string | Yes | Audience name |
| `description` | string | Yes | Audience description |

### FlexibleRuleUserListDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inclusiveRuleOperator` | string | No | Operator for combining inclusive operands |
| `inclusiveOperands` | array of object | Yes | Inclusive rule operands |
| `exclusiveOperands` | array of object | Yes | Exclusive rule operands |

### FormQuestion

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `label` | string | No | Question label text shown to the user |
| `key` | string | Yes | Question key |
| `type` | string (enum: `CUSTOM`, `CITY`, `COMPANY_NAME`, `COUNTRY`, `DATE_OF_BIRTH`, `EMAIL`, `FIRST_NAME`, `FULL_NAME`, `GENDER`, `JOB_TITLE`, `LAST_NAME`, `MARITAL_STATUS`, `MILITARY_STATUS`, `PHONE`, `POST_CODE`, `RELATIONSHIP_STATUS`, `STATE`, `STREET_ADDRESS`, `WORK_EMAIL`, `WORK_PHONE_NUMBER`, `ZIP`, `SHORT_ANSWER`) | Yes | Question input type — use a prefilled type for standard fields or CUSTOM / SHORT_ANSWER for freeform questions |
| `options` | array of object | No | Answer options for multiple-choice questions (only applies to CUSTOM type) |

### FormQuestionOption

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | string | Yes | Option key |
| `value` | string | Yes | Option value |

### GeoAddressComponentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `long_name` | string | No | Full name of the address component |
| `short_name` | string | No | Abbreviated name of the address component |
| `types` | array of string | No | Address component types |

### GeoGeometryDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `location` | object | No |  |
| `location_type` | string | No | Location type (e.g. APPROXIMATE) |
| `viewport` | object | No |  |

### GeoLatLngDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `lat` | number | No | Latitude |
| `lng` | number | No | Longitude |

### GeoLocationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Location display name |
| `urn` | string | Yes | Location URN |
| `facetUrn` | string | Yes | Facet URN |
| `selectionType` | string (enum: `include`, `exclude`) | Yes | Selection type |

### GeoViewportDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `northeast` | object | No |  |
| `southwest` | object | No |  |

### GoogleAdContentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Ad identifier |
| `name` | string | No | Ad name |
| `mediaType` | string (enum: `IMAGE`, `VIDEO`, `CAROUSEL`) | No | Media type |
| `headlines` | array of string | No | Ad headlines |
| `longHeadlines` | array of string | No | Long headlines |
| `descriptions` | array of string | No | Ad descriptions |
| `finalUrl` | string | No | Final URL |
| `path1` | string | No | Display path 1 |
| `path2` | string | No | Display path 2 |
| `isDeleted` | boolean | No | Whether the ad is soft-deleted |
| `adError` | string | No | Ad-level error message from Google |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No | Ad publishing status |
| `adId` | string | No | Internal ad identifier |
| `adCampaignId` | string | No | Ad campaign identifier |
| `adGroupId` | string | No | Ad group identifier |
| `googleAdId` | string | No | Google Ads ad resource ID |
| `media` | array of object | No | Ad media items |
| `callToActionLabel` | string (enum: `AUTOMATED`, `LEARN_MORE`, `GET_QUOTE`, `APPLY_NOW`, `SIGN_UP`, `CONTACT_US`, `SUBSCRIBE`, `DOWNLOAD`, `BOOK_NOW`, `SHOP_NOW`, `BUY_NOW`, `DONATE_NOW`, `ORDER_NOW`, `PLAY_NOW`, `SEE_MORE`) | No | Call to action label |
| `businessName` | string | No | Business name |
| `youtubeVideoLinks` | array of object | No | YouTube video links |
| `carouselCards` | array of object | No | Carousel cards |
| `placements` | array of string (enum: `GMAIL`, `YOUTUBE_IN_STREAM`, `YOUTUBE_SHORTS`, `YOUTUBE_IN_FEED`, `DISCOVER`, `DISPLAY`) | No | Channel placements |
| `customChannels` | boolean | No | Custom channels flag |

### GoogleAdGroupAudienceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `geo_locations` | array of object | No | Geo-location targeting |
| `locales` | array of object | No | Language/locale targeting |

### GoogleAdGroupDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Ad group identifier |
| `adGroupId` | string | No | Google ad group identifier |
| `name` | string | No | Ad group name |
| `adCampaignId` | string | No | Ad campaign identifier |
| `adContent` | array of object | No | Ad content items |
| `keywords` | object | No |  |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No | Ad group publishing status |
| `adGroupError` | string | No | Ad group-level error from Google |
| `googleAdGroupId` | string | No | Google Ads ad group resource ID |
| `customChannels` | boolean | No | Custom channels flag |
| `selectedChannels` | array of string (enum: `GMAIL`, `YOUTUBE_IN_STREAM`, `YOUTUBE_SHORTS`, `YOUTUBE_IN_FEED`, `DISCOVER`, `DISPLAY`) | No | Selected channel placements |
| `googleAudienceId` | string | No | Google audience resource ID |
| `audience` | object | No |  |

### GoogleAdScheduleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dayOfWeek` | string (enum: `FRIDAY`, `MONDAY`, `SATURDAY`, `SUNDAY`, `THURSDAY`, `TUESDAY`, `UNKNOWN`, `UNSPECIFIED`, `WEDNESDAY`, `ALL_DAYS`, `MONDAY_TO_FRIDAY`, `SATURDAY_AND_SUNDAY`) | Yes | Day of week |
| `from` | string | Yes | Start time (HH:MM) |
| `to` | string | Yes | End time (HH:MM) |

### GoogleAssetImageDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes | Image URL |
| `resourceName` | string | No | Google Ads resource name |
| `name` | string | No | Asset name |
| `error` | string | No | Error message if asset upload failed |

### GoogleAssetsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calls` | array of string | No | Call extension asset resource names |
| `sitelinks` | array of string | No | Sitelink asset resource names |
| `leadForm` | string | No | Lead form asset resource name |
| `images` | array of object | No | Image assets |
| `businessLogo` | object | No |  |

### GoogleBiddingStrategyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | No | Bidding strategy type |
| `value` | number | No | Bid value in micros |

### GoogleBudgetDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `budgetType` | string (enum: `DAILY`, `LIFETIME`) | No | Budget type |
| `amount` | number | No | Budget amount in micros |
| `scheduleStartDate` | string | No | Schedule start date |
| `scheduleEndDate` | string | No | Schedule end date |

### GoogleCampaignAudienceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `geo_locations` | array of object | No | Geo-location targeting |
| `locales` | array of object | No | Language/locale targeting |
| `gender` | array of object | No | Gender targeting |
| `ageRange` | array of object | No | Age range targeting |
| `segments` | array of object | No | Audience segment targeting |
| `targetInterests` | object | No |  |

### GoogleCampaignGoalDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `CONVERSIONS`, `CLICK`, `YOUTUBE_ENGAGEMENT`) | Yes | Campaign goal type |
| `value` | string | No | Goal value (e.g. conversion action resource name) |
| `isCustomConversionGoal` | boolean | No | Whether this is a custom conversion goal |

### GoogleCarouselCardDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headline` | string | No | Card headline |
| `finalUrl` | string | No | Card final URL |
| `callToActionLabel` | string | No | Call to action label |
| `media` | array of object | No | Card media items |

### GoogleDemographicTargetDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enum` | string | Yes | Demographic enum value |
| `negative` | boolean | Yes | Whether this is a negative target |

### GoogleGeoLocationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | string | No | Geo target constant resource name |
| `id` | string | No | Location identifier (place_id) |
| `name` | string | No | Location display name |
| `country_name` | string | No | Country name |
| `type` | string | No | Location type (city, region, country, address, etc.) |
| `radius` | number | No | Radius for proximity targeting |
| `radiusUnit` | string (enum: `km`, `mi`) | No | Radius unit |
| `selectionType` | string (enum: `include`, `exclude`) | No | Include or exclude this location |
| `resourceName` | string | No | Google Ads resource name |
| `place_id` | string | No | Google place ID |
| `formatted_address` | string | No | Full formatted address string |
| `geometry` | object | No |  |
| `address_components` | array of object | No | Address components from Google Geocoding API |

### GoogleKeywordItemDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keyword` | string | Yes | Keyword text |
| `matchType` | string | Yes | Match type (BROAD, PHRASE, EXACT) |

### GoogleKeywordsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `positives` | array of object | No | Positive keywords |
| `negatives` | array of object | No | Negative keywords |

### GoogleLocaleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Language display name |
| `key` | string | No | Language key |
| `id` | string | No | Language identifier |
| `resourceName` | string | No | Language resource name |

### GoogleMediaDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `IMAGE`) | No | Media type |
| `src` | string | No | Media source URL |
| `isLogo` | boolean | No | Is logo flag |
| `error` | string | No | Error message if media failed |
| `url` | string | No | Public URL of the media |
| `imageType` | string | No | Image type classification |

### GoogleNetworkSettingsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetSearchNetwork` | boolean | Yes | Target Google Search Network |
| `targetContentNetwork` | boolean | Yes | Target Google Display Network |

### GoogleSegmentTargetDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | Yes | Segment type |
| `id` | string | Yes | Segment identifier |

### GoogleTargetInterestsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `affinity` | array of string | No | Affinity audience IDs |
| `inMarket` | array of string | No | In-market audience IDs |

### GoogleYouTubeVideoLinkDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `youtubeVideoId` | string | Yes | YouTube video ID |

### GreetingCard

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Greeting card title |
| `style` | string | Yes | Greeting card style |
| `content` | array of string | Yes | Greeting card content |

### HiddenFieldDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Field name |
| `value` | string | Yes | Field value |

### KeywordSuggestionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes | Target URL |
| `languageCode` | string | No | Language code |
| `locations` | array of string | No | Target locations |
| `keywords` | array of string | No | Seed keywords |

### LeadFormAssetPayloadDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `resourceName` | string | No | Google Ads resource name for an existing lead form asset |
| `headline` | string | Yes | Lead form headline |
| `description` | string | Yes | Lead form description |
| `businessName` | string | Yes | Business name shown on the form |
| `privacyPolicyUrl` | string | Yes | Privacy policy URL |
| `fields` | array of object | Yes | Form fields to collect user input |
| `callToActionType` | string (enum: `LEARN_MORE`, `GET_QUOTE`, `APPLY_NOW`, `SIGN_UP`, `CONTACT_US`, `SUBSCRIBE`, `DOWNLOAD`, `BOOK_NOW`, `GET_OFFER`, `REGISTER`, `GET_INFO`, `REQUEST_DEMO`, `JOIN_NOW`, `GET_STARTED`, `VISIT_SITE`) | Yes | Call to action button type |
| `callToActionDescription` | string | No | Description text for the CTA button |
| `backgroundImageAsset` | string | No | Background image asset resource name |
| `desiredIntent` | string (enum: `LOW_INTENT`, `HIGH_INTENT`) | No | Desired lead intent level |
| `customQuestionFields` | array of object | No | Custom question fields appended after standard fields |
| `postSubmitHeadline` | string | No | Headline shown after form submission |
| `postSubmitDescription` | string | No | Description shown after form submission |
| `postSubmitCallToActionType` | string (enum: `VISIT_SITE`, `DOWNLOAD`, `LEARN_MORE`, `SHOP_NOW`) | No | Post-submit CTA button type |
| `finalUrls` | string | No | Final URL shown after form submission |

### LeadFormContentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `questions` | array of object | Yes | Form questions |
| `description` | object | No |  |
| `headline` | object | Yes |  |
| `postSubmissionInfo` | object | Yes |  |
| `legalInfo` | object | Yes |  |

### LeadFormFieldDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inputType` | string | Yes | Field input type from Google Ads LeadFormFieldUserInputType |
| `singleChoiceAnswers` | array of string | No | Single-choice answer options for the field |

### LeadFormQuestionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `question` | object | Yes |  |
| `name` | string | Yes | Question field name |
| `questionDetails` | object | Yes |  |
| `predefinedField` | string | No | Predefined field identifier |

### LegalInfoDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `consents` | array of object | Yes | Consent entries |
| `privacyPolicyUrl` | string | Yes | Privacy policy URL |
| `legalDisclaimer` | object | No |  |

### LinkedInAdDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `introductoryText` | string | No |  |
| `destinationUrl` | string | No |  |
| `callToActionLabel` | string | No |  |
| `destinationFormId` | string | No |  |
| `contentReferenceString` | string | No |  |
| `media` | array of object | No |  |
| `adCampaignId` | string | No |  |
| `adId` | string | No |  |
| `headline` | string | No |  |
| `publishingStatus` | string (enum: `DRAFT`, `SCHEDULED`, `PUBLISHED`, `PUBLISHING`, `FAILED`, `IN_REVIEW`, `PAUSED`, `ARCHIVED`, `WITH_ISSUES`, `REJECTED`) | No |  |
| `adCampaignGroupId` | string | No |  |
| `description` | string | No |  |
| `meta` | object | No |  |
| `linkedInError` | string | No | LinkedIn API error message |

### LinkedInBudgetDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `budgetType` | string (enum: `DAILY`, `LIFETIME`) | No |  |
| `amount` | number | No |  |
| `scheduleStartDate` | string | No | Schedule start date (ISO 8601) |
| `scheduleEndDate` | string | No | Schedule end date (ISO 8601) |

### LinkedInCreateLeadFormBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `owner` | object | Yes |  |
| `creationLocale` | object | Yes |  |
| `name` | string | Yes | Form name |
| `state` | string (enum: `PUBLISHED`) | Yes | Form state |
| `content` | object | Yes |  |
| `hiddenFields` | array of object | No | Hidden fields |

### LinkedInMediaDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `video`, `image`) | No | Media type |
| `src` | string | No | Media source URL |
| `frames` | array of string | No | Video frame URLs |
| `selectedPoster` | number | No | Selected poster frame index |
| `thumbnailUrl` | string | No | Thumbnail URL |
| `name` | string | No | Media name |
| `headline` | string | No | Media headline |
| `destinationUrl` | string | No | Click-through destination URL |
| `fileSizeBytes` | number | No | File size in bytes |

### LinkedInUpdateAdStatusBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operationType` | string (enum: `PAUSED`, `ARCHIVED`, `RESUME`) | Yes | Update operation |
| `type` | string (enum: `adGroup`, `adCampaign`, `ad`) | Yes | Ad object type |

### LocaleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `country` | string | Yes | Country code |
| `language` | string | Yes | Language code |

### LocalizedStringDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `localized` | object | Yes | Locale-keyed string map |

### LocationIdBodyDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

### MediaDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `src` | string | Yes | Media source URL |
| `thumbnailUrl` | string | No | Thumbnail URL (required when type is video) |
| `selectedPoster` | number | No | Selected poster index (required when type is video) |
| `type` | string (enum: `image`, `video`) | Yes | Media content type |
| `name` | string | No | Media file name |
| `headline` | string | No | Media headline |
| `description` | string | No | Media description |
| `link` | string | No | Media destination link |

### MemberDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `memberType` | string (enum: `KEYWORD`, `URL`, `APP`) | Yes | Member type |
| `keyword` | string | No | Keyword value |
| `url` | string | No | URL value |
| `app` | string | No | App identifier |

### MultipleChoiceOptionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | number | Yes | Option ID |
| `text` | object | Yes |  |

### MultipleChoiceQuestionDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `options` | array of object | Yes | Choice options |

### PostSubmissionCallToActionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `callToActionTarget` | object | Yes |  |
| `callToActionLabel` | string (enum: `VISIT_COMPANY_WEBSITE`, `DOWNLOAD_NOW`, `TRY_NOW`, `VIEW_NOW`, `LEARN_MORE`) | Yes | Call to action label |

### PostSubmissionCallToActionTargetDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `landingPageUrl` | string | Yes | Landing page URL |

### PostSubmissionInfoDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | object | Yes |  |
| `callToAction` | object | Yes |  |

### PublishAdDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |

### QuestionDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `textQuestionDetails` | object | No | Text question details (empty object for text questions) |
| `multipleChoiceQuestionDetails` | object | No |  |

### RuleBasedUserListDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `prepopulationStatus` | string (enum: `REQUESTED`) | No | Prepopulation status |
| `flexibleRuleUserList` | object | Yes |  |

### RuleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ruleItemGroups` | array of object | Yes | List of rule item groups |

### RuleItemDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string (enum: `url__`, `referrer__`) | Yes | Rule item name |
| `stringRuleItem` | object | Yes |  |

### RuleItemGroupDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ruleItems` | array of object | Yes | List of rule items |

### RuleOperandDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `lookbackWindowDays` | number | Yes | Lookback window in days |
| `rule` | object | Yes |  |

### SelectedAttributeDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `urn` | string | Yes | Targeting attribute URN |
| `name` | string | Yes | Display name |
| `categoryName` | string | Yes | Category name |
| `facet` | string | Yes | Facet identifier |

### SitelinkAssetPayloadDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `resourceName` | string | No | Google Ads resource name for an existing sitelink asset |
| `linkText` | string | Yes | Sitelink display text |
| `finalUrls` | string | Yes | Final landing page URL |
| `description1` | string | No | First description line |
| `description2` | string | No | Second description line |
| `startDate` | string | No | Start date for the sitelink (YYYY-MM-DD) |
| `endDate` | string | No | End date for the sitelink (YYYY-MM-DD) |
| `adScheduleTargets` | array of object | No | Ad schedule targets restricting when the sitelink is shown |

### SponsoredAccountOwnerDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sponsoredAccount` | string | Yes | Sponsored account URN |

### StringRuleItemDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operator` | string | Yes | Rule operator |
| `value` | string | Yes | Rule value |

### TargetAudienceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `include` | array of array of object | No | Included targeting attributes (groups of ANDed attributes, ORed together) |
| `exclude` | array of array of object | No | Excluded targeting attributes |

### ThankYouPage

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Thank you page title |
| `body` | string | Yes | Thank you page body |
| `buttonText` | string | Yes | Button text label |
| `buttonType` | string | Yes | Button action type |
| `buttonLink` | string | No | Button destination link |
| `businessPhone` | string | No | Business phone number |
| `countryCode` | string | No | Phone country code |

### UnitCostDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | number | Yes | Bid amount in currency minor units |

### UpdateCustomAudienceBatchDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `csvPath` | string | No | CSV file path |
| `operationType` | string | Yes | Batch operation type |
| `smartlistIds` | array of string | No | Smartlist IDs array |
| `dynamicAudience` | string | No | Dynamic audience flag |

### UpdateCustomAudienceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `contactId` | string | Yes | Contact identifier |
| `fbAdAccountId` | string | No | Facebook ad account ID |

### UpsertAdDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Ad identifier |
| `locationId` | string | Yes | Location identifier |
| `name` | string | No | Ad name |
| `primaryText` | string | No | Ad primary text |
| `headline` | string | No | Ad headline text |
| `description` | string | No | Ad description text |
| `imageUrl` | string | No | Ad image URL |
| `mediaType` | string (enum: `SINGLE`, `CAROUSEL`) | No | Ad media type |
| `media` | array of object | No | Media items (images or videos) attached to the ad creative |
| `multiAdvertiserAds` | boolean | No | Enable multi-advertiser ads |
| `campaignId` | string | Yes | Parent campaign ID |
| `adsetId` | string | Yes | Parent ad set ID |
| `cta` | string | No | Call to action type |
| `conversationFormId` | string | No | Conversation form ID |
| `destinationLink` | string | No | Destination link URL |
| `destinationFormId` | string | No | Destination form ID |

### UpsertAdsetDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Ad set identifier |
| `locationId` | string | Yes | Location identifier |
| `name` | string | No | Ad set name |
| `pageId` | string | No | Facebook page ID |
| `instagramActorId` | string | No | Instagram actor ID |
| `messagingPlatforms` | string (enum: `WHATSAPP`, `MESSENGER`, `INSTAGRAM_DIRECT`) | No | Messaging platforms |
| `whatsappNumber` | string | No | WhatsApp phone number |
| `audience` | object | No |  |
| `budget` | object | No |  |
| `conversionLocation` | string | No | Conversion location |
| `customEventType` | string | No | Custom event type |
| `pixelId` | string | No | Conversion pixel ID |
| `campaignId` | string | Yes | Parent campaign ID |

### UpsertAssetsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `type` | string (enum: `CALL`, `SITELINK`, `LEAD_FORM`) | Yes | Asset type to create or update |
| `payload` | object | object | object | Yes | Asset payload — shape depends on the type field: CallAssetPayload (CALL), SitelinkAssetPayload (SITELINK), or LeadFormAssetPayload (LEAD_FORM) |

### UpsertAudienceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `resourceName` | string | No | Audience resource name |
| `name` | string | Yes | Audience name |
| `dimensions` | object | No |  |
| `exclusionDimension` | object | No |  |

### UpsertCampaignDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Campaign identifier |
| `locationId` | string | Yes | Location identifier |
| `name` | string | No | Campaign name |
| `objective` | string (enum: `OUTCOME_LEADS`, `OUTCOME_TRAFFIC`, `OUTCOME_ENGAGEMENT`, `OUTCOME_SALES`) | No | Campaign objective |
| `specialAdCategories` | string (enum: `EMPLOYMENT`, `CREDIT`, `FINANCIAL_PRODUCTS_SERVICES`, `HOUSING`, `ISSUES_ELECTIONS_POLITICS`, `ONLINE_GAMBLING_AND_GAMING`, `NONE`) | No | Special ad categories |
| `source` | string | No | Campaign data source |

### UpsertConversionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `conversionId` | string | No | Conversion identifier |
| `name` | string | Yes | Conversion name |
| `type` | string (enum: `UPLOAD_CLICKS`, `UPLOAD_CALLS`, `WEBPAGE`, `LEAD_FORM_SUBMIT`) | Yes | Conversion type |
| `category` | string | Yes | Conversion category |
| `valueSettings` | object | Yes |  |
| `countingType` | string (enum: `ONE_PER_CLICK`, `MANY_PER_CLICK`) | Yes | How conversions are counted per interaction |
| `attributionModel` | string (enum: `GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN`, `GOOGLE_ADS_LAST_CLICK`) | Yes | Attribution model used to credit conversions |
| `clickThroughWindow` | number | Yes | Click-through conversion window in days |

### UpsertConversionPixelDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location identifier |
| `conversionPixelId` | string | No | Conversion pixel ID |
| `name` | string | No | Pixel name |
| `igUserId` | string | No | Instagram user ID |
| `type` | string | Yes | Pixel event type |

### UpsertSegmentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Segment name |
| `description` | string | No | Segment description |
| `members` | array of object | No | Segment members — keywords, URLs, or apps that define the custom segment |
| `status` | string | No | Segment status |
| `type` | string | No | Segment type |
| `id` | string | No | Segment identifier |
| `membershipStatus` | string | No | Membership status |
| `ruleBasedUserList` | object | No |  |
| `membershipLifeSpan` | number | No | Membership life span |
| `seedUserListIds` | array of string | No | Seed user list IDs |
| `countryCodes` | array of string | No | Country codes |
| `expansionLevel` | string (enum: `BALANCED`, `BROAD`, `NARROW`) | No | Expansion level |

### WelcomeMessageQuestion

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `question` | string | Yes | Question title text |
| `response` | string | No | Auto-response message |
