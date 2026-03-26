# Common Schemas

Shared schema definitions used across multiple GoHighLevel API endpoints.

## BadRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

## UnauthorizedDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |
| `error` | string | No |  |

## UnprocessableDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | array | No |  |
| `error` | string | No |  |
