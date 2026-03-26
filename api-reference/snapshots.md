# Snapshots API

Documentation for Snapshots API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Snapshots](#snapshots)

## Snapshots

### GET `/snapshots/`

**Get Snapshots**

Get a list of all own and imported Snapshots

**Operation ID:** `get-custom-snapshots`

**Tags:** Snapshots

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `companyId` | query | string | Yes | Company Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `snapshots` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/snapshots/share/link`

**Create Snapshot Share Link**

Create a share link for snapshot

**Operation ID:** `create-snapshot-share-link`

**Tags:** Snapshots

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `companyId` | query | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `snapshot_id` | string | Yes | id for snapshot to be shared |
| `share_type` | string (enum: `link`, `permanent_link`, `agency_link`, `location_link`) | Yes | Type of share link to generate |
| `relationship_number` | string | No | Comma separated Relationship number of Agencies to create agency restricted share link |
| `share_location_id` | string | No | Comma separated Sub-Account ids to create sub-account restricted share link |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | id for shared snapshot |
| `shareLink` | string | No | Share Link for snapshot |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/snapshots/snapshot-status/{snapshotId}`

**Get Snapshot Push between Dates**

Get list of sub-accounts snapshot pushed in time period

**Operation ID:** `get-snapshot-push`

**Tags:** Snapshots

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `snapshotId` | path | string | Yes |  |
| `companyId` | query | string | Yes |  |
| `from` | query | string | Yes |  |
| `to` | query | string | Yes |  |
| `lastDoc` | query | string | Yes | Id for last document till what you want to skip |
| `limit` | query | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/snapshots/snapshot-status/{snapshotId}/location/{locationId}`

**Get Last Snapshot Push**

Get Latest Snapshot Push Status for a location id

**Operation ID:** `get-latest-snapshot-push`

**Tags:** Snapshots

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `companyId` | query | string | Yes |  |
| `snapshotId` | path | string | Yes |  |
| `locationId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Schemas

### CreateSnapshotShareLinkRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `snapshot_id` | string | Yes | id for snapshot to be shared |
| `share_type` | string (enum: `link`, `permanent_link`, `agency_link`, `location_link`) | Yes | Type of share link to generate |
| `relationship_number` | string | No | Comma separated Relationship number of Agencies to create agency restricted share link |
| `share_location_id` | string | No | Comma separated Sub-Account ids to create sub-account restricted share link |

### CreateSnapshotShareLinkSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | id for shared snapshot |
| `shareLink` | string | No | Share Link for snapshot |

### GetLatestSnapshotPushStatusSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | No |  |

### GetSnapshotPushStatusSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | No |  |

### GetSnapshotsSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `snapshots` | array of object | No |  |

### SnapshotStatusSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Document id |
| `locationId` | string | No | Sub-account id |
| `status` | string | No | Status of snapshot push |
| `dateAdded` | string | No | Timestamp of when snapshot processing starts for sub-account  |

### SnapshotStatusSchemaWithAssets

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Document id |
| `locationId` | string | No | Sub-account id |
| `status` | string | No | Status of snapshot push |
| `completed` | array of string | No | List of completed assets |
| `pending` | array of string | No | List of pending assets |

### SnapshotsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Snapshot Id. |
| `name` | string | No | Name of the snapshot |
| `type` | string | No | Type of snapshot - own or imported. |
