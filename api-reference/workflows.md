# Workflows API

Documentation for workflows API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Workflows](#workflows)

## Workflows

### GET `/workflows/`

**Get Workflow**

Get Workflow

**Operation ID:** `get-workflow`

**Tags:** Workflows

**Required Scopes:** `workflows.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `workflows` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### GetWorkflowSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `workflows` | array of object | No |  |

### WorkflowSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `status` | string | No |  |
| `version` | number | No |  |
| `createdAt` | string | No |  |
| `updatedAt` | string | No |  |
| `locationId` | string | No |  |
