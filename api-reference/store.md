# Store API

Documentation for store API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Shipping Zone](#shipping-zone)
- [Shipping Zone Rates](#shipping-zone-rates)
- [Shipping Carrier](#shipping-carrier)
- [Store Setting](#store-setting)

## Shipping Zone

### POST `/store/shipping-zone`

**Create Shipping Zone**

The "Create Shipping Zone" API allows adding a new shipping zone.

**Operation ID:** `create-shipping-zone`

**Tags:** Shipping Zone

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping zone |
| `countries` | array of object | Yes | List of countries that are available |

**`countries` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | number (enum: `['US', 'CA', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']`) | Yes | Country code |
| `states` | array of object | No | List of states that are available. If states is empty, then all states are available |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/store/shipping-zone`

**List Shipping Zones**

The "List Shipping Zone" API allows to retrieve a list of shipping zone.

**Operation ID:** `list-shipping-zones`

**Tags:** Shipping Zone

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `limit` | query | number | No | The maximum number of items to be included in a single page of results |
| `offset` | query | number | No | The starting index of the page, indicating the position from which the results should be retrieved. |
| `withShippingRate` | query | boolean | No | Include shipping rates array |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `data` | array of object | Yes | An array of items |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/store/shipping-zone/{shippingZoneId}`

**Get Shipping Zone**

The "List Shipping Zone" API allows to retrieve a paginated list of shipping zone.

**Operation ID:** `get-shipping-zones`

**Tags:** Shipping Zone

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the item that needs to be returned |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `withShippingRate` | query | boolean | No | Include shipping rates array |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/store/shipping-zone/{shippingZoneId}`

**Update Shipping Zone**

The "update Shipping Zone" API allows update a shipping zone to the system. 

**Operation ID:** `update-shipping-zone`

**Tags:** Shipping Zone

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the item that needs to be returned |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | No | Location Id or Agency Id |
| `altType` | string (enum: `location`) | No |  |
| `name` | string | No | Name of the shipping zone |
| `countries` | array of object | No | List of countries that are available |

**`countries` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | number (enum: `['US', 'CA', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']`) | Yes | Country code |
| `states` | array of object | No | List of states that are available. If states is empty, then all states are available |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/store/shipping-zone/{shippingZoneId}`

**Delete shipping zone**

Delete specific shipping zone with Id :shippingZoneId

**Operation ID:** `delete-shipping-zone`

**Tags:** Shipping Zone

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the item that needs to be returned |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/store/shipping-zone/shipping-rates`

**Get available shipping rates**

This return available shipping rates for country based on order amount

**Operation ID:** `get-available-shipping-zones`

**Tags:** Shipping Zone

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `country` | string (enum: `US`, `CA`, `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `KR`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `UA`, `AE`, `GB`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | Yes | Country code of the customer |
| `address` | object | No |  |
| `amountAvailable` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | it will not calculate the order amount form backend if it is true |
| `totalOrderAmount` | number | Yes | The amount of the price. ( min: 0.01 ) |
| `weightAvailable` | boolean | No | Flag to pass when the weight is already calculated and should not calculate again |
| `totalOrderWeight` | number | Yes | Estimated weight of the order calculated from the order creation side in kg(s) |
| `source` | object | Yes |  |
| `products` | array of object | Yes | An array of price IDs and quantity |
| `couponCode` | string | No | Coupon code |

**`address` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the customer |
| `companyName` | string | No | Name of the Company |
| `addressLine1` | string | No | Address line 1 of the customer |
| `country` | string (enum: `US`, `CA`, `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `KR`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `UA`, `AE`, `GB`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | Yes | Country code of the customer |
| `state` | string (enum: `AL`, `AK`, `AS`, `AZ`, `AR`, `AA`, `AE`, `AP`, `CA`, `CO`, `CT`, `DE`, `DC`, `FM`, `FL`, `GA`, `GU`, `HI`, `ID`, `IL`, `IN`, `IA`, `KS`, `KY`, `LA`, `ME`, `MH`, `MD`, `MA`, `MI`, `MN`, `MS`, `MO`, `MT`, `NE`, `NV`, `NH`, `NJ`, `NM`, `NY`, `NC`, `ND`, `MP`, `OH`, `OK`, `OR`, `PW`, `PA`, `PR`, `RI`, `SC`, `SD`, `TN`, `TX`, `UT`, `VT`, `VI`, `VA`, `WA`, `WV`, `WI`, `WY`, `AB`, `BC`, `MB`, `NB`, `NL`, `NT`, `NS`, `NU`, `ON`, `PE`, `QC`, `SK`, `YT`, `BA`, `CT`, `CC`, `CH`, `CB`, `CN`, `ER`, `FO`, `JY`, `LP`, `LR`, `MZ`, `MN`, `NQ`, `RN`, `SA`, `SJ`, `SL`, `SC`, `SF`, `SE`, `TF`, `TU`, `ACT`, `NSW`, `NT`, `QLD`, `SA`, `TAS`, `VIC`, `WA`, `AC`, `AL`, `AM`, `AP`, `BA`, `CE`, `DF`, `ES`, `GO`, `MA`, `MG`, `MS`, `MT`, `PA`, `PB`, `PE`, `PI`, `PR`, `RJ`, `RN`, `RO`, `RR`, `RS`, `SC`, `SE`, `SP`, `TO`, `AI`, `AN`, `AP`, `AT`, `BI`, `CO`, `AR`, `LI`, `LL`, `LR`, `MA`, `ML`, `RM`, `TA`, `VS`, `NB`, `AMA`, `ANT`, `ARA`, `ATL`, `BOL`, `BOY`, `CAL`, `CAQ`, `CAS`, `CAU`, `CES`, `CHO`, `CUN`, `COR`, `GUA`, `GUV`, `HUI`, `LAG`, `MAG`, `MET`, `NAR`, `NSA`, `PUT`, `QUI`, `RIS`, `SAP`, `SAN`, `SUC`, `TOL`, `VAC`, `VAU`, `VID`, `CR-A`, `CR-C`, `CR-G`, `CR-H`, `CR-L`, `CR-P`, `CR-SJ`, `GT-16`, `GT-15`, `GT-04`, `GT-20`, `GT-02`, `GT-05`, `GT-01`, `GT-13`, `GT-18`, `GT-21`, `GT-22`, `GT-17`, `GT-09`, `GT-14`, `GT-11`, `GT-03`, `GT-12`, `GT-06`, `GT-07`, `GT-10`, `GT-08`, `GT-19`, `HK`, `KL`, `NT`, `AN`, `AP`, `AR`, `AS`, `BR`, `CH`, `CG`, `DN`, `DD`, `DL`, `GA`, `GJ`, `HR`, `HP`, `JK`, `JH`, `KA`, `KL`, `LA`, `LD`, `MP`, `MH`, `MN`, `ML`, `MZ`, `NL`, `OR`, `PY`, `PB`, `RJ`, `SK`, `TN`, `TS`, `TR`, `UP`, `UK`, `WB`, `CW`, `CN`, `CE`, `CO`, `DL`, `D`, `G`, `KY`, `KE`, `KK`, `LS`, `LM`, `LK`, `LD`, `LH`, `MO`, `MH`, `MN`, `OY`, `RN`, `SO`, `TA`, `WD`, `WH`, `WX`, `WW`, `AG`, `AL`, `AN`, `AO`, `AR`, `AP`, `AT`, `AV`, `BA`, `BT`, `BL`, `BN`, `BG`, `BI`, `BO`, `BZ`, `BS`, `BR`, `CA`, `CL`, `CB`, `CI`, `CE`, `CT`, `CZ`, `CH`, `CO`, `CS`, `CR`, `KR`, `CN`, `EN`, `FM`, `FE`, `FI`, `FG`, `FC`, `FR`, `GE`, `GO`, `GR`, `IM`, `IS`, `AQ`, `SP`, `LT`, `LE`, `LC`, `LI`, `LO`, `LU`, `MC`, `MN`, `MS`, `MT`, `VS`, `ME`, `MI`, `MO`, `MB`, `NA`, `NO`, `NU`, `OG`, `OT`, `OR`, `PD`, `PA`, `PR`, `PV`, `PG`, `PU`, `PE`, `PC`, `PI`, `PT`, `PN`, `PZ`, `PO`, `RG`, `RA`, `RC`, `RE`, `RI`, `RN`, `RM`, `RO`, `SA`, `SS`, `SV`, `SI`, `SR`, `SO`, `TA`, `TE`, `TR`, `TO`, `TP`, `TN`, `TV`, `TS`, `UD`, `VA`, `VE`, `VB`, `VC`, `VR`, `VV`, `VI`, `VT`, `JP-23`, `JP-05`, `JP-02`, `JP-12`, `JP-38`, `JP-18`, `JP-40`, `JP-07`, `JP-21`, `JP-10`, `JP-34`, `JP-01`, `JP-28`, `JP-08`, `JP-17`, `JP-03`, `JP-37`, `JP-46`, `JP-14`, `JP-39`, `JP-43`, `JP-26`, `JP-24`, `JP-04`, `JP-45`, `JP-20`, `JP-42`, `JP-29`, `JP-15`, `JP-44`, `JP-33`, `JP-47`, `JP-27`, `JP-41`, `JP-11`, `JP-25`, `JP-32`, `JP-22`, `JP-09`, `JP-36`, `JP-13`, `JP-31`, `JP-16`, `JP-30`, `JP-06`, `JP-35`, `JP-19`, `JHR`, `KDH`, `KTN`, `KUL`, `LBN`, `MLK`, `NSN`, `PHG`, `PNG`, `PRK`, `PLS`, `PJY`, `SBH`, `SWK`, `SGR`, `TRG`, `AGU`, `BCN`, `BCS`, `CAM`, `CHP`, `CHH`, `CMX`, `COA`, `COL`, `DUR`, `GUA`, `GRO`, `HID`, `JAL`, `MIC`, `MOR`, `MEX`, `NAY`, `NLE`, `OAX`, `PUE`, `QUE`, `ROO`, `SLP`, `SIN`, `SON`, `TAB`, `TAM`, `TLA`, `VER`, `YUC`, `ZAC`, `AUK`, `BOP`, `CAN`, `CIT`, `GIS`, `HKB`, `MWT`, `MBH`, `NSN`, `NTL`, `OTA`, `STL`, `TKI`, `TAS`, `WKO`, `WGN`, `WTC`, `JK`, `BA`, `GB`, `IS`, `KP`, `PB`, `SD`, `AMA`, `ANC`, `APU`, `ARE`, `AYA`, `CAJ`, `CAL`, `CUS`, `HUV`, `HUC`, `ICA`, `JUN`, `LAL`, `LAM`, `LIM`, `LOR`, `MDD`, `MOQ`, `PAS`, `PIU`, `PUN`, `SAM`, `TAC`, `TUM`, `UCA`, `PH-ABR`, `PH-AGN`, `PH-AGS`, `PH-AKL`, `PH-ALB`, `PH-ANT`, `PH-APA`, `PH-AUR`, `PH-BAS`, `PH-BAN`, `PH-BTN`, `PH-BTG`, `PH-BEN`, `PH-BIL`, `PH-BOH`, `PH-BUK`, `PH-BUL`, `PH-CAG`, `PH-CAN`, `PH-CAS`, `PH-CAM`, `PH-CAP`, `PH-CAT`, `PH-CAV`, `PH-CEB`, `PH-NCO`, `PH-DAO`, `PH-DAV`, `PH-DAS`, `PH-EAS`, `PH-GUI`, `PH-IFU`, `PH-ILN`, `PH-ILS`, `PH-ILI`, `PH-ISA`, `PH-KAL`, `PH-LUN`, `PH-LAG`, `PH-LAN`, `PH-LAS`, `PH-LEY`, `PH-MAG`, `PH-MAD`, `PH-MAS`, `PH-00`, `PH-MSC`, `PH-MSR`, `PH-MOU`, `PH-NEC`, `PH-NER`, `PH-NSA`, `PH-NUE`, `PH-NUV`, `PH-MDC`, `PH-MDR`, `PH-PLW`, `PH-PAM`, `PH-PAN`, `PH-QUE`, `PH-QUI`, `PH-RIZ`, `PH-ROM`, `PH-WSA`, `PH-SAR`, `PH-SIG`, `PH-SOR`, `PH-SCO`, `PH-SLE`, `PH-SUK`, `PH-SLU`, `PH-SUN`, `PH-SUR`, `PH-TAR`, `PH-TAW`, `PH-ZMB`, `PH-ZAN`, `PH-ZAS`, `PH-ZSI`, `PT-20`, `PT-01`, `PT-02`, `PT-03`, `PT-04`, `PT-05`, `PT-06`, `PT-07`, `PT-08`, `PT-09`, `PT-10`, `PT-11`, `PT-30`, `PT-12`, `PT-13`, `PT-14`, `PT-15`, `PT-16`, `PT-17`, `PT-18`, `AB`, `AR`, `AG`, `BC`, `BH`, `BN`, `BT`, `BR`, `BV`, `B`, `BZ`, `CL`, `CS`, `CJ`, `CT`, `CV`, `DB`, `DJ`, `GL`, `GR`, `GJ`, `HR`, `HD`, `IL`, `IS`, `IF`, `MM`, `MH`, `MS`, `NT`, `OT`, `PH`, `SJ`, `SM`, `SB`, `SV`, `TR`, `TM`, `TL`, `VL`, `VS`, `VN`, `KR-26`, `KR-43`, `KR-44`, `KR-27`, `KR-30`, `KR-42`, `KR-29`, `KR-47`, `KR-41`, `KR-48`, `KR-28`, `KR-49`, `KR-45`, `KR-46`, `KR-50`, `KR-11`, `KR-31`, `C`, `VI`, `AB`, `A`, `AL`, `O`, `AV`, `BA`, `PM`, `B`, `BU`, `CC`, `CA`, `S`, `CS`, `CE`, `CR`, `CO`, `CU`, `GI`, `GR`, `GU`, `SS`, `H`, `HU`, `J`, `LO`, `GC`, `LE`, `L`, `LU`, `M`, `MA`, `ML`, `MU`, `NA`, `OR`, `P`, `PO`, `SA`, `TF`, `SG`, `SE`, `SO`, `T`, `TE`, `TO`, `V`, `VA`, `BI`, `ZA`, `Z`, `AZ`, `AJ`, `DU`, `FU`, `RK`, `SH`, `UQ`, `BFP`, `ENG`, `NIR`, `SCT`, `WLS`, `AR`, `CA`, `CL`, `CO`, `DU`, `FS`, `FD`, `LA`, `MA`, `MO`, `PA`, `RN`, `RV`, `RO`, `SA`, `SJ`, `SO`, `TA`, `TT`) | No | State code of the customer |
| `city` | string | No | City of the customer |
| `zip` | string | No | Zip code of the customer |
| `phone` | string | No | Phone number of the customer |
| `email` | string | No | Email of the customer |

**`source` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `funnel`, `website`, `invoice`, `calendar`, `text2Pay`, `document_contracts`, `membership`, `mobile_app`, `communities`, `point_of_sale`, `manual`, `form`, `survey`, `payment_link`, `external`) | Yes | Source of order |
| `subType` | string (enum: `one_step_order_form`, `two_step_order_form`, `upsell`, `tap_to_pay`, `card_payment`, `store`, `contact_view`, `email_campaign`, `payments_dashboard`, `shopify`, `subscription_view`, `store_upsell`, `woocommerce`, `service`, `meeting`, `imported_csv`, `qr_code`) | No | Source subtype of order |

**`products` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | id of product |
| `qty` | number | Yes | No of quantities |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | array of object | Yes | Shipping rate data |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Shipping Zone Rates

### POST `/store/shipping-zone/{shippingZoneId}/shipping-rate`

**Create Shipping Rate**

The "Create Shipping Rate" API allows adding a new shipping rate.

**Operation ID:** `create-shipping-rate`

**Tags:** Shipping Zone Rates

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the item that needs to be returned |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping zone |
| `description` | string | No | Delivery description |
| `currency` | string | Yes | The currency of the amount of the rate / handling fee |
| `amount` | number | Yes | The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate). |
| `conditionType` | string (enum: `none`, `price`, `weight`) | Yes | Type of condition to provide the conditional pricing |
| `minCondition` | number | Yes | Minimum condition for applying this price. set 0 or null if there is no minimum |
| `maxCondition` | number | Yes | Maximum condition for applying this price. set 0 or null if there is no maximum |
| `isCarrierRate` | boolean | No | is this a carrier rate |
| `shippingCarrierId` | string | Yes | Shipping carrier id |
| `percentageOfRateFee` | number | No | Percentage of rate fee if it is a carrier rate. |
| `shippingCarrierServices` | array of object | No | An array of items |

**`shippingCarrierServices` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the shipping carrier service |
| `value` | string | Yes | Value of the shipping carrier service |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/store/shipping-zone/{shippingZoneId}/shipping-rate`

**List Shipping Rates**

The "List Shipping Rate" API allows to retrieve a list of shipping rate.

**Operation ID:** `list-shipping-rates`

**Tags:** Shipping Zone Rates

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the item that needs to be returned |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `limit` | query | number | No | The maximum number of items to be included in a single page of results |
| `offset` | query | number | No | The starting index of the page, indicating the position from which the results should be retrieved. |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `data` | array of object | Yes | An array of items |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/store/shipping-zone/{shippingZoneId}/shipping-rate/{shippingRateId}`

**Get Shipping Rate**

The "List Shipping Rate" API allows to retrieve a paginated list of shipping rate.

**Operation ID:** `get-shipping-rates`

**Tags:** Shipping Zone Rates

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the shipping zone |
| `shippingRateId` | path | string | Yes | ID of the shipping rate that needs to be returned |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/store/shipping-zone/{shippingZoneId}/shipping-rate/{shippingRateId}`

**Update Shipping Rate**

The "update Shipping Rate" API allows update a shipping rate to the system. 

**Operation ID:** `update-shipping-rate`

**Tags:** Shipping Zone Rates

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the shipping zone |
| `shippingRateId` | path | string | Yes | ID of the shipping rate that needs to be returned |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | No | Location Id or Agency Id |
| `altType` | string (enum: `location`) | No |  |
| `name` | string | No | Name of the shipping zone |
| `description` | string | No | Delivery description |
| `currency` | string | No | The currency of the amount of the rate / handling fee |
| `amount` | number | No | The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate). |
| `conditionType` | string (enum: `none`, `price`, `weight`) | No | Type of condition to provide the conditional pricing |
| `minCondition` | number | No | Minimum condition for applying this price. set 0 or null if there is no minimum |
| `maxCondition` | number | No | Maximum condition for applying this price. set 0 or null if there is no maximum |
| `isCarrierRate` | boolean | No | is this a carrier rate |
| `shippingCarrierId` | string | No | Shipping carrier id |
| `percentageOfRateFee` | number | No | Percentage of rate fee if it is a carrier rate. |
| `shippingCarrierServices` | array of object | No | An array of items |

**`shippingCarrierServices` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the shipping carrier service |
| `value` | string | Yes | Value of the shipping carrier service |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/store/shipping-zone/{shippingZoneId}/shipping-rate/{shippingRateId}`

**Delete shipping rate**

Delete specific shipping rate with Id :shippingRateId

**Operation ID:** `delete-shipping-rate`

**Tags:** Shipping Zone Rates

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingZoneId` | path | string | Yes | ID of the shipping zone |
| `shippingRateId` | path | string | Yes | ID of the shipping rate that needs to be returned |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Shipping Carrier

### POST `/store/shipping-carrier`

**Create Shipping Carrier**

The "Create Shipping Carrier" API allows adding a new shipping carrier.

**Operation ID:** `create-shipping-carrier`

**Tags:** Shipping Carrier

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping carrier |
| `callbackUrl` | string | Yes | The URL endpoint that GHL needs to retrieve shipping rates. This must be a public URL. |
| `services` | array of object | No | An array of available shipping carrier services |
| `allowsMultipleServiceSelection` | boolean | No | The seller can choose multiple services while creating shipping rates if this is true. |

**`services` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the shipping carrier service |
| `value` | string | Yes | Value of the shipping carrier service |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/store/shipping-carrier`

**List Shipping Carriers**

The "List Shipping Carrier" API allows to retrieve a list of shipping carrier.

**Operation ID:** `list-shipping-carriers`

**Tags:** Shipping Carrier

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | array of object | Yes | An array of items |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/store/shipping-carrier/{shippingCarrierId}`

**Get Shipping Carrier**

The "List Shipping Carrier" API allows to retrieve a paginated list of shipping carrier.

**Operation ID:** `get-shipping-carriers`

**Tags:** Shipping Carrier

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingCarrierId` | path | string | Yes | ID of the shipping carrier that needs to be returned |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/store/shipping-carrier/{shippingCarrierId}`

**Update Shipping Carrier**

The "update Shipping Carrier" API allows update a shipping carrier to the system. 

**Operation ID:** `update-shipping-carrier`

**Tags:** Shipping Carrier

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingCarrierId` | path | string | Yes | ID of the shipping carrier that needs to be returned |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | No | Location Id or Agency Id |
| `altType` | string (enum: `location`) | No |  |
| `name` | string | No | Name of the shipping carrier |
| `callbackUrl` | string | No | The URL endpoint that GHL needs to retrieve shipping rates. This must be a public URL. |
| `services` | array of object | No | An array of available shipping carrier services |
| `allowsMultipleServiceSelection` | boolean | No | The seller can choose multiple services while creating shipping rates if this is true. |

**`services` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the shipping carrier service |
| `value` | string | Yes | Value of the shipping carrier service |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/store/shipping-carrier/{shippingCarrierId}`

**Delete shipping carrier**

Delete specific shipping carrier with Id :shippingCarrierId

**Operation ID:** `delete-shipping-carrier`

**Tags:** Shipping Carrier

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `shippingCarrierId` | path | string | Yes | ID of the shipping carrier that needs to be returned |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Store Setting

### POST `/store/store-setting`

**Create/Update Store Settings**

Create or update store settings by altId and altType.

**Operation ID:** `create-store-setting`

**Tags:** Store Setting

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `shippingOrigin` | object | Yes |  |
| `storeOrderNotification` | object | No |  |
| `storeOrderFulfillmentNotification` | object | No |  |

**`shippingOrigin` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the store / company |
| `country` | number (enum: `['US', 'CA', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']`) | Yes | Country code |
| `state` | string (enum: `AL`, `AK`, `AS`, `AZ`, `AR`, `AA`, `AE`, `AP`, `CA`, `CO`, `CT`, `DE`, `DC`, `FM`, `FL`, `GA`, `GU`, `HI`, `ID`, `IL`, `IN`, `IA`, `KS`, `KY`, `LA`, `ME`, `MH`, `MD`, `MA`, `MI`, `MN`, `MS`, `MO`, `MT`, `NE`, `NV`, `NH`, `NJ`, `NM`, `NY`, `NC`, `ND`, `MP`, `OH`, `OK`, `OR`, `PW`, `PA`, `PR`, `RI`, `SC`, `SD`, `TN`, `TX`, `UT`, `VT`, `VI`, `VA`, `WA`, `WV`, `WI`, `WY`, `AB`, `BC`, `MB`, `NB`, `NL`, `NT`, `NS`, `NU`, `ON`, `PE`, `QC`, `SK`, `YT`, `BA`, `CT`, `CC`, `CH`, `CB`, `CN`, `ER`, `FO`, `JY`, `LP`, `LR`, `MZ`, `MN`, `NQ`, `RN`, `SA`, `SJ`, `SL`, `SC`, `SF`, `SE`, `TF`, `TU`, `ACT`, `NSW`, `NT`, `QLD`, `SA`, `TAS`, `VIC`, `WA`, `AC`, `AL`, `AM`, `AP`, `BA`, `CE`, `DF`, `ES`, `GO`, `MA`, `MG`, `MS`, `MT`, `PA`, `PB`, `PE`, `PI`, `PR`, `RJ`, `RN`, `RO`, `RR`, `RS`, `SC`, `SE`, `SP`, `TO`, `AI`, `AN`, `AP`, `AT`, `BI`, `CO`, `AR`, `LI`, `LL`, `LR`, `MA`, `ML`, `RM`, `TA`, `VS`, `NB`, `AMA`, `ANT`, `ARA`, `ATL`, `BOL`, `BOY`, `CAL`, `CAQ`, `CAS`, `CAU`, `CES`, `CHO`, `CUN`, `COR`, `GUA`, `GUV`, `HUI`, `LAG`, `MAG`, `MET`, `NAR`, `NSA`, `PUT`, `QUI`, `RIS`, `SAP`, `SAN`, `SUC`, `TOL`, `VAC`, `VAU`, `VID`, `CR-A`, `CR-C`, `CR-G`, `CR-H`, `CR-L`, `CR-P`, `CR-SJ`, `GT-16`, `GT-15`, `GT-04`, `GT-20`, `GT-02`, `GT-05`, `GT-01`, `GT-13`, `GT-18`, `GT-21`, `GT-22`, `GT-17`, `GT-09`, `GT-14`, `GT-11`, `GT-03`, `GT-12`, `GT-06`, `GT-07`, `GT-10`, `GT-08`, `GT-19`, `HK`, `KL`, `NT`, `AN`, `AP`, `AR`, `AS`, `BR`, `CH`, `CG`, `DN`, `DD`, `DL`, `GA`, `GJ`, `HR`, `HP`, `JK`, `JH`, `KA`, `KL`, `LA`, `LD`, `MP`, `MH`, `MN`, `ML`, `MZ`, `NL`, `OR`, `PY`, `PB`, `RJ`, `SK`, `TN`, `TS`, `TR`, `UP`, `UK`, `WB`, `CW`, `CN`, `CE`, `CO`, `DL`, `D`, `G`, `KY`, `KE`, `KK`, `LS`, `LM`, `LK`, `LD`, `LH`, `MO`, `MH`, `MN`, `OY`, `RN`, `SO`, `TA`, `WD`, `WH`, `WX`, `WW`, `AG`, `AL`, `AN`, `AO`, `AR`, `AP`, `AT`, `AV`, `BA`, `BT`, `BL`, `BN`, `BG`, `BI`, `BO`, `BZ`, `BS`, `BR`, `CA`, `CL`, `CB`, `CI`, `CE`, `CT`, `CZ`, `CH`, `CO`, `CS`, `CR`, `KR`, `CN`, `EN`, `FM`, `FE`, `FI`, `FG`, `FC`, `FR`, `GE`, `GO`, `GR`, `IM`, `IS`, `AQ`, `SP`, `LT`, `LE`, `LC`, `LI`, `LO`, `LU`, `MC`, `MN`, `MS`, `MT`, `VS`, `ME`, `MI`, `MO`, `MB`, `NA`, `NO`, `NU`, `OG`, `OT`, `OR`, `PD`, `PA`, `PR`, `PV`, `PG`, `PU`, `PE`, `PC`, `PI`, `PT`, `PN`, `PZ`, `PO`, `RG`, `RA`, `RC`, `RE`, `RI`, `RN`, `RM`, `RO`, `SA`, `SS`, `SV`, `SI`, `SR`, `SO`, `TA`, `TE`, `TR`, `TO`, `TP`, `TN`, `TV`, `TS`, `UD`, `VA`, `VE`, `VB`, `VC`, `VR`, `VV`, `VI`, `VT`, `JP-23`, `JP-05`, `JP-02`, `JP-12`, `JP-38`, `JP-18`, `JP-40`, `JP-07`, `JP-21`, `JP-10`, `JP-34`, `JP-01`, `JP-28`, `JP-08`, `JP-17`, `JP-03`, `JP-37`, `JP-46`, `JP-14`, `JP-39`, `JP-43`, `JP-26`, `JP-24`, `JP-04`, `JP-45`, `JP-20`, `JP-42`, `JP-29`, `JP-15`, `JP-44`, `JP-33`, `JP-47`, `JP-27`, `JP-41`, `JP-11`, `JP-25`, `JP-32`, `JP-22`, `JP-09`, `JP-36`, `JP-13`, `JP-31`, `JP-16`, `JP-30`, `JP-06`, `JP-35`, `JP-19`, `JHR`, `KDH`, `KTN`, `KUL`, `LBN`, `MLK`, `NSN`, `PHG`, `PNG`, `PRK`, `PLS`, `PJY`, `SBH`, `SWK`, `SGR`, `TRG`, `AGU`, `BCN`, `BCS`, `CAM`, `CHP`, `CHH`, `CMX`, `COA`, `COL`, `DUR`, `GUA`, `GRO`, `HID`, `JAL`, `MIC`, `MOR`, `MEX`, `NAY`, `NLE`, `OAX`, `PUE`, `QUE`, `ROO`, `SLP`, `SIN`, `SON`, `TAB`, `TAM`, `TLA`, `VER`, `YUC`, `ZAC`, `AUK`, `BOP`, `CAN`, `CIT`, `GIS`, `HKB`, `MWT`, `MBH`, `NSN`, `NTL`, `OTA`, `STL`, `TKI`, `TAS`, `WKO`, `WGN`, `WTC`, `JK`, `BA`, `GB`, `IS`, `KP`, `PB`, `SD`, `AMA`, `ANC`, `APU`, `ARE`, `AYA`, `CAJ`, `CAL`, `CUS`, `HUV`, `HUC`, `ICA`, `JUN`, `LAL`, `LAM`, `LIM`, `LOR`, `MDD`, `MOQ`, `PAS`, `PIU`, `PUN`, `SAM`, `TAC`, `TUM`, `UCA`, `PH-ABR`, `PH-AGN`, `PH-AGS`, `PH-AKL`, `PH-ALB`, `PH-ANT`, `PH-APA`, `PH-AUR`, `PH-BAS`, `PH-BAN`, `PH-BTN`, `PH-BTG`, `PH-BEN`, `PH-BIL`, `PH-BOH`, `PH-BUK`, `PH-BUL`, `PH-CAG`, `PH-CAN`, `PH-CAS`, `PH-CAM`, `PH-CAP`, `PH-CAT`, `PH-CAV`, `PH-CEB`, `PH-NCO`, `PH-DAO`, `PH-DAV`, `PH-DAS`, `PH-EAS`, `PH-GUI`, `PH-IFU`, `PH-ILN`, `PH-ILS`, `PH-ILI`, `PH-ISA`, `PH-KAL`, `PH-LUN`, `PH-LAG`, `PH-LAN`, `PH-LAS`, `PH-LEY`, `PH-MAG`, `PH-MAD`, `PH-MAS`, `PH-00`, `PH-MSC`, `PH-MSR`, `PH-MOU`, `PH-NEC`, `PH-NER`, `PH-NSA`, `PH-NUE`, `PH-NUV`, `PH-MDC`, `PH-MDR`, `PH-PLW`, `PH-PAM`, `PH-PAN`, `PH-QUE`, `PH-QUI`, `PH-RIZ`, `PH-ROM`, `PH-WSA`, `PH-SAR`, `PH-SIG`, `PH-SOR`, `PH-SCO`, `PH-SLE`, `PH-SUK`, `PH-SLU`, `PH-SUN`, `PH-SUR`, `PH-TAR`, `PH-TAW`, `PH-ZMB`, `PH-ZAN`, `PH-ZAS`, `PH-ZSI`, `PT-20`, `PT-01`, `PT-02`, `PT-03`, `PT-04`, `PT-05`, `PT-06`, `PT-07`, `PT-08`, `PT-09`, `PT-10`, `PT-11`, `PT-30`, `PT-12`, `PT-13`, `PT-14`, `PT-15`, `PT-16`, `PT-17`, `PT-18`, `AB`, `AR`, `AG`, `BC`, `BH`, `BN`, `BT`, `BR`, `BV`, `B`, `BZ`, `CL`, `CS`, `CJ`, `CT`, `CV`, `DB`, `DJ`, `GL`, `GR`, `GJ`, `HR`, `HD`, `IL`, `IS`, `IF`, `MM`, `MH`, `MS`, `NT`, `OT`, `PH`, `SJ`, `SM`, `SB`, `SV`, `TR`, `TM`, `TL`, `VL`, `VS`, `VN`, `KR-26`, `KR-43`, `KR-44`, `KR-27`, `KR-30`, `KR-42`, `KR-29`, `KR-47`, `KR-41`, `KR-48`, `KR-28`, `KR-49`, `KR-45`, `KR-46`, `KR-50`, `KR-11`, `KR-31`, `C`, `VI`, `AB`, `A`, `AL`, `O`, `AV`, `BA`, `PM`, `B`, `BU`, `CC`, `CA`, `S`, `CS`, `CE`, `CR`, `CO`, `CU`, `GI`, `GR`, `GU`, `SS`, `H`, `HU`, `J`, `LO`, `GC`, `LE`, `L`, `LU`, `M`, `MA`, `ML`, `MU`, `NA`, `OR`, `P`, `PO`, `SA`, `TF`, `SG`, `SE`, `SO`, `T`, `TE`, `TO`, `V`, `VA`, `BI`, `ZA`, `Z`, `AZ`, `AJ`, `DU`, `FU`, `RK`, `SH`, `UQ`, `BFP`, `ENG`, `NIR`, `SCT`, `WLS`, `AR`, `CA`, `CL`, `CO`, `DU`, `FS`, `FD`, `LA`, `MA`, `MO`, `PA`, `RN`, `RV`, `RO`, `SA`, `SJ`, `SO`, `TA`, `TT`) | No | State code |
| `city` | string | Yes | City name |
| `street1` | string | Yes | Street address line 1 |
| `street2` | string | No | Street address line 2 |
| `zip` | string | Yes | Zip code |
| `phone` | string | No | Business Phone Number |
| `email` | string | No | Email |

**`storeOrderNotification` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Store order notification enabled |
| `subject` | string | Yes | Store order email subject |
| `emailTemplateId` | string | Yes | Email Template Id |
| `defaultEmailTemplateId` | string | Yes | Default Email Template Id |

**`storeOrderFulfillmentNotification` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Store order fulfillment notification enabled |
| `subject` | string | Yes | Store order fulfillment email subject |
| `emailTemplateId` | string | Yes | Email Template Id |
| `defaultEmailTemplateId` | string | Yes | Default Email Template Id |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/store/store-setting`

**Get Store Settings**

Get store settings by altId and altType.

**Operation ID:** `get-store-settings`

**Tags:** Store Setting

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `Authorization` | header | string | Yes | Access Token |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AvailableShippingRate

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the shipping zone |
| `description` | string | No | Delivery description |
| `currency` | string | Yes | The currency of the amount of the rate / handling fee |
| `amount` | number | Yes | The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate). |
| `isCarrierRate` | boolean | No | is this a carrier rate |
| `shippingCarrierId` | string | Yes | Shipping carrier id |
| `percentageOfRateFee` | number | No | Percentage of rate fee if it is a carrier rate. |
| `shippingCarrierServices` | array of object | No | An array of items |
| `_id` | string | Yes | The unique identifier for the product. |
| `shippingZoneId` | string | Yes | The unique identifier for the shipping zone. |

### ContactAddress

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the customer |
| `companyName` | string | No | Name of the Company |
| `addressLine1` | string | No | Address line 1 of the customer |
| `country` | string (enum: `US`, `CA`, `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `KR`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `UA`, `AE`, `GB`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | Yes | Country code of the customer |
| `state` | string (enum: `AL`, `AK`, `AS`, `AZ`, `AR`, `AA`, `AE`, `AP`, `CA`, `CO`, `CT`, `DE`, `DC`, `FM`, `FL`, `GA`, `GU`, `HI`, `ID`, `IL`, `IN`, `IA`, `KS`, `KY`, `LA`, `ME`, `MH`, `MD`, `MA`, `MI`, `MN`, `MS`, `MO`, `MT`, `NE`, `NV`, `NH`, `NJ`, `NM`, `NY`, `NC`, `ND`, `MP`, `OH`, `OK`, `OR`, `PW`, `PA`, `PR`, `RI`, `SC`, `SD`, `TN`, `TX`, `UT`, `VT`, `VI`, `VA`, `WA`, `WV`, `WI`, `WY`, `AB`, `BC`, `MB`, `NB`, `NL`, `NT`, `NS`, `NU`, `ON`, `PE`, `QC`, `SK`, `YT`, `BA`, `CT`, `CC`, `CH`, `CB`, `CN`, `ER`, `FO`, `JY`, `LP`, `LR`, `MZ`, `MN`, `NQ`, `RN`, `SA`, `SJ`, `SL`, `SC`, `SF`, `SE`, `TF`, `TU`, `ACT`, `NSW`, `NT`, `QLD`, `SA`, `TAS`, `VIC`, `WA`, `AC`, `AL`, `AM`, `AP`, `BA`, `CE`, `DF`, `ES`, `GO`, `MA`, `MG`, `MS`, `MT`, `PA`, `PB`, `PE`, `PI`, `PR`, `RJ`, `RN`, `RO`, `RR`, `RS`, `SC`, `SE`, `SP`, `TO`, `AI`, `AN`, `AP`, `AT`, `BI`, `CO`, `AR`, `LI`, `LL`, `LR`, `MA`, `ML`, `RM`, `TA`, `VS`, `NB`, `AMA`, `ANT`, `ARA`, `ATL`, `BOL`, `BOY`, `CAL`, `CAQ`, `CAS`, `CAU`, `CES`, `CHO`, `CUN`, `COR`, `GUA`, `GUV`, `HUI`, `LAG`, `MAG`, `MET`, `NAR`, `NSA`, `PUT`, `QUI`, `RIS`, `SAP`, `SAN`, `SUC`, `TOL`, `VAC`, `VAU`, `VID`, `CR-A`, `CR-C`, `CR-G`, `CR-H`, `CR-L`, `CR-P`, `CR-SJ`, `GT-16`, `GT-15`, `GT-04`, `GT-20`, `GT-02`, `GT-05`, `GT-01`, `GT-13`, `GT-18`, `GT-21`, `GT-22`, `GT-17`, `GT-09`, `GT-14`, `GT-11`, `GT-03`, `GT-12`, `GT-06`, `GT-07`, `GT-10`, `GT-08`, `GT-19`, `HK`, `KL`, `NT`, `AN`, `AP`, `AR`, `AS`, `BR`, `CH`, `CG`, `DN`, `DD`, `DL`, `GA`, `GJ`, `HR`, `HP`, `JK`, `JH`, `KA`, `KL`, `LA`, `LD`, `MP`, `MH`, `MN`, `ML`, `MZ`, `NL`, `OR`, `PY`, `PB`, `RJ`, `SK`, `TN`, `TS`, `TR`, `UP`, `UK`, `WB`, `CW`, `CN`, `CE`, `CO`, `DL`, `D`, `G`, `KY`, `KE`, `KK`, `LS`, `LM`, `LK`, `LD`, `LH`, `MO`, `MH`, `MN`, `OY`, `RN`, `SO`, `TA`, `WD`, `WH`, `WX`, `WW`, `AG`, `AL`, `AN`, `AO`, `AR`, `AP`, `AT`, `AV`, `BA`, `BT`, `BL`, `BN`, `BG`, `BI`, `BO`, `BZ`, `BS`, `BR`, `CA`, `CL`, `CB`, `CI`, `CE`, `CT`, `CZ`, `CH`, `CO`, `CS`, `CR`, `KR`, `CN`, `EN`, `FM`, `FE`, `FI`, `FG`, `FC`, `FR`, `GE`, `GO`, `GR`, `IM`, `IS`, `AQ`, `SP`, `LT`, `LE`, `LC`, `LI`, `LO`, `LU`, `MC`, `MN`, `MS`, `MT`, `VS`, `ME`, `MI`, `MO`, `MB`, `NA`, `NO`, `NU`, `OG`, `OT`, `OR`, `PD`, `PA`, `PR`, `PV`, `PG`, `PU`, `PE`, `PC`, `PI`, `PT`, `PN`, `PZ`, `PO`, `RG`, `RA`, `RC`, `RE`, `RI`, `RN`, `RM`, `RO`, `SA`, `SS`, `SV`, `SI`, `SR`, `SO`, `TA`, `TE`, `TR`, `TO`, `TP`, `TN`, `TV`, `TS`, `UD`, `VA`, `VE`, `VB`, `VC`, `VR`, `VV`, `VI`, `VT`, `JP-23`, `JP-05`, `JP-02`, `JP-12`, `JP-38`, `JP-18`, `JP-40`, `JP-07`, `JP-21`, `JP-10`, `JP-34`, `JP-01`, `JP-28`, `JP-08`, `JP-17`, `JP-03`, `JP-37`, `JP-46`, `JP-14`, `JP-39`, `JP-43`, `JP-26`, `JP-24`, `JP-04`, `JP-45`, `JP-20`, `JP-42`, `JP-29`, `JP-15`, `JP-44`, `JP-33`, `JP-47`, `JP-27`, `JP-41`, `JP-11`, `JP-25`, `JP-32`, `JP-22`, `JP-09`, `JP-36`, `JP-13`, `JP-31`, `JP-16`, `JP-30`, `JP-06`, `JP-35`, `JP-19`, `JHR`, `KDH`, `KTN`, `KUL`, `LBN`, `MLK`, `NSN`, `PHG`, `PNG`, `PRK`, `PLS`, `PJY`, `SBH`, `SWK`, `SGR`, `TRG`, `AGU`, `BCN`, `BCS`, `CAM`, `CHP`, `CHH`, `CMX`, `COA`, `COL`, `DUR`, `GUA`, `GRO`, `HID`, `JAL`, `MIC`, `MOR`, `MEX`, `NAY`, `NLE`, `OAX`, `PUE`, `QUE`, `ROO`, `SLP`, `SIN`, `SON`, `TAB`, `TAM`, `TLA`, `VER`, `YUC`, `ZAC`, `AUK`, `BOP`, `CAN`, `CIT`, `GIS`, `HKB`, `MWT`, `MBH`, `NSN`, `NTL`, `OTA`, `STL`, `TKI`, `TAS`, `WKO`, `WGN`, `WTC`, `JK`, `BA`, `GB`, `IS`, `KP`, `PB`, `SD`, `AMA`, `ANC`, `APU`, `ARE`, `AYA`, `CAJ`, `CAL`, `CUS`, `HUV`, `HUC`, `ICA`, `JUN`, `LAL`, `LAM`, `LIM`, `LOR`, `MDD`, `MOQ`, `PAS`, `PIU`, `PUN`, `SAM`, `TAC`, `TUM`, `UCA`, `PH-ABR`, `PH-AGN`, `PH-AGS`, `PH-AKL`, `PH-ALB`, `PH-ANT`, `PH-APA`, `PH-AUR`, `PH-BAS`, `PH-BAN`, `PH-BTN`, `PH-BTG`, `PH-BEN`, `PH-BIL`, `PH-BOH`, `PH-BUK`, `PH-BUL`, `PH-CAG`, `PH-CAN`, `PH-CAS`, `PH-CAM`, `PH-CAP`, `PH-CAT`, `PH-CAV`, `PH-CEB`, `PH-NCO`, `PH-DAO`, `PH-DAV`, `PH-DAS`, `PH-EAS`, `PH-GUI`, `PH-IFU`, `PH-ILN`, `PH-ILS`, `PH-ILI`, `PH-ISA`, `PH-KAL`, `PH-LUN`, `PH-LAG`, `PH-LAN`, `PH-LAS`, `PH-LEY`, `PH-MAG`, `PH-MAD`, `PH-MAS`, `PH-00`, `PH-MSC`, `PH-MSR`, `PH-MOU`, `PH-NEC`, `PH-NER`, `PH-NSA`, `PH-NUE`, `PH-NUV`, `PH-MDC`, `PH-MDR`, `PH-PLW`, `PH-PAM`, `PH-PAN`, `PH-QUE`, `PH-QUI`, `PH-RIZ`, `PH-ROM`, `PH-WSA`, `PH-SAR`, `PH-SIG`, `PH-SOR`, `PH-SCO`, `PH-SLE`, `PH-SUK`, `PH-SLU`, `PH-SUN`, `PH-SUR`, `PH-TAR`, `PH-TAW`, `PH-ZMB`, `PH-ZAN`, `PH-ZAS`, `PH-ZSI`, `PT-20`, `PT-01`, `PT-02`, `PT-03`, `PT-04`, `PT-05`, `PT-06`, `PT-07`, `PT-08`, `PT-09`, `PT-10`, `PT-11`, `PT-30`, `PT-12`, `PT-13`, `PT-14`, `PT-15`, `PT-16`, `PT-17`, `PT-18`, `AB`, `AR`, `AG`, `BC`, `BH`, `BN`, `BT`, `BR`, `BV`, `B`, `BZ`, `CL`, `CS`, `CJ`, `CT`, `CV`, `DB`, `DJ`, `GL`, `GR`, `GJ`, `HR`, `HD`, `IL`, `IS`, `IF`, `MM`, `MH`, `MS`, `NT`, `OT`, `PH`, `SJ`, `SM`, `SB`, `SV`, `TR`, `TM`, `TL`, `VL`, `VS`, `VN`, `KR-26`, `KR-43`, `KR-44`, `KR-27`, `KR-30`, `KR-42`, `KR-29`, `KR-47`, `KR-41`, `KR-48`, `KR-28`, `KR-49`, `KR-45`, `KR-46`, `KR-50`, `KR-11`, `KR-31`, `C`, `VI`, `AB`, `A`, `AL`, `O`, `AV`, `BA`, `PM`, `B`, `BU`, `CC`, `CA`, `S`, `CS`, `CE`, `CR`, `CO`, `CU`, `GI`, `GR`, `GU`, `SS`, `H`, `HU`, `J`, `LO`, `GC`, `LE`, `L`, `LU`, `M`, `MA`, `ML`, `MU`, `NA`, `OR`, `P`, `PO`, `SA`, `TF`, `SG`, `SE`, `SO`, `T`, `TE`, `TO`, `V`, `VA`, `BI`, `ZA`, `Z`, `AZ`, `AJ`, `DU`, `FU`, `RK`, `SH`, `UQ`, `BFP`, `ENG`, `NIR`, `SCT`, `WLS`, `AR`, `CA`, `CL`, `CO`, `DU`, `FS`, `FD`, `LA`, `MA`, `MO`, `PA`, `RN`, `RV`, `RO`, `SA`, `SJ`, `SO`, `TA`, `TT`) | No | State code of the customer |
| `city` | string | No | City of the customer |
| `zip` | string | No | Zip code of the customer |
| `phone` | string | No | Phone number of the customer |
| `email` | string | No | Email of the customer |

### CreateShippingCarrierDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping carrier |
| `callbackUrl` | string | Yes | The URL endpoint that GHL needs to retrieve shipping rates. This must be a public URL. |
| `services` | array of object | No | An array of available shipping carrier services |
| `allowsMultipleServiceSelection` | boolean | No | The seller can choose multiple services while creating shipping rates if this is true. |

### CreateShippingCarrierResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### CreateShippingRateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping zone |
| `description` | string | No | Delivery description |
| `currency` | string | Yes | The currency of the amount of the rate / handling fee |
| `amount` | number | Yes | The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate). |
| `conditionType` | string (enum: `none`, `price`, `weight`) | Yes | Type of condition to provide the conditional pricing |
| `minCondition` | number | Yes | Minimum condition for applying this price. set 0 or null if there is no minimum |
| `maxCondition` | number | Yes | Maximum condition for applying this price. set 0 or null if there is no maximum |
| `isCarrierRate` | boolean | No | is this a carrier rate |
| `shippingCarrierId` | string | Yes | Shipping carrier id |
| `percentageOfRateFee` | number | No | Percentage of rate fee if it is a carrier rate. |
| `shippingCarrierServices` | array of object | No | An array of items |

### CreateShippingRateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### CreateShippingZoneDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping zone |
| `countries` | array of object | Yes | List of countries that are available |

### CreateShippingZoneResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### CreateStoreSettingDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `shippingOrigin` | object | Yes |  |
| `storeOrderNotification` | object | No |  |
| `storeOrderFulfillmentNotification` | object | No |  |

### CreateStoreSettingResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### DeleteShippingCarrierResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### DeleteShippingRateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### DeleteShippingZoneResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### GetAvailableShippingRates

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `country` | string (enum: `US`, `CA`, `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `KR`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `UA`, `AE`, `GB`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | Yes | Country code of the customer |
| `address` | object | No |  |
| `amountAvailable` | string (enum: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `VA`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `KP`, `KR`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MK`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `AN`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `ES`, `LK`, `SD`, `SR`, `SJ`, `SZ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UG`, `GB`, `UA`, `AE`, `US`, `UM`, `UY`, `UZ`, `VU`, `VE`, `VN`, `VG`, `VI`, `WF`, `EH`, `YE`, `ZM`, `ZW`) | No | it will not calculate the order amount form backend if it is true |
| `totalOrderAmount` | number | Yes | The amount of the price. ( min: 0.01 ) |
| `weightAvailable` | boolean | No | Flag to pass when the weight is already calculated and should not calculate again |
| `totalOrderWeight` | number | Yes | Estimated weight of the order calculated from the order creation side in kg(s) |
| `source` | object | Yes |  |
| `products` | array of object | Yes | An array of price IDs and quantity |
| `couponCode` | string | No | Coupon code |

### GetAvailableShippingRatesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | array of object | Yes | Shipping rate data |

### GetShippingCarrierResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### GetShippingRateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### GetShippingZoneResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### GetStoreSettingResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### ListShippingCarrierResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | array of object | Yes | An array of items |

### ListShippingRateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `data` | array of object | Yes | An array of items |

### ListShippingZoneResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `data` | array of object | Yes | An array of items |

### OrderSource

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `funnel`, `website`, `invoice`, `calendar`, `text2Pay`, `document_contracts`, `membership`, `mobile_app`, `communities`, `point_of_sale`, `manual`, `form`, `survey`, `payment_link`, `external`) | Yes | Source of order |
| `subType` | string (enum: `one_step_order_form`, `two_step_order_form`, `upsell`, `tap_to_pay`, `card_payment`, `store`, `contact_view`, `email_campaign`, `payments_dashboard`, `shopify`, `subscription_view`, `store_upsell`, `woocommerce`, `service`, `meeting`, `imported_csv`, `qr_code`) | No | Source subtype of order |

### ProductItem

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | id of product |
| `qty` | number | Yes | No of quantities |

### ShippingCarrierSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping carrier |
| `callbackUrl` | string | Yes | The URL endpoint that GHL needs to retrieve shipping rates. This must be a public URL. |
| `services` | array of object | No | An array of available shipping carrier services |
| `allowsMultipleServiceSelection` | boolean | No | The seller can choose multiple services while creating shipping rates if this is true. |
| `_id` | string | Yes | The unique identifier for the product. |
| `marketplaceAppId` | string | Yes | The unique identifier for the marketplace app. |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### ShippingCarrierServiceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the shipping carrier service |
| `value` | string | Yes | Value of the shipping carrier service |

### ShippingRateSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping zone |
| `description` | string | No | Delivery description |
| `currency` | string | Yes | The currency of the amount of the rate / handling fee |
| `amount` | number | Yes | The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate). |
| `conditionType` | string (enum: `none`, `price`, `weight`) | Yes | Type of condition to provide the conditional pricing |
| `minCondition` | number | Yes | Minimum condition for applying this price. set 0 or null if there is no minimum |
| `maxCondition` | number | Yes | Maximum condition for applying this price. set 0 or null if there is no maximum |
| `isCarrierRate` | boolean | No | is this a carrier rate |
| `shippingCarrierId` | string | Yes | Shipping carrier id |
| `percentageOfRateFee` | number | No | Percentage of rate fee if it is a carrier rate. |
| `shippingCarrierServices` | array of object | No | An array of items |
| `_id` | string | Yes | The unique identifier for the product. |
| `shippingZoneId` | string | Yes | The unique identifier for the shipping zone. |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### ShippingZoneCountryDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | number (enum: `['US', 'CA', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']`) | Yes | Country code |
| `states` | array of object | No | List of states that are available. If states is empty, then all states are available |

### ShippingZoneCountryStateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | string (enum: `AL`, `AK`, `AS`, `AZ`, `AR`, `AA`, `AE`, `AP`, `CA`, `CO`, `CT`, `DE`, `DC`, `FM`, `FL`, `GA`, `GU`, `HI`, `ID`, `IL`, `IN`, `IA`, `KS`, `KY`, `LA`, `ME`, `MH`, `MD`, `MA`, `MI`, `MN`, `MS`, `MO`, `MT`, `NE`, `NV`, `NH`, `NJ`, `NM`, `NY`, `NC`, `ND`, `MP`, `OH`, `OK`, `OR`, `PW`, `PA`, `PR`, `RI`, `SC`, `SD`, `TN`, `TX`, `UT`, `VT`, `VI`, `VA`, `WA`, `WV`, `WI`, `WY`, `AB`, `BC`, `MB`, `NB`, `NL`, `NT`, `NS`, `NU`, `ON`, `PE`, `QC`, `SK`, `YT`, `BA`, `CT`, `CC`, `CH`, `CB`, `CN`, `ER`, `FO`, `JY`, `LP`, `LR`, `MZ`, `MN`, `NQ`, `RN`, `SA`, `SJ`, `SL`, `SC`, `SF`, `SE`, `TF`, `TU`, `ACT`, `NSW`, `NT`, `QLD`, `SA`, `TAS`, `VIC`, `WA`, `AC`, `AL`, `AM`, `AP`, `BA`, `CE`, `DF`, `ES`, `GO`, `MA`, `MG`, `MS`, `MT`, `PA`, `PB`, `PE`, `PI`, `PR`, `RJ`, `RN`, `RO`, `RR`, `RS`, `SC`, `SE`, `SP`, `TO`, `AI`, `AN`, `AP`, `AT`, `BI`, `CO`, `AR`, `LI`, `LL`, `LR`, `MA`, `ML`, `RM`, `TA`, `VS`, `NB`, `AMA`, `ANT`, `ARA`, `ATL`, `BOL`, `BOY`, `CAL`, `CAQ`, `CAS`, `CAU`, `CES`, `CHO`, `CUN`, `COR`, `GUA`, `GUV`, `HUI`, `LAG`, `MAG`, `MET`, `NAR`, `NSA`, `PUT`, `QUI`, `RIS`, `SAP`, `SAN`, `SUC`, `TOL`, `VAC`, `VAU`, `VID`, `CR-A`, `CR-C`, `CR-G`, `CR-H`, `CR-L`, `CR-P`, `CR-SJ`, `GT-16`, `GT-15`, `GT-04`, `GT-20`, `GT-02`, `GT-05`, `GT-01`, `GT-13`, `GT-18`, `GT-21`, `GT-22`, `GT-17`, `GT-09`, `GT-14`, `GT-11`, `GT-03`, `GT-12`, `GT-06`, `GT-07`, `GT-10`, `GT-08`, `GT-19`, `HK`, `KL`, `NT`, `AN`, `AP`, `AR`, `AS`, `BR`, `CH`, `CG`, `DN`, `DD`, `DL`, `GA`, `GJ`, `HR`, `HP`, `JK`, `JH`, `KA`, `KL`, `LA`, `LD`, `MP`, `MH`, `MN`, `ML`, `MZ`, `NL`, `OR`, `PY`, `PB`, `RJ`, `SK`, `TN`, `TS`, `TR`, `UP`, `UK`, `WB`, `CW`, `CN`, `CE`, `CO`, `DL`, `D`, `G`, `KY`, `KE`, `KK`, `LS`, `LM`, `LK`, `LD`, `LH`, `MO`, `MH`, `MN`, `OY`, `RN`, `SO`, `TA`, `WD`, `WH`, `WX`, `WW`, `AG`, `AL`, `AN`, `AO`, `AR`, `AP`, `AT`, `AV`, `BA`, `BT`, `BL`, `BN`, `BG`, `BI`, `BO`, `BZ`, `BS`, `BR`, `CA`, `CL`, `CB`, `CI`, `CE`, `CT`, `CZ`, `CH`, `CO`, `CS`, `CR`, `KR`, `CN`, `EN`, `FM`, `FE`, `FI`, `FG`, `FC`, `FR`, `GE`, `GO`, `GR`, `IM`, `IS`, `AQ`, `SP`, `LT`, `LE`, `LC`, `LI`, `LO`, `LU`, `MC`, `MN`, `MS`, `MT`, `VS`, `ME`, `MI`, `MO`, `MB`, `NA`, `NO`, `NU`, `OG`, `OT`, `OR`, `PD`, `PA`, `PR`, `PV`, `PG`, `PU`, `PE`, `PC`, `PI`, `PT`, `PN`, `PZ`, `PO`, `RG`, `RA`, `RC`, `RE`, `RI`, `RN`, `RM`, `RO`, `SA`, `SS`, `SV`, `SI`, `SR`, `SO`, `TA`, `TE`, `TR`, `TO`, `TP`, `TN`, `TV`, `TS`, `UD`, `VA`, `VE`, `VB`, `VC`, `VR`, `VV`, `VI`, `VT`, `JP-23`, `JP-05`, `JP-02`, `JP-12`, `JP-38`, `JP-18`, `JP-40`, `JP-07`, `JP-21`, `JP-10`, `JP-34`, `JP-01`, `JP-28`, `JP-08`, `JP-17`, `JP-03`, `JP-37`, `JP-46`, `JP-14`, `JP-39`, `JP-43`, `JP-26`, `JP-24`, `JP-04`, `JP-45`, `JP-20`, `JP-42`, `JP-29`, `JP-15`, `JP-44`, `JP-33`, `JP-47`, `JP-27`, `JP-41`, `JP-11`, `JP-25`, `JP-32`, `JP-22`, `JP-09`, `JP-36`, `JP-13`, `JP-31`, `JP-16`, `JP-30`, `JP-06`, `JP-35`, `JP-19`, `JHR`, `KDH`, `KTN`, `KUL`, `LBN`, `MLK`, `NSN`, `PHG`, `PNG`, `PRK`, `PLS`, `PJY`, `SBH`, `SWK`, `SGR`, `TRG`, `AGU`, `BCN`, `BCS`, `CAM`, `CHP`, `CHH`, `CMX`, `COA`, `COL`, `DUR`, `GUA`, `GRO`, `HID`, `JAL`, `MIC`, `MOR`, `MEX`, `NAY`, `NLE`, `OAX`, `PUE`, `QUE`, `ROO`, `SLP`, `SIN`, `SON`, `TAB`, `TAM`, `TLA`, `VER`, `YUC`, `ZAC`, `AUK`, `BOP`, `CAN`, `CIT`, `GIS`, `HKB`, `MWT`, `MBH`, `NSN`, `NTL`, `OTA`, `STL`, `TKI`, `TAS`, `WKO`, `WGN`, `WTC`, `JK`, `BA`, `GB`, `IS`, `KP`, `PB`, `SD`, `AMA`, `ANC`, `APU`, `ARE`, `AYA`, `CAJ`, `CAL`, `CUS`, `HUV`, `HUC`, `ICA`, `JUN`, `LAL`, `LAM`, `LIM`, `LOR`, `MDD`, `MOQ`, `PAS`, `PIU`, `PUN`, `SAM`, `TAC`, `TUM`, `UCA`, `PH-ABR`, `PH-AGN`, `PH-AGS`, `PH-AKL`, `PH-ALB`, `PH-ANT`, `PH-APA`, `PH-AUR`, `PH-BAS`, `PH-BAN`, `PH-BTN`, `PH-BTG`, `PH-BEN`, `PH-BIL`, `PH-BOH`, `PH-BUK`, `PH-BUL`, `PH-CAG`, `PH-CAN`, `PH-CAS`, `PH-CAM`, `PH-CAP`, `PH-CAT`, `PH-CAV`, `PH-CEB`, `PH-NCO`, `PH-DAO`, `PH-DAV`, `PH-DAS`, `PH-EAS`, `PH-GUI`, `PH-IFU`, `PH-ILN`, `PH-ILS`, `PH-ILI`, `PH-ISA`, `PH-KAL`, `PH-LUN`, `PH-LAG`, `PH-LAN`, `PH-LAS`, `PH-LEY`, `PH-MAG`, `PH-MAD`, `PH-MAS`, `PH-00`, `PH-MSC`, `PH-MSR`, `PH-MOU`, `PH-NEC`, `PH-NER`, `PH-NSA`, `PH-NUE`, `PH-NUV`, `PH-MDC`, `PH-MDR`, `PH-PLW`, `PH-PAM`, `PH-PAN`, `PH-QUE`, `PH-QUI`, `PH-RIZ`, `PH-ROM`, `PH-WSA`, `PH-SAR`, `PH-SIG`, `PH-SOR`, `PH-SCO`, `PH-SLE`, `PH-SUK`, `PH-SLU`, `PH-SUN`, `PH-SUR`, `PH-TAR`, `PH-TAW`, `PH-ZMB`, `PH-ZAN`, `PH-ZAS`, `PH-ZSI`, `PT-20`, `PT-01`, `PT-02`, `PT-03`, `PT-04`, `PT-05`, `PT-06`, `PT-07`, `PT-08`, `PT-09`, `PT-10`, `PT-11`, `PT-30`, `PT-12`, `PT-13`, `PT-14`, `PT-15`, `PT-16`, `PT-17`, `PT-18`, `AB`, `AR`, `AG`, `BC`, `BH`, `BN`, `BT`, `BR`, `BV`, `B`, `BZ`, `CL`, `CS`, `CJ`, `CT`, `CV`, `DB`, `DJ`, `GL`, `GR`, `GJ`, `HR`, `HD`, `IL`, `IS`, `IF`, `MM`, `MH`, `MS`, `NT`, `OT`, `PH`, `SJ`, `SM`, `SB`, `SV`, `TR`, `TM`, `TL`, `VL`, `VS`, `VN`, `KR-26`, `KR-43`, `KR-44`, `KR-27`, `KR-30`, `KR-42`, `KR-29`, `KR-47`, `KR-41`, `KR-48`, `KR-28`, `KR-49`, `KR-45`, `KR-46`, `KR-50`, `KR-11`, `KR-31`, `C`, `VI`, `AB`, `A`, `AL`, `O`, `AV`, `BA`, `PM`, `B`, `BU`, `CC`, `CA`, `S`, `CS`, `CE`, `CR`, `CO`, `CU`, `GI`, `GR`, `GU`, `SS`, `H`, `HU`, `J`, `LO`, `GC`, `LE`, `L`, `LU`, `M`, `MA`, `ML`, `MU`, `NA`, `OR`, `P`, `PO`, `SA`, `TF`, `SG`, `SE`, `SO`, `T`, `TE`, `TO`, `V`, `VA`, `BI`, `ZA`, `Z`, `AZ`, `AJ`, `DU`, `FU`, `RK`, `SH`, `UQ`, `BFP`, `ENG`, `NIR`, `SCT`, `WLS`, `AR`, `CA`, `CL`, `CO`, `DU`, `FS`, `FD`, `LA`, `MA`, `MO`, `PA`, `RN`, `RV`, `RO`, `SA`, `SJ`, `SO`, `TA`, `TT`) | Yes | State code |

### ShippingZoneSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the shipping zone |
| `countries` | array of object | Yes | List of countries that are available |
| `_id` | string | Yes | The unique identifier for the product. |
| `shippingRates` | array of object | No | Array of shipping rates under this shipping zone |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### StoreOrderFulfillmentNotificationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Store order fulfillment notification enabled |
| `subject` | string | Yes | Store order fulfillment email subject |
| `emailTemplateId` | string | Yes | Email Template Id |
| `defaultEmailTemplateId` | string | Yes | Default Email Template Id |

### StoreOrderNotificationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Store order notification enabled |
| `subject` | string | Yes | Store order email subject |
| `emailTemplateId` | string | Yes | Email Template Id |
| `defaultEmailTemplateId` | string | Yes | Default Email Template Id |

### StoreSettingSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `shippingOrigin` | object | Yes |  |
| `storeOrderNotification` | object | No |  |
| `storeOrderFulfillmentNotification` | object | No |  |
| `_id` | string | Yes | The unique identifier for the settings. |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### StoreShippingOriginDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the store / company |
| `country` | number (enum: `['US', 'CA', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']`) | Yes | Country code |
| `state` | string (enum: `AL`, `AK`, `AS`, `AZ`, `AR`, `AA`, `AE`, `AP`, `CA`, `CO`, `CT`, `DE`, `DC`, `FM`, `FL`, `GA`, `GU`, `HI`, `ID`, `IL`, `IN`, `IA`, `KS`, `KY`, `LA`, `ME`, `MH`, `MD`, `MA`, `MI`, `MN`, `MS`, `MO`, `MT`, `NE`, `NV`, `NH`, `NJ`, `NM`, `NY`, `NC`, `ND`, `MP`, `OH`, `OK`, `OR`, `PW`, `PA`, `PR`, `RI`, `SC`, `SD`, `TN`, `TX`, `UT`, `VT`, `VI`, `VA`, `WA`, `WV`, `WI`, `WY`, `AB`, `BC`, `MB`, `NB`, `NL`, `NT`, `NS`, `NU`, `ON`, `PE`, `QC`, `SK`, `YT`, `BA`, `CT`, `CC`, `CH`, `CB`, `CN`, `ER`, `FO`, `JY`, `LP`, `LR`, `MZ`, `MN`, `NQ`, `RN`, `SA`, `SJ`, `SL`, `SC`, `SF`, `SE`, `TF`, `TU`, `ACT`, `NSW`, `NT`, `QLD`, `SA`, `TAS`, `VIC`, `WA`, `AC`, `AL`, `AM`, `AP`, `BA`, `CE`, `DF`, `ES`, `GO`, `MA`, `MG`, `MS`, `MT`, `PA`, `PB`, `PE`, `PI`, `PR`, `RJ`, `RN`, `RO`, `RR`, `RS`, `SC`, `SE`, `SP`, `TO`, `AI`, `AN`, `AP`, `AT`, `BI`, `CO`, `AR`, `LI`, `LL`, `LR`, `MA`, `ML`, `RM`, `TA`, `VS`, `NB`, `AMA`, `ANT`, `ARA`, `ATL`, `BOL`, `BOY`, `CAL`, `CAQ`, `CAS`, `CAU`, `CES`, `CHO`, `CUN`, `COR`, `GUA`, `GUV`, `HUI`, `LAG`, `MAG`, `MET`, `NAR`, `NSA`, `PUT`, `QUI`, `RIS`, `SAP`, `SAN`, `SUC`, `TOL`, `VAC`, `VAU`, `VID`, `CR-A`, `CR-C`, `CR-G`, `CR-H`, `CR-L`, `CR-P`, `CR-SJ`, `GT-16`, `GT-15`, `GT-04`, `GT-20`, `GT-02`, `GT-05`, `GT-01`, `GT-13`, `GT-18`, `GT-21`, `GT-22`, `GT-17`, `GT-09`, `GT-14`, `GT-11`, `GT-03`, `GT-12`, `GT-06`, `GT-07`, `GT-10`, `GT-08`, `GT-19`, `HK`, `KL`, `NT`, `AN`, `AP`, `AR`, `AS`, `BR`, `CH`, `CG`, `DN`, `DD`, `DL`, `GA`, `GJ`, `HR`, `HP`, `JK`, `JH`, `KA`, `KL`, `LA`, `LD`, `MP`, `MH`, `MN`, `ML`, `MZ`, `NL`, `OR`, `PY`, `PB`, `RJ`, `SK`, `TN`, `TS`, `TR`, `UP`, `UK`, `WB`, `CW`, `CN`, `CE`, `CO`, `DL`, `D`, `G`, `KY`, `KE`, `KK`, `LS`, `LM`, `LK`, `LD`, `LH`, `MO`, `MH`, `MN`, `OY`, `RN`, `SO`, `TA`, `WD`, `WH`, `WX`, `WW`, `AG`, `AL`, `AN`, `AO`, `AR`, `AP`, `AT`, `AV`, `BA`, `BT`, `BL`, `BN`, `BG`, `BI`, `BO`, `BZ`, `BS`, `BR`, `CA`, `CL`, `CB`, `CI`, `CE`, `CT`, `CZ`, `CH`, `CO`, `CS`, `CR`, `KR`, `CN`, `EN`, `FM`, `FE`, `FI`, `FG`, `FC`, `FR`, `GE`, `GO`, `GR`, `IM`, `IS`, `AQ`, `SP`, `LT`, `LE`, `LC`, `LI`, `LO`, `LU`, `MC`, `MN`, `MS`, `MT`, `VS`, `ME`, `MI`, `MO`, `MB`, `NA`, `NO`, `NU`, `OG`, `OT`, `OR`, `PD`, `PA`, `PR`, `PV`, `PG`, `PU`, `PE`, `PC`, `PI`, `PT`, `PN`, `PZ`, `PO`, `RG`, `RA`, `RC`, `RE`, `RI`, `RN`, `RM`, `RO`, `SA`, `SS`, `SV`, `SI`, `SR`, `SO`, `TA`, `TE`, `TR`, `TO`, `TP`, `TN`, `TV`, `TS`, `UD`, `VA`, `VE`, `VB`, `VC`, `VR`, `VV`, `VI`, `VT`, `JP-23`, `JP-05`, `JP-02`, `JP-12`, `JP-38`, `JP-18`, `JP-40`, `JP-07`, `JP-21`, `JP-10`, `JP-34`, `JP-01`, `JP-28`, `JP-08`, `JP-17`, `JP-03`, `JP-37`, `JP-46`, `JP-14`, `JP-39`, `JP-43`, `JP-26`, `JP-24`, `JP-04`, `JP-45`, `JP-20`, `JP-42`, `JP-29`, `JP-15`, `JP-44`, `JP-33`, `JP-47`, `JP-27`, `JP-41`, `JP-11`, `JP-25`, `JP-32`, `JP-22`, `JP-09`, `JP-36`, `JP-13`, `JP-31`, `JP-16`, `JP-30`, `JP-06`, `JP-35`, `JP-19`, `JHR`, `KDH`, `KTN`, `KUL`, `LBN`, `MLK`, `NSN`, `PHG`, `PNG`, `PRK`, `PLS`, `PJY`, `SBH`, `SWK`, `SGR`, `TRG`, `AGU`, `BCN`, `BCS`, `CAM`, `CHP`, `CHH`, `CMX`, `COA`, `COL`, `DUR`, `GUA`, `GRO`, `HID`, `JAL`, `MIC`, `MOR`, `MEX`, `NAY`, `NLE`, `OAX`, `PUE`, `QUE`, `ROO`, `SLP`, `SIN`, `SON`, `TAB`, `TAM`, `TLA`, `VER`, `YUC`, `ZAC`, `AUK`, `BOP`, `CAN`, `CIT`, `GIS`, `HKB`, `MWT`, `MBH`, `NSN`, `NTL`, `OTA`, `STL`, `TKI`, `TAS`, `WKO`, `WGN`, `WTC`, `JK`, `BA`, `GB`, `IS`, `KP`, `PB`, `SD`, `AMA`, `ANC`, `APU`, `ARE`, `AYA`, `CAJ`, `CAL`, `CUS`, `HUV`, `HUC`, `ICA`, `JUN`, `LAL`, `LAM`, `LIM`, `LOR`, `MDD`, `MOQ`, `PAS`, `PIU`, `PUN`, `SAM`, `TAC`, `TUM`, `UCA`, `PH-ABR`, `PH-AGN`, `PH-AGS`, `PH-AKL`, `PH-ALB`, `PH-ANT`, `PH-APA`, `PH-AUR`, `PH-BAS`, `PH-BAN`, `PH-BTN`, `PH-BTG`, `PH-BEN`, `PH-BIL`, `PH-BOH`, `PH-BUK`, `PH-BUL`, `PH-CAG`, `PH-CAN`, `PH-CAS`, `PH-CAM`, `PH-CAP`, `PH-CAT`, `PH-CAV`, `PH-CEB`, `PH-NCO`, `PH-DAO`, `PH-DAV`, `PH-DAS`, `PH-EAS`, `PH-GUI`, `PH-IFU`, `PH-ILN`, `PH-ILS`, `PH-ILI`, `PH-ISA`, `PH-KAL`, `PH-LUN`, `PH-LAG`, `PH-LAN`, `PH-LAS`, `PH-LEY`, `PH-MAG`, `PH-MAD`, `PH-MAS`, `PH-00`, `PH-MSC`, `PH-MSR`, `PH-MOU`, `PH-NEC`, `PH-NER`, `PH-NSA`, `PH-NUE`, `PH-NUV`, `PH-MDC`, `PH-MDR`, `PH-PLW`, `PH-PAM`, `PH-PAN`, `PH-QUE`, `PH-QUI`, `PH-RIZ`, `PH-ROM`, `PH-WSA`, `PH-SAR`, `PH-SIG`, `PH-SOR`, `PH-SCO`, `PH-SLE`, `PH-SUK`, `PH-SLU`, `PH-SUN`, `PH-SUR`, `PH-TAR`, `PH-TAW`, `PH-ZMB`, `PH-ZAN`, `PH-ZAS`, `PH-ZSI`, `PT-20`, `PT-01`, `PT-02`, `PT-03`, `PT-04`, `PT-05`, `PT-06`, `PT-07`, `PT-08`, `PT-09`, `PT-10`, `PT-11`, `PT-30`, `PT-12`, `PT-13`, `PT-14`, `PT-15`, `PT-16`, `PT-17`, `PT-18`, `AB`, `AR`, `AG`, `BC`, `BH`, `BN`, `BT`, `BR`, `BV`, `B`, `BZ`, `CL`, `CS`, `CJ`, `CT`, `CV`, `DB`, `DJ`, `GL`, `GR`, `GJ`, `HR`, `HD`, `IL`, `IS`, `IF`, `MM`, `MH`, `MS`, `NT`, `OT`, `PH`, `SJ`, `SM`, `SB`, `SV`, `TR`, `TM`, `TL`, `VL`, `VS`, `VN`, `KR-26`, `KR-43`, `KR-44`, `KR-27`, `KR-30`, `KR-42`, `KR-29`, `KR-47`, `KR-41`, `KR-48`, `KR-28`, `KR-49`, `KR-45`, `KR-46`, `KR-50`, `KR-11`, `KR-31`, `C`, `VI`, `AB`, `A`, `AL`, `O`, `AV`, `BA`, `PM`, `B`, `BU`, `CC`, `CA`, `S`, `CS`, `CE`, `CR`, `CO`, `CU`, `GI`, `GR`, `GU`, `SS`, `H`, `HU`, `J`, `LO`, `GC`, `LE`, `L`, `LU`, `M`, `MA`, `ML`, `MU`, `NA`, `OR`, `P`, `PO`, `SA`, `TF`, `SG`, `SE`, `SO`, `T`, `TE`, `TO`, `V`, `VA`, `BI`, `ZA`, `Z`, `AZ`, `AJ`, `DU`, `FU`, `RK`, `SH`, `UQ`, `BFP`, `ENG`, `NIR`, `SCT`, `WLS`, `AR`, `CA`, `CL`, `CO`, `DU`, `FS`, `FD`, `LA`, `MA`, `MO`, `PA`, `RN`, `RV`, `RO`, `SA`, `SJ`, `SO`, `TA`, `TT`) | No | State code |
| `city` | string | Yes | City name |
| `street1` | string | Yes | Street address line 1 |
| `street2` | string | No | Street address line 2 |
| `zip` | string | Yes | Zip code |
| `phone` | string | No | Business Phone Number |
| `email` | string | No | Email |

### UpdateShippingCarrierDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | No | Location Id or Agency Id |
| `altType` | string (enum: `location`) | No |  |
| `name` | string | No | Name of the shipping carrier |
| `callbackUrl` | string | No | The URL endpoint that GHL needs to retrieve shipping rates. This must be a public URL. |
| `services` | array of object | No | An array of available shipping carrier services |
| `allowsMultipleServiceSelection` | boolean | No | The seller can choose multiple services while creating shipping rates if this is true. |

### UpdateShippingCarrierResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### UpdateShippingRateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | No | Location Id or Agency Id |
| `altType` | string (enum: `location`) | No |  |
| `name` | string | No | Name of the shipping zone |
| `description` | string | No | Delivery description |
| `currency` | string | No | The currency of the amount of the rate / handling fee |
| `amount` | number | No | The amount of the shipping rate if it is normal rate (0 means free ). Fixed Handling fee if it is a carrier rate (it will add to the carrier rate). |
| `conditionType` | string (enum: `none`, `price`, `weight`) | No | Type of condition to provide the conditional pricing |
| `minCondition` | number | No | Minimum condition for applying this price. set 0 or null if there is no minimum |
| `maxCondition` | number | No | Maximum condition for applying this price. set 0 or null if there is no maximum |
| `isCarrierRate` | boolean | No | is this a carrier rate |
| `shippingCarrierId` | string | No | Shipping carrier id |
| `percentageOfRateFee` | number | No | Percentage of rate fee if it is a carrier rate. |
| `shippingCarrierServices` | array of object | No | An array of items |

### UpdateShippingRateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |

### UpdateShippingZoneDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | No | Location Id or Agency Id |
| `altType` | string (enum: `location`) | No |  |
| `name` | string | No | Name of the shipping zone |
| `countries` | array of object | No | List of countries that are available |

### UpdateShippingZoneResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |
| `data` | object | Yes |  |
