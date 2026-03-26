# Invoices API

Documentation for invoice API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Template](#template)
- [Schedule](#schedule)
- [Text2Pay](#text2pay)
- [Invoice](#invoice)
- [Estimate](#estimate)

## Template

### POST `/invoices/template`

**Create template**

API to create a template

**Operation ID:** `create-invoice-template`

**Tags:** Template

**Required Scopes:** `invoices/template.write`, `invoices/template.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `internal` | boolean | No |  |
| `name` | string | Yes | Name of the template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `discount` | object | No |  |
| `termsNotes` | string | No |  |
| `title` | string | No | Template title |
| `tipsConfiguration` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of string | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`tipsConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tipsPercentage` | array of string | Yes | Percentage of tips allowed |
| `tipsEnabled` | boolean | Yes | Tips enabled status |

**`lateFeesConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes | Enable late fees |
| `value` | number | Yes | Late Fees Value |
| `type` | string (enum: `fixed`, `percentage`) | Yes | Late Fees Type |
| `frequency` | object | Yes |  |
| `grace` | object | No |  |
| `maxLateFees` | object | No |  |

**`paymentMethods` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripe` | object | Yes |  |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/template`

**List templates**

API to get list of templates

**Operation ID:** `list-invoice-templates`

**Tags:** Template

**Required Scopes:** `invoices/template.readonly`, `invoices/template.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |
| `status` | query | string | No | status to be filtered |
| `startAt` | query | string | No | startAt in YYYY-MM-DD format |
| `endAt` | query | string | No | endAt in YYYY-MM-DD format |
| `search` | query | string | No | To search for an invoice by id / name / email / phoneNo |
| `paymentMode` | query | string (enum: `default`, `live`, `test`) | No | payment mode |
| `limit` | query | string | Yes | Limit the number of items to return |
| `offset` | query | string | Yes | Number of items to skip |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes |  |
| `totalCount` | number | Yes | Total number of Templates |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/template/{templateId}`

**Get an template**

API to get an template by template id

**Operation ID:** `get-invoice-template`

**Tags:** Template

**Required Scopes:** `invoices/template.readonly`, `invoices/template.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `templateId` | path | string | Yes | Template Id |
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/invoices/template/{templateId}`

**Update template**

API to update an template by template id

**Operation ID:** `update-invoice-template`

**Tags:** Template

**Required Scopes:** `invoices/template.write`, `invoices/template.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `templateId` | path | string | Yes | Template Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `internal` | boolean | No |  |
| `name` | string | Yes | Name of the template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `discount` | object | No |  |
| `termsNotes` | string | No |  |
| `title` | string | No | Template title |
| `miscellaneousCharges` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/invoices/template/{templateId}`

**Delete template**

API to update an template by template id

**Operation ID:** `delete-invoice-template`

**Tags:** Template

**Required Scopes:** `invoices/template.write`, `invoices/template.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `templateId` | path | string | Yes | Template Id |
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | success |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/invoices/template/{templateId}/late-fees-configuration`

**Update template late fees configuration**

API to update template late fees configuration by template id

**Operation ID:** `update-invoice-template-late-fees-configuration`

**Tags:** Template

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `templateId` | path | string | Yes | Template Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `lateFeesConfiguration` | object | Yes |  |

**`lateFeesConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes | Enable late fees |
| `value` | number | Yes | Late Fees Value |
| `type` | string (enum: `fixed`, `percentage`) | Yes | Late Fees Type |
| `frequency` | object | Yes |  |
| `grace` | object | No |  |
| `maxLateFees` | object | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/invoices/template/{templateId}/payment-methods-configuration`

**Update template late fees configuration**

API to update template late fees configuration by template id

**Operation ID:** `update-invoice-payment-methods-configuration`

**Tags:** Template

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `templateId` | path | string | Yes | Template Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `paymentMethods` | object | No |  |

**`paymentMethods` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripe` | object | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schedule

### POST `/invoices/schedule`

**Create Invoice Schedule**

API to create an invoice Schedule

**Operation ID:** `create-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.write`, `invoices/schedule.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes |  |
| `contactDetails` | object | Yes |  |
| `schedule` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `discount` | object | Yes |  |
| `termsNotes` | string | No |  |
| `title` | string | No |  |
| `tipsConfiguration` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

**`contactDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

**`schedule` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `executeAt` | string | No |  |
| `rrule` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`tipsConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tipsPercentage` | array of string | Yes | Percentage of tips allowed |
| `tipsEnabled` | boolean | Yes | Tips enabled status |

**`lateFeesConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes | Enable late fees |
| `value` | number | Yes | Late Fees Value |
| `type` | string (enum: `fixed`, `percentage`) | Yes | Late Fees Type |
| `frequency` | object | Yes |  |
| `grace` | object | No |  |
| `maxLateFees` | object | No |  |

**`paymentMethods` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripe` | object | Yes |  |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/schedule`

**List schedules**

API to get list of schedules

**Operation ID:** `list-invoice-schedules`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.readonly`, `invoices/schedule.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |
| `status` | query | string | No | status to be filtered |
| `startAt` | query | string | No | startAt in YYYY-MM-DD format |
| `endAt` | query | string | No | endAt in YYYY-MM-DD format |
| `search` | query | string | No | To search for an invoice by id / name / email / phoneNo |
| `paymentMode` | query | string (enum: `default`, `live`, `test`) | No | payment mode |
| `limit` | query | string | Yes | Limit the number of items to return |
| `offset` | query | string | Yes | Number of items to skip |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedules` | array of object | Yes |  |
| `total` | number | Yes | Total number of Schedules |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/schedule/{scheduleId}`

**Get an schedule**

API to get an schedule by schedule id

**Operation ID:** `get-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.readonly`, `invoices/schedule.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `scheduleId` | path | string | Yes | Schedule Id |
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/invoices/schedule/{scheduleId}`

**Update schedule**

API to update an schedule by schedule id

**Operation ID:** `update-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.write`, `invoices/schedule.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `scheduleId` | path | string | Yes | Schedule Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes |  |
| `contactDetails` | object | Yes |  |
| `schedule` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `discount` | object | Yes |  |
| `termsNotes` | string | No |  |
| `title` | string | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

**`contactDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

**`schedule` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `executeAt` | string | No |  |
| `rrule` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/invoices/schedule/{scheduleId}`

**Delete schedule**

API to delete an schedule by schedule id

**Operation ID:** `delete-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.write`, `invoices/schedule.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `scheduleId` | path | string | Yes | Schedule Id |
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | success |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/schedule/{scheduleId}/updateAndSchedule`

**Update scheduled recurring invoice**

API to update scheduled recurring invoice

**Operation ID:** `update-and-schedule-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.write`, `invoices/schedule.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `scheduleId` | path | string | Yes | Schedule Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/schedule/{scheduleId}/schedule`

**Schedule an schedule invoice**

API to schedule an schedule invoice to start sending to the customer

**Operation ID:** `schedule-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.write`, `invoices/schedule.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `scheduleId` | path | string | Yes | Schedule Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `liveMode` | boolean | Yes |  |
| `autoPayment` | object | No |  |

**`autoPayment` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes |  |
| `type` | string | No |  |
| `paymentMethodId` | string | No |  |
| `customerId` | string | No |  |
| `card` | object | No |  |
| `usBankAccount` | object | No |  |
| `sepaDirectDebit` | object | No |  |
| `bacsDirectDebit` | object | No |  |
| `becsDirectDebit` | object | No |  |
| `cardId` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/schedule/{scheduleId}/auto-payment`

**Manage Auto payment for an schedule invoice**

API to manage auto payment for a schedule

**Operation ID:** `auto-payment-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.write`, `invoices/schedule.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `scheduleId` | path | string | Yes | Schedule Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `id` | string | Yes |  |
| `autoPayment` | object | Yes |  |

**`autoPayment` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes |  |
| `type` | string | No |  |
| `paymentMethodId` | string | No |  |
| `customerId` | string | No |  |
| `card` | object | No |  |
| `usBankAccount` | object | No |  |
| `sepaDirectDebit` | object | No |  |
| `bacsDirectDebit` | object | No |  |
| `becsDirectDebit` | object | No |  |
| `cardId` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/schedule/{scheduleId}/cancel`

**Cancel an scheduled invoice**

API to cancel a scheduled invoice by schedule id

**Operation ID:** `cancel-invoice-schedule`

**Tags:** Schedule

**Required Scopes:** `invoices/schedule.write`, `invoices/schedule.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `scheduleId` | path | string | Yes | Schedule Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Text2Pay

### POST `/invoices/text2pay`

**Create & Send**

API to create or update a text2pay invoice

**Operation ID:** `text2pay-invoice`

**Tags:** Text2Pay

**Required Scopes:** `invoices.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes | Invoice Name |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the invoice. |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the invoice |
| `contactDetails` | object | Yes |  |
| `invoiceNumber` | string | No | Invoice Number |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | No | Due date in YYYY-MM-DD format |
| `sentTo` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `paymentSchedule` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `tipsConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |
| `id` | string | No | id of invoice to update. If skipped, a new invoice will be created |
| `includeTermsNote` | boolean | No | include terms & notes with receipts |
| `action` | string (enum: `draft`, `send`) | Yes | create invoice in draft mode or send mode |
| `userId` | string | Yes | id of user generating invoice |
| `discount` | object | No |  |
| `businessDetails` | object | No |  |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`contactDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

**`sentTo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | array of string | Yes | Email Address |
| `emailCc` | array of string | No | cc to be kept in any sent out emails |
| `emailBcc` | array of string | No | bcc to be kept in any sent out emails |
| `phoneNo` | array of string | No | Contact Phone Number |

**`paymentSchedule` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`, `percentage`) | Yes | Payment schedule type |
| `schedules` | array of string | Yes | payment schedule item |

**`lateFeesConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes | Enable late fees |
| `value` | number | Yes | Late Fees Value |
| `type` | string (enum: `fixed`, `percentage`) | Yes | Late Fees Type |
| `frequency` | object | Yes |  |
| `grace` | object | No |  |
| `maxLateFees` | object | No |  |

**`tipsConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tipsPercentage` | array of string | Yes | Percentage of tips allowed |
| `tipsEnabled` | boolean | Yes | Tips enabled status |

**`paymentMethods` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripe` | object | Yes |  |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoice` | object | Yes |  |
| `invoiceUrl` | string | Yes | preview url of generated invoice |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Invoice

### GET `/invoices/generate-invoice-number`

**Generate Invoice Number**

Get the next invoice number for the given location

**Operation ID:** `generate-invoice-number`

**Tags:** Invoice

**Required Scopes:** `invoices.readonly`, `invoices.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | Location Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoiceNumber` | number | No | Invoice Number |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/{invoiceId}`

**Get invoice**

API to get invoice by invoice id

**Operation ID:** `get-invoice`

**Tags:** Invoice

**Required Scopes:** `invoices.readonly`, `invoices.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `invoiceId` | path | string | Yes | Invoice Id |
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |
| `totalSummary` | object | Yes |  |
| `remindersConfiguration` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/invoices/{invoiceId}`

**Update invoice**

API to update invoice by invoice id

**Operation ID:** `update-invoice`

**Tags:** Invoice

**Required Scopes:** `invoices.write`, `invoices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `invoiceId` | path | string | Yes | Invoice Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes | Name to be updated |
| `title` | string | No | Title for the invoice |
| `currency` | string | Yes | Currency |
| `description` | string | No | Description |
| `businessDetails` | object | No |  |
| `invoiceNumber` | string | No | Invoice Number |
| `contactId` | string | No | Id of the contact which you need to send the invoice |
| `contactDetails` | object | No |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `discount` | object | No |  |
| `invoiceItems` | array of object | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `liveMode` | boolean | No | Payment mode |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `paymentSchedule` | object | No |  |
| `tipsConfiguration` | object | No |  |
| `xeroDetails` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`contactDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`invoiceItems` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`paymentSchedule` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`, `percentage`) | Yes | Payment schedule type |
| `schedules` | array of string | Yes | payment schedule item |

**`tipsConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tipsPercentage` | array of string | Yes | Percentage of tips allowed |
| `tipsEnabled` | boolean | Yes | Tips enabled status |

**`paymentMethods` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripe` | object | Yes |  |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/invoices/{invoiceId}`

**Delete invoice**

API to delete invoice by invoice id

**Operation ID:** `delete-invoice`

**Tags:** Invoice

**Required Scopes:** `invoices.write`, `invoices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `invoiceId` | path | string | Yes | Invoice Id |
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

**`400` - Bad Request**

**Response Example:**

```json
{
  "statusCode": 400,
  "message": "Unable to find an invoice with the given invoice id"
}
```

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/invoices/{invoiceId}/late-fees-configuration`

**Update invoice late fees configuration**

API to update invoice late fees configuration by invoice id

**Operation ID:** `update-invoice-late-fees-configuration`

**Tags:** Invoice

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `invoiceId` | path | string | Yes | Invoice Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `lateFeesConfiguration` | object | Yes |  |

**`lateFeesConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes | Enable late fees |
| `value` | number | Yes | Late Fees Value |
| `type` | string (enum: `fixed`, `percentage`) | Yes | Late Fees Type |
| `frequency` | object | Yes |  |
| `grace` | object | No |  |
| `maxLateFees` | object | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/{invoiceId}/void`

**Void invoice**

API to delete invoice by invoice id

**Operation ID:** `void-invoice`

**Tags:** Invoice

**Required Scopes:** `invoices.write`, `invoices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `invoiceId` | path | string | Yes | Invoice Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

**`400` - Bad Request**

**Response Example:**

```json
{
  "statusCode": 400,
  "message": "Unable to find an invoice with the given invoice id"
}
```

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/{invoiceId}/send`

**Send invoice**

API to send invoice by invoice id

**Operation ID:** `send-invoice`

**Tags:** Invoice

**Required Scopes:** `invoices.write`, `invoices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `invoiceId` | path | string | Yes | Invoice Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes |  |
| `sentFrom` | object | No |  |
| `autoPayment` | object | No |  |

**`sentFrom` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fromName` | string | No | Sender name to be used while sending invoice |
| `fromEmail` | string | No | Email id to be used while sending out invoices |

**`autoPayment` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes |  |
| `type` | string | No |  |
| `paymentMethodId` | string | No |  |
| `customerId` | string | No |  |
| `card` | object | No |  |
| `usBankAccount` | object | No |  |
| `sepaDirectDebit` | object | No |  |
| `bacsDirectDebit` | object | No |  |
| `becsDirectDebit` | object | No |  |
| `cardId` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoice` | object | Yes |  |
| `smsData` | object | Yes |  |
| `emailData` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/{invoiceId}/record-payment`

**Record a manual payment for an invoice**

API to record manual payment for an invoice by invoice id

**Operation ID:** `record-invoice`

**Tags:** Invoice

**Required Scopes:** `invoices.write`, `invoices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `invoiceId` | path | string | Yes | Invoice Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `mode` | string (enum: `cash`, `card`, `cheque`, `bank_transfer`, `other`) | Yes | manual payment method |
| `card` | object | Yes |  |
| `cheque` | object | Yes |  |
| `notes` | string | Yes | Any note to be recorded with the transaction |
| `amount` | number | No | Amount to be paid against the invoice. |
| `meta` | object | No |  |
| `paymentScheduleIds` | array of string | No | Payment Schedule Ids to be recorded against the invoice. |
| `fulfilledAt` | string | No | Updated At to be recorded against the invoice. |

**`card` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `brand` | string | Yes |  |
| `last4` | string | Yes |  |

**`cheque` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `number` | string | Yes | check number |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | status |
| `invoice` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/invoices/stats/last-visited-at`

**Update invoice last visited at**

API to update invoice last visited at by invoice id

**Operation ID:** `update-invoice-last-visited-at`

**Tags:** Invoice

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoiceId` | string | Yes | Invoice Id |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/invoices/`

**Create Invoice**

API to create an invoice

**Operation ID:** `create-invoice`

**Tags:** Invoice

**Required Scopes:** `invoices.write`, `invoices.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes | Invoice Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the invoice. |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the invoice |
| `contactDetails` | object | Yes |  |
| `invoiceNumber` | string | No | Invoice Number |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | No | Due date in YYYY-MM-DD format |
| `sentTo` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `paymentSchedule` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `tipsConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`contactDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

**`sentTo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | array of string | Yes | Email Address |
| `emailCc` | array of string | No | cc to be kept in any sent out emails |
| `emailBcc` | array of string | No | bcc to be kept in any sent out emails |
| `phoneNo` | array of string | No | Contact Phone Number |

**`paymentSchedule` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`, `percentage`) | Yes | Payment schedule type |
| `schedules` | array of string | Yes | payment schedule item |

**`lateFeesConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes | Enable late fees |
| `value` | number | Yes | Late Fees Value |
| `type` | string (enum: `fixed`, `percentage`) | Yes | Late Fees Type |
| `frequency` | object | Yes |  |
| `grace` | object | No |  |
| `maxLateFees` | object | No |  |

**`tipsConfiguration` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tipsPercentage` | array of string | Yes | Percentage of tips allowed |
| `tipsEnabled` | boolean | Yes | Tips enabled status |

**`paymentMethods` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripe` | object | Yes |  |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/`

**List invoices**

API to get list of invoices

**Operation ID:** `list-invoices`

**Tags:** Invoice

**Required Scopes:** `invoices.readonly`, `invoices.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | location Id / company Id based on altType |
| `altType` | query | string (enum: `location`) | Yes | Alt Type |
| `status` | query | string | No | status to be filtered |
| `startAt` | query | string | No | startAt in YYYY-MM-DD format |
| `endAt` | query | string | No | endAt in YYYY-MM-DD format |
| `search` | query | string | No | To search for an invoice by id / name / email / phoneNo |
| `paymentMode` | query | string (enum: `default`, `live`, `test`) | No | payment mode |
| `contactId` | query | string | No | Contact ID for the invoice |
| `limit` | query | string | Yes | Limit the number of items to return |
| `offset` | query | string | Yes | Number of items to skip |
| `sortField` | query | string (enum: `issueDate`) | No | The field on which sorting should be applied |
| `sortOrder` | query | string (enum: `ascend`, `descend`) | No | The order of sort which should be applied for the sortField |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoices` | array of object | Yes |  |
| `total` | number | Yes | Total number of invoices |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Estimate

### POST `/invoices/estimate`

**Create New Estimate**

Create a new estimate with the provided details

**Operation ID:** `create-new-estimate`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Estimate Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the estimate. |
| `liveMode` | boolean | No | livemode for estimate Default: `True` |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the estimate |
| `contactDetails` | object | Yes |  |
| `estimateNumber` | number | No | Estimate Number, if not specified will take in the next valid estimate number |
| `issueDate` | string | No | issue date estimate |
| `expiryDate` | string | No | expiry date estimate |
| `sentTo` | object | No |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Estimate Default: `False` |
| `meta` | object | No | Meta data for the estimate |
| `sendEstimateDetails` | object | No |  |
| `frequencySettings` | object | Yes |  |
| `estimateNumberPrefix` | string | No | Prefix for the estimate number Default: `EST-` |
| `userId` | string | No | User Id |
| `attachments` | array of object | No | attachments for the invoice |
| `autoInvoice` | object | No |  |
| `miscellaneousCharges` | object | No |  |
| `paymentScheduleConfig` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`contactDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

**`sentTo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | array of string | Yes | Email Address |
| `emailCc` | array of string | No | cc to be kept in any sent out emails |
| `emailBcc` | array of string | No | bcc to be kept in any sent out emails |
| `phoneNo` | array of string | No | Contact Phone Number |

**`sendEstimateDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes | livemode for estimate |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `sentFrom` | object | No |  |
| `estimateName` | string | No | estimate name |

**`frequencySettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | enabled for the frequency settings |
| `schedule` | object | Yes |  |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`autoInvoice` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Enable Auto Invoice |
| `directPayments` | boolean | No | Direct Payments |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

**`paymentScheduleConfig` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`, `percentage`) | Yes | Payment Schedule Type |
| `dateConfig` | object | Yes |  |
| `schedules` | array of array of any | Yes | Payment Schedule Items |

#### Responses

**`201` - Created**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |
| `companyId` | string | Yes | Company identifier associated with the estimate |
| `contactDetails` | object | Yes |  |
| `issueDate` | string | Yes | Date when the estimate was issued |
| `expiryDate` | string | Yes | Date when the estimate expires |
| `sentBy` | string | No | User who sent the estimate |
| `automaticTaxesCalculated` | boolean | Yes | Indicates if automatic taxes were calculated |
| `meta` | object | Yes | Additional metadata associated with the estimate |
| `estimateActionHistory` | array of string | Yes | History of actions taken on the estimate |
| `sentTo` | object | Yes |  |
| `frequencySettings` | object | Yes |  |
| `lastVisitedAt` | string | Yes | Timestamp when the estimate was last visited |
| `totalamountInUSD` | number | Yes | Total amount in USD |
| `autoInvoice` | object | No |  |
| `traceId` | string | Yes | Trace ID for logging and debugging |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/invoices/estimate/{estimateId}`

**Update Estimate**

Update an existing estimate with new details

**Operation ID:** `update-estimate`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `estimateId` | path | string | Yes | Estimate Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Estimate Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the estimate. |
| `liveMode` | boolean | No | livemode for estimate Default: `True` |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the estimate |
| `contactDetails` | object | Yes |  |
| `estimateNumber` | number | No | Estimate Number, if not specified will take in the next valid estimate number |
| `issueDate` | string | No | issue date estimate |
| `expiryDate` | string | No | expiry date estimate |
| `sentTo` | object | No |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Estimate Default: `False` |
| `meta` | object | No | Meta data for the estimate |
| `sendEstimateDetails` | object | No |  |
| `frequencySettings` | object | Yes |  |
| `estimateNumberPrefix` | string | No | Prefix for the estimate number Default: `EST-` |
| `userId` | string | No | User Id |
| `attachments` | array of object | No | attachments for the invoice |
| `autoInvoice` | object | No |  |
| `miscellaneousCharges` | object | No |  |
| `paymentScheduleConfig` | object | No |  |
| `estimateStatus` | string (enum: `all`, `draft`, `sent`, `accepted`, `declined`, `invoiced`, `viewed`) | No | Estimate Status |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`contactDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

**`sentTo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | array of string | Yes | Email Address |
| `emailCc` | array of string | No | cc to be kept in any sent out emails |
| `emailBcc` | array of string | No | bcc to be kept in any sent out emails |
| `phoneNo` | array of string | No | Contact Phone Number |

**`sendEstimateDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes | livemode for estimate |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `sentFrom` | object | No |  |
| `estimateName` | string | No | estimate name |

**`frequencySettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | enabled for the frequency settings |
| `schedule` | object | Yes |  |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`autoInvoice` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Enable Auto Invoice |
| `directPayments` | boolean | No | Direct Payments |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

**`paymentScheduleConfig` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`, `percentage`) | Yes | Payment Schedule Type |
| `dateConfig` | object | Yes |  |
| `schedules` | array of array of any | Yes | Payment Schedule Items |

#### Responses

**`200` - Successfully updated**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |
| `companyId` | string | Yes | Company identifier associated with the estimate |
| `contactDetails` | object | Yes |  |
| `issueDate` | string | Yes | Date when the estimate was issued |
| `expiryDate` | string | Yes | Date when the estimate expires |
| `sentBy` | string | No | User who sent the estimate |
| `automaticTaxesCalculated` | boolean | Yes | Indicates if automatic taxes were calculated |
| `meta` | object | Yes | Additional metadata associated with the estimate |
| `estimateActionHistory` | array of string | Yes | History of actions taken on the estimate |
| `sentTo` | object | Yes |  |
| `frequencySettings` | object | Yes |  |
| `lastVisitedAt` | string | Yes | Timestamp when the estimate was last visited |
| `totalamountInUSD` | number | Yes | Total amount in USD |
| `autoInvoice` | object | No |  |
| `traceId` | string | Yes | Trace ID for logging and debugging |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/invoices/estimate/{estimateId}`

**Delete Estimate**

Delete an existing estimate

**Operation ID:** `delete-estimate`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `estimateId` | path | string | Yes | Estimate Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successfully Deleted**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |
| `companyId` | string | Yes | Company identifier associated with the estimate |
| `contactDetails` | object | Yes |  |
| `issueDate` | string | Yes | Date when the estimate was issued |
| `expiryDate` | string | Yes | Date when the estimate expires |
| `sentBy` | string | No | User who sent the estimate |
| `automaticTaxesCalculated` | boolean | Yes | Indicates if automatic taxes were calculated |
| `meta` | object | Yes | Additional metadata associated with the estimate |
| `estimateActionHistory` | array of string | Yes | History of actions taken on the estimate |
| `sentTo` | object | Yes |  |
| `frequencySettings` | object | Yes |  |
| `lastVisitedAt` | string | Yes | Timestamp when the estimate was last visited |
| `totalamountInUSD` | number | Yes | Total amount in USD |
| `autoInvoice` | object | No |  |
| `traceId` | string | Yes | Trace ID for logging and debugging |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/estimate/number/generate`

**Generate Estimate Number**

Get the next estimate number for the given location

**Operation ID:** `generate-estimate-number`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.readonly`, `invoices/estimate.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimateNumber` | number | Yes |  |
| `traceId` | string | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/estimate/{estimateId}/send`

**Send Estimate**

API to send estimate by estimate id

**Operation ID:** `send-estimate`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `estimateId` | path | string | Yes | Estimate Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes | livemode for estimate |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `sentFrom` | object | No |  |
| `estimateName` | string | No | estimate name |

**`sentFrom` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fromName` | string | No | Sender name to be used while sending invoice |
| `fromEmail` | string | No | Email id to be used while sending out invoices |

#### Responses

**`201` - Created**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |
| `companyId` | string | Yes | Company identifier associated with the estimate |
| `contactDetails` | object | Yes |  |
| `issueDate` | string | Yes | Date when the estimate was issued |
| `expiryDate` | string | Yes | Date when the estimate expires |
| `sentBy` | string | No | User who sent the estimate |
| `automaticTaxesCalculated` | boolean | Yes | Indicates if automatic taxes were calculated |
| `meta` | object | Yes | Additional metadata associated with the estimate |
| `estimateActionHistory` | array of string | Yes | History of actions taken on the estimate |
| `sentTo` | object | Yes |  |
| `frequencySettings` | object | Yes |  |
| `lastVisitedAt` | string | Yes | Timestamp when the estimate was last visited |
| `totalamountInUSD` | number | Yes | Total amount in USD |
| `autoInvoice` | object | No |  |
| `traceId` | string | Yes | Trace ID for logging and debugging |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/estimate/{estimateId}/invoice`

**Create Invoice from Estimate**

Create a new invoice from an existing estimate

**Operation ID:** `create-invoice-from-estimate`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `estimateId` | path | string | Yes | Estimate Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `markAsInvoiced` | boolean | Yes | Mark Estimate as Invoiced |
| `version` | string (enum: `v1`, `v2`) | No | Version of the update request |

#### Responses

**`200` - Successfully Created**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimate` | object | Yes |  |
| `invoice` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/estimate/list`

**List Estimates**

Get a paginated list of estimates

**Operation ID:** `list-estimates`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.readonly`, `invoices/estimate.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `startAt` | query | string | No | startAt in YYYY-MM-DD format |
| `endAt` | query | string | No | endAt in YYYY-MM-DD format |
| `search` | query | string | No | search text for estimates name |
| `status` | query | string (enum: `all`, `draft`, `sent`, `accepted`, `declined`, `invoiced`, `viewed`) | No | estimate status |
| `contactId` | query | string | No | Contact ID for the estimate |
| `limit` | query | string | Yes | Limit the number of items to return |
| `offset` | query | string | Yes | Number of items to skip |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimates` | array of string | Yes | List of estimates |
| `total` | number | Yes | Total number of estimates |
| `traceId` | string | Yes | Unique identifier for tracing the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/invoices/estimate/stats/last-visited-at`

**Update estimate last visited at**

API to update estimate last visited at by estimate id

**Operation ID:** `update-estimate-last-visited-at`

**Tags:** Estimate

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimateId` | string | Yes | Estimate Id |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/invoices/estimate/template`

**List Estimate Templates**

Get a list of estimate templates or a specific template by ID

**Operation ID:** `list-estimate-templates`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.readonly`, `invoices/estimate.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `search` | query | string | No | To search for an estimate template by id / name |
| `limit` | query | string | Yes | Limit the number of items to return |
| `offset` | query | string | Yes | Number of items to skip |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of string | Yes | List of estimate templates |
| `totalCount` | number | Yes | Total number of estimate templates available |
| `traceId` | string | Yes | Unique identifier for tracing the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/invoices/estimate/template`

**Create Estimate Template**

Create a new estimate template

**Operation ID:** `create-estimate-template`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Estimate Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of array of any | Yes | An array of items for the estimate. |
| `liveMode` | boolean | No | livemode for estimate Default: `True` |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the estimate |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Estimate Default: `False` |
| `meta` | object | No | Meta data for the estimate |
| `sendEstimateDetails` | object | No |  |
| `estimateNumberPrefix` | string | No | Prefix for the estimate number Default: `EST-` |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`sendEstimateDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes | livemode for estimate |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `sentFrom` | object | No |  |
| `estimateName` | string | No | estimate name |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`201` - Successfully created**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/invoices/estimate/template/{templateId}`

**Update Estimate Template**

Update an existing estimate template

**Operation ID:** `update-estimate-template`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `templateId` | path | string | Yes | Template Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Estimate Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of array of any | Yes | An array of items for the estimate. |
| `liveMode` | boolean | No | livemode for estimate Default: `True` |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the estimate |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Estimate Default: `False` |
| `meta` | object | No | Meta data for the estimate |
| `sendEstimateDetails` | object | No |  |
| `estimateNumberPrefix` | string | No | Prefix for the estimate number Default: `EST-` |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

**`businessDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

**`discount` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

**`sendEstimateDetails` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes | livemode for estimate |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `sentFrom` | object | No |  |
| `estimateName` | string | No | estimate name |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

**`miscellaneousCharges` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

#### Responses

**`200` - Successfully updated**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/invoices/estimate/template/{templateId}`

**Delete Estimate Template**

Delete an existing estimate template

**Operation ID:** `delete-estimate-template`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.write`, `invoices/estimate.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `templateId` | path | string | Yes | Template Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |

#### Responses

**`200` - Successfully deleted**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/invoices/estimate/template/preview`

**Preview Estimate Template**

Get a preview of an estimate template

**Operation ID:** `preview-estimate-template`

**Tags:** Estimate

**Required Scopes:** `invoices/estimate.readonly`, `invoices/estimate.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `templateId` | query | string | Yes | Template Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AdditionalEmailsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | string | Yes |  |

### AddressDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `addressLine1` | string | No | Address Line 1 |
| `addressLine2` | string | No | Address Line 2 |
| `city` | string | No | City |
| `state` | string | No | State |
| `countryCode` | string | No | Country Code |
| `postalCode` | string | No | Postal Code |

### AltDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |

### AttachmentsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id of the file selected |
| `name` | string | Yes | Name of the file  |
| `url` | string | Yes | URL of the file |
| `type` | string | Yes | Type of the file |
| `size` | number | Yes | Size of the file |

### AutoInvoice

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### AutoInvoicingDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Enable Auto Invoice |
| `directPayments` | boolean | No | Direct Payments |

### AutoPaymentDetailsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes |  |
| `type` | string | No |  |
| `paymentMethodId` | string | No |  |
| `customerId` | string | No |  |
| `card` | object | No |  |
| `usBankAccount` | object | No |  |
| `sepaDirectDebit` | object | No |  |
| `bacsDirectDebit` | object | No |  |
| `becsDirectDebit` | object | No |  |
| `cardId` | string | No |  |

### AutoPaymentInvoiceScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### AutoPaymentScheduleDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `id` | string | Yes |  |
| `autoPayment` | object | Yes |  |

### BacsDirectDebitDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sort_code` | string | Yes |  |
| `last4` | string | Yes |  |

### BecsDirectDebitDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bsb_number` | string | Yes |  |
| `last4` | string | Yes |  |

### BusinessDetails

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### BusinessDetailsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoUrl` | string | No | Business Logo URL |
| `name` | string | No | Business Name |
| `phoneNo` | string | No | Business Phone Number |
| `address` | object | No |  |
| `website` | string | No | Business Website Link |
| `customValues` | array of string | No | Custom Values |

### CancelInvoiceScheduleDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |

### CancelInvoiceScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### CardDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `brand` | string | Yes |  |
| `last4` | string | Yes |  |

### ChequeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `number` | string | Yes | check number |

### ContactDetails

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### ContactDetailsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Contact ID |
| `name` | string | Yes | Contact Name |
| `phoneNo` | string | Yes | Contact Phone Number |
| `email` | string | Yes | Contact Email |
| `additionalEmails` | array of object | No | Secondary email addresses for the contact to be saved |
| `companyName` | string | No | Contact Company Name |
| `address` | object | No |  |
| `customFields` | array of string | No | Custom Values |

### CreateEstimatesDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Estimate Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the estimate. |
| `liveMode` | boolean | No | livemode for estimate Default: `True` |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the estimate |
| `contactDetails` | object | Yes |  |
| `estimateNumber` | number | No | Estimate Number, if not specified will take in the next valid estimate number |
| `issueDate` | string | No | issue date estimate |
| `expiryDate` | string | No | expiry date estimate |
| `sentTo` | object | No |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Estimate Default: `False` |
| `meta` | object | No | Meta data for the estimate |
| `sendEstimateDetails` | object | No |  |
| `frequencySettings` | object | Yes |  |
| `estimateNumberPrefix` | string | No | Prefix for the estimate number Default: `EST-` |
| `userId` | string | No | User Id |
| `attachments` | array of object | No | attachments for the invoice |
| `autoInvoice` | object | No |  |
| `miscellaneousCharges` | object | No |  |
| `paymentScheduleConfig` | object | No |  |

### CreateInvoiceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes | Invoice Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the invoice. |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the invoice |
| `contactDetails` | object | Yes |  |
| `invoiceNumber` | string | No | Invoice Number |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | No | Due date in YYYY-MM-DD format |
| `sentTo` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `paymentSchedule` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `tipsConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

### CreateInvoiceFromEstimateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `markAsInvoiced` | boolean | Yes | Mark Estimate as Invoiced |
| `version` | string (enum: `v1`, `v2`) | No | Version of the update request |

### CreateInvoiceFromEstimateResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimate` | object | Yes |  |
| `invoice` | object | Yes |  |

### CreateInvoiceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

### CreateInvoiceScheduleDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes |  |
| `contactDetails` | object | Yes |  |
| `schedule` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `discount` | object | Yes |  |
| `termsNotes` | string | No |  |
| `title` | string | No |  |
| `tipsConfiguration` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

### CreateInvoiceScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### CreateInvoiceTemplateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `internal` | boolean | No |  |
| `name` | string | Yes | Name of the template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `discount` | object | No |  |
| `termsNotes` | string | No |  |
| `title` | string | No | Template title |
| `tipsConfiguration` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of string | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

### CreateInvoiceTemplateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### CustomRRuleOptionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `intervalType` | string (enum: `yearly`, `monthly`, `weekly`, `daily`, `hourly`, `minutely`, `secondly`) | Yes |  |
| `interval` | number | Yes |  |
| `startDate` | string | Yes | Start date in YYYY-MM-DD format |
| `startTime` | string | No | Start time in HH:mm:ss format |
| `endDate` | string | No | End date in YYYY-MM-DD format |
| `endTime` | string | No | End time in HH:mm:ss format |
| `dayOfMonth` | number | No | -1, 1, 2, 3, ..., 27, 28 |
| `dayOfWeek` | string (enum: `mo`, `tu`, `we`, `th`, `fr`, `sa`, `su`) | No |  |
| `numOfWeek` | number | No | -1, 1, 2, 3, 4 |
| `monthOfYear` | string (enum: `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sep`, `oct`, `nov`, `dec`) | No |  |
| `count` | number | No | Max number of task executions |
| `daysBefore` | number | No | Execute task number of days before |
| `useStartAsPrimaryUserAccepted` | boolean | No | Start as primary user accepted date |
| `endType` | string | No | End type like after, by, count |

### DefaultInvoiceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

### DeleteInvoiceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

### DeleteInvoiceScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | success |

### DeleteInvoiceTemplateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | success |

### DiscountDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | No | Discount Value Default: `0` |
| `type` | string (enum: `percentage`, `fixed`) | Yes | Discount type Default: `percentage` |
| `validOnProductIds` | array of string | No | Product Ids on which discount is applicable |

### EstimateIdParam

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimateId` | string | Yes | Estimate Id |

### EstimateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |
| `companyId` | string | Yes | Company identifier associated with the estimate |
| `contactDetails` | object | Yes |  |
| `issueDate` | string | Yes | Date when the estimate was issued |
| `expiryDate` | string | Yes | Date when the estimate expires |
| `sentBy` | string | No | User who sent the estimate |
| `automaticTaxesCalculated` | boolean | Yes | Indicates if automatic taxes were calculated |
| `meta` | object | Yes | Additional metadata associated with the estimate |
| `estimateActionHistory` | array of string | Yes | History of actions taken on the estimate |
| `sentTo` | object | Yes |  |
| `frequencySettings` | object | Yes |  |
| `lastVisitedAt` | string | Yes | Timestamp when the estimate was last visited |
| `totalamountInUSD` | number | Yes | Total amount in USD |
| `autoInvoice` | object | No |  |
| `traceId` | string | Yes | Trace ID for logging and debugging |

### EstimateTemplateResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `_id` | string | Yes | Unique identifier |
| `liveMode` | boolean | Yes | Indicates if it is in live mode |
| `deleted` | boolean | Yes | Indicates if deleted |
| `name` | string | Yes | Name |
| `currency` | string | Yes | Currency code |
| `businessDetails` | object | Yes |  |
| `items` | array of array of any | Yes | An array of items |
| `discount` | object | Yes |  |
| `title` | string | No | Title |
| `estimateNumberPrefix` | string | No | Estimate number prefix |
| `attachments` | array of object | No | Attachments |
| `updatedBy` | string | No | User Id of who last updated |
| `total` | number | Yes | Total amount |
| `createdAt` | string | Yes | Timestamp when created |
| `updatedAt` | string | Yes | Timestamp when last updated |
| `__v` | number | Yes | Version number |
| `automaticTaxesEnabled` | boolean | Yes | Indicates if automatic taxes are enabled for this estimate |
| `termsNotes` | string | No | Terms and conditions for the estimate, supports HTML markup |

### EstimateTemplatesDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Estimate Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of array of any | Yes | An array of items for the estimate. |
| `liveMode` | boolean | No | livemode for estimate Default: `True` |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the estimate |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Estimate Default: `False` |
| `meta` | object | No | Meta data for the estimate |
| `sendEstimateDetails` | object | No |  |
| `estimateNumberPrefix` | string | No | Prefix for the estimate number Default: `EST-` |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

### FrequencySettingsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | enabled for the frequency settings |
| `schedule` | object | Yes |  |

### GenerateEstimateNumberResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimateNumber` | number | Yes |  |
| `traceId` | string | Yes |  |

### GenerateInvoiceNumberResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoiceNumber` | number | No | Invoice Number |

### GetInvoiceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |
| `totalSummary` | object | Yes |  |
| `remindersConfiguration` | object | No |  |

### GetScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### GetTemplateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### InvoiceItemDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Invoice Item Name |
| `description` | string | No | Invoice descriptions |
| `productId` | string | No | Product Id |
| `priceId` | string | No | Price Id |
| `currency` | string | Yes | Currency |
| `amount` | number | Yes | Product amount |
| `qty` | number | Yes | Product Quantity |
| `taxes` | array of object | No | Tax |
| `automaticTaxCategoryId` | string | No | Tax category id for calculating automatic tax |
| `isSetupFeeItem` | boolean | No | Setupfee item, only created when 1st invoice of recurring schedule is generated |
| `type` | string (enum: `one_time`, `recurring`) | No | Price type of the item |
| `taxInclusive` | boolean | No | true if item amount is tax inclusive Default: `False` |

### InvoiceSettingsSenderConfigurationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fromName` | string | No | Sender name to be used while sending invoice |
| `fromEmail` | string | No | Email id to be used while sending out invoices |

### ItemTaxDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes |  |
| `name` | string | Yes |  |
| `rate` | number | Yes |  |
| `calculation` | string (enum: `exclusive`) | No |  |
| `description` | string | No |  |
| `taxId` | string | No |  |

### LateFeesConfigurationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enable` | boolean | Yes | Enable late fees |
| `value` | number | Yes | Late Fees Value |
| `type` | string (enum: `fixed`, `percentage`) | Yes | Late Fees Type |
| `frequency` | object | Yes |  |
| `grace` | object | No |  |
| `maxLateFees` | object | No |  |

### LateFeesFrequencyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `intervalCount` | number | No | Late fees interval count |
| `interval` | string (enum: `minute`, `hour`, `day`, `week`, `month`, `one_time`) | Yes | Late fees interval |

### LateFeesGraceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `intervalCount` | number | Yes | Late fees grace interval count |
| `interval` | string (enum: `day`) | Yes | Late fees grace interval |

### LateFeesMaxFeesDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`) | Yes |  |
| `value` | number | Yes | 10 |

### ListEstimateTemplateResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of string | Yes | List of estimate templates |
| `totalCount` | number | Yes | Total number of estimate templates available |
| `traceId` | string | Yes | Unique identifier for tracing the request |

### ListEstimatesResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `estimates` | array of string | Yes | List of estimates |
| `total` | number | Yes | Total number of estimates |
| `traceId` | string | Yes | Unique identifier for tracing the request |

### ListInvoicesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoices` | array of object | Yes |  |
| `total` | number | Yes | Total number of invoices |

### ListSchedulesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedules` | array of object | Yes |  |
| `total` | number | Yes | Total number of Schedules |

### ListTemplatesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes |  |
| `totalCount` | number | Yes | Total number of Templates |

### OldCreateInvoiceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### PatchInvoiceStatsLastViewedDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoiceId` | string | Yes | Invoice Id |

### PaymentMethodDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stripe` | object | Yes |  |

### PaymentScheduleConfigDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`, `percentage`) | Yes | Payment Schedule Type |
| `dateConfig` | object | Yes |  |
| `schedules` | array of array of any | Yes | Payment Schedule Items |

### PaymentScheduleDateConfigDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `depositDateType` | string (enum: `estimate_accepted`, `custom`) | Yes | Deposit date type |
| `scheduleDateType` | string (enum: `regular_interval`, `custom`) | Yes | Payment Schedule Date Type |

### PaymentScheduleDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `fixed`, `percentage`) | Yes | Payment schedule type |
| `schedules` | array of string | Yes | payment schedule item |

### ProcessingFeeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `charges` | array of array of any | Yes | charges for the processing fee |
| `collectedMiscellaneousCharges` | number | No | collected miscellaneous charges |
| `paidCharges` | array of object | No | paid miscellaneous charges |

### ProcessingFeePaidChargeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | name of the processing fee |
| `charge` | number | Yes | charge for the processing fee |
| `amount` | number | Yes | amount of the processing fee |
| `_id` | string | Yes | id of the processing fee |

### RecordPaymentDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `mode` | string (enum: `cash`, `card`, `cheque`, `bank_transfer`, `other`) | Yes | manual payment method |
| `card` | object | Yes |  |
| `cheque` | object | Yes |  |
| `notes` | string | Yes | Any note to be recorded with the transaction |
| `amount` | number | No | Amount to be paid against the invoice. |
| `meta` | object | No |  |
| `paymentScheduleIds` | array of string | No | Payment Schedule Ids to be recorded against the invoice. |
| `fulfilledAt` | string | No | Updated At to be recorded against the invoice. |

### RecordPaymentResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | status |
| `invoice` | object | Yes |  |

### ReminderDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Flag indicating if the reminder is enabled or not |
| `emailTemplate` | string | Yes | Email template to be used for sending reminders |
| `smsTemplate` | string | Yes | SMS template to be used for sending reminders |
| `emailSubject` | string | Yes | Subject of the reminder |
| `reminderId` | string | Yes | Unique identifier for the reminder |
| `reminderName` | string | Yes | Name of the reminder |
| `reminderTime` | string (enum: `before`, `after`) | Yes | Time condition for the reminder |
| `intervalType` | string (enum: `yearly`, `monthly`, `weekly`, `daily`, `hourly`, `minutely`, `secondly`) | Yes | Interval type for the reminder |
| `maxReminders` | number | Yes | Maximum number of reminders that can be sent |
| `reminderInvoiceCondition` | string (enum: `invoice_sent`, `invoice_overdue`) | Yes | Condition for sending the reminder |
| `reminderNumber` | number | Yes | frequency gap of the reminder to exeucte |
| `startTime` | string | No | Business Hour Start Time |
| `endTime` | string | No | Business Hour End Time |
| `timezone` | string | No | Timezone at which reminder will be sent |

### ReminderExecutionDetailsList

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### ReminderSettingsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `defaultEmailTemplateId` | string | Yes | default template Id of reminder |
| `reminders` | array of object | Yes | List of reminders |

### RemindersConfigurationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `reminderExecutionDetailsList` | object | Yes |  |
| `reminderSettings` | object | Yes |  |

### ScheduleInvoiceScheduleDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `liveMode` | boolean | Yes |  |
| `autoPayment` | object | No |  |

### ScheduleInvoiceScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### ScheduleOptionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `executeAt` | string | No |  |
| `rrule` | object | No |  |

### SendEstimateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes | livemode for estimate |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `sentFrom` | object | No |  |
| `estimateName` | string | No | estimate name |

### SendInvoiceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `userId` | string | Yes | Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future comm... |
| `action` | string (enum: `sms_and_email`, `send_manually`, `email`, `sms`) | Yes |  |
| `liveMode` | boolean | Yes |  |
| `sentFrom` | object | No |  |
| `autoPayment` | object | No |  |

### SendInvoicesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoice` | object | Yes |  |
| `smsData` | object | Yes |  |
| `emailData` | object | Yes |  |

### SentTo

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### SentToDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `email` | array of string | Yes | Email Address |
| `emailCc` | array of string | No | cc to be kept in any sent out emails |
| `emailBcc` | array of string | No | bcc to be kept in any sent out emails |
| `phoneNo` | array of string | No | Contact Phone Number |

### SepaDirectDebitDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bank_code` | string | Yes |  |
| `last4` | string | Yes |  |
| `branch_code` | string | Yes |  |

### StripePaymentMethodDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enableBankDebitOnly` | boolean | Yes | Enable Bank Debit Only |

### Text2PayDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes | Invoice Name |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the invoice. |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the invoice |
| `contactDetails` | object | Yes |  |
| `invoiceNumber` | string | No | Invoice Number |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | No | Due date in YYYY-MM-DD format |
| `sentTo` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `paymentSchedule` | object | No |  |
| `lateFeesConfiguration` | object | No |  |
| `tipsConfiguration` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |
| `id` | string | No | id of invoice to update. If skipped, a new invoice will be created |
| `includeTermsNote` | boolean | No | include terms & notes with receipts |
| `action` | string (enum: `draft`, `send`) | Yes | create invoice in draft mode or send mode |
| `userId` | string | Yes | id of user generating invoice |
| `discount` | object | No |  |
| `businessDetails` | object | No |  |

### Text2PayInvoiceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invoice` | object | Yes |  |
| `invoiceUrl` | string | Yes | preview url of generated invoice |

### TipsConfigurationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tipsPercentage` | array of string | Yes | Percentage of tips allowed |
| `tipsEnabled` | boolean | Yes | Tips enabled status |

### TotalSummaryDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `subTotal` | number | Yes | subTotal |
| `discount` | number | Yes | discount |
| `tax` | number | Yes | tax |

### USBankAccountDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bank_name` | string | Yes |  |
| `last4` | string | Yes |  |

### UpdateAndScheduleInvoiceScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### UpdateEstimateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Estimate Name |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency code |
| `items` | array of object | Yes | An array of items for the estimate. |
| `liveMode` | boolean | No | livemode for estimate Default: `True` |
| `discount` | object | Yes |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `title` | string | No | Title for the estimate |
| `contactDetails` | object | Yes |  |
| `estimateNumber` | number | No | Estimate Number, if not specified will take in the next valid estimate number |
| `issueDate` | string | No | issue date estimate |
| `expiryDate` | string | No | expiry date estimate |
| `sentTo` | object | No |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Estimate Default: `False` |
| `meta` | object | No | Meta data for the estimate |
| `sendEstimateDetails` | object | No |  |
| `frequencySettings` | object | Yes |  |
| `estimateNumberPrefix` | string | No | Prefix for the estimate number Default: `EST-` |
| `userId` | string | No | User Id |
| `attachments` | array of object | No | attachments for the invoice |
| `autoInvoice` | object | No |  |
| `miscellaneousCharges` | object | No |  |
| `paymentScheduleConfig` | object | No |  |
| `estimateStatus` | string (enum: `all`, `draft`, `sent`, `accepted`, `declined`, `invoiced`, `viewed`) | No | Estimate Status |

### UpdateInvoiceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes | Name to be updated |
| `title` | string | No | Title for the invoice |
| `currency` | string | Yes | Currency |
| `description` | string | No | Description |
| `businessDetails` | object | No |  |
| `invoiceNumber` | string | No | Invoice Number |
| `contactId` | string | No | Id of the contact which you need to send the invoice |
| `contactDetails` | object | No |  |
| `termsNotes` | string | No | Terms notes, Also supports HTML markups |
| `discount` | object | No |  |
| `invoiceItems` | array of object | Yes |  |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `liveMode` | boolean | No | Payment mode |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `paymentSchedule` | object | No |  |
| `tipsConfiguration` | object | No |  |
| `xeroDetails` | object | No |  |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `paymentMethods` | object | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

### UpdateInvoiceLateFeesConfigurationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `lateFeesConfiguration` | object | Yes |  |

### UpdateInvoiceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |

### UpdateInvoiceScheduleDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `name` | string | Yes |  |
| `contactDetails` | object | Yes |  |
| `schedule` | object | Yes |  |
| `liveMode` | boolean | Yes |  |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `discount` | object | Yes |  |
| `termsNotes` | string | No |  |
| `title` | string | No |  |
| `attachments` | array of object | No | attachments for the invoice |
| `miscellaneousCharges` | object | No |  |

### UpdateInvoiceScheduleResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Schedule Id |
| `status` | object | Yes | Schedule Status |
| `liveMode` | boolean | Yes | Live Mode |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `schedule` | object | No |  |
| `invoices` | array of object | Yes | List of invoices |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes |  |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `termsNotes` | string | Yes | Terms notes |
| `compiledTermsNotes` | string | Yes | Compiled terms notes |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### UpdateInvoiceTemplateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `internal` | boolean | No |  |
| `name` | string | Yes | Name of the template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes |  |
| `items` | array of object | Yes |  |
| `discount` | object | No |  |
| `termsNotes` | string | No |  |
| `title` | string | No | Template title |
| `miscellaneousCharges` | object | No |  |

### UpdateInvoiceTemplateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Template Id |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the Template |
| `businessDetails` | object | Yes |  |
| `currency` | string | Yes | Currency |
| `discount` | object | No |  |
| `items` | array of string | Yes | Invoice Items |
| `invoiceNumberPrefix` | string | No | prefix for invoice number |
| `total` | number | Yes | Total Amount |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |

### UpdatePaymentMethodsConfigurationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |
| `paymentMethods` | object | No |  |

### VoidInvoiceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | location Id / company Id based on altType |
| `altType` | string (enum: `location`) | Yes | Alt Type |

### VoidInvoiceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Invoice Id |
| `status` | string (enum: `draft`, `sent`, `payment_processing`, `paid`, `void`, `partially_paid`) | Yes | Invoice Status |
| `liveMode` | boolean | Yes | Live Mode |
| `amountPaid` | number | Yes | Amount Paid |
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `name` | string | Yes | Name of the invoice |
| `businessDetails` | object | Yes | Business Details |
| `invoiceNumber` | number | Yes | Invoice Number |
| `currency` | string | Yes | Currency |
| `contactDetails` | object | Yes | Contact Details |
| `issueDate` | string | Yes | Issue date in YYYY-MM-DD format |
| `dueDate` | string | Yes | Due date in YYYY-MM-DD format |
| `discount` | object | No | Discount |
| `invoiceItems` | array of string | Yes | Invoice Items |
| `total` | number | Yes | Total Amount |
| `title` | string | Yes | Title |
| `amountDue` | number | Yes | Total Amount Due |
| `createdAt` | string | Yes | created at |
| `updatedAt` | string | Yes | updated at |
| `automaticTaxesEnabled` | boolean | No | Automatic taxes enabled for the Invoice |
| `automaticTaxesCalculated` | boolean | No | Is Automatic taxes calculated for the Invoice items |
| `paymentSchedule` | object | No | split invoice into payment schedule summing up to full invoice amount |
