# Contacts API

Documentation for Contacts API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Search](#search)
- [Tasks](#tasks)
- [Appointments](#appointments)
- [Tags](#tags)
- [Notes](#notes)
- [Bulk](#bulk)
- [Contacts](#contacts)
- [Followers](#followers)
- [Campaigns](#campaigns)
- [Workflow](#workflow)

## Search

### POST `/contacts/search`

**Search Contacts**

Search contacts based on combinations of advanced filters. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad

**Operation ID:** `search-contacts-advanced`

**Tags:** Search

**Required Scopes:** `contacts.readonly`

**External Documentation:** [Click here for more information](https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad)

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

#### Responses

**`200` - Success**

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/contacts/search/duplicate`

**Get Duplicate Contact**

Get Duplicate Contact.

If `Allow Duplicate Contact` is disabled under Settings, the global unique identifier will be used for searching the contact. If the setting is enabled, first priority for search is `email` and the second priority will be `phone`.

**Operation ID:** `get-duplicate-contact`

**Tags:** Search

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `number` | query | string | No | Phone Number - Pass in URL Encoded form. i.e +1423164516 will become `%2B1423164516` |
| `email` | query | string | No | Email - Pass in URL Encoded form. i.e test+abc@gmail.com will become `test%2Babc%40gmail.com` |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Tasks

### GET `/contacts/{contactId}/tasks`

**Get all Tasks**

Get all Tasks

**Operation ID:** `get-all-tasks`

**Tags:** Tasks

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tasks` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/contacts/{contactId}/tasks`

**Create Task**

Create Task

**Operation ID:** `create-task`

**Tags:** Tasks

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `body` | string | No |  |
| `dueDate` | string | Yes |  |
| `completed` | boolean | Yes |  |
| `assignedTo` | string | No |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `task` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/contacts/{contactId}/tasks/{taskId}`

**Get Task**

Get Task

**Operation ID:** `get-task`

**Tags:** Tasks

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `taskId` | path | string | Yes | Task Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `task` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/contacts/{contactId}/tasks/{taskId}`

**Update Task**

Update Task

**Operation ID:** `update-task`

**Tags:** Tasks

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `taskId` | path | string | Yes | Task Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No |  |
| `body` | string | No |  |
| `dueDate` | string | No |  |
| `completed` | boolean | No |  |
| `assignedTo` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `task` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}/tasks/{taskId}`

**Delete Task**

Delete Task

**Operation ID:** `delete-task`

**Tags:** Tasks

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `taskId` | path | string | Yes | Task Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/contacts/{contactId}/tasks/{taskId}/completed`

**Update Task Completed**

Update Task Completed

**Operation ID:** `update-task-completed`

**Tags:** Tasks

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `taskId` | path | string | Yes | Task Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `completed` | boolean | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `task` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Appointments

### GET `/contacts/{contactId}/appointments`

**Get Appointments for Contact**

Get Appointments for Contact

**Operation ID:** `get-appointments-for-contact`

**Tags:** Appointments

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `events` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Tags

### POST `/contacts/{contactId}/tags`

**Add Tags**

Add Tags

**Operation ID:** `add-tags`

**Tags:** Tags

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of string | Yes |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}/tags`

**Remove Tags**

Remove Tags

**Operation ID:** `remove-tags`

**Tags:** Tags

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Notes

### GET `/contacts/{contactId}/notes`

**Get All Notes**

Get All Notes

**Operation ID:** `get-all-notes`

**Tags:** Notes

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notes` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/contacts/{contactId}/notes`

**Create Note**

Create Note

**Operation ID:** `create-note`

**Tags:** Notes

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No |  |
| `body` | string | Yes |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `note` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/contacts/{contactId}/notes/{id}`

**Get Note**

Get Note

**Operation ID:** `get-note`

**Tags:** Notes

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `id` | path | string | Yes | Note Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `note` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/contacts/{contactId}/notes/{id}`

**Update Note**

Update Note

**Operation ID:** `update-note`

**Tags:** Notes

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `id` | path | string | Yes | Note Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No |  |
| `body` | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `note` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}/notes/{id}`

**Delete Note**

Delete Note

**Operation ID:** `delete-note`

**Tags:** Notes

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `id` | path | string | Yes | Note Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Bulk

### POST `/contacts/bulk/tags/update/{type}`

**Update Contacts Tags**

Allows you to update tags to multiple contacts at once, you can add or remove tags from the contacts

**Operation ID:** `create-association`

**Tags:** Bulk

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `type` | path | string (enum: `add`, `remove`) | Yes | Tags operation type |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contacts` | array of string | Yes | list of contact ids to be processed |
| `tags` | array of string | Yes | list of tags to be added or removed |
| `locationId` | string | Yes | location id from where the bulk request is executed |
| `removeAllTags` | boolean | No | Option to implement remove all tags. if true, all tags will be removed from the contacts. Can only be used with remove type. |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | Yes | Indicates if the operation was successful |
| `errorCount` | number | Yes | Number of errors encountered during the operation |
| `responses` | array of string | Yes | Responses for each contact processed |

**`400` - Bad Request**

**`422` - Unprocessable Entity**

---

### POST `/contacts/bulk/business`

**Add/Remove Contacts From Business**

Add/Remove Contacts From Business . Passing a `null` businessId will remove the businessId from the contacts

**Operation ID:** `add-remove-contact-from-business`

**Tags:** Bulk

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `ids` | array of string | Yes |  |
| `businessId` | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |
| `ids` | array of string | Yes |  |

**`422` - Unprocessable Entity**

---

## Contacts

### GET `/contacts/{contactId}`

**Get Contact**

Get Contact

**Operation ID:** `get-contact`

**Tags:** Contacts

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contact` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/contacts/{contactId}`

**Update Contact**

Please find the list of acceptable values for the `country` field  here

**Operation ID:** `update-contact`

**Tags:** Contacts

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `inboundDndSettings` | object | No |  |
| `tags` | array of string | No | This field will overwrite all current tags associated with the contact. To update a tags, it is recommended to use the Add Tag or Remove Tag API instead. |
| `customFields` | array of object | object | object | object | object | object | object | object | object | No |  |
| `source` | string | No |  |
| `country` | string | No |  |
| `assignedTo` | string | No | User's Id |

**`dndSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Call` | object | No |  |
| `Email` | object | No |  |
| `SMS` | object | No |  |
| `WhatsApp` | object | No |  |
| `GMB` | object | No |  |
| `FB` | object | No |  |

**`inboundDndSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `all` | object | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |
| `contact` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}`

**Delete Contact**

Delete Contact

**Operation ID:** `delete-contact`

**Tags:** Contacts

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/contacts/upsert`

**Upsert Contact**

Please find the list of acceptable values for the `country` field  here

The Upsert API will adhere to the configuration defined under the “Allow Duplicate Contact” setting at the Location level. If the setting is configured to check both Email and Phone, the API will attempt to identify an existing contact based on the priority sequence specified in the setting, and will create or update the contact accordingly.

If two separate contacts already exist—one with the same email and another with the same phone—and an upsert request includes both the email and phone, the API will update the contact that matches the first field in the configured sequence, and ignore the second field to prevent duplication.

**Operation ID:** `upsert-contact`

**Tags:** Contacts

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `locationId` | string | Yes |  |
| `gender` | string | No |  |
| `phone` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `inboundDndSettings` | object | No |  |
| `tags` | array of string | No | This field will overwrite all current tags associated with the contact. To update a tags, it is recommended to use the Add Tag or Remove Tag API instead. |
| `customFields` | array of object | object | object | object | object | object | object | object | object | No |  |
| `source` | string | No |  |
| `country` | string | No |  |
| `companyName` | string | No |  |
| `assignedTo` | string | No | User's Id |

**`dndSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Call` | object | No |  |
| `Email` | object | No |  |
| `SMS` | object | No |  |
| `WhatsApp` | object | No |  |
| `GMB` | object | No |  |
| `FB` | object | No |  |

**`inboundDndSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `all` | object | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `new` | boolean | No |  |
| `contact` | object | No |  |
| `traceId` | string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/contacts/business/{businessId}`

**Get Contacts By BusinessId**

Get Contacts By BusinessId

**Operation ID:** `get-contacts-by-businessId`

**Tags:** Contacts

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `businessId` | path | string | Yes |  |
| `limit` | query | string | No |  |
| `locationId` | query | string | Yes |  |
| `skip` | query | string | No |  |
| `query` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contacts` | array of object | No |  |
| `count` | number | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/contacts/`

**Create Contact**

Please find the list of acceptable values for the `country` field  here

**Operation ID:** `create-contact`

**Tags:** Contacts

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `locationId` | string | Yes |  |
| `gender` | string | No |  |
| `phone` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `inboundDndSettings` | object | No |  |
| `tags` | array of string | No |  |
| `customFields` | array of object | object | object | object | object | object | object | object | object | No |  |
| `source` | string | No |  |
| `country` | string | No |  |
| `companyName` | string | No |  |
| `assignedTo` | string | No | User's Id |

**`dndSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Call` | object | No |  |
| `Email` | object | No |  |
| `SMS` | object | No |  |
| `WhatsApp` | object | No |  |
| `GMB` | object | No |  |
| `FB` | object | No |  |

**`inboundDndSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `all` | object | No |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contact` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/contacts/`

**Get Contacts**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Get Contacts

 **Note:** This API endpoint is deprecated. Please use the [Search Contacts](https://highlevel.stoplight.io/docs/integrations/dbe4f3a00a106-search-contacts) endpoint instead.

**Operation ID:** `get-contacts`

**Tags:** Contacts

**Required Scopes:** `contacts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `startAfterId` | query | string | No | Start After Id |
| `startAfter` | query | number | No | Start Afte |
| `query` | query | string | No | Contact Query |
| `limit` | query | number | No | Limit Per Page records count. will allow maximum up to 100 and default will be 20 |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contacts` | array of object | No |  |
| `count` | number | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Followers

### POST `/contacts/{contactId}/followers`

**Add Followers**

Add Followers

**Operation ID:** `add-followers-contact`

**Tags:** Followers

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | Yes |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersAdded` | array of string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}/followers`

**Remove Followers**

Remove Followers

**Operation ID:** `remove-followers-contact`

**Tags:** Followers

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersRemoved` | array of string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Campaigns

### POST `/contacts/{contactId}/campaigns/{campaignId}`

**Add Contact to Campaign**

Add contact to Campaign

**Operation ID:** `add-contact-to-campaign`

**Tags:** Campaigns

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `campaignId` | path | string | Yes | Campaigns Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}/campaigns/{campaignId}`

**Remove Contact From Campaign**

Remove Contact From Campaign

**Operation ID:** `remove-contact-from-campaign`

**Tags:** Campaigns

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `campaignId` | path | string | Yes | Campaigns Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}/campaigns/removeAll`

**Remove Contact From Every Campaign**

Remove Contact From Every Campaign

**Operation ID:** `remove-contact-from-every-campaign`

**Tags:** Campaigns

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Workflow

### POST `/contacts/{contactId}/workflow/{workflowId}`

**Add Contact to Workflow**

Add Contact to Workflow

**Operation ID:** `add-contact-to-workflow`

**Tags:** Workflow

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `workflowId` | path | string | Yes | Workflow Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `eventStartTime` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/contacts/{contactId}/workflow/{workflowId}`

**Delete Contact from Workflow**

Delete Contact from Workflow

**Operation ID:** `delete-contact-from-workflow`

**Tags:** Workflow

**Required Scopes:** `contacts.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `contactId` | path | string | Yes | Contact Id |
| `workflowId` | path | string | Yes | Workflow Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `eventStartTime` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AddContactToCampaignDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### AttributionSource

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes |  |
| `campaign` | string | No |  |
| `utmSource` | string | No |  |
| `utmMedium` | string | No |  |
| `utmContent` | string | No |  |
| `referrer` | string | No |  |
| `campaignId` | string | No |  |
| `fbclid` | string | No |  |
| `gclid` | string | No |  |
| `msclikid` | string | No |  |
| `dclid` | string | No |  |
| `fbc` | string | No |  |
| `fbp` | string | No |  |
| `fbEventId` | string | No |  |
| `userAgent` | string | No |  |
| `ip` | string | No |  |
| `medium` | string | No |  |
| `mediumId` | string | No |  |

### CheckboxField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | array of string | No |  |

### Contact

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `phoneLabel` | string | No |  |
| `country` | string | No |  |
| `address` | string | No |  |
| `source` | string | No |  |
| `type` | string | No |  |
| `locationId` | string | No |  |
| `dnd` | boolean | No |  |
| `state` | string | No |  |
| `businessName` | string | No |  |
| `customFields` | array of object | No |  |
| `tags` | array of string | No |  |
| `dateAdded` | string | No |  |
| `additionalEmails` | array of string | No |  |
| `phone` | string | No |  |
| `companyName` | string | No |  |
| `additionalPhones` | array of string | No |  |
| `dateUpdated` | string | No |  |
| `city` | string | No |  |
| `dateOfBirth` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `firstNameLowerCase` | string | No |  |
| `lastNameLowerCase` | string | No |  |
| `email` | string | No |  |
| `assignedTo` | string | No |  |
| `followers` | array of string | No |  |
| `validEmail` | boolean | No |  |
| `dndSettings` | object | No |  |
| `opportunities` | array of object | No |  |
| `postalCode` | string | No |  |
| `businessId` | string | No |  |
| `searchAfter` | array of string | No |  |

### ContactOpportunity

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `pipeline_id` | string | Yes |  |
| `pipeline_stage_id` | string | Yes |  |
| `monetary_value` | number | Yes |  |
| `status` | string | Yes |  |

### ContactsBulkUpateResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |
| `ids` | array of string | Yes |  |

### ContactsBusinessUpdate

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `ids` | array of string | Yes |  |
| `businessId` | string | Yes |  |

### ContactsByIdSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contact` | object | No |  |

### ContactsMetaSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | No |  |
| `nextPageUrl` | string | No |  |
| `startAfterId` | string | No |  |
| `startAfter` | number | No |  |
| `currentPage` | number | No |  |
| `nextPage` | number | No |  |
| `prevPage` | number | No |  |

### ContactsSearchSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `locationId` | string | No |  |
| `email` | string | No |  |
| `timezone` | string | No |  |
| `country` | string | No |  |
| `source` | string | No |  |
| `dateAdded` | string | No |  |
| `customFields` | array of object | No |  |
| `tags` | array of string | No |  |
| `businessId` | string | No |  |
| `attributions` | array of object | No |  |
| `followers` | array of string | No |  |

### ContactsSearchSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contacts` | array of object | No |  |
| `count` | number | No |  |

### ContactsWorkflowSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### CreateAddFollowersSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersAdded` | array of string | No |  |

### CreateAddTagSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of string | No |  |

### CreateContactDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `locationId` | string | Yes |  |
| `gender` | string | No |  |
| `phone` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `inboundDndSettings` | object | No |  |
| `tags` | array of string | No |  |
| `customFields` | array of object | object | object | object | object | object | object | object | object | No |  |
| `source` | string | No |  |
| `country` | string | No |  |
| `companyName` | string | No |  |
| `assignedTo` | string | No | User's Id |

### CreateContactSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `dateAdded` | string | No |  |
| `dateUpdated` | string | No |  |
| `deleted` | boolean | No |  |
| `tags` | array of string | No |  |
| `type` | string | No |  |
| `customFields` | array of object | No |  |
| `locationId` | string | No |  |
| `firstName` | string | No |  |
| `firstNameLowerCase` | string | No |  |
| `fullNameLowerCase` | string | No |  |
| `lastName` | string | No |  |
| `lastNameLowerCase` | string | No |  |
| `email` | string | No |  |
| `emailLowerCase` | string | No |  |
| `bounceEmail` | boolean | No |  |
| `unsubscribeEmail` | boolean | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `phone` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `country` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `source` | string | No |  |
| `companyName` | string | No |  |
| `dateOfBirth` | string | No |  |
| `birthMonth` | number | No |  |
| `birthDay` | number | No |  |
| `lastSessionActivityAt` | string | No |  |
| `offers` | array of string | No |  |
| `products` | array of string | No |  |
| `businessId` | string | No |  |
| `assignedTo` | string | No | User's Id |

### CreateContactsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contact` | object | No |  |

### CreateDeleteCantactsCampaignsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### CreateDeleteTagSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of string | No |  |

### CreateTaskParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `body` | string | No |  |
| `dueDate` | string | Yes |  |
| `completed` | boolean | Yes |  |
| `assignedTo` | string | No |  |

### CreateWorkflowDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `eventStartTime` | string | No |  |

### CustomFieldSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `value` | string | No |  |

### DeleteContactsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### DeleteFollowersSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | No |  |
| `followersRemoved` | array of string | No |  |

### DeleteNoteSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### DeleteTaskSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |

### DndSettingSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | string (enum: `active`, `inactive`, `permanent`) | Yes |  |
| `message` | string | No |  |
| `code` | string | No |  |

### DndSettingsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Call` | object | No |  |
| `Email` | object | No |  |
| `SMS` | object | No |  |
| `WhatsApp` | object | No |  |
| `GMB` | object | No |  |
| `FB` | object | No |  |

### FileField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | object | No |  |

### FollowersDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followers` | array of string | Yes |  |

### GetContectByIdSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `locationId` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No |  |
| `emailLowerCase` | string | No |  |
| `timezone` | string | No |  |
| `companyName` | string | No |  |
| `phone` | string | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `type` | string | No |  |
| `source` | string | No |  |
| `assignedTo` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `country` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `tags` | array of string | No |  |
| `dateOfBirth` | string | No |  |
| `dateAdded` | string | No |  |
| `dateUpdated` | string | No |  |
| `attachments` | string | No |  |
| `ssn` | string | No |  |
| `keyword` | string | No |  |
| `firstNameLowerCase` | string | No |  |
| `fullNameLowerCase` | string | No |  |
| `lastNameLowerCase` | string | No |  |
| `lastActivity` | string | No |  |
| `customFields` | array of object | No |  |
| `businessId` | string | No |  |
| `attributionSource` | object | No |  |
| `lastAttributionSource` | object | No |  |
| `visitorId` | string | No | visitorId is the Unique ID assigned to each Live chat visitor. |

### GetCreateUpdateNoteSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `note` | object | No |  |

### GetEventSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `calendarId` | string | No |  |
| `status` | string | No |  |
| `title` | string | No |  |
| `assignedUserId` | string | No |  |
| `notes` | string | No |  |
| `startTime` | string | No |  |
| `endTime` | string | No |  |
| `address` | string | No |  |
| `locationId` | string | No |  |
| `contactId` | string | No |  |
| `groupId` | string | No |  |
| `appointmentStatus` | string | No |  |
| `users` | array of string | No |  |
| `dateAdded` | string | No |  |
| `dateUpdated` | string | No |  |
| `assignedResources` | array of string | No |  |

### GetEventsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `events` | array of object | No |  |

### GetNoteSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `body` | string | No |  |
| `userId` | string | No |  |
| `dateAdded` | string | No |  |
| `contactId` | string | No |  |

### GetNotesListSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notes` | array of object | No |  |

### InboundDndSettingSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | string (enum: `active`, `inactive`) | Yes |  |
| `message` | string | No |  |

### InboundDndSettingsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `all` | object | No |  |

### LargeTextField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | string | No |  |

### MonetoryField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | object | No |  |

### MultiSelectField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | array of string | No |  |

### NotesDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No |  |
| `body` | string | Yes |  |

### NumericField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | object | No |  |

### RadioField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | string | No |  |

### SearchBodyV2DTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### SearchContactSuccessResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contacts` | array of object | Yes |  |
| `total` | number | Yes |  |

### SingleSelectField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | string | No |  |

### TagsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tags` | array of string | Yes |  |

### TaskByIsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `task` | object | No |  |

### TaskSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `title` | string | No |  |
| `body` | string | No |  |
| `assignedTo` | string | No |  |
| `dueDate` | string | No |  |
| `completed` | boolean | No |  |
| `contactId` | string | No |  |

### TasksListSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tasks` | array of object | No |  |

### TextField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | string | No |  |

### UpdateContactDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `inboundDndSettings` | object | No |  |
| `tags` | array of string | No | This field will overwrite all current tags associated with the contact. To update a tags, it is recommended to use the Add Tag or Remove Tag API instead. |
| `customFields` | array of object | object | object | object | object | object | object | object | object | No |  |
| `source` | string | No |  |
| `country` | string | No |  |
| `assignedTo` | string | No | User's Id |

### UpdateContactsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |
| `contact` | object | No |  |

### UpdateTagsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contacts` | array of string | Yes | list of contact ids to be processed |
| `tags` | array of string | Yes | list of tags to be added or removed |
| `locationId` | string | Yes | location id from where the bulk request is executed |
| `removeAllTags` | boolean | No | Option to implement remove all tags. if true, all tags will be removed from the contacts. Can only be used with remove type. |

### UpdateTagsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | Yes | Indicates if the operation was successful |
| `errorCount` | number | Yes | Number of errors encountered during the operation |
| `responses` | array of string | Yes | Responses for each contact processed |

### UpdateTaskBody

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No |  |
| `body` | string | No |  |
| `dueDate` | string | No |  |
| `completed` | boolean | No |  |
| `assignedTo` | string | No |  |

### UpdateTaskStatusParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `completed` | boolean | Yes |  |

### UpsertContactDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `name` | string | No |  |
| `email` | string | No |  |
| `locationId` | string | Yes |  |
| `gender` | string | No |  |
| `phone` | string | No |  |
| `address1` | string | No |  |
| `city` | string | No |  |
| `state` | string | No |  |
| `postalCode` | string | No |  |
| `website` | string | No |  |
| `timezone` | string | No |  |
| `dnd` | boolean | No |  |
| `dndSettings` | object | No |  |
| `inboundDndSettings` | object | No |  |
| `tags` | array of string | No | This field will overwrite all current tags associated with the contact. To update a tags, it is recommended to use the Add Tag or Remove Tag API instead. |
| `customFields` | array of object | object | object | object | object | object | object | object | object | No |  |
| `source` | string | No |  |
| `country` | string | No |  |
| `companyName` | string | No |  |
| `assignedTo` | string | No | User's Id |

### UpsertContactsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `new` | boolean | No |  |
| `contact` | object | No |  |
| `traceId` | string | No |  |

### customFieldsInputArraySchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | array of string | No |  |

### customFieldsInputObjectSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `key` | string | No |  |
| `field_value` | object | No |  |

### customFieldsInputStringSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Pass either `id` or `key` of custom field |
| `key` | string | No | Pass either `id` or `key` of custom field |
| `field_value` | string | No |  |
