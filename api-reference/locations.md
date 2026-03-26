# Sub-Accounts (Locations) API

Documentation for Sub-Account (Formerly location) API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Search](#search)
- [Sub-Account (Formerly Location)](#sub-account-formerly-location)
- [Tags](#tags)
- [Tasks Search](#tasks-search)
- [Recurring Tasks](#recurring-tasks)
- [Custom Field](#custom-field)
- [Custom Value](#custom-value)
- [Timezone](#timezone)
- [Template](#template)

## Search

### GET `/locations/search`

**Search**

Search Sub-Account (Formerly Location)

**Operation ID:** `search-locations`

**Tags:** Search

**Required Scopes:** `locations.readonly`, `locations.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `companyId` | query | string | No | The company/agency id on which you want to perform the search |
| `skip` | query | string | No | The value by which the results should be skipped. Default will be 0 |
| `limit` | query | string | No | The value by which the results should be limited. Default will be 10 |
| `order` | query | string | No | The order in which the results should be returned - Allowed values asc, desc. Default will be asc |
| `email` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locations` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Sub-Account (Formerly Location)

### GET `/locations/{locationId}`

**Get Sub-Account (Formerly Location)**

Get details of a Sub-Account (Formerly Location) by passing the sub-account id

**Operation ID:** `get-location`

**Tags:** Sub-Account (Formerly Location)

**Required Scopes:** `locations.readonly`, `locations.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `location` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/locations/{locationId}`

**Put Sub-Account (Formerly Location)**

Update a Sub-Account (Formerly Location) based on the data provided

**Operation ID:** `put-location`

**Tags:** Sub-Account (Formerly Location)

**Required Scopes:** `locations.write`

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
| `name` | string | No | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created |
| `companyId` | string | Yes | Company/Agency Id |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `country` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | The country in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `prospectInfo` | object | No |  |
| `settings` | object | No |  |
| `social` | object | No |  |
| `twilio` | object | No |  |
| `mailgun` | object | No |  |
| `snapshot` | object | No |  |

**`prospectInfo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | Yes | First name of the prospect |
| `lastName` | string | Yes | Last name of the prospect |
| `email` | string | Yes | Email of the prospect |

**`settings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `allowDuplicateContact` | boolean | No |  |
| `allowDuplicateOpportunity` | boolean | No |  |
| `allowFacebookNameMerge` | boolean | No |  |
| `disableContactTimezone` | boolean | No |  |

**`social` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facebookUrl` | string | No | Facebook URL |
| `googlePlus` | string | No | Googleplus URL |
| `linkedIn` | string | No | LinkedIn URL |
| `foursquare` | string | No | Foursquare URL |
| `twitter` | string | No | Twitter URL |
| `yelp` | string | No | Yelp URL |
| `instagram` | string | No | Instagram URL |
| `youtube` | string | No | Instagram URL |
| `pinterest` | string | No | Instagram URL |
| `blogRss` | string | No | Instagram URL |
| `googlePlacesId` | string | No | Google Business Places ID |

**`twilio` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sid` | string | Yes | SID provided by Twilio |
| `authToken` | string | Yes | Auth token provided by Twilio |

**`mailgun` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `apiKey` | string | Yes | API key provided by Mailgun |
| `domain` | string | Yes | Domain connected with Mailgun |

**`snapshot` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Snaptshot ID |
| `override` | boolean | No | If you want override all conflicted assets then pass true. Default value is false. Default: `False` |

#### Responses

**`200` - Successful update response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Location Id |
| `companyId` | string | No | Company/Agency Id |
| `name` | string | No | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created |
| `email` | string | No | The email for the sub-account/location |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `domain` | string | No |  |
| `country` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | The country in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `settings` | object | No |  |
| `social` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/locations/{locationId}`

**Delete Sub-Account (Formerly Location)**

Delete a Sub-Account (Formerly Location) from the Agency

**Operation ID:** `delete-location`

**Tags:** Sub-Account (Formerly Location)

**Required Scopes:** `locations.internal-access-only`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `deleteTwilioAccount` | query | boolean | Yes | Boolean value to indicate whether to delete Twilio Account or not |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the API |
| `message` | string | Yes | Success message of the API |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/locations/`

**Create Sub-Account (Formerly Location)**


                  Create a new Sub-Account (Formerly Location) based on the data provided 
                  
                    
                                !
                      
                      
                        
                          This feature is only available on Agency Pro ($497) plan.
                        
                      
                  
                
    

**Operation ID:** `create-location`

**Tags:** Sub-Account (Formerly Location)

**Required Scopes:** `locations.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created with the appropriate country-code |
| `companyId` | string | Yes | Company/Agency Id |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `country` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | The 2 letter country-code in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `prospectInfo` | object | No |  |
| `settings` | object | No |  |
| `social` | object | No |  |
| `twilio` | object | No |  |
| `mailgun` | object | No |  |
| `snapshotId` | string | No | The snapshot ID to be loaded into the location. |

**`prospectInfo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | Yes | First name of the prospect |
| `lastName` | string | Yes | Last name of the prospect |
| `email` | string | Yes | Email of the prospect |

**`settings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `allowDuplicateContact` | boolean | No |  |
| `allowDuplicateOpportunity` | boolean | No |  |
| `allowFacebookNameMerge` | boolean | No |  |
| `disableContactTimezone` | boolean | No |  |

**`social` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facebookUrl` | string | No | Facebook URL |
| `googlePlus` | string | No | Googleplus URL |
| `linkedIn` | string | No | LinkedIn URL |
| `foursquare` | string | No | Foursquare URL |
| `twitter` | string | No | Twitter URL |
| `yelp` | string | No | Yelp URL |
| `instagram` | string | No | Instagram URL |
| `youtube` | string | No | Instagram URL |
| `pinterest` | string | No | Instagram URL |
| `blogRss` | string | No | Instagram URL |
| `googlePlacesId` | string | No | Google Business Places ID |

**`twilio` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sid` | string | Yes | SID provided by Twilio |
| `authToken` | string | Yes | Auth token provided by Twilio |

**`mailgun` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `apiKey` | string | Yes | API key provided by Mailgun |
| `domain` | string | Yes | Domain connected with Mailgun |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Location Id |
| `companyId` | string | No | Company/Agency Id |
| `name` | string | No | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created |
| `email` | string | No | The email for the sub-account/location |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `domain` | string | No |  |
| `country` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | The country in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `settings` | object | No |  |
| `social` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Tags

### GET `/locations/{locationId}/tags`

**Get Tags**

Get Sub-Account (Formerly Location) Tags

**Operation ID:** `get-location-tags`

**Tags:** Tags

**Required Scopes:** `locations/tags.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/locations/{locationId}/tags`

**Create Tag**

Create tag

**Operation ID:** `create-tag`

**Tags:** Tags

**Required Scopes:** `locations/tags.write`

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
| `name` | string | Yes | Tag name |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tag` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/locations/{locationId}/tags/{tagId}`

**Get tag by id**

Get tag by id

**Operation ID:** `get-tag-by-id`

**Tags:** Tags

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `tagId` | path | string | Yes | Tag Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tag` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/locations/{locationId}/tags/{tagId}`

**Update tag**

Update tag

**Operation ID:** `update-tag`

**Tags:** Tags

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `tagId` | path | string | Yes | Tag Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Tag name |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tag` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/locations/{locationId}/tags/{tagId}`

**Delete tag**

Delete tag

**Operation ID:** `delete-tag`

**Tags:** Tags

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `tagId` | path | string | Yes | Tag Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Tasks Search

### POST `/locations/{locationId}/tasks/search`

**Task Search Filter**

Task Search

**Operation ID:** `task-search`

**Tags:** Tasks Search

**Required Scopes:** `locations/tasks.readonly`

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
| `contactId` | array of string | No | Contact Ids |
| `completed` | boolean | No | Task Completed Or Pending |
| `assignedTo` | array of string | No | Assigned User Ids |
| `query` | string | No | Search Value |
| `limit` | number | No | Limit To Api Default: `25` |
| `skip` | number | No | Number Of Tasks To Skip Default: `0` |
| `businessId` | string | No | Bussiness Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tasks` | array of array of any | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Recurring Tasks

### GET `/locations/{locationId}/recurring-tasks/{id}`

**Get Recurring Task By Id**

Get Recurring Task By Id

**Operation ID:** `get-recurring-task-by-id`

**Tags:** Recurring Tasks

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Recurring Task Id |
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recurringTask` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/locations/{locationId}/recurring-tasks/{id}`

**Update Recurring Task**

Update Recurring Task

**Operation ID:** `update-recurring-task`

**Tags:** Recurring Tasks

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Recurring Task Id |
| `locationId` | path | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Name of the task |
| `description` | string | No | Description of the task |
| `contactIds` | array of string | No | Contact Id |
| `owners` | array of string | No | Assigned To |
| `rruleOptions` | object | No |  |
| `ignoreTaskCreation` | boolean | No | Create initial task or not |

**`rruleOptions` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `intervalType` | string (enum: `yearly`, `monthly`, `weekly`, `daily`, `hourly`) | Yes |  |
| `interval` | number | Yes |  |
| `startDate` | string | Yes | Start Date |
| `endDate` | string | No | End Date |
| `dayOfMonth` | number | No | 1, 2, 3, ..., 27, 31 |
| `dayOfWeek` | string (enum: `MO`, `TU`, `WE`, `TH`, `FR`, `SA`, `SU`) | No |  |
| `monthOfYear` | number | No | 1, 2, ....., 11, 12 |
| `count` | number | No | Max number of task executions |
| `createTaskIfOverDue` | boolean | No | Create Task If Over Due |
| `dueAfterSeconds` | number | Yes | Due after seconds |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recurringTask` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/locations/{locationId}/recurring-tasks/{id}`

**Delete Recurring Task**

Delete Recurring Task

**Operation ID:** `delete-recurring-task`

**Tags:** Recurring Tasks

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Recurring Task Id |
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Recurring Task Id |
| `success` | boolean | Yes | Success |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/locations/{locationId}/recurring-tasks`

**Create Recurring Task**

Create Recurring Task

**Operation ID:** `create-recurring-task`

**Tags:** Recurring Tasks

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Name of the task |
| `description` | string | No | Description of the task |
| `contactIds` | array of string | No | Contact Id |
| `owners` | array of string | No | Assigned To |
| `rruleOptions` | object | Yes |  |
| `ignoreTaskCreation` | boolean | No | Create initial task or not |

**`rruleOptions` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `intervalType` | string (enum: `yearly`, `monthly`, `weekly`, `daily`, `hourly`) | Yes |  |
| `interval` | number | Yes |  |
| `startDate` | string | Yes | Start Date |
| `endDate` | string | No | End Date |
| `dayOfMonth` | number | No | 1, 2, 3, ..., 27, 31 |
| `dayOfWeek` | string (enum: `MO`, `TU`, `WE`, `TH`, `FR`, `SA`, `SU`) | No |  |
| `monthOfYear` | number | No | 1, 2, ....., 11, 12 |
| `count` | number | No | Max number of task executions |
| `createTaskIfOverDue` | boolean | No | Create Task If Over Due |
| `dueAfterSeconds` | number | Yes | Due after seconds |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recurringTask` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Custom Field

### GET `/locations/{locationId}/customFields`

**Get Custom Fields**

Get Custom Fields

**Operation ID:** `get-custom-fields`

**Tags:** Custom Field

**Required Scopes:** `locations/customFields.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `model` | query | string (enum: `contact`, `opportunity`, `all`) | No | Model of the custom field you want to retrieve |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customFields` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/locations/{locationId}/customFields`

**Create Custom Field**

Create Custom Field

**Operation ID:** `create-custom-field`

**Tags:** Custom Field

**Required Scopes:** `locations/customFields.write`

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
| `name` | string | Yes |  |
| `dataType` | string | Yes |  |
| `placeholder` | string | No |  |
| `acceptedFormat` | array of string | No |  |
| `isMultipleFile` | boolean | No |  |
| `maxNumberOfFiles` | number | No |  |
| `textBoxListOptions` | array of object | object | No |  |
| `position` | number | No |  Default: `0` |
| `model` | string (enum: `contact`, `opportunity`) | No | Model of the custom field you want to create |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customField` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/locations/{locationId}/customFields/{id}`

**Get Custom Field**

Get Custom Field

**Operation ID:** `get-custom-field`

**Tags:** Custom Field

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Custom Field Id or Field Key (e.g. "contact.first_name" or "opportunity.pipeline_id") |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customField` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/locations/{locationId}/customFields/{id}`

**Update Custom Field**

Update Custom Field

**Operation ID:** `update-custom-field`

**Tags:** Custom Field

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Custom Field Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `placeholder` | string | No |  |
| `acceptedFormat` | array of string | No |  |
| `isMultipleFile` | boolean | No |  |
| `maxNumberOfFiles` | number | No |  |
| `textBoxListOptions` | array of object | object | No |  |
| `position` | number | No |  Default: `0` |
| `model` | string (enum: `contact`, `opportunity`) | No | Model of the custom field you want to update |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customField` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/locations/{locationId}/customFields/{id}`

**Delete Custom Field**

Delete Custom Field

**Operation ID:** `delete-custom-field`

**Tags:** Custom Field

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Custom Field Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/locations/{locationId}/customFields/upload`

**Uploads File to customFields**

Uploads File to customFields

**Operation ID:** `upload-file-customFields`

**Tags:** Custom Field

**Required Scopes:** `locations/customFields.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `multipart/form-data`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Id(Contact Id/Opportunity Id/Custom Field Id) |
| `maxFiles` | string | No | Max number of files |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadedFiles` | object | No | Uploaded files |
| `meta` | array of string | No | Meta data of uploaded files |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Custom Value

### GET `/locations/{locationId}/customValues`

**Get Custom Values**

Get Custom Values

**Operation ID:** `get-custom-values`

**Tags:** Custom Value

**Required Scopes:** `locations/customValues.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customValues` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/locations/{locationId}/customValues`

**Create Custom Value**

Create Custom Value

**Operation ID:** `create-custom-value`

**Tags:** Custom Value

**Required Scopes:** `locations/customValues.write`

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
| `name` | string | Yes |  |
| `value` | string | Yes |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customValue` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/locations/{locationId}/customValues/{id}`

**Get Custom Value**

Get Custom Value

**Operation ID:** `get-custom-value`

**Tags:** Custom Value

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Custom Value Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customValue` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/locations/{locationId}/customValues/{id}`

**Update Custom Value**

Update Custom Value

**Operation ID:** `update-custom-value`

**Tags:** Custom Value

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Custom Value Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `value` | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customValue` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/locations/{locationId}/customValues/{id}`

**Delete Custom Value**

Delete Custom Value

**Operation ID:** `delete-custom-value`

**Tags:** Custom Value

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Custom Value Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Timezone

### GET `/locations/{locationId}/timezones`

**Fetch Timezones**

Fetch the available timezones

**Operation ID:** `get-timezones`

**Tags:** Timezone

**Required Scopes:** `locations.readonly`, `locations.readonly`

**API Version:** `2021-07-28`

#### Responses

**`200` - Successful response**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Template

### GET `/locations/{locationId}/templates`

**GET all or email/sms templates**

GET all or email/sms templates

**Operation ID:** `GET-all-or-email-sms-templates`

**Tags:** Template

**Required Scopes:** `locations/templates.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `deleted` | query | boolean | No |  |
| `skip` | query | string | No |  |
| `limit` | query | string | No |  |
| `type` | query | string (enum: `sms`, `email`, `whatsapp`) | No |  |
| `originId` | query | string | Yes | Origin Id |
| `locationId` | path | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `templates` | array of object | object | No |  |
| `totalCount` | number | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/locations/{locationId}/templates/{id}`

**DELETE an email/sms template**

DELETE an email/sms template

**Operation ID:** `DELETE-an-email-sms-template`

**Tags:** Template

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location Id |
| `id` | path | string | Yes | Template Id |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### BusinessSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No |  |
| `address` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `country` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `logoUrl` | string | No |  |

### CreateCustomFieldsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `dataType` | string | Yes |  |
| `placeholder` | string | No |  |
| `acceptedFormat` | array of string | No |  |
| `isMultipleFile` | boolean | No |  |
| `maxNumberOfFiles` | number | No |  |
| `textBoxListOptions` | array of object | object | No |  |
| `position` | number | No |  Default: `0` |
| `model` | string (enum: `contact`, `opportunity`) | No | Model of the custom field you want to create |

### CreateLocationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created with the appropriate country-code |
| `companyId` | string | Yes | Company/Agency Id |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `country` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | The 2 letter country-code in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `prospectInfo` | object | No |  |
| `settings` | object | No |  |
| `social` | object | No |  |
| `twilio` | object | No |  |
| `mailgun` | object | No |  |
| `snapshotId` | string | No | The snapshot ID to be loaded into the location. |

### CreateLocationSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Location Id |
| `companyId` | string | No | Company/Agency Id |
| `name` | string | No | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created |
| `email` | string | No | The email for the sub-account/location |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `domain` | string | No |  |
| `country` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | The country in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `settings` | object | No |  |
| `social` | object | No |  |

### CustomFieldDeleteSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### CustomFieldSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `fieldKey` | string | No |  |
| `placeholder` | string | No |  |
| `dataType` | string | No |  |
| `position` | number | No |  |
| `picklistOptions` | array of string | No |  |
| `picklistImageOptions` | array of string | No |  |
| `isAllowedCustomOption` | boolean | No |  |
| `isMultiFileAllowed` | boolean | No |  |
| `maxFileLimit` | number | No |  |
| `locationId` | string | No |  |
| `model` | string (enum: `contact`, `opportunity`) | No | Model of the custom field |

### CustomFieldSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customField` | object | No |  |

### CustomFieldsListSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customFields` | array of object | No |  |

### CustomRRulesOptions

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `intervalType` | string (enum: `yearly`, `monthly`, `weekly`, `daily`, `hourly`) | Yes |  |
| `interval` | number | Yes |  |
| `startDate` | string | Yes | Start Date |
| `endDate` | string | No | End Date |
| `dayOfMonth` | number | No | 1, 2, 3, ..., 27, 31 |
| `dayOfWeek` | string (enum: `MO`, `TU`, `WE`, `TH`, `FR`, `SA`, `SU`) | No |  |
| `monthOfYear` | number | No | 1, 2, ....., 11, 12 |
| `count` | number | No | Max number of task executions |
| `createTaskIfOverDue` | boolean | No | Create Task If Over Due |
| `dueAfterSeconds` | number | Yes | Due after seconds |

### CustomValueDeleteSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### CustomValueIdSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customValue` | object | No |  |

### CustomValueSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `fieldKey` | string | No |  |
| `value` | string | No |  |
| `locationId` | string | No |  |

### CustomValuesListSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customValues` | array of object | No |  |

### DeleteRecurringTaskResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Recurring Task Id |
| `success` | boolean | Yes | Success |

### EmailTemplateSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `subject` | string | No |  |
| `attachments` | array of array of any | No |  |
| `html` | string | No |  |

### FileUploadBody

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Id(Contact Id/Opportunity Id/Custom Field Id) |
| `maxFiles` | string | No | Max number of files |

### FileUploadResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadedFiles` | object | No | Uploaded files |
| `meta` | array of string | No | Meta data of uploaded files |

### GetEmailTemplateResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `type` | string | No |  |
| `dateAdded` | string | No |  |
| `template` | object | No |  |
| `locationId` | string | No |  |

### GetLocationByIdSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `companyId` | string | No |  |
| `name` | string | No |  |
| `domain` | string | No |  |
| `address` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `logoUrl` | string | No |  |
| `country` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `business` | object | No |  |
| `social` | object | No |  |
| `settings` | object | No |  |
| `reseller` | object | No |  |

### GetLocationByIdSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `location` | object | No |  |

### GetLocationSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Location Id |
| `name` | string | No | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created |
| `email` | string | No | The email for the sub-account/location |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `country` | string | No | The country in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `settings` | object | No |  |
| `social` | object | No |  |

### GetSmsTemplateResponseSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `type` | string | No |  |
| `template` | object | No |  |
| `dateAdded` | string | No |  |
| `locationId` | string | No |  |
| `urlAttachments` | array of string | No |  |

### GetTemplatesSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `templates` | array of object | object | No |  |
| `totalCount` | number | No |  |

### LocationDeletedSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status of the API |
| `message` | string | Yes | Success message of the API |

### LocationTagDeleteSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### LocationTagSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tag` | object | No |  |

### LocationTagsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No |  |
| `locationId` | string | No |  |
| `id` | string | No |  |

### LocationTagsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of object | No |  |

### LocationTaskListSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tasks` | array of array of any | No |  |

### MailgunSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `apiKey` | string | Yes | API key provided by Mailgun |
| `domain` | string | Yes | Domain connected with Mailgun |

### ProspectInfoDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | Yes | First name of the prospect |
| `lastName` | string | Yes | Last name of the prospect |
| `email` | string | Yes | Email of the prospect |

### RecurringTaskCreateDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Name of the task |
| `description` | string | No | Description of the task |
| `contactIds` | array of string | No | Contact Id |
| `owners` | array of string | No | Assigned To |
| `rruleOptions` | object | Yes |  |
| `ignoreTaskCreation` | boolean | No | Create initial task or not |

### RecurringTaskResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Recurring Task Id |
| `title` | string | Yes | Name of the task |
| `description` | string | Yes | Description of the task |
| `locationId` | string | Yes | Location Id |
| `updatedAt` | string | Yes | Updated At |
| `createdAt` | string | Yes | Created At |
| `rruleOptions` | object | Yes |  |
| `totalOccurrence` | number | Yes | Total Occurrence |
| `deleted` | boolean | Yes | Deleted |
| `assignedTo` | string | No | Assigned To |
| `contactId` | string | No | Contact Id |

### RecurringTaskSingleResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recurringTask` | object | Yes |  |

### RecurringTaskUpdateDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Name of the task |
| `description` | string | No | Description of the task |
| `contactIds` | array of string | No | Contact Id |
| `owners` | array of string | No | Assigned To |
| `rruleOptions` | object | No |  |
| `ignoreTaskCreation` | boolean | No | Create initial task or not |

### SearchSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locations` | array of object | No |  |

### SettingsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `allowDuplicateContact` | boolean | No |  |
| `allowDuplicateOpportunity` | boolean | No |  |
| `allowFacebookNameMerge` | boolean | No |  |
| `disableContactTimezone` | boolean | No |  |

### SmsTemplateSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `body` | string | No |  |
| `attachments` | array of array of any | No |  |

### SnapshotPutSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Snaptshot ID |
| `override` | boolean | No | If you want override all conflicted assets then pass true. Default value is false. Default: `False` |

### SocialSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facebookUrl` | string | No | Facebook URL |
| `googlePlus` | string | No | Googleplus URL |
| `linkedIn` | string | No | LinkedIn URL |
| `foursquare` | string | No | Foursquare URL |
| `twitter` | string | No | Twitter URL |
| `yelp` | string | No | Yelp URL |
| `instagram` | string | No | Instagram URL |
| `youtube` | string | No | Instagram URL |
| `pinterest` | string | No | Instagram URL |
| `blogRss` | string | No | Instagram URL |
| `googlePlacesId` | string | No | Google Business Places ID |

### TaskSearchParamsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contactId` | array of string | No | Contact Ids |
| `completed` | boolean | No | Task Completed Or Pending |
| `assignedTo` | array of string | No | Assigned User Ids |
| `query` | string | No | Search Value |
| `limit` | number | No | Limit To Api Default: `25` |
| `skip` | number | No | Number Of Tasks To Skip Default: `0` |
| `businessId` | string | No | Bussiness Id |

### TwilioSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sid` | string | Yes | SID provided by Twilio |
| `authToken` | string | Yes | Auth token provided by Twilio |

### UpdateCustomFieldsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `placeholder` | string | No |  |
| `acceptedFormat` | array of string | No |  |
| `isMultipleFile` | boolean | No |  |
| `maxNumberOfFiles` | number | No |  |
| `textBoxListOptions` | array of object | object | No |  |
| `position` | number | No |  Default: `0` |
| `model` | string (enum: `contact`, `opportunity`) | No | Model of the custom field you want to update |

### UpdateLocationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | The name for the sub-account/location |
| `phone` | string | No | The phone number of the business for which sub-account is created |
| `companyId` | string | Yes | Company/Agency Id |
| `address` | string | No | The address of the business for which sub-account is created |
| `city` | string | No | The city where the business is located for which sub-account is created |
| `state` | string | No | The state in which the business operates for which sub-account is created |
| `country` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | The country in which the business is present for which sub-account is created |
| `postalCode` | string | No | The postal code of the business for which sub-account is created |
| `website` | string | No | The website of the business for which sub-account is created |
| `timezone` | string | No | The timezone of the business for which sub-account is created |
| `prospectInfo` | object | No |  |
| `settings` | object | No |  |
| `social` | object | No |  |
| `twilio` | object | No |  |
| `mailgun` | object | No |  |
| `snapshot` | object | No |  |

### customValuesDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `value` | string | Yes |  |

### tagBody

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Tag name |

### textBoxListOptionsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `label` | string | No |  |
| `prefillValue` | string | No |  |
