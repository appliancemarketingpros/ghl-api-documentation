# Associations API

Documentation for Associations API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Relations](#relations)
- [Associations](#associations)

## Relations

### POST `/associations/relations`

**Create Relation for you associated entities.**

Create Relation.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

**Operation ID:** `create-relation`

**Tags:** Relations

**Required Scopes:** `associations/relation.write`

**External Documentation:** [Click here for more information](https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3)

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Your Sub Account's ID |
| `associationId` | string | Yes | Association's Id |
| `firstRecordId` | string | Yes | First Record's Id. For instance, if you have an association between a contact and a custom object, and you specify the contact as the first object while creating the association, then your firstRecord... |
| `secondRecordId` | string | Yes | Second Record's Id.For instance, if you have an association between a contact and a custom object, and you specify the custom object as the second entity while creating the association, then your seco... |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/associations/relations/{recordId}`

**Get all relations By record Id**

Get all relations by record Id

**Operation ID:** `get-relations-by-record-id`

**Tags:** Relations

**Required Scopes:** `associations/relation.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `recordId` | path | string | Yes |  |
| `locationId` | query | string | Yes | Your Sub Account's ID |
| `skip` | query | number | Yes |  |
| `limit` | query | number | Yes |  |
| `associationIds` | query | array of string | No | Association Ids |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/associations/relations/{relationId}`

**Delete Relation**

Delete Relation

**Operation ID:** `delete-relation`

**Tags:** Relations

**Required Scopes:** `associations/relation.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `relationId` | path | string | Yes |  |
| `locationId` | query | string | Yes | Your Sub Account's ID |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Associations

### GET `/associations/key/{key_name}`

**Get association key by key name**

Using this api you can get standard / user defined association by key

**Operation ID:** `get-association-key-by-key-name`

**Tags:** Associations

**Required Scopes:** `associations.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `key_name` | path | string | Yes |  |
| `locationId` | query | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/associations/objectKey/{objectKey}`

**Get association by object keys**

Get association by object keys like contacts, custom objects and opportunities. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

**Operation ID:** `get-association-by-object-keys`

**Tags:** Associations

**Required Scopes:** `associations.readonly`

**External Documentation:** [Click here for more information](https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3)

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `objectKey` | path | string | No |  |
| `locationId` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/associations/{associationId}`

**Update Association By Id**

Update Association , Allows you to update labels of an associations. Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

**Operation ID:** `update-association`

**Tags:** Associations

**Required Scopes:** `associations.write`

**External Documentation:** [Click here for more information](https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3)

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `associationId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstObjectLabel` | object | Yes |  |
| `secondObjectLabel` | object | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/associations/{associationId}`

**Delete Association**

Delete USER_DEFINED Association By Id, deleting an association will also all the relations for that association

**Operation ID:** `delete-association`

**Tags:** Associations

**Required Scopes:** `associations.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `associationId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `deleted` | boolean | Yes | Deletion status |
| `id` | string | Yes | Association Id |
| `message` | string | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/associations/{associationId}`

**Get association by ID**

Using this api you can get SYSTEM_DEFINED / USER_DEFINED association by id 

**Operation ID:** `get-association-by-ID`

**Tags:** Associations

**Required Scopes:** `associations.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `associationId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/associations/`

**Create Association**

Allow you to create contact - contact , contact - custom objects associations, will add more in the future.Documentation Link - https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3

**Operation ID:** `create-association`

**Tags:** Associations

**Required Scopes:** `associations.write`

**External Documentation:** [Click here for more information](https://doc.clickup.com/8631005/d/h/87cpx-293776/cd0f4122abc04d3)

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `key` | string | Yes | Association's Unique key |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/associations/`

**Get all associations for a sub-account / location**

Get all Associations

**Operation ID:** `find-associations`

**Tags:** Associations

**Required Scopes:** `associations.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `skip` | query | number | Yes |  |
| `limit` | query | number | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### DeleteAssociationsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `deleted` | boolean | Yes | Deletion status |
| `id` | string | Yes | Association Id |
| `message` | string | Yes |  |

### GetPostSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |
| `associationType` | object | Yes | Association Type can be USER_DEFINED or SYSTEM_DEFINED |

### UpdateAssociationReqDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstObjectLabel` | object | Yes |  |
| `secondObjectLabel` | object | Yes |  |

### createAssociationReqDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `key` | string | Yes | Association's Unique key |
| `firstObjectLabel` | object | Yes | First Objects Association Label (custom_objects.children) |
| `firstObjectKey` | object | Yes | First Objects Key |
| `secondObjectLabel` | object | Yes | Second Object Association Label (contact) |
| `secondObjectKey` | object | Yes | Second Objects Key |

### createRelationReqDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Your Sub Account's ID |
| `associationId` | string | Yes | Association's Id |
| `firstRecordId` | string | Yes | First Record's Id. For instance, if you have an association between a contact and a custom object, and you specify the contact as the first object while creating the association, then your firstRecord... |
| `secondRecordId` | string | Yes | Second Record's Id.For instance, if you have an association between a contact and a custom object, and you specify the custom object as the second entity while creating the association, then your seco... |
