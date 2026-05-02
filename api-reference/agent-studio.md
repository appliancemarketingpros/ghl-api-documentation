# Agent Studio API

Documentation for Agent Studio APIs

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Agents](#agents)

## Agents

### POST `/agent-studio/agent`

**Create Agent**

Creates a new agent with staging version. The agent will be created with an initial staging version that can later be promoted to production. 

**Operation ID:** `createAgent`

**Tags:** Agents

**Required Scopes:** `agent-studio.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `source` | query | string | No |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID |
| `name` | string | No | Name of the agent |
| `description` | string | No | Description of the agent |
| `agencyId` | string | No | Agency ID |
| `authorId` | string | No | Author ID |
| `authorName` | string | No | Author name |
| `authorEmail` | string | No | Author email |
| `status` | string (enum: `active`, `inactive`, `archived`) | Yes | Status of the agent |
| `version` | object | Yes | Version data for the agent including nodes, edges, and configuration |
| `nodes` | array of string | No | Nodes array (deprecated, prefer using version.nodes) |
| `edges` | array of string | No | Edges array (deprecated, prefer using version.edges) |

#### Responses

**`201` - Agent created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agent` | object | Yes | Created agent data with metadata |
| `versions` | array of any | Yes | Created versions array (initial staging version) |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### GET `/agent-studio/agent`

**List Agents**

Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset. Optionally filter by isPublished=true to return only agents with a published production version.

**Operation ID:** `getAgents`

**Tags:** Agents

**Required Scopes:** `agent-studio.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `isPublished` | query | string | No | Optional filter to return only agents with a published production version |
| `limit` | query | string | Yes |  |
| `offset` | query | string | Yes |  |
| `source` | query | string | No |  |

#### Responses

**`200` - Agents retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agents` | array of object | Yes | List of agents with metadata |
| `pagination` | object | Yes | Pagination metadata |

**`400` - Bad Request - locationId is required**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### PATCH `/agent-studio/agent/versions/{versionId}`

**Update Agent**

Updates a specific agent version by versionId. Supports updating nodes, edges, variables, and configuration. 

**Operation ID:** `updateAgentVersion`

**Tags:** Agents

**Required Scopes:** `agent-studio.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `versionId` | path | string | Yes |  |
| `source` | query | string | No |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID for authorization |
| `versionName` | string | No | Version name |
| `description` | string | No | Description of the version |
| `nodes` | array of object | No | Complete array of nodes for the agent workflow. Provide all nodes including unchanged ones. |
| `edges` | array of object | No | Complete array of edges connecting the nodes. Provide all edges including unchanged ones. |
| `globalVariables` | array of object | No | Global variables accessible throughout the agent workflow |
| `inputVariables` | array of object | No | Input variables required from user at execution time |
| `runtimeVariables` | array of object | No | Runtime variables generated during agent execution |
| `globalConfig` | object | No | Global configuration including prompts and settings |
| `userId` | string | No | User ID performing the update |
| `userName` | string | No | User name performing the update |

#### Responses

**`200` - Version updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `data` | object | Yes | Updated agent or version data |

**`400` - Bad Request**

**`401` - Unauthorized**

**`404` - Version not found**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### PATCH `/agent-studio/agent/{agentId}`

**Update Agent Metadata**

Updates agent metadata such as name, description, and status. 

**Operation ID:** `updateAgentMetadata`

**Tags:** Agents

**Required Scopes:** `agent-studio.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |
| `source` | query | string | No |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID for authorization (cannot be updated) |
| `name` | string | No | Name of the agent |
| `description` | string | No | Description of the agent |
| `status` | string (enum: `active`, `inactive`, `archived`) | No | Status of the agent |

#### Responses

**`200` - Agent metadata updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `data` | object | Yes | Updated agent or version data |

**`400` - Bad Request**

**`401` - Unauthorized**

**`404` - Agent not found**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### DELETE `/agent-studio/agent/{agentId}`

**Delete Agent**

Deletes an agent and all its versions. 

**Operation ID:** `deleteAgent`

**Tags:** Agents

**Required Scopes:** `agent-studio.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |
| `locationId` | query | string | Yes |  |
| `source` | query | string | No |  |

#### Responses

**`200` - Agent deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agentId` | string | No | Deleted agent ID |

**`400` - Bad Request**

**`401` - Unauthorized**

**`404` - Agent not found**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### GET `/agent-studio/agent/{agentId}`

**Get Agent**

Gets a specific agent by its ID for the specified location with all its versions. Returns complete agent metadata and all non-deleted versions (draft, staging, production). locationId is required parameter. The agent must have active status.

**Operation ID:** `getAgentById`

**Tags:** Agents

**Required Scopes:** `agent-studio.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |
| `locationId` | query | string | Yes |  |
| `source` | query | string | No |  |

#### Responses

**`200` - Agent retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agent` | object | Yes | Agent metadata with all active versions |
| `traceId` | string | No | Request trace ID for debugging |

**`400` - Bad Request - locationId is required**

**`401` - Unauthorized**

**`404` - Agent not found or not available**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/agent-studio/agent/versions/{versionId}/publish`

**Promote to Production**

Promotes a draft version to production.

**Operation ID:** `promoteAndPublish`

**Tags:** Agents

**Required Scopes:** `agent-studio.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `versionId` | path | string | Yes |  |
| `source` | query | string | No |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID for authorization |
| `userId` | string | No | User ID performing the promotion action |
| `userName` | string | No | User name performing the promotion action |
| `userEmail` | string | No | User email performing the promotion action |

#### Responses

**`200` - Version promoted and published successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `data` | object | Yes | Result data with production and new draft version details |

**`400` - Bad Request - Only draft versions can be promoted**

**`401` - Unauthorized**

**`404` - Version not found**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/agent-studio/agent/{agentId}/execute`

**Execute Agent**

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body. 

**Session Management:**
- For the first message in a new session, do not include the `executionId` in the request payload.
- The API will return an `executionId` along with the agent response, which uniquely identifies this conversation session.
- To continue the conversation within the same session, include the `executionId` from the previous response in subsequent requests. This allows the agent to maintain conversation context and history across multiple interactions.

**Operation ID:** `executeAgent`

**Tags:** Agents

**Required Scopes:** `agent-studio.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |
| `source` | query | string | No |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Message to send to the agent |
| `executionId` | string | No | Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Omit this field for the first message in a new session. Include the executio... |
| `inputVariables` | object | No | Input variables to pass to the agent. These should match the input variables defined in the agent configuration. |
| `versionId` | string | No | Published version ID to execute. If not provided, the latest published production version will be used. |
| `attachments` | array of object | No | Attachments for the message |
| `locationId` | string | Yes | Location ID |
| `contactId` | string | No | Contact ID to associate with this execution. When provided, contact data will be hydrated and made available to the agent. |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | Yes | Type of attachment |
| `imageUrl` | string | Yes | URL of the image attachment |

#### Responses

**`200` - Agent executed successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `executionId` | string | Yes | Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Use this ID in subsequent requests to continue the conversation. |
| `interactionId` | string | Yes | Unique identifier for a single interaction cycle, consisting of one user input and the corresponding agent response. Each message exchange generates a new interactionId. |
| `response` | string | Yes | Agent response text |
| `type` | string | Yes | Response type |
| `nextExpectedInput` | string | Yes | Expected input type for next interaction |
| `goalCompletion` | boolean | Yes | When end node is added in the graph, this will be true if the agent reached the end node in the graph |
| `executionStatus` | string | Yes | Execution status |
| `flowSwitch` | boolean | Yes | Whether flow was switched |
| `attachments` | array of any | Yes | Response attachments |
| `generativeOutputs` | array of any | Yes | Generated outputs |

**`400` - Agent is not active or invalid request - locationId is required**

**`401` - Unauthorized**

**`403` - User does not have required scopes to execute this agent**

**`404` - Agent not found**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### GET `/agent-studio/public-api/agents`

**List Agents (Deprecated)**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

**Deprecated endpoint - use GET /agent instead.**

Lists all active agents that have a published production version for the specified location. locationId is required parameter. Supports pagination using limit and offset.

**Operation ID:** `getAgents-deprecated`

**Tags:** Agents

**Required Scopes:** `agent-studio.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `limit` | query | string | Yes |  |
| `offset` | query | string | Yes |  |
| `source` | query | string | No |  |

#### Responses

**`200` - Agents retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agents` | array of object | Yes | List of agents with metadata |
| `pagination` | object | Yes | Pagination metadata |

**`400` - Bad Request - locationId is required**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### GET `/agent-studio/public-api/agents/{agentId}`

**Get Agent (Deprecated)**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

**Deprecated endpoint - use GET /agent/:agentId instead.**

Gets a specific agent by its ID for the specified location with all its versions. locationId is required parameter. The agent must have active status.

**Operation ID:** `getAgentById-deprecated`

**Tags:** Agents

**Required Scopes:** `agent-studio.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |
| `locationId` | query | string | Yes |  |
| `source` | query | string | No |  |

#### Responses

**`200` - Agent retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agent` | object | Yes | Agent metadata with all active versions |
| `traceId` | string | No | Request trace ID for debugging |

**`400` - Bad Request - locationId is required**

**`401` - Unauthorized**

**`404` - Agent not found or not available**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

### POST `/agent-studio/public-api/agents/{agentId}/execute`

**Execute Agent (Deprecated)**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

**Deprecated endpoint - use POST /agent/:agentId/execute instead.**

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body. 

**Session Management:**
- For the first message in a new session, do not include the `executionId` in the request payload.
- The API will return an `executionId` along with the agent response, which uniquely identifies this conversation session.
- To continue the conversation within the same session, include the `executionId` from the previous response in subsequent requests.

**Operation ID:** `executeAgent-deprecated`

**Tags:** Agents

**Required Scopes:** `agent-studio.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |
| `source` | query | string | No |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Message to send to the agent |
| `executionId` | string | No | Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Omit this field for the first message in a new session. Include the executio... |
| `inputVariables` | object | No | Input variables to pass to the agent. These should match the input variables defined in the agent configuration. |
| `versionId` | string | No | Published version ID to execute. If not provided, the latest published production version will be used. |
| `attachments` | array of object | No | Attachments for the message |
| `locationId` | string | Yes | Location ID |
| `contactId` | string | No | Contact ID to associate with this execution. When provided, contact data will be hydrated and made available to the agent. |

**`attachments` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | Yes | Type of attachment |
| `imageUrl` | string | Yes | URL of the image attachment |

#### Responses

**`200` - Agent executed successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `executionId` | string | Yes | Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Use this ID in subsequent requests to continue the conversation. |
| `interactionId` | string | Yes | Unique identifier for a single interaction cycle, consisting of one user input and the corresponding agent response. Each message exchange generates a new interactionId. |
| `response` | string | Yes | Agent response text |
| `type` | string | Yes | Response type |
| `nextExpectedInput` | string | Yes | Expected input type for next interaction |
| `goalCompletion` | boolean | Yes | When end node is added in the graph, this will be true if the agent reached the end node in the graph |
| `executionStatus` | string | Yes | Execution status |
| `flowSwitch` | boolean | Yes | Whether flow was switched |
| `attachments` | array of any | Yes | Response attachments |
| `generativeOutputs` | array of any | Yes | Generated outputs |

**`400` - Agent is not active or invalid request - locationId is required**

**`401` - Unauthorized**

**`403` - User does not have required scopes to execute this agent**

**`404` - Agent not found**

**`422` - Unprocessable Entity**

**`500` - Internal Server Error**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

---

## Schemas

### CreatePublicAgentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID |
| `name` | string | No | Name of the agent |
| `description` | string | No | Description of the agent |
| `agencyId` | string | No | Agency ID |
| `authorId` | string | No | Author ID |
| `authorName` | string | No | Author name |
| `authorEmail` | string | No | Author email |
| `status` | string (enum: `active`, `inactive`, `archived`) | Yes | Status of the agent |
| `version` | object | Yes | Version data for the agent including nodes, edges, and configuration |
| `nodes` | array of string | No | Nodes array (deprecated, prefer using version.nodes) |
| `edges` | array of string | No | Edges array (deprecated, prefer using version.edges) |

### CreatePublicAgentResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agent` | object | Yes | Created agent data with metadata |
| `versions` | array of any | Yes | Created versions array (initial staging version) |

### DeletePublicAgentResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agentId` | string | No | Deleted agent ID |

### ExecutePublicAgentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Message to send to the agent |
| `executionId` | string | No | Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Omit this field for the first message in a new session. Include the executio... |
| `inputVariables` | object | No | Input variables to pass to the agent. These should match the input variables defined in the agent configuration. |
| `versionId` | string | No | Published version ID to execute. If not provided, the latest published production version will be used. |
| `attachments` | array of object | No | Attachments for the message |
| `locationId` | string | Yes | Location ID |
| `contactId` | string | No | Contact ID to associate with this execution. When provided, contact data will be hydrated and made available to the agent. |

### ExecutePublicAgentResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `executionId` | string | Yes | Unique session identifier that maintains conversational context across multiple interactions within the same agent session. Use this ID in subsequent requests to continue the conversation. |
| `interactionId` | string | Yes | Unique identifier for a single interaction cycle, consisting of one user input and the corresponding agent response. Each message exchange generates a new interactionId. |
| `response` | string | Yes | Agent response text |
| `type` | string | Yes | Response type |
| `nextExpectedInput` | string | Yes | Expected input type for next interaction |
| `goalCompletion` | boolean | Yes | When end node is added in the graph, this will be true if the agent reached the end node in the graph |
| `executionStatus` | string | Yes | Execution status |
| `flowSwitch` | boolean | Yes | Whether flow was switched |
| `attachments` | array of any | Yes | Response attachments |
| `generativeOutputs` | array of any | Yes | Generated outputs |

### GetAgentByIdResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agent` | object | Yes | Agent metadata with all active versions |
| `traceId` | string | No | Request trace ID for debugging |

### GetPublishedAgentsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `agents` | array of object | Yes | List of agents with metadata |
| `pagination` | object | Yes | Pagination metadata |

### InternalServerErrorDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusCode` | number | No |  |
| `message` | string | No |  |

### PromoteAndPublishDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID for authorization |
| `userId` | string | No | User ID performing the promotion action |
| `userName` | string | No | User name performing the promotion action |
| `userEmail` | string | No | User email performing the promotion action |

### PromoteAndPublishResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `data` | object | Yes | Result data with production and new draft version details |

### PublicAttachmentSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | Yes | Type of attachment |
| `imageUrl` | string | Yes | URL of the image attachment |

### UpdatePublicAgentMetadataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID for authorization (cannot be updated) |
| `name` | string | No | Name of the agent |
| `description` | string | No | Description of the agent |
| `status` | string (enum: `active`, `inactive`, `archived`) | No | Status of the agent |

### UpdatePublicAgentResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success status |
| `message` | string | Yes | Response message |
| `data` | object | Yes | Updated agent or version data |

### UpdatePublicAgentVersionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID for authorization |
| `versionName` | string | No | Version name |
| `description` | string | No | Description of the version |
| `nodes` | array of object | No | Complete array of nodes for the agent workflow. Provide all nodes including unchanged ones. |
| `edges` | array of object | No | Complete array of edges connecting the nodes. Provide all edges including unchanged ones. |
| `globalVariables` | array of object | No | Global variables accessible throughout the agent workflow |
| `inputVariables` | array of object | No | Input variables required from user at execution time |
| `runtimeVariables` | array of object | No | Runtime variables generated during agent execution |
| `globalConfig` | object | No | Global configuration including prompts and settings |
| `userId` | string | No | User ID performing the update |
| `userName` | string | No | User name performing the update |
