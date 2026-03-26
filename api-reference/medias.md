# Media Library API

Documentation for Files API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Medias](#medias)

## Medias

### GET `/medias/files`

**Get List of Files/ Folders**

Fetches list of files and folders from the media library

**Operation ID:** `fetch-media-content`

**Tags:** Medias

**Required Scopes:** `medias.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `offset` | query | string | No | Number of files to skip in listing |
| `limit` | query | string | No | Number of files to show in the listing |
| `sortBy` | query | string | Yes | Field to sorting the file listing by |
| `sortOrder` | query | string | Yes | Direction in which file needs to be sorted |
| `type` | query | string | Yes | Type |
| `query` | query | string | No | Query text |
| `altType` | query | string (enum: `location`) | Yes | AltType |
| `altId` | query | string | Yes | location Id |
| `parentId` | query | string | No | parent id or folder id |
| `fetchAll` | query | string | No | Fetch all files or folders |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `files` | array of string | Yes | Array of File Objects |

---

### POST `/medias/upload-file`

**Upload File into Media Library**

If hosted is set to true then fileUrl is required. Else file is required. If adding a file, maximum allowed is 25 MB

**Operation ID:** `upload-media-content`

**Tags:** Medias

**Required Scopes:** `medias.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `multipart/form-data`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `file` | string | No |  |
| `hosted` | boolean | No |  |
| `fileUrl` | string | No |  |
| `name` | string | No |  |
| `parentId` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fileId` | string | Yes | ID of the uploaded file |
| `url` | string | Yes | Google Cloud Storage URL of the uploaded file |

---

### DELETE `/medias/{id}`

**Delete File or Folder**

Deletes specific file or folder from the media library

**Operation ID:** `delete-media-content`

**Tags:** Medias

**Required Scopes:** `medias.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |
| `altType` | query | string (enum: `location`) | Yes | AltType |
| `altId` | query | string | Yes | location Id |

#### Responses

**`200` - Successful response**

---

### POST `/medias/{id}`

**Update File/ Folder**

Updates a single file or folder by ID

**Operation ID:** `update-media-object`

**Tags:** Medias

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Unique identifier of the file or folder to update |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | New name for the file or folder |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the file or folder |
| `altId` | string | Yes | Location identifier that owns the file or folder |

#### Responses

**`200` - Successful response**

---

### POST `/medias/folder`

**Create Folder**

Creates a new folder in the media library

**Operation ID:** `create-media-folder`

**Tags:** Medias

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id |
| `altType` | string (enum: `location`) | Yes | Type of entity (location only) |
| `name` | string | Yes | Name of the folder to be created |
| `parentId` | string | No | ID of the parent folder (optional) |

#### Responses

**`200` - Returns the newly created folder object**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location identifier that owns this folder |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the folder |
| `name` | string | Yes | Name of the folder |
| `parentId` | string | No | ID of the parent folder (null for root folders) |
| `type` | string | Yes | Type of the object (always 'folder' for folders) |
| `deleted` | boolean | No | Whether the folder has been deleted |
| `pendingUpload` | boolean | No | Whether there are pending uploads to this folder |
| `category` | string | No | Primary category of content stored in the folder |
| `subCategory` | string | No | Sub-category of content stored in the folder |
| `isPrivate` | boolean | No | Whether the folder is private and not publicly accessible |
| `relocatedFolder` | boolean | No | Whether the folder has been moved from its original location |
| `migrationCompleted` | boolean | No | Whether the data migration process has been completed for this folder |
| `appFolder` | boolean | No | Whether this is a system-generated application folder |
| `isEssential` | boolean | No | Whether the folder is essential and should not be deleted |
| `status` | string | No | Current status of the folder |
| `lastUpdatedBy` | string | No | ID of the user who last updated the folder |

---

### PUT `/medias/update-files`

**Bulk Update Files/ Folders**

Updates metadata or status of multiple files and folders

**Operation ID:** `bulk-update-media-objects`

**Tags:** Medias

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location identifier |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the files |
| `filesToBeUpdated` | array of object | Yes | Array of file objects to be updated |

**`filesToBeUpdated` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the file or folder to be updated |
| `name` | string | No | New name for the file or folder |

#### Responses

**`200` - Successful response**

---

### PUT `/medias/delete-files`

**Bulk Delete / Trash Files or Folders**

Soft-deletes or trashes multiple files and folders in a single request

**Operation ID:** `bulk-delete-media-objects`

**Tags:** Medias

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `filesToBeDeleted` | array of object | Yes | Array of file objects to be deleted or trashed |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the files |
| `altId` | string | Yes | Location identifier |
| `status` | string (enum: `deleted`, `trashed`) | Yes | Status to set for the files (deleted or trashed) |

**`filesToBeDeleted` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Unique identifier of the file or folder to be deleted |

#### Responses

**`200` - Successful response**

---

## Schemas

### CreateFolderParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id |
| `altType` | string (enum: `location`) | Yes | Type of entity (location only) |
| `name` | string | Yes | Name of the folder to be created |
| `parentId` | string | No | ID of the parent folder (optional) |

### DeleteMediaObjectItem

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Unique identifier of the file or folder to be deleted |

### DeleteMediaObjectsBodyParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `filesToBeDeleted` | array of object | Yes | Array of file objects to be deleted or trashed |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the files |
| `altId` | string | Yes | Location identifier |
| `status` | string (enum: `deleted`, `trashed`) | Yes | Status to set for the files (deleted or trashed) |

### FolderDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location identifier that owns this folder |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the folder |
| `name` | string | Yes | Name of the folder |
| `parentId` | string | No | ID of the parent folder (null for root folders) |
| `type` | string | Yes | Type of the object (always 'folder' for folders) |
| `deleted` | boolean | No | Whether the folder has been deleted |
| `pendingUpload` | boolean | No | Whether there are pending uploads to this folder |
| `category` | string | No | Primary category of content stored in the folder |
| `subCategory` | string | No | Sub-category of content stored in the folder |
| `isPrivate` | boolean | No | Whether the folder is private and not publicly accessible |
| `relocatedFolder` | boolean | No | Whether the folder has been moved from its original location |
| `migrationCompleted` | boolean | No | Whether the data migration process has been completed for this folder |
| `appFolder` | boolean | No | Whether this is a system-generated application folder |
| `isEssential` | boolean | No | Whether the folder is essential and should not be deleted |
| `status` | string | No | Current status of the folder |
| `lastUpdatedBy` | string | No | ID of the user who last updated the folder |

### GetFilesResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `files` | array of string | Yes | Array of File Objects |

### MoveOrDeleteObjectParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altType` | string | Yes |  |
| `altId` | string | Yes |  |
| `_id` | string | Yes |  |

### UpdateMediaObject

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the file or folder to be updated |
| `name` | string | No | New name for the file or folder |

### UpdateMediaObjects

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location identifier |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the files |
| `filesToBeUpdated` | array of object | Yes | Array of file objects to be updated |

### UpdateObject

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | New name for the file or folder |
| `altType` | string (enum: `location`) | Yes | Type of entity that owns the file or folder |
| `altId` | string | Yes | Location identifier that owns the file or folder |

### UploadFileResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fileId` | string | Yes | ID of the uploaded file |
| `url` | string | Yes | Google Cloud Storage URL of the uploaded file |
