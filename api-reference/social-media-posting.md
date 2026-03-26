# Social Media Posting API

Documentation for Social Media Posting API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Oauth | Google](#oauth-|-google)
- [Post](#post)
- [Account](#account)
- [Oauth | Facebook](#oauth-|-facebook)
- [Oauth | Instagram](#oauth-|-instagram)
- [Oauth | LinkedIn](#oauth-|-linkedin)
- [Oauth | Twitter](#oauth-|-twitter)
- [CSV](#csv)
- [Oauth | Tiktok](#oauth-|-tiktok)
- [Category](#category)
- [Tag](#tag)
- [Statistics](#statistics)

## Oauth | Google

### GET `/social-media-posting/oauth/google/start`

**Starts OAuth For Google Account**

Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Google login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener('message', 
      function(e) {
        if (e.data && e.data.page === 'social_media_posting') {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: "close" 
      page: string,                  Ex: "social-media-posting" 
      platform: string,              Ex: "google" 
      placement: string,             Ex: "placement" 
      accountId: string,             Ex: "658a9b6833b91e0ecb8f3958" 
      reconnectAccounts: string[]]   Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] 
    }
  ### The accountId retrieved from above data can be used to fetch Google account details using below API -
  API: '/social-media-posting/oauth/google/accounts/:accountId' 

  Method: GET

**Operation ID:** `start-google-oauth`

**Tags:** Oauth | Google

**Required Scopes:** `socialplanner/oauth.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | Yes | User Id |
| `page` | query | string | No | Page |
| `reconnect` | query | string | No | Reconnect |

#### Responses

**`200` - Successful Response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/{locationId}/google/locations/{accountId}`

**Get google business locations**

Get google business locations

**Operation ID:** `get-google-locations`

**Tags:** Oauth | Google

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/oauth/{locationId}/google/locations/{accountId}`

**Set google business locations**

Set google business locations

**Operation ID:** `set-google-locations`

**Tags:** Oauth | Google

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `location` | object | No |  |
| `account` | object | No |  |
| `companyId` | string | No | Company ID |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Post

### POST `/social-media-posting/{locationId}/posts/list`

**Get posts**

Get Posts

**Operation ID:** `get-posts`

**Tags:** Post

**Required Scopes:** `socialplanner/post.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | No | type must be one of the following values: recent, all, scheduled, draft, failed, in_review, published, in_progress and deleted Default: `all` |
| `accounts` | string | No | List of account Ids seperated by comma as a string |
| `skip` | string | Yes |  Default: `0` |
| `limit` | string | Yes |  Default: `10` |
| `fromDate` | string | Yes | From Date |
| `toDate` | string | Yes | To Date |
| `includeUsers` | string | Yes | Include User Data |
| `postType` | object | No | Post Type must be one of the following values: - post, story, reel |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/{locationId}/posts`

**Create post**

Create posts for all supported platforms. It is possible to create customized posts per channel by using the same platform account IDs in a request and hitting the create post API multiple times with different summaries and account IDs per platform.

The content and media limitations, as well as platform rate limiters corresponding to the respective platforms, are provided in the following reference link:

  Link: [Platform Limitations](https://help.leadconnectorhq.com/support/solutions/articles/48001240003-social-planner-image-video-content-and-api-limitations "Social Planner Help")

**Operation ID:** `create-post`

**Tags:** Post

**Required Scopes:** `socialplanner/post.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountIds` | array of string | Yes | Account Ids |
| `summary` | string | No | Post Content   The limitations of content as per the platforms is provided through the reference link in API description. The summary will be trimmed based on the limit |
| `media` | array of object | No | Post Media Data   The limitations of media as per the platforms is provided through the reference link in API description |
| `status` | object | No | Status must be one of the following values: null, in_progress, draft, failed, published, scheduled, in_review, notification_sent, deleted |
| `scheduleDate` | string | No | Schedule Date |
| `createdBy` | string | No | Created By |
| `followUpComment` | string | No | Follow Up Comment on platform. It is not allowed on Tiktok and GMB accounts and there is a limit of 280 charecters for twitter account |
| `ogTagsDetails` | object | No |  |
| `type` | object | Yes | Post Type must be one of the following values: - post, story, reel |
| `postApprovalDetails` | object | No |  |
| `scheduleTimeUpdated` | boolean | No | if schedule datetime is updated |
| `tags` | array of string | No | Array of Tag Value |
| `categoryId` | string | No | Category Id |
| `tiktokPostDetails` | object | No |  |
| `gmbPostDetails` | object | No |  |
| `userId` | string | Yes | User ID |

**`media` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes |  |
| `caption` | string | No |  |
| `type` | string | No |  |
| `thumbnail` | string | No |  |
| `defaultThumb` | string | No |  |
| `id` | string | No |  |

**`ogTagsDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `metaImage` | string | No | Meta Image |
| `metaLink` | string | No | Meta Link |

**`postApprovalDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `approver` | string | No | Approver |
| `requesterNote` | string | No | Requester Notes |
| `approverNote` | string | No | Approver Notes |
| `approvalStatus` | object | No | Approval Status must be one of the following values: pending, approved, rejected, not_required |

**`tiktokPostDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `privacyLevel` | object | No | privacy level is an enum and must be one of the following values: PUBLIC_TO_EVERYONE, MUTUAL_FOLLOW_FRIENDS, SELF_ONLY |
| `promoteOtherBrand` | boolean | No | promote other brand |
| `enableComment` | boolean | No | enable comment |
| `enableDuet` | boolean | No | enable duet |
| `enableStitch` | boolean | No | enable stitch |
| `videoDisclosure` | boolean | No | video disclosure |
| `promoteYourBrand` | boolean | No | promote your brand |

**`gmbPostDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gmbEventType` | string | No | gmbEventType must be one of the following values: STANDARD, EVENT, OFFER |
| `title` | string | No | Title |
| `offerTitle` | string | No | Offer Title |
| `startDate` | object | No |  |
| `endDate` | object | No |  |
| `termsConditions` | string | No | Terms Condition Url |
| `url` | string | No | Url |
| `couponCode` | string | No | Coupon Code |
| `redeemOnlineUrl` | string | No | Redeem Online Url |
| `actionType` | object | No | Action Type must be one of the following values: none, order, book, shop, learn_more, call, sign_up |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/{locationId}/posts/{id}`

**Get post**

Get post

**Operation ID:** `get-post`

**Tags:** Post

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Post Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/social-media-posting/{locationId}/posts/{id}`

**Edit post**

Create posts for all supported platforms. It is possible to create customized posts per channel by using the same platform account IDs in a request and hitting the create post API multiple times with different summaries and account IDs per platform.

The content and media limitations, as well as platform rate limiters corresponding to the respective platforms, are provided in the following reference link:

  Link: [Platform Limitations](https://help.leadconnectorhq.com/support/solutions/articles/48001240003-social-planner-image-video-content-and-api-limitations "Social Planner Help")

**Operation ID:** `edit-post`

**Tags:** Post

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Post Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountIds` | array of string | No | Account Ids |
| `summary` | string | No | Post Content   The limitations of content as per the platforms is provided through the reference link in API description |
| `media` | array of object | No | Post Media Data   The limitations of media as per the platforms is provided through the reference link in API description |
| `status` | object | No | Status must be one of the following values: in_progress, draft, failed, published, scheduled, in_review, notification_sent, deleted |
| `scheduleDate` | string | No | Schedule Date |
| `createdBy` | string | No | Created By |
| `followUpComment` | string | No | Follow Up Comment on platform. It is not allowed on Tiktok and GMB accounts and there is a limit of 280 charecters for twitter account |
| `ogTagsDetails` | object | No |  |
| `type` | object | Yes | Post Type must be one of the following values: - post, story, reel |
| `postApprovalDetails` | object | No |  |
| `scheduleTimeUpdated` | boolean | No | if schedule datetime is updated |
| `tags` | array of string | No | Array of Tag Value |
| `categoryId` | string | No | Category Id |
| `tiktokPostDetails` | object | No |  |
| `gmbPostDetails` | object | No |  |
| `userId` | string | No | User ID |

**`media` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes |  |
| `caption` | string | No |  |
| `type` | string | No |  |
| `thumbnail` | string | No |  |
| `defaultThumb` | string | No |  |
| `id` | string | No |  |

**`ogTagsDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `metaImage` | string | No | Meta Image |
| `metaLink` | string | No | Meta Link |

**`postApprovalDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `approver` | string | No | Approver |
| `requesterNote` | string | No | Requester Notes |
| `approverNote` | string | No | Approver Notes |
| `approvalStatus` | object | No | Approval Status must be one of the following values: pending, approved, rejected, not_required |

**`tiktokPostDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `privacyLevel` | object | No | privacy level is an enum and must be one of the following values: PUBLIC_TO_EVERYONE, MUTUAL_FOLLOW_FRIENDS, SELF_ONLY |
| `promoteOtherBrand` | boolean | No | promote other brand |
| `enableComment` | boolean | No | enable comment |
| `enableDuet` | boolean | No | enable duet |
| `enableStitch` | boolean | No | enable stitch |
| `videoDisclosure` | boolean | No | video disclosure |
| `promoteYourBrand` | boolean | No | promote your brand |

**`gmbPostDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gmbEventType` | string | No | gmbEventType must be one of the following values: STANDARD, EVENT, OFFER |
| `title` | string | No | Title |
| `offerTitle` | string | No | Offer Title |
| `startDate` | object | No |  |
| `endDate` | object | No |  |
| `termsConditions` | string | No | Terms Condition Url |
| `url` | string | No | Url |
| `couponCode` | string | No | Coupon Code |
| `redeemOnlineUrl` | string | No | Redeem Online Url |
| `actionType` | object | No | Action Type must be one of the following values: none, order, book, shop, learn_more, call, sign_up |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/social-media-posting/{locationId}/posts/{id}`

**Delete Post**

Delete Post

**Operation ID:** `delete-post`

**Tags:** Post

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Post Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/{locationId}/posts/bulk-delete`

**Bulk Delete Social Planner Posts**

Deletes multiple posts based on the provided list of post IDs. 
                  This operation is useful for clearing up large numbers of posts efficiently. 
                  
Note: 
                  
1.The maximum number of posts that can be deleted in a single request is '50'.
                  
2.However, It will only get deleted in Highlevel database but still
                   it is recommended to be cautious of this operation.

**Operation ID:** `bulk-delete-social-planner-posts`

**Tags:** Post

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `postIds` | array of string | No | Requested Results |

#### Responses

**`201` - Posts deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | any | Yes | Message and deleted count |

**`400` - Cannot delete more than 50 posts at a time.**

**`401` - Unauthorized**

**`404` - No posts found with the given IDs.**

**`422` - Unprocessable Entity**

**`500` - An error occurred while trying to delete the posts. Please try again later.**

---

## Account

### GET `/social-media-posting/{locationId}/accounts`

**Get Accounts**

Get list of accounts and groups

**Operation ID:** `get-account`

**Tags:** Account

**Required Scopes:** `socialplanner/account.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/social-media-posting/{locationId}/accounts/{id}`

**Delete Account**

Delete account and account from group

**Operation ID:** `delete-account`

**Tags:** Account

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Id |
| `companyId` | query | string | No | Company ID |
| `userId` | query | string | No | User ID |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Oauth | Facebook

### GET `/social-media-posting/oauth/facebook/start`

**Starts OAuth For Facebook Account**

Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Facebook login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener('message', 
      function(e) {
        if (e.data && e.data.page === 'social_media_posting') {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: "close" 
      page: string,                  Ex: "social-media-posting" 
      platform: string,              Ex: "facebook" 
      placement: string,             Ex: "placement" 
      accountId: string,             Ex: "658a9b6833b91e0ecb8f3958" 
      reconnectAccounts: string[]]   Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] 
    }
  ### The accountId retrieved from above data can be used to fetch Facebook account details using below API -
  API: '/social-media-posting/oauth/facebook/accounts/:accountId' 

  Method: GET

**Operation ID:** `start-facebook-oauth`

**Tags:** Oauth | Facebook

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Account Location Id |
| `userId` | query | string | Yes | User ID |
| `page` | query | string | No | Facebook Page |
| `reconnect` | query | string | No | Reconnect boolean as string |

#### Responses

**`200` - Successful Response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/{locationId}/facebook/accounts/{accountId}`

**Get facebook pages**

Get facebook pages

**Operation ID:** `get-facebook-page-group`

**Tags:** Oauth | Facebook

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Responses

**`200` - Successful response, runs Facebook OAuth and redirects to application**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/oauth/{locationId}/facebook/accounts/{accountId}`

**Attach facebook pages**

Attach facebook pages

**Operation ID:** `attach-facebook-page-group`

**Tags:** Oauth | Facebook

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | object | No |  |
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `companyId` | string | No | Company ID |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Oauth | Instagram

### GET `/social-media-posting/oauth/instagram/start`

**Starts OAuth For Instagram Account**

Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Instagram login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener('message', 
      function(e) {
        if (e.data && e.data.page === 'social_media_posting') {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: "close" 
      page: string,                  Ex: "social-media-posting" 
      platform: string,              Ex: "instagram" 
      placement: string,             Ex: "placement" 
      accountId: string,             Ex: "658a9b6833b91e0ecb8f3958" 
      reconnectAccounts: string[]]   Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] 
    }
  ### The accountId retrieved from above data can be used to fetch Instagram account details using below API -
  API: '/social-media-posting/oauth/instagram/accounts/:accountId' 

  Method: GET

**Operation ID:** `start-instagram-oauth`

**Tags:** Oauth | Instagram

**Required Scopes:** `socialplanner/oauth.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | Yes | User Id |
| `page` | query | string | No | Page |
| `reconnect` | query | string | No | Reconnect |

#### Responses

**`200` - Successful Response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/{locationId}/instagram/accounts/{accountId}`

**Get Instagram Professional Accounts**

Get Instagram Professional Accounts

**Operation ID:** `get-instagram-page-group`

**Tags:** Oauth | Instagram

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/oauth/{locationId}/instagram/accounts/{accountId}`

**Attach Instagram Professional Accounts**

Attach Instagram Professional Accounts

**Operation ID:** `attach-instagram-page-group`

**Tags:** Oauth | Instagram

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `pageId` | string | Yes |  |
| `companyId` | string | No | Company ID |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Oauth | LinkedIn

### GET `/social-media-posting/oauth/linkedin/start`

**Starts OAuth For LinkedIn Account**

Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to LinkedIn login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener('message', 
      function(e) {
        if (e.data && e.data.page === 'social_media_posting') {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: "close" 
      page: string,                  Ex: "social-media-posting" 
      platform: string,              Ex: "linkedin" 
      placement: string,             Ex: "placement" 
      accountId: string,             Ex: "658a9b6833b91e0ecb8f3958" 
      reconnectAccounts: string[]]   Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] 
    }
  ### The accountId retrieved from above data can be used to fetch LinkedIn account details using below API -
  API: '/social-media-posting/oauth/linkedin/accounts/:accountId' 

  Method: GET

**Operation ID:** `start-linkedin-oauth`

**Tags:** Oauth | LinkedIn

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | Yes | User Id |
| `page` | query | string | No | Page |
| `reconnect` | query | string | No | Reconnect |

#### Responses

**`200` - Successful Response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/{locationId}/linkedin/accounts/{accountId}`

**Get Linkedin pages and profile**

Get Linkedin pages and profile

**Operation ID:** `get-linkedin-page-profile`

**Tags:** Oauth | LinkedIn

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/oauth/{locationId}/linkedin/accounts/{accountId}`

**Attach linkedin pages and profile**

Attach linkedin pages and profile

**Operation ID:** `attach-linkedin-page-profile`

**Tags:** Oauth | LinkedIn

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `page`, `group`, `profile`, `location`, `business`) | No |  |
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `urn` | string | No |  |
| `companyId` | string | No | Company ID |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Oauth | Twitter

### GET `/social-media-posting/oauth/twitter/start`

**Starts OAuth For Twitter Account**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.


  
    !
  
  As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.


**Operation ID:** `start-twitter-oauth`

**Tags:** Oauth | Twitter

**Required Scopes:** `socialplanner/oauth.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | Yes | User Id |
| `page` | query | string | No | Page |
| `reconnect` | query | string | No | Reconnect |

#### Responses

**`200` - Successful Response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/{locationId}/twitter/accounts/{accountId}`

**Get Twitter profile**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.


  
    !
  
  As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.


**Operation ID:** `get-twitter-profile`

**Tags:** Oauth | Twitter

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/oauth/{locationId}/twitter/accounts/{accountId}`

**Attach Twitter profile**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.


  
    !
  
  As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.


**Operation ID:** `attach-twitter-profile`

**Tags:** Oauth | Twitter

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `originId` | string | No |  |
| `name` | string | No |  |
| `username` | string | No |  |
| `avatar` | string | No |  |
| `protected` | boolean | No |  |
| `verified` | boolean | No |  |
| `companyId` | string | No | Company ID |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## CSV

### POST `/social-media-posting/{locationId}/csv`

**Upload CSV**

**Operation ID:** `upload-csv`

**Tags:** CSV

**Required Scopes:** `socialplanner/csv.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `multipart/form-data`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `file` | string | No |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/{locationId}/csv`

**Get Upload Status**

**Operation ID:** `get-upload-status`

**Tags:** CSV

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `skip` | query | string | No |  |
| `limit` | query | string | No |  |
| `includeUsers` | query | string | No |  |
| `userId` | query | string | No | User ID |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/{locationId}/set-accounts`

**Set Accounts**

**Operation ID:** `set-accounts`

**Tags:** CSV

**Required Scopes:** `socialplanner/csv.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountIds` | array of string | Yes | Account Ids |
| `filePath` | string | Yes | File path |
| `rowsCount` | number | Yes | Entires Count. rowcCount must be between 1 and number of posts in CSV |
| `fileName` | string | Yes | Name of file |
| `approver` | string | No |  |
| `userId` | string | No | User ID |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/{locationId}/csv/{id}`

**Get CSV Post**

**Operation ID:** `get-csv-post`

**Tags:** CSV

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |
| `id` | path | string | Yes | CSV Id |
| `skip` | query | string | No |  |
| `limit` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/social-media-posting/{locationId}/csv/{id}`

**Start CSV Finalize**

**Operation ID:** `start-csv-finalize`

**Tags:** CSV

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |
| `id` | path | string | Yes | CSV Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No | User ID |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/social-media-posting/{locationId}/csv/{id}`

**Delete CSV**

**Operation ID:** `delete-csv`

**Tags:** CSV

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |
| `id` | path | string | Yes | CSV Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/social-media-posting/{locationId}/csv/{csvId}/post/{postId}`

**Delete CSV Post**

**Operation ID:** `delete-csv-post`

**Tags:** CSV

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |
| `postId` | path | string | Yes | CSV Post Id |
| `csvId` | path | string | Yes | CSV Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Oauth | Tiktok

### GET `/social-media-posting/oauth/tiktok/start`

**Starts OAuth For Tiktok Account**

Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Tiktok login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener('message', 
      function(e) {
        if (e.data && e.data.page === 'social_media_posting') {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: "close" 
      page: string,                  Ex: "social-media-posting" 
      platform: string,              Ex: "tiktok" 
      placement: string,             Ex: "placement" 
      accountId: string,             Ex: "658a9b6833b91e0ecb8f3958" 
      reconnectAccounts: string[]]   Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] 
    }
  ### The accountId retrieved from above data can be used to fetch Tiktok account details using below API -
  API: '/social-media-posting/oauth/tiktok/accounts/:accountId' 

  Method: GET

**Operation ID:** `start-tiktok-oauth`

**Tags:** Oauth | Tiktok

**Required Scopes:** `socialplanner/oauth.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | Yes | User Id |
| `page` | query | string | No | Page |
| `reconnect` | query | string | No | Reconnect |

#### Responses

**`200` - Successful Response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/{locationId}/tiktok/accounts/{accountId}`

**Get Tiktok profile**

Get Tiktok profile

**Operation ID:** `get-tiktok-profile`

**Tags:** Oauth | Tiktok

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/oauth/{locationId}/tiktok/accounts/{accountId}`

**Attach Tiktok profile**

Attach Tiktok profile

**Operation ID:** `attach-tiktok-profile`

**Tags:** Oauth | Tiktok

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `page`, `group`, `profile`, `location`, `business`) | No |  |
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `verified` | boolean | No |  |
| `username` | string | No |  |
| `companyId` | string | No | Company ID |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/tiktok-business/start`

**Starts OAuth For Tiktok Business Account**

Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Tiktok-Business login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener('message', 
      function(e) {
        if (e.data && e.data.page === 'social_media_posting') {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } = e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: "close" 
      page: string,                  Ex: "social-media-posting" 
      platform: string,              Ex: "tiktok-business" 
      placement: string,             Ex: "placement" 
      accountId: string,             Ex: "658a9b6833b91e0ecb8f3958" 
      reconnectAccounts: string[]]   Ex: ["658a9b6833b91e0ecb834acd", "efd2daa9b6833b91e0ecb8f3511"] 
    }
  ### The accountId retrieved from above data can be used to fetch Tiktok-Business account details using below API -
  API: '/social-media-posting/oauth/tiktok-business/accounts/:accountId' 

  Method: GET

**Operation ID:** `start-tiktok-business-oauth`

**Tags:** Oauth | Tiktok

**Required Scopes:** `socialplanner/oauth.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | Yes | User Id |
| `page` | query | string | No | Page |
| `reconnect` | query | string | No | Reconnect |

#### Responses

**`200` - Successful Response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/oauth/{locationId}/tiktok-business/accounts/{accountId}`

**Get Tiktok Business profile**

Get Tiktok Business profile

**Operation ID:** `get-tiktok-business-profile`

**Tags:** Oauth | Tiktok

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Account Location Id |
| `accountId` | path | string | Yes | Account Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Category

### GET `/social-media-posting/{locationId}/categories`

**Get categories by location id**

**Operation ID:** `get-categories-location-id`

**Tags:** Category

**Required Scopes:** `socialplanner/category.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `searchText` | query | string | No | Search text string |
| `limit` | query | string | No | Limit |
| `skip` | query | string | No | Skip |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/social-media-posting/{locationId}/categories/{id}`

**Get categories by id**

**Operation ID:** `get-categories-id`

**Tags:** Category

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `id` | path | string | Yes | Category Id |
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Tag

### GET `/social-media-posting/{locationId}/tags`

**Get tags by location id**

**Operation ID:** `get-tags-location-id`

**Tags:** Tag

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `searchText` | query | string | No | Search text string |
| `limit` | query | string | No | Limit |
| `skip` | query | string | No | Skip |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/social-media-posting/{locationId}/tags/details`

**Get tags by ids**

**Operation ID:** `get-tags-by-ids`

**Tags:** Tag

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tagIds` | array of string | Yes | Array of Tag Ids |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Statistics

### POST `/social-media-posting/statistics`

**Get Social Media Statistics**

Retrieve analytics data for multiple social media accounts. Provides metrics for the last 7 days with comparison to the previous 7 days. Supports filtering by platforms and specific connected accounts.

**Operation ID:** `get-social-media-statistics`

**Tags:** Statistics

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location ID |

#### Request Body

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `profileIds` | array of string | Yes | Array of connected social media account IDs to fetch analytics for. This can be found as 'profileId' in /accounts api. |
| `platforms` | array of string (enum: `facebook`, `instagram`, `linkedin`, `google`, `pinterest`, `youtube`, `tiktok`) | No | Array of social media platforms to filter analytics by. If not provided, all platforms will be included. NOTE: Linkedin (PAGE only) and Tiktok (BUSINESS only) are supported. |

#### Responses

**`201` - Successfully retrieved analytics data**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `results` | object | No | Analytics data grouped by metrics and platforms |
| `message` | string | No |  |
| `traceId` | string | No |  |

**`400` - Bad Request - Occurs when more than 100 accounts are requested or invalid parameters are provided**

**`401` - Unauthorized - Invalid or missing authentication credentials**

**`422` - Unprocessable Entity - Invalid request body format**

---

## Schemas

### AccountsListResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### AccountsListResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accounts` | array of object | No |  |
| `groups` | array of object | No |  |

### AttachFBAccountDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | object | No |  |
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `companyId` | string | No | Company ID |

### AttachGMBLocationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `location` | object | No |  |
| `account` | object | No |  |
| `companyId` | string | No | Company ID |

### AttachIGAccountDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `pageId` | string | Yes |  |
| `companyId` | string | No | Company ID |

### AttachLinkedinAccountDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `page`, `group`, `profile`, `location`, `business`) | No |  |
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `urn` | string | No |  |
| `companyId` | string | No | Company ID |

### AttachTiktokAccountDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `page`, `group`, `profile`, `location`, `business`) | No |  |
| `originId` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `verified` | boolean | No |  |
| `username` | string | No |  |
| `companyId` | string | No | Company ID |

### AttachTwitterAccountDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `originId` | string | No |  |
| `name` | string | No |  |
| `username` | string | No |  |
| `avatar` | string | No |  |
| `protected` | boolean | No |  |
| `verified` | boolean | No |  |
| `companyId` | string | No | Company ID |

### BulkDeletePostSuccessfulResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `deletedCount` | number | No |  |

### BulkDeleteResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | any | Yes | Message and deleted count |

### CSVDefaultDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No | User ID |

### CSVImportSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Csv Id |
| `locationId` | string | No | locationId |
| `fileName` | string | No | File Name |
| `accountIds` | array of string | No | Account Ids |
| `file` | string | No | File path |
| `status` | string | No | status must be one of the following values: pending, in_progress, completed, failed, in_review, importing, deleted |
| `count` | number | No | Posts count |
| `createdBy` | string | No | Created By Id |
| `traceId` | string | No | Trace Id |
| `originId` | string | No | Origin Id |
| `approver` | string | No | Approver Id |
| `createdAt` | string | No | Date Created |

### CSVMediaResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | No | Media Url |
| `type` | string | No | Media Type |
| `size` | number | No | Media Size |
| `width` | number | No | Media Width |
| `height` | number | No | Media Height |
| `aspectRatio` | number | No | Media Aspect Ratio |
| `duration` | number | No | Media Aspect Ratio |
| `format` | string | No | Media format |
| `videoCodecName` | string | No | Video Codec |
| `frameRate` | number | No | Video Frame Rate |
| `audioCodecName` | string | No | Audio Codec |
| `audioChannels` | number | No | Audio Channel |
| `displayAspectRatio` | string | No | Display Aspect Ratio |
| `frames` | array of string | No | List of frames |
| `selectedPoster` | number | No | Selected Poster |
| `error` | string | No | Error |
| `instagramError` | string | No | Instagram media error. It can we one of the following errors: imageSize, imageType, imageAspectRatio, videoType, videoDuration, videoSize, videoAspectRatio, videoWidthHeight, audioCodec, audioCodecCha... |
| `gmbError` | string | No | GMB media error. It can be one of the following errors: imageSize, imageDimension, imageType |
| `facebookError` | string | No | Facebook media error. It can be one of the following errors: imageSize, imageType, videoDuration, videoSize |
| `linkedinError` | string | No | LinkedIn media error. It can be one of the following errors: imageSize, imageType, videoType, videoDuration, videoSize |
| `twitterError` | string | No | Twitter media error. It can be one of the following errors: imageSize, videoType, videoDuration, videoSize |
| `tiktokError` | string | No | Tiktok media error. It can be one of the following errors: videoType, videoDuration, videoSize, videoWidthHeight, videoCodec, videoFrameRate |
| `tiktokBusinessError` | string | No | Tikok Business media error. It can be one of the following errors: videoType, videoDuration, videoSize, videoWidthHeight, videoCodec, videoFrameRate |
| `invalidError` | string | No | Media error. It can be one of the following values: imageSize, imageWidth |

### CSVPostSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountIds` | array of string | No | Account Ids |
| `link` | object | No |  |
| `medias` | array of object | No | Post Media List |
| `scheduleDate` | string | No |  |
| `summary` | string | No |  |
| `followUpComment` | string | No |  |
| `type` | object | No |  |
| `tiktokPostDetails` | object | No |  |
| `gmbPostDetails` | object | No |  |
| `errorMessage` | string | No | Error Description |

### CSVResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `csv` | object | No |  |

### CategorySchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Category Name |
| `primaryColor` | string | No | Color For Category |
| `secondaryColor` | string | No | Secondary Color |
| `locationId` | string | No | Location ID |
| `_id` | string | No | ID |
| `createdBy` | string | No | Created By User |
| `deleted` | boolean | Yes | Deleted Value |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |

### CreatePostDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountIds` | array of string | Yes | Account Ids |
| `summary` | string | No | Post Content   The limitations of content as per the platforms is provided through the reference link in API description. The summary will be trimmed based on the limit |
| `media` | array of object | No | Post Media Data   The limitations of media as per the platforms is provided through the reference link in API description |
| `status` | object | No | Status must be one of the following values: null, in_progress, draft, failed, published, scheduled, in_review, notification_sent, deleted |
| `scheduleDate` | string | No | Schedule Date |
| `createdBy` | string | No | Created By |
| `followUpComment` | string | No | Follow Up Comment on platform. It is not allowed on Tiktok and GMB accounts and there is a limit of 280 charecters for twitter account |
| `ogTagsDetails` | object | No |  |
| `type` | object | Yes | Post Type must be one of the following values: - post, story, reel |
| `postApprovalDetails` | object | No |  |
| `scheduleTimeUpdated` | boolean | No | if schedule datetime is updated |
| `tags` | array of string | No | Array of Tag Value |
| `categoryId` | string | No | Category Id |
| `tiktokPostDetails` | object | No |  |
| `gmbPostDetails` | object | No |  |
| `userId` | string | Yes | User ID |

### CreatePostSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### CreatePostSuccessfulResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `post` | object | No |  |

### CsvPostStatusResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |

### CsvResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | No |  |
| `fileName` | string | No |  |
| `accountIds` | array of string | No | Account Ids |
| `file` | string | No |  |
| `status` | object | No | status must be one of the following values: pending, in_progress, completed, failed, in_review, importing, deleted |
| `count` | number | No |  |
| `createdBy` | string | No |  |
| `traceId` | string | No |  |
| `originId` | string | No |  |
| `approver` | string | No |  |

### DateSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `year` | number | Yes |  |
| `month` | number | Yes |  |
| `day` | number | Yes |  |

### DeleteAccountResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | No | Location Id |
| `id` | string | No | Id |

### DeleteCsvResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### DeletePostResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### DeletePostResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `postId` | string | Yes | Post Id |

### DeletePostSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### DeletePostSuccessfulResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `postId` | string | No |  |

### DeletePostsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `postIds` | array of string | No | Requested Results |

### EndDateSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `endDate` | object | No |  |
| `endTime` | object | No |  |

### FacebookPageSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `isOwned` | boolean | No |  |
| `isConnected` | boolean | No |  |

### FormatedApprovalDetails

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `approver` | string | No | Approver |
| `requesterNote` | string | No | Requester Notes |
| `approverNote` | string | No | Approver Notes |
| `approvalStatus` | object | No | Approval Status must be one of the following values: pending, approved, rejected, not_required |
| `approverUser` | object | No |  |

### GMBPostSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gmbEventType` | string | No | gmbEventType must be one of the following values: STANDARD, EVENT, OFFER |
| `title` | string | No | Title |
| `offerTitle` | string | No | Offer Title |
| `startDate` | object | No |  |
| `endDate` | object | No |  |
| `termsConditions` | string | No | Terms Condition Url |
| `url` | string | No | Url |
| `couponCode` | string | No | Coupon Code |
| `redeemOnlineUrl` | string | No | Redeem Online Url |
| `actionType` | object | No | Action Type must be one of the following values: none, order, book, shop, learn_more, call, sign_up |

### GetAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `oauthId` | string | No |  |
| `profileId` | string | No |  |
| `name` | string | No |  |
| `platform` | string | No | platform must be one of the following values: google, facebook, instagram, linkedin, twitter, tiktok |
| `type` | string | No |  |
| `expire` | string | No |  |
| `isExpired` | boolean | No |  |
| `meta` | object | No |  |

### GetByIdResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetByIdResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Category Name |
| `primaryColor` | string | No | Color For Category |
| `secondaryColor` | string | No | Secondary Color |
| `locationId` | string | No | Location ID |
| `_id` | string | No | ID |
| `createdBy` | string | No | Created By User |
| `deleted` | boolean | Yes | Deleted Value |
| `message` | string | No | Message |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |

### GetByLocationIdResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetByLocationIdResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | number | Yes | Count |
| `categories` | array of object | Yes | Meta Data |

### GetCategorySchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `category` | object | No |  |

### GetCsvPostResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetCsvPostResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `csv` | object | No |  |
| `count` | number | No |  |
| `posts` | array of object | No | CSV Posts |

### GetFacebookAccountsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetFacebookAccountsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pages` | array of object | No | Facebook Pages Details |

### GetGoogleLocationAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locations` | object | No |  |

### GetGoogleLocationResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetGoogleLocationSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `location` | object | No |  |
| `account` | object | No |  |

### GetGroupSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Group Id |
| `name` | string | Yes | name of group |
| `accountIds` | array of string | Yes |  |

### GetInstagramAccountsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetInstagramAccountsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accounts` | array of object | No | Instagram Account Details |

### GetLinkedInAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pages` | array of object | No | LinkedIn Pages |
| `profile` | array of object | No | LinkedIn Profile Details |

### GetLinkedInAccountsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetPostFormattedSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No |  |
| `source` | string (enum: `composer`, `csv`, `recurring`, `review`, `rss`) | No | source must be one of the following values: composer, recurring, csv |
| `locationId` | string | Yes | Location Id |
| `platform` | string | No | platform must be one of the following values: google, facebook, instagram, linkedin, twitter, tiktok |
| `displayDate` | string | No |  |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |
| `accountId` | string | No | Account Id |
| `error` | string | Yes | Error |
| `postId` | string | No |  |
| `publishedAt` | string | No |  |
| `accountIds` | array of string | No | Account Ids |
| `summary` | string | No |  |
| `media` | array of object | No | Post Media Data   The limitations of media as per the platforms is provided through the reference link in API description |
| `status` | object | No | Status must be one of the following values: in_progress, draft, failed, published, scheduled, in_review, notification_sent, deleted |
| `createdBy` | string | No |  |
| `type` | object | Yes | Post Type must be one of the following values: - post, story, reel |
| `tags` | array of string | No | Tag Ids |
| `ogTagsDetails` | object | No |  |
| `postApprovalDetails` | object | No |  |
| `tiktokPostDetails` | object | No |  |
| `gmbPostDetails` | object | No |  |
| `user` | object | No |  |

### GetPostSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetPostSuccessfulResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `post` | object | No |  |

### GetTagsByIdResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetTagsByIdResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of object | Yes | Social Media Tag Data |
| `count` | number | No | Count |

### GetTagsByLocationIdResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetTagsByLocationIdResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of object | No | Tags Data |
| `count` | number | No | Count |

### GetTiktokAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetTiktokAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `profile` | array of object | No | Tiktok Business Account |

### GetTiktokBusinessAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetTiktokBusinessAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `profile` | array of object | No | Tiktok Profile |

### GetTwitterAccountsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetTwitterAccountsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `profile` | array of object | No | Twitter Profile Details |

### GetUploadStatusResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### GetUploadStatusResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `csvs` | object | Yes |  |
| `count` | number | Yes |  |

### GoogleAccountsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No |  |
| `accountName` | string | No |  |
| `type` | string | No |  |
| `verificationState` | string | No |  |
| `vettedState` | string | No |  |

### GoogleLocationSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No |  |
| `storeCode` | string | No |  |
| `title` | string | No |  |
| `metadata` | object | No | Meta data not related to User |
| `storefrontAddress` | object | No | Store front address |
| `relationshipData` | object | No | All locations and chain related to this one |
| `maxLocation` | boolean | No |  |
| `isVerified` | boolean | No |  |
| `isConnected` | boolean | No |  |

### IOgTagsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | No | Tag url |
| `ogDescription` | string | No | Tag description |
| `ogImage` | object | No |  |
| `ogTitle` | string | No | Tag Title |
| `ogUrl` | string | No | Tag Url |
| `ogSiteName` | string | No | Site Name |
| `error` | string | No | Og Tag Error |

### InstagramAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `pageId` | string | No |  |
| `isConnected` | boolean | No |  |

### LinkedInPageSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Page ID |
| `name` | string | No | LinkedIn Page Name |
| `avatar` | string | No | Profile Avatar url |
| `urn` | string | No | URN |
| `isConnected` | boolean | No | is connected to app |

### LinkedInProfileSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Id |
| `name` | string | No | Name of profile |
| `avatar` | string | No | Profile avatar |
| `urn` | string | No | URN |
| `isConnected` | boolean | No | is connected to app |

### LocationAndAccountDeleteResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### OgImageSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | No | Image url |
| `width` | number | No | Image width |
| `height` | number | No | Image height |
| `type` | string | No | Image Type |

### OgTagsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `metaImage` | string | No | Meta Image |
| `metaLink` | string | No | Meta Link |

### PostApprovalSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `approver` | string | No | Approver |
| `requesterNote` | string | No | Requester Notes |
| `approverNote` | string | No | Approver Notes |
| `approvalStatus` | object | No | Approval Status must be one of the following values: pending, approved, rejected, not_required |

### PostCreateRequest

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountIds` | array of string | No | Account Ids |
| `summary` | string | No | Post Content   The limitations of content as per the platforms is provided through the reference link in API description |
| `media` | array of object | No | Post Media Data   The limitations of media as per the platforms is provided through the reference link in API description |
| `status` | object | No | Status must be one of the following values: in_progress, draft, failed, published, scheduled, in_review, notification_sent, deleted |
| `scheduleDate` | string | No | Schedule Date |
| `createdBy` | string | No | Created By |
| `followUpComment` | string | No | Follow Up Comment on platform. It is not allowed on Tiktok and GMB accounts and there is a limit of 280 charecters for twitter account |
| `ogTagsDetails` | object | No |  |
| `type` | object | Yes | Post Type must be one of the following values: - post, story, reel |
| `postApprovalDetails` | object | No |  |
| `scheduleTimeUpdated` | boolean | No | if schedule datetime is updated |
| `tags` | array of string | No | Array of Tag Value |
| `categoryId` | string | No | Category Id |
| `tiktokPostDetails` | object | No |  |
| `gmbPostDetails` | object | No |  |
| `userId` | string | No | User ID |

### PostMediaSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes |  |
| `caption` | string | No |  |
| `type` | string | No |  |
| `thumbnail` | string | No |  |
| `defaultThumb` | string | No |  |
| `id` | string | No |  |

### PostSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### PostSuccessfulResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `posts` | array of object | No | Post Data |
| `count` | number | No |  |

### PostUserSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | User Id |
| `title` | string | Yes | Title |
| `firstName` | string | Yes | First name |
| `lastName` | string | Yes | Last name |
| `profilePhoto` | string | Yes | Profile photo |
| `phone` | string | Yes | Phone number |
| `email` | string | Yes | Email Id |

### SearchPostDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | No | type must be one of the following values: recent, all, scheduled, draft, failed, in_review, published, in_progress and deleted Default: `all` |
| `accounts` | string | No | List of account Ids seperated by comma as a string |
| `skip` | string | Yes |  Default: `0` |
| `limit` | string | Yes |  Default: `10` |
| `fromDate` | string | Yes | From Date |
| `toDate` | string | Yes | To Date |
| `includeUsers` | string | Yes | Include User Data |
| `postType` | object | No | Post Type must be one of the following values: - post, story, reel |

### SetAccountsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountIds` | array of string | Yes | Account Ids |
| `filePath` | string | Yes | File path |
| `rowsCount` | number | Yes | Entires Count. rowcCount must be between 1 and number of posts in CSV |
| `fileName` | string | Yes | Name of file |
| `approver` | string | No |  |
| `userId` | string | No | User ID |

### SetAccountsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |

### SocialGoogleMediaAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No |  |
| `oAuthId` | string | No |  |
| `oldId` | string | No |  |
| `locationId` | string | No |  |
| `originId` | string | No |  |
| `platform` | object | No |  |
| `type` | object | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `meta` | object | No |  |
| `active` | boolean | No |  |
| `deleted` | boolean | No |  |
| `createdAt` | string | No | created date |
| `updatedAt` | string | No | updated date |

### SocialMediaFBAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### SocialMediaFacebookAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No |  |
| `oAuthId` | string | No |  |
| `oldId` | string | No |  |
| `locationId` | string | No |  |
| `originId` | string | No |  |
| `platform` | object | No |  |
| `type` | object | No | type value must be page |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `meta` | object | No |  |
| `active` | boolean | No |  |
| `deleted` | boolean | No |  |
| `createdAt` | string | No | created date |
| `updatedAt` | string | No | updated date |

### SocialMediaGmbAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### SocialMediaInstagramAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### SocialMediaInstagramAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No |  |
| `oAuthId` | string | No |  |
| `oldId` | string | No |  |
| `locationId` | string | No |  |
| `originId` | string | No |  |
| `platform` | object | No |  |
| `type` | object | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `meta` | object | No |  |
| `active` | boolean | No |  |
| `deleted` | boolean | No |  |
| `createdAt` | string | No | created date |
| `updatedAt` | string | No | updated date |

### SocialMediaLinkedInAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### SocialMediaLinkedInAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No |  |
| `oAuthId` | string | No |  |
| `oldId` | string | No |  |
| `locationId` | string | No |  |
| `originId` | string | No |  |
| `platform` | object | No |  |
| `type` | object | No | type must be one of the following values: page, profile |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `meta` | object | No |  |
| `active` | boolean | No |  |
| `deleted` | boolean | No |  |
| `createdAt` | string | No | created date |
| `updatedAt` | string | No | updated date |

### SocialMediaTagSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tag` | string | No | Tag Name |
| `locationId` | string | No | Location Id |
| `_id` | string | No | ID |
| `createdBy` | string | No | Created By User Id |
| `deleted` | boolean | No | Deleted boolean value |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |

### SocialMediaTiktokAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### SocialMediaTiktokAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No |  |
| `oAuthId` | string | No |  |
| `oldId` | string | No |  |
| `locationId` | string | No |  |
| `originId` | string | No |  |
| `platform` | object | No |  |
| `type` | object | No | type must be one of the following values: profile, business |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `meta` | object | No |  |
| `active` | boolean | No |  |
| `deleted` | boolean | No |  |
| `createdAt` | string | No | created date |
| `updatedAt` | string | No | updated date |

### SocialMediaTwitterAccountResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### SocialMediaTwitterAccountSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No |  |
| `oAuthId` | string | No |  |
| `oldId` | string | No |  |
| `locationId` | string | No |  |
| `originId` | string | No |  |
| `platform` | object | No |  |
| `type` | object | No |  |
| `name` | string | No |  |
| `avatar` | string | No |  |
| `meta` | object | No |  |
| `active` | boolean | No |  |
| `deleted` | boolean | No |  |
| `createdAt` | string | No | created date |
| `updatedAt` | string | No | updated date |

### StartDateSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `startDate` | object | No |  |
| `startTime` | object | No |  |

### TiktokPostSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `privacyLevel` | object | No | privacy level is an enum and must be one of the following values: PUBLIC_TO_EVERYONE, MUTUAL_FOLLOW_FRIENDS, SELF_ONLY |
| `promoteOtherBrand` | boolean | No | promote other brand |
| `enableComment` | boolean | No | enable comment |
| `enableDuet` | boolean | No | enable duet |
| `enableStitch` | boolean | No | enable stitch |
| `videoDisclosure` | boolean | No | video disclosure |
| `promoteYourBrand` | boolean | No | promote your brand |

### TiktokProfileSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Id |
| `name` | string | No | Name of account |
| `username` | string | No | Username of account |
| `avatar` | string | No | Avatar of profile account |
| `verified` | boolean | No | Is verified |
| `isConnected` | boolean | No | Is connected |
| `type` | object | No | Tiktok Account Type must be one of the following values: business, profile |

### TimeSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `hours` | number | Yes |  |
| `minutes` | number | Yes |  |
| `seconds` | number | Yes |  |

### TwitterProfileSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | ID of profile |
| `name` | string | No | Name of profile |
| `username` | string | No | Username of profile |
| `avatar` | string | No | Avatar of profile |
| `protected` | boolean | No | Is protected |
| `verified` | boolean | No | Is verified |
| `isConnected` | boolean | No | Is connected |

### UpdatePostSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |

### UpdateTagDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tagIds` | array of string | Yes | Array of Tag Ids |

### UploadCSVDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `file` | string | No |  |

### UploadFileResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success or Failure |
| `statusCode` | number | Yes | Status Code |
| `message` | string | Yes | Message |
| `results` | object | No |  |

### UploadFileResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `filePath` | string | No |  |
| `rowsCount` | number | No |  |
| `fileName` | string | No |  |
