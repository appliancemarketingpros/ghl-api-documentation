# Custom Menus API

Documentation for Custom menus API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Custom Menu Links](#custom-menu-links)

## Custom Menu Links

### GET `/custom-menus/{customMenuId}`

**Get Custom Menu Link**

Fetches a single custom menus based on id. This endpoint allows clients to retrieve custom menu configurations, which may include menu items, categories, and associated metadata

**Operation ID:** `get-custom-menu-by-id`

**Tags:** Custom Menu Links

**Required Scopes:** `custom-menu-link.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `customMenuId` | path | string | Yes | Unique identifier of the custom menu |

#### Responses

**`200` - Successfully retrieved custom menu. Returns a single custom menu object, potentially including its structure, items, and relevant metadata.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customMenu` | object | No |  |

**`400` - Bad Request. Invalid query parameters provided.**

**`401` - Unauthorized**

**`403` - Forbidden. The client does not have necessary permissions to access custom menu.**

**`422` - Unprocessable Entity**

---

### DELETE `/custom-menus/{customMenuId}`

**Delete Custom Menu Link**

Removes a specific custom menu from the system. This operation requires authentication and proper permissions. The custom menu is identified by its unique ID, and the operation is performed within the context of a specific company.

**Operation ID:** `delete-custom-menu`

**Tags:** Custom Menu Links

**Required Scopes:** `custom-menu-link.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `customMenuId` | path | string | Yes | ID of the custom menu to delete |

#### Responses

**`200` - Custom menu successfully deleted**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Indicates whether the custom menu was successfully deleted |
| `message` | string | No | A message providing additional information about the deletion operation |
| `deletedMenuId` | string | No | The ID of the deleted custom menu |
| `deletedAt` | string | No | Timestamp of when the deletion was performed |

**`400` - Bad Request. Invalid parameters provided.**

**`401` - Unauthorized**

**`403` - Forbidden. The client does not have necessary permissions to delete this custom menu.**

**`404` - Not Found. The specified custom menu does not exist or has already been deleted.**

**`422` - Unprocessable Entity**

---

### PUT `/custom-menus/{customMenuId}`

**Update Custom Menu Link**

Updates an existing custom menu for a given company. Requires authentication and proper permissions.

**Operation ID:** `update-custom-menu`

**Tags:** Custom Menu Links

**Required Scopes:** `custom-menu-link.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `customMenuId` | path | string | Yes | ID of the custom menu to update |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title of the custom menu |
| `url` | string | No | URL of the custom menu |
| `icon` | object | No |  |
| `showOnCompany` | boolean | No | Whether the menu must be displayed on the agency's level Default: `True` |
| `showOnLocation` | boolean | No | Whether the menu must be displayed for sub-accounts level Default: `True` |
| `showToAllLocations` | boolean | No | Whether the menu must be displayed to all sub-accounts Default: `True` |
| `openMode` | string (enum: `iframe`, `new_tab`, `current_tab`) | No | Mode for opening the menu link |
| `locations` | array of string | No | List of sub-account IDs where the menu should be shown. This list is applicable only when showOnLocation is true and showToAllLocations is false |
| `userRole` | string (enum: `all`, `admin`, `user`) | No | Which user-roles should the menu be accessible to? |
| `allowCamera` | boolean | No | Whether to allow camera access (only for iframe mode) |
| `allowMicrophone` | boolean | No | Whether to allow microphone access (only for iframe mode) |

**`icon` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the icon |
| `fontFamily` | string (enum: `fab`, `fas`, `far`) | No | Font family of the icon |

#### Responses

**`200` - Custom menu successfully updated**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Status of update |
| `customMenu` | object | No |  |

**`400` - Bad Request - Invalid input**

**`401` - Unauthorized**

**`403` - Forbidden - Insufficient permissions**

**`404` - Not Found - Custom menu or company not found**

**`422` - Unprocessable Entity**

---

### GET `/custom-menus/`

**Get Custom Menu Links**

Fetches a collection of custom menus based on specified criteria. This endpoint allows clients to retrieve custom menu configurations, which may include menu items, categories, and associated metadata. The response can be tailored using query parameters for filtering, sorting, and pagination.

**Operation ID:** `get-custom-menus`

**Tags:** Custom Menu Links

**Required Scopes:** `custom-menu-link.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | No | Unique identifier of the location |
| `skip` | query | number | No | Number of items to skip for pagination |
| `limit` | query | number | No | Maximum number of items to return |
| `query` | query | string | No | Search query to filter custom menus by name, supports partial \|\| full names |
| `showOnCompany` | query | boolean | No | Filter to show only agency-level menu links. When omitted, fetches both agency and sub-account menu links. Ignored if locationId is provided |

#### Responses

**`200` - Successfully retrieved custom menus. Returns an array of custom menu objects, potentially including their structure, items, and relevant metadata.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customMenus` | array of object | No | Array of custom menu links |
| `totalLinks` | number | No | Total number of custom menu records |

**`400` - Bad Request. Invalid query parameters provided.**

**`401` - Unauthorized**

**`403` - Forbidden. The client does not have necessary permissions to access custom menus.**

**`422` - Unprocessable Entity**

---

### POST `/custom-menus/`

**Create Custom Menu Link**

Creates a new custom menu for a company. Requires authentication and proper permissions. For Icon Usage Details please refer to  https://doc.clickup.com/8631005/d/h/87cpx-243696/d60fa70db6b92b2

**Operation ID:** `create-custom-menu`

**Tags:** Custom Menu Links

**Required Scopes:** `custom-menu-link.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Title of the custom menu |
| `url` | string | Yes | URL of the custom menu |
| `icon` | object | Yes |  |
| `showOnCompany` | boolean | Yes | Whether the menu must be displayed on the agency's level Default: `True` |
| `showOnLocation` | boolean | Yes | Whether the menu must be displayed for sub-accounts level Default: `True` |
| `showToAllLocations` | boolean | Yes | Whether the menu must be displayed to all sub-accounts Default: `True` |
| `openMode` | string (enum: `iframe`, `new_tab`, `current_tab`) | Yes | Mode for opening the menu link |
| `locations` | array of string | Yes | List of sub-account IDs where the menu should be shown. This list is applicable only when showOnLocation is true and showToAllLocations is false |
| `userRole` | string (enum: `all`, `admin`, `user`) | Yes | Which user-roles should the menu be accessible to? |
| `allowCamera` | boolean | No | Whether to allow camera access (only for iframe mode) |
| `allowMicrophone` | boolean | No | Whether to allow microphone access (only for iframe mode) |

**`icon` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the icon |
| `fontFamily` | string (enum: `fab`, `fas`, `far`) | Yes | Font family of the icon |

#### Responses

**`201` - Custom menu successfully created**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customMenu` | object | No |  |

**`400` - Bad Request - Invalid input**

**`401` - Unauthorized**

**`403` - Forbidden - Insufficient permissions**

**`422` - Unprocessable Entity**

---

## Schemas

### CreateCustomMenuDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | Title of the custom menu |
| `url` | string | Yes | URL of the custom menu |
| `icon` | object | Yes |  |
| `showOnCompany` | boolean | Yes | Whether the menu must be displayed on the agency's level Default: `True` |
| `showOnLocation` | boolean | Yes | Whether the menu must be displayed for sub-accounts level Default: `True` |
| `showToAllLocations` | boolean | Yes | Whether the menu must be displayed to all sub-accounts Default: `True` |
| `openMode` | string (enum: `iframe`, `new_tab`, `current_tab`) | Yes | Mode for opening the menu link |
| `locations` | array of string | Yes | List of sub-account IDs where the menu should be shown. This list is applicable only when showOnLocation is true and showToAllLocations is false |
| `userRole` | string (enum: `all`, `admin`, `user`) | Yes | Which user-roles should the menu be accessible to? |
| `allowCamera` | boolean | No | Whether to allow camera access (only for iframe mode) |
| `allowMicrophone` | boolean | No | Whether to allow microphone access (only for iframe mode) |

### CustomMenuSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Unique identifier for the custom menu |
| `icon` | object | No |  |
| `title` | string | No | Title of the custom menu |
| `url` | string | No | URL of the custom menu |
| `order` | number | No | Order of the custom menu |
| `showOnCompany` | boolean | No | Filter to show only agency-level menu links. When omitted, fetches both agency and sub-account menu links. Ignored if locationId is provided |
| `showOnLocation` | boolean | No | Whether the menu must be displayed for sub-accounts level |
| `showToAllLocations` | boolean | No | Whether the menu must be displayed to all sub-accounts |
| `locations` | array of string | No | List of sub-account IDs where the menu should be shown. This list is applicable only when showOnLocation is true and showToAllLocations is false |
| `openMode` | string (enum: `iframe`, `new_tab`, `current_tab`) | No | Mode for opening the menu link |
| `userRole` | string (enum: `all`, `admin`, `user`) | No | Which user-roles should the menu be accessible to? |
| `allowCamera` | boolean | No | Indicates if camera access is allowed for this menu |
| `allowMicrophone` | boolean | No | Indicates if microphone access is allowed for this menu |

### DeleteCustomMenuSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Indicates whether the custom menu was successfully deleted |
| `message` | string | No | A message providing additional information about the deletion operation |
| `deletedMenuId` | string | No | The ID of the deleted custom menu |
| `deletedAt` | string | No | Timestamp of when the deletion was performed |

### GetCustomMenusResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customMenus` | array of object | No | Array of custom menu links |
| `totalLinks` | number | No | Total number of custom menu records |

### GetSingleCustomMenusSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `customMenu` | object | No |  |

### IconSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the icon |
| `fontFamily` | string (enum: `fab`, `fas`, `far`) | Yes | Font family of the icon |

### IconSchemaOptional

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the icon |
| `fontFamily` | string (enum: `fab`, `fas`, `far`) | No | Font family of the icon |

### UpdateCustomMenuDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title of the custom menu |
| `url` | string | No | URL of the custom menu |
| `icon` | object | No |  |
| `showOnCompany` | boolean | No | Whether the menu must be displayed on the agency's level Default: `True` |
| `showOnLocation` | boolean | No | Whether the menu must be displayed for sub-accounts level Default: `True` |
| `showToAllLocations` | boolean | No | Whether the menu must be displayed to all sub-accounts Default: `True` |
| `openMode` | string (enum: `iframe`, `new_tab`, `current_tab`) | No | Mode for opening the menu link |
| `locations` | array of string | No | List of sub-account IDs where the menu should be shown. This list is applicable only when showOnLocation is true and showToAllLocations is false |
| `userRole` | string (enum: `all`, `admin`, `user`) | No | Which user-roles should the menu be accessible to? |
| `allowCamera` | boolean | No | Whether to allow camera access (only for iframe mode) |
| `allowMicrophone` | boolean | No | Whether to allow microphone access (only for iframe mode) |

### UpdateCustomMenuLinkResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Status of update |
| `customMenu` | object | No |  |
