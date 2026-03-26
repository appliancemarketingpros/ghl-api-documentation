# OAuth 2.0 API

Documentation for OAuth 2.0 API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [OAuth 2.0](#oauth-2.0)

## OAuth 2.0

### POST `/oauth/token`

**Get Access Token**

Use Access Tokens to access GoHighLevel resources on behalf of an authenticated location/company.

**Operation ID:** `get-access-token`

**Tags:** OAuth 2.0

#### Request Body

**Required:** Yes

**Content Type:** `application/x-www-form-urlencoded`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `client_id` | string | Yes | The ID provided by GHL for your integration |
| `client_secret` | string | Yes |  |
| `grant_type` | string (enum: `authorization_code`, `refresh_token`, `client_credentials`) | Yes |  |
| `code` | string | No |  |
| `refresh_token` | string | No |  |
| `user_type` | string (enum: `Company`, `Location`) | No | The type of token to be requested |
| `redirect_uri` | string | No | The redirect URI for your application |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `access_token` | string | No |  |
| `token_type` | string | No |  |
| `expires_in` | number | No |  |
| `refresh_token` | string | No |  |
| `scope` | string | No |  |
| `userType` | string | No |  |
| `locationId` | string | No | Location ID - Present only for Sub-Account Access Token |
| `companyId` | string | No | Company ID |
| `approvedLocations` | array of string | No | Approved locations to generate location access token |
| `userId` | string | Yes | USER ID - Represent user id of person who performed installation |
| `planId` | string | No | Plan Id of the subscribed plan in paid apps. |
| `isBulkInstallation` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/oauth/locationToken`

**Get Location Access Token from Agency Token**

This API allows you to generate locationAccessToken from AgencyAccessToken

**Operation ID:** `get-location-access-token`

**Tags:** OAuth 2.0

**Required Scopes:** `oauth.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/x-www-form-urlencoded`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes | Company Id of location you want to request token for |
| `locationId` | string | Yes | The location ID for which you want to obtain accessToken |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `access_token` | string | No | Location access token which can be used to authenticate & authorize API under following scope |
| `token_type` | string | No |  |
| `expires_in` | number | No | Time in seconds remaining for token to expire |
| `scope` | string | No | Scopes the following accessToken have access to |
| `locationId` | string | No | Location ID - Present only for Sub-Account Access Token |
| `planId` | string | No | Plan Id of the subscribed plan in paid apps. |
| `userId` | string | Yes | USER ID - Represent user id of person who performed installation |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/oauth/installedLocations`

**Get Location where app is installed**

This API allows you fetch location where app is installed upon

**Operation ID:** `get-installed-location`

**Tags:** OAuth 2.0

**Required Scopes:** `oauth.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `skip` | query | string | No | Parameter to skip the number installed locations |
| `limit` | query | string | No | Parameter to limit the number installed locations |
| `query` | query | string | No | Parameter to search for the installed location by name |
| `isInstalled` | query | boolean | No | Filters out location which are installed for specified app under the specified company |
| `companyId` | query | string | Yes | Parameter to search by the companyId |
| `appId` | query | string | Yes | Parameter to search by the appId |
| `versionId` | query | string | No | VersionId of the app |
| `onTrial` | query | boolean | No | Filters out locations which are installed for specified app in trial mode |
| `planId` | query | string | No | Filters out location which are installed for specified app under the specified planId |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locations` | array of object | No |  |
| `count` | number | No | Total location count under the company |
| `installToFutureLocations` | boolean | No | Boolean to control if user wants app to be automatically installed to future locations |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### GetAccessCodeSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `access_token` | string | No |  |
| `token_type` | string | No |  |
| `expires_in` | number | No |  |
| `refresh_token` | string | No |  |
| `scope` | string | No |  |
| `userType` | string | No |  |
| `locationId` | string | No | Location ID - Present only for Sub-Account Access Token |
| `companyId` | string | No | Company ID |
| `approvedLocations` | array of string | No | Approved locations to generate location access token |
| `userId` | string | Yes | USER ID - Represent user id of person who performed installation |
| `planId` | string | No | Plan Id of the subscribed plan in paid apps. |
| `isBulkInstallation` | boolean | No |  |

### GetAccessCodebodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `client_id` | string | Yes | The ID provided by GHL for your integration |
| `client_secret` | string | Yes |  |
| `grant_type` | string (enum: `authorization_code`, `refresh_token`, `client_credentials`) | Yes |  |
| `code` | string | No |  |
| `refresh_token` | string | No |  |
| `user_type` | string (enum: `Company`, `Location`) | No | The type of token to be requested |
| `redirect_uri` | string | No | The redirect URI for your application |

### GetInstalledLocationsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locations` | array of object | No |  |
| `count` | number | No | Total location count under the company |
| `installToFutureLocations` | boolean | No | Boolean to control if user wants app to be automatically installed to future locations |

### GetLocationAccessCodeBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes | Company Id of location you want to request token for |
| `locationId` | string | Yes | The location ID for which you want to obtain accessToken |

### GetLocationAccessTokenSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `access_token` | string | No | Location access token which can be used to authenticate & authorize API under following scope |
| `token_type` | string | No |  |
| `expires_in` | number | No | Time in seconds remaining for token to expire |
| `scope` | string | No | Scopes the following accessToken have access to |
| `locationId` | string | No | Location ID - Present only for Sub-Account Access Token |
| `planId` | string | No | Plan Id of the subscribed plan in paid apps. |
| `userId` | string | Yes | USER ID - Represent user id of person who performed installation |

### InstalledLocationSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Location ID |
| `name` | string | Yes | Name of the location |
| `address` | string | Yes | Address linked to location |
| `isInstalled` | boolean | No | Check if the requested app is installed for following location |
