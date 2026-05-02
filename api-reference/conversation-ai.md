# Conversation Ai API

Documentation for AI Employees API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Actions](#actions)
- [Agents](#agents)
- [Generations](#generations)

## Actions

### POST `/conversation-ai/agents/{agentId}/actions`

**Attach Action to Agent**

Creates and attach a new action for an AI agent. Actions define specific tasks or behaviors that the agent can perform, such as booking appointments, sending follow-ups, or collecting information.

**Operation ID:** `create-action`

**Tags:** Actions

**Required Scopes:** `conversation-ai.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `triggerWorkflow`, `updateContactField`, `appointmentBooking`, `stopBot`, `humanHandOver`, `advancedFollowup`, `transferBot`) | Yes |  |
| `name` | string | Yes |  |
| `details` | object | object | object | object | object | object | object | Yes | Action-specific details. The structure depends on the action type. For TRIGGER_WORKFLOW use triggerWorkflowDto, for UPDATE_CONTACT_FIELD use updateContactFieldDto, for APPOINTMENT_BOOKING use appointm... |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/conversation-ai/agents/{agentId}/actions/list`

**List Actions for an Agent**

List for actions for an agent

**Operation ID:** `list-actions`

**Tags:** Actions

**Required Scopes:** `conversation-ai.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes | Grouped actions by type |
| `success` | boolean | Yes | Success status of the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/conversation-ai/agents/{agentId}/actions/{actionId}`

**Get Action by ID**

Retrieves detailed information about a specific action using its unique identifier. Returns the action configuration, associated agents, and performance metrics.

**Operation ID:** `get-action-by-id`

**Tags:** Actions

**Required Scopes:** `conversation-ai.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `actionId` | path | string | Yes | The unique identifier of the action ID Attached to the agent |
| `agentId` | path | string | Yes |  |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/conversation-ai/agents/{agentId}/actions/{actionId}`

**Update Action**

Updates an existing action's configuration. This includes modifying the action name, description, trigger conditions, and behavior settings.

**Operation ID:** `update-action`

**Tags:** Actions

**Required Scopes:** `conversation-ai.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `actionId` | path | string | Yes | The unique identifier of the action ID Attached to the agent |
| `agentId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `triggerWorkflow`, `updateContactField`, `appointmentBooking`, `stopBot`, `humanHandOver`, `advancedFollowup`, `transferBot`) | Yes |  |
| `name` | string | Yes |  |
| `details` | object | object | object | object | object | object | object | Yes | Action-specific details. The structure depends on the action type. For TRIGGER_WORKFLOW use triggerWorkflowDto, for UPDATE_CONTACT_FIELD use updateContactFieldDto, for APPOINTMENT_BOOKING use appointm... |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/conversation-ai/agents/{agentId}/actions/{actionId}`

**Remove Action from Agent**

Permanently deletes an action. This will remove the action from all associated agents and cannot be undone.

**Operation ID:** `delete-action`

**Tags:** Actions

**Required Scopes:** `conversation-ai.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `actionId` | path | string | Yes | The unique identifier of the action ID Attached to the agent |
| `agentId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/conversation-ai/agents/{agentId}/followup-settings`

**Update Followup Settings**

Update the followup settings for an action

**Operation ID:** `update-followup-settings`

**Tags:** Actions

**Required Scopes:** `conversation-ai.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `actionIds` | array of string | Yes |  |
| `followupSettings` | object | Yes |  |

**`followupSettings` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dynamicChannelSwitching` | boolean | Yes | Whether to dynamically switch channels for followups Default: `True` |
| `followUpHours` | boolean | No | Whether to respect working hours for followups |
| `workingHours` | array of object | No | Working hours configuration for followups |
| `timezoneToUse` | string (enum: `contact`, `business`) | No | Timezone to use for followups, contact or location |

#### Responses

**`200` - Success**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Agents

### POST `/conversation-ai/agents`

**Create an Agent**

Creates a new AI agent for the location. The agent will be created with the specified configuration including name, role, actions, and behavior settings.

**Operation ID:** `create-agent`

**Tags:** Agents

**Required Scopes:** `conversation-ai.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | No | Mode of operation - OFF, SUGGESTIVE, or AUTO_PILOT Default: `off` |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | No | Communication channels the agent can operate on |
| `isPrimary` | boolean | No | Indicates if this agent is a primary agent. Default: `False` |
| `waitTime` | number | No | Wait time before agent responds (max 5 for minutes, 300 for seconds) Default: `2` |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | No | Unit for wait time - SECONDS or MINUTES Default: `seconds` |
| `sleepEnabled` | boolean | No | Indicates if sleep functionality is enabled. Default: `False` |
| `sleepTime` | number | No | Duration of sleep period (required if sleepEnabled is true). Set to null for indefinite sleep. (max 2880 for minutes, 172800 for seconds, 48 for hours) |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time - HOURS, MINUTES, or SECONDS (required if sleepEnabled is true). Set to null for indefinite sleep. |
| `personality` | string | Yes | Personality traits of the agent. |
| `goal` | string | Yes | The goal of the agent. |
| `instructions` | string | Yes | Instructions for the agent. |
| `autoPilotMaxMessages` | number | No | Maximum number of messages in auto-pilot mode before requiring human intervention. (max: 100, min: 1) Default: `75` |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `respondToImages` | boolean | No | Allow agent to respond to images Default: `False` |
| `respondToAudio` | boolean | No | Allow agent to respond to audio Default: `False` |
| `sleepOnManualMessage` | boolean | No | Enable sleep when a manual outbound message is sent. |
| `sleepOnWorkflowMessage` | boolean | No | Enable sleep when a workflow outbound message is sent. |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the agent. |
| `name` | string | Yes | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | Yes | Current operating mode of the agent. |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | Yes | Communication channels the agent operates on. |
| `waitTime` | number | Yes | Wait time before agent responds. |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | Yes | Unit for wait time. |
| `sleepEnabled` | boolean | Yes | Indicates if sleep functionality is enabled. |
| `sleepTime` | number | No | Duration of sleep period. |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time. |
| `actions` | array of object | Yes | List of actions associated with this agent. |
| `isPrimary` | boolean | Yes | Indicates if this agent is a primary agent. |
| `autoPilotMaxMessages` | number | Yes | Maximum number of messages in auto-pilot mode before requiring human intervention. |
| `goal` | string | No | The goal of the agent. |
| `personality` | string | No | Personality traits of the agent. |
| `instructions` | string | No | Instructions for the agent. |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `sleepOnManualMessage` | boolean | No | Whether the bot sleeps on manual outbound messages. |
| `sleepOnWorkflowMessage` | boolean | No | Whether the bot sleeps on workflow outbound messages. |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/conversation-ai/agents/search`

**Search Agents**

Searches for AI agents based on various criteria including name, status, and configuration. Supports advanced filtering and full-text search capabilities.

**Operation ID:** `search-agent`

**Tags:** Agents

**Required Scopes:** `conversation-ai.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `startAfter` | query | string | No | Start after is the agent id to start after, Serving as skip, send empty when first page |
| `limit` | query | number | No | Records per page |
| `query` | query | string | No | query to search on agent name, must be provided in lowercase |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agents` | array of object | Yes | List of agents matching the search criteria. |
| `totalCount` | number | Yes | Total number of agents in the location (unfiltered count). |
| `count` | number | Yes | Number of agents in the current response (filtered/paginated count). |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/conversation-ai/agents/{agentId}`

**Update Agent**

Updates an existing AI agent's configuration. All fields in the agent configuration can be updated including name, status, actions, and behavior settings.

**Operation ID:** `update-agent`

**Tags:** Agents

**Required Scopes:** `conversation-ai.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes | Conversations AI agent id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | No | Mode of operation for the agent, required if primary is enabled. |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | No | Channels the agent can use. |
| `isPrimary` | boolean | No | Indicates if this agent is a primary agent. |
| `waitTime` | number | No | Wait time before agent responds (max 5 for minutes, 300 for seconds). |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | No | Unit for wait time - SECONDS or MINUTES |
| `sleepEnabled` | boolean | No | Indicates if sleep functionality is enabled. |
| `sleepTime` | number | No | Duration of sleep period (required if sleepEnabled is true). Set to null for indefinite sleep. (max 2880 for minutes, 172800 for seconds, 48 for hours) |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time - HOURS, MINUTES, or SECONDS (required if sleepEnabled is true). Set to null for indefinite sleep. |
| `personality` | string | No | Personality traits of the agent. |
| `goal` | string | No | The goal of the agent. |
| `instructions` | string | No | Instructions for the agent. |
| `autoPilotMaxMessages` | number | Yes | Maximum number of messages in auto-pilot mode before requiring human intervention. (max: 100, min: 1) Default: `75` |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `respondToImages` | boolean | No | Allow agent to respond to images Default: `False` |
| `respondToAudio` | boolean | No | Allow agent to respond to audio Default: `False` |
| `sleepOnManualMessage` | boolean | No | Enable sleep when a manual outbound message is sent. |
| `sleepOnWorkflowMessage` | boolean | No | Enable sleep when a workflow outbound message is sent. |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the agent. |
| `name` | string | Yes | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | Yes | Current operating mode of the agent. |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | Yes | Communication channels the agent operates on. |
| `waitTime` | number | Yes | Wait time before agent responds. |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | Yes | Unit for wait time. |
| `sleepEnabled` | boolean | Yes | Indicates if sleep functionality is enabled. |
| `sleepTime` | number | No | Duration of sleep period. |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time. |
| `actions` | array of object | Yes | List of actions associated with this agent. |
| `isPrimary` | boolean | Yes | Indicates if this agent is a primary agent. |
| `autoPilotMaxMessages` | number | Yes | Maximum number of messages in auto-pilot mode before requiring human intervention. |
| `goal` | string | No | The goal of the agent. |
| `personality` | string | No | Personality traits of the agent. |
| `instructions` | string | No | Instructions for the agent. |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `sleepOnManualMessage` | boolean | No | Whether the bot sleeps on manual outbound messages. |
| `sleepOnWorkflowMessage` | boolean | No | Whether the bot sleeps on workflow outbound messages. |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/conversation-ai/agents/{agentId}`

**Get Agent**

Retrieves a specific AI agent by its ID. Returns the complete agent configuration including name, status, actions, and settings.

**Operation ID:** `get-agent`

**Tags:** Agents

**Required Scopes:** `conversation-ai.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes | Conversations AI agent id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the agent. |
| `name` | string | Yes | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | Yes | Current operating mode of the agent. |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | Yes | Communication channels the agent operates on. |
| `waitTime` | number | Yes | Wait time before agent responds. |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | Yes | Unit for wait time. |
| `sleepEnabled` | boolean | Yes | Indicates if sleep functionality is enabled. |
| `sleepTime` | number | No | Duration of sleep period. |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time. |
| `actions` | array of object | Yes | List of actions associated with this agent. |
| `isPrimary` | boolean | Yes | Indicates if this agent is a primary agent. |
| `autoPilotMaxMessages` | number | Yes | Maximum number of messages in auto-pilot mode before requiring human intervention. |
| `goal` | string | No | The goal of the agent. |
| `personality` | string | No | Personality traits of the agent. |
| `instructions` | string | No | Instructions for the agent. |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `sleepOnManualMessage` | boolean | No | Whether the bot sleeps on manual outbound messages. |
| `sleepOnWorkflowMessage` | boolean | No | Whether the bot sleeps on workflow outbound messages. |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/conversation-ai/agents/{agentId}`

**Delete Agent**

Deletes an AI agent permanently. This action cannot be undone. All associated configurations and conversation history will be removed.

**Operation ID:** `delete-agent`

**Tags:** Agents

**Required Scopes:** `conversation-ai.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes | Conversations AI agent id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the agent was deleted successfully. |
| `id` | string | Yes | Unique identifier of the deleted agent. |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Generations

### GET `/conversation-ai/generations`

**Get the generation details**

Retrieves detailed information about AI responses including the System Prompt, Conversation history, Knowledge base, website, FAQ chunks, and Rich Text chunks.

**Operation ID:** `get-generation-details`

**Tags:** Generations

**Required Scopes:** `conversation-ai.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `messageId` | query | string | Yes | Message Id |
| `source` | query | string (enum: `conversation`, `workflow`) | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `prompt` | string | Yes | The complete prompt used for the AI response. |
| `intent` | string | No | The intent/goal extracted from location prompt. |
| `responseMessage` | string | Yes | The response message generated by the AI. |
| `faqs` | array of any | No | FAQ chunks used in generating the response from fine-tuned data. |
| `website` | array of any | No | Website content chunks used in generating the response. |
| `agentId` | string | No | ID of the employee/agent that generated the response. |
| `input` | string | No | The original input message that triggered this response. |
| `actionLogs` | array of any | Yes | List of actions taken during this interaction. |
| `history` | array of any | Yes | Conversation history leading up to this response. |
| `mode` | string | No | Mode of operation during this interaction. |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### ActionDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the action |
| `name` | string | Yes | Name of the action |
| `type` | string (enum: `triggerWorkflow`, `updateContactField`, `appointmentBooking`, `stopBot`, `humanHandOver`, `advancedFollowup`, `transferBot`) | Yes | Type of the action |
| `agentId` | string | No | Agent ID where the action belongs |
| `details` | object | object | object | object | object | object | object | Yes | Action-specific details. The structure depends on the action type. For TRIGGER_WORKFLOW use triggerWorkflowDto, for UPDATE_CONTACT_FIELD use updateContactFieldDto, for APPOINTMENT_BOOKING use appointm... |

### ActionsIdDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the action. |
| `type` | string (enum: `triggerWorkflow`, `updateContactField`, `appointmentBooking`, `stopBot`, `humanHandOver`, `advancedFollowup`, `transferBot`) | Yes | type of action. |

### CreateActionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `triggerWorkflow`, `updateContactField`, `appointmentBooking`, `stopBot`, `humanHandOver`, `advancedFollowup`, `transferBot`) | Yes |  |
| `name` | string | Yes |  |
| `details` | object | object | object | object | object | object | object | Yes | Action-specific details. The structure depends on the action type. For TRIGGER_WORKFLOW use triggerWorkflowDto, for UPDATE_CONTACT_FIELD use updateContactFieldDto, for APPOINTMENT_BOOKING use appointm... |

### CreateEmployeeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | No | Mode of operation - OFF, SUGGESTIVE, or AUTO_PILOT Default: `off` |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | No | Communication channels the agent can operate on |
| `isPrimary` | boolean | No | Indicates if this agent is a primary agent. Default: `False` |
| `waitTime` | number | No | Wait time before agent responds (max 5 for minutes, 300 for seconds) Default: `2` |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | No | Unit for wait time - SECONDS or MINUTES Default: `seconds` |
| `sleepEnabled` | boolean | No | Indicates if sleep functionality is enabled. Default: `False` |
| `sleepTime` | number | No | Duration of sleep period (required if sleepEnabled is true). Set to null for indefinite sleep. (max 2880 for minutes, 172800 for seconds, 48 for hours) |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time - HOURS, MINUTES, or SECONDS (required if sleepEnabled is true). Set to null for indefinite sleep. |
| `personality` | string | Yes | Personality traits of the agent. |
| `goal` | string | Yes | The goal of the agent. |
| `instructions` | string | Yes | Instructions for the agent. |
| `autoPilotMaxMessages` | number | No | Maximum number of messages in auto-pilot mode before requiring human intervention. (max: 100, min: 1) Default: `75` |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `respondToImages` | boolean | No | Allow agent to respond to images Default: `False` |
| `respondToAudio` | boolean | No | Allow agent to respond to audio Default: `False` |
| `sleepOnManualMessage` | boolean | No | Enable sleep when a manual outbound message is sent. |
| `sleepOnWorkflowMessage` | boolean | No | Enable sleep when a workflow outbound message is sent. |

### DeleteActionDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | ID of the deleted action |

### DeleteEmployeeResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates if the agent was deleted successfully. |
| `id` | string | Yes | Unique identifier of the deleted agent. |

### EmployeeListItemDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the agent. |
| `name` | string | Yes | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | Yes | Current operating mode of the agent. |
| `channels` | array of string | Yes | Communication channels the agent operates on. |
| `waitTime` | number | Yes | Wait time before agent responds. |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | Yes | Unit for wait time. |
| `sleepEnabled` | boolean | Yes | Indicates if sleep functionality is enabled. |
| `sleepTime` | number | No | Duration of sleep period. |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time. |
| `actions` | array of object | Yes | List of actions associated with this agent. |
| `isPrimary` | boolean | Yes | Indicates if this agent is a primary agent. (First agent created for a location is primary by default) |
| `autoPilotMaxMessages` | number | Yes | Maximum number of messages in auto-pilot mode before requiring human intervention. |
| `goal` | object | No | Goal configuration for the agent. |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `createdAt` | string | Yes | Timestamp when the agent was created. |
| `updatedAt` | string | Yes | Timestamp when the agent was last updated. |
| `sleepOnManualMessage` | boolean | No | Whether the bot sleeps on manual outbound messages. |
| `sleepOnWorkflowMessage` | boolean | No | Whether the bot sleeps on workflow outbound messages. |

### EmployeeResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the agent. |
| `name` | string | Yes | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | Yes | Current operating mode of the agent. |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | Yes | Communication channels the agent operates on. |
| `waitTime` | number | Yes | Wait time before agent responds. |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | Yes | Unit for wait time. |
| `sleepEnabled` | boolean | Yes | Indicates if sleep functionality is enabled. |
| `sleepTime` | number | No | Duration of sleep period. |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time. |
| `actions` | array of object | Yes | List of actions associated with this agent. |
| `isPrimary` | boolean | Yes | Indicates if this agent is a primary agent. |
| `autoPilotMaxMessages` | number | Yes | Maximum number of messages in auto-pilot mode before requiring human intervention. |
| `goal` | string | No | The goal of the agent. |
| `personality` | string | No | Personality traits of the agent. |
| `instructions` | string | No | Instructions for the agent. |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `sleepOnManualMessage` | boolean | No | Whether the bot sleeps on manual outbound messages. |
| `sleepOnWorkflowMessage` | boolean | No | Whether the bot sleeps on workflow outbound messages. |

### FetchAIResponseDetailsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `prompt` | string | Yes | The complete prompt used for the AI response. |
| `intent` | string | No | The intent/goal extracted from location prompt. |
| `responseMessage` | string | Yes | The response message generated by the AI. |
| `faqs` | array of any | No | FAQ chunks used in generating the response from fine-tuned data. |
| `website` | array of any | No | Website content chunks used in generating the response. |
| `agentId` | string | No | ID of the employee/agent that generated the response. |
| `input` | string | No | The original input message that triggered this response. |
| `actionLogs` | array of any | Yes | List of actions taken during this interaction. |
| `history` | array of any | Yes | Conversation history leading up to this response. |
| `mode` | string | No | Mode of operation during this interaction. |

### FollowupSequence

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | number | Yes | Unique identifier for this followup step |
| `followupTimeUnit` | string (enum: `days`, `hours`, `minutes`) | Yes | Time unit for followup delay |
| `followupTime` | number | Yes | Time duration before followup (max: 60 minutes, 24 hours, or 180 days depending on unit) |
| `aiEnabledMessage` | boolean | No | Whether to use AI to generate the followup message Default: `True` |
| `triggerWorkflow` | boolean | No | Whether to trigger a workflow during this followup Default: `False` |
| `customMessage` | string | No | Custom message to send (when aiEnabledMessage is false) |
| `workflowId` | string | No | Workflow ID to trigger (when triggerWorkflow is true) |
| `contactRequested` | boolean | No | Whether contact was requested in this followup |

### FollowupSettings

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dynamicChannelSwitching` | boolean | Yes | Whether to dynamically switch channels for followups Default: `True` |
| `followUpHours` | boolean | No | Whether to respect working hours for followups |
| `workingHours` | array of object | No | Working hours configuration for followups |
| `timezoneToUse` | string (enum: `contact`, `business`) | No | Timezone to use for followups, contact or location |

### Interval

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `startHour` | number | Yes | Start hour (24-hour format) |
| `startMinute` | number | Yes | Start minute |
| `endHour` | number | Yes | End hour (24-hour format) |
| `endMinute` | number | Yes | End minute |

### SearchEmployeeResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agents` | array of object | Yes | List of agents matching the search criteria. |
| `totalCount` | number | Yes | Total number of agents in the location (unfiltered count). |
| `count` | number | Yes | Number of agents in the current response (filtered/paginated count). |

### UpdateEmployeeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the agent. |
| `businessName` | string | No | Name of the business the agent represents. |
| `mode` | string (enum: `off`, `suggestive`, `auto-pilot`) | No | Mode of operation for the agent, required if primary is enabled. |
| `channels` | array of string (enum: `IG`, `FB`, `SMS`, `WebChat`, `WhatsApp`, `Live_Chat`) | No | Channels the agent can use. |
| `isPrimary` | boolean | No | Indicates if this agent is a primary agent. |
| `waitTime` | number | No | Wait time before agent responds (max 5 for minutes, 300 for seconds). |
| `waitTimeUnit` | string (enum: `minutes`, `seconds`) | No | Unit for wait time - SECONDS or MINUTES |
| `sleepEnabled` | boolean | No | Indicates if sleep functionality is enabled. |
| `sleepTime` | number | No | Duration of sleep period (required if sleepEnabled is true). Set to null for indefinite sleep. (max 2880 for minutes, 172800 for seconds, 48 for hours) |
| `sleepTimeUnit` | string (enum: `hours`, `minutes`, `seconds`) | No | Unit of sleep time - HOURS, MINUTES, or SECONDS (required if sleepEnabled is true). Set to null for indefinite sleep. |
| `personality` | string | No | Personality traits of the agent. |
| `goal` | string | No | The goal of the agent. |
| `instructions` | string | No | Instructions for the agent. |
| `autoPilotMaxMessages` | number | Yes | Maximum number of messages in auto-pilot mode before requiring human intervention. (max: 100, min: 1) Default: `75` |
| `knowledgeBaseIds` | array of string | No | Array of knowledge base IDs associated with this agent. |
| `respondToImages` | boolean | No | Allow agent to respond to images Default: `False` |
| `respondToAudio` | boolean | No | Allow agent to respond to audio Default: `False` |
| `sleepOnManualMessage` | boolean | No | Enable sleep when a manual outbound message is sent. |
| `sleepOnWorkflowMessage` | boolean | No | Enable sleep when a workflow outbound message is sent. |

### UpdateFollowupSettingsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `actionIds` | array of string | Yes |  |
| `followupSettings` | object | Yes |  |

### WorkingHours

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dayOfTheWeek` | number | Yes | Day of the week (0=Sunday, 1=Monday, etc.) |
| `intervals` | array of object | No | Time intervals for this day |

### advancedFollowupDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Whether advanced followup is enabled |
| `scenarioId` | string (enum: `contactStoppedReplying`, `contactIsBusy`, `contactRequested`) | Yes | ID of the followup scenario |
| `followupSequence` | array of object | Yes | Sequence of followup actions to perform |
| `followupSettings` | object | No |  |

### appointmentBookingDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `actionId` | string | No | Optional action ID reference |
| `calendarId` | string | Yes | Calendar ID for appointment booking |
| `onlySendLink` | boolean | Yes | If true, only sends the appointment link without booking |
| `triggerWorkflow` | boolean | Yes | Whether to trigger a workflow after booking (cannot be true when onlySendLink is true) |
| `workflowIds` | array of string | No | Workflow IDs to trigger after booking (required when triggerWorkflow is true) |
| `sleepAfterBooking` | boolean | Yes | Whether to put the agent to sleep after booking (cannot be true when onlySendLink is true) |
| `sleepTimeUnit` | string (enum: `days`, `hours`, `minutes`) | No | Unit for sleep time (required when sleepAfterBooking is true) |
| `sleepTime` | number | No | Sleep duration (required when sleepAfterBooking is true) |
| `transferBot` | boolean | Yes | Whether to transfer to another agent after booking (cannot be true when onlySendLink is true) |
| `transferAgent` | string | No | Agent ID to transfer to (required when transferBot is true) |
| `rescheduleEnabled` | boolean | Yes | Whether to allow appointment rescheduling (cannot be true when onlySendLink is true) Default: `False` |
| `cancelEnabled` | boolean | Yes | Whether to allow appointment cancellation (cannot be true when onlySendLink is true) Default: `False` |

### createActionResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

### deleteActionResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

### fetchActionDetailsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

### fetchActionsForEmployeeResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes | Grouped actions by type |
| `success` | boolean | Yes | Success status of the request |

### humanHandOverDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Whether human handover action is enabled |
| `triggerCondition` | string | Yes | Condition that triggers human handover |
| `examples` | array of string | No | Example phrases that trigger human handover (required when handoverType is custom or contactRequest) |
| `assignToUserId` | string | No | ID of the user to assign the conversation to |
| `skipAssignToUser` | boolean | No | Whether to skip assigning to a specific user |
| `createTask` | boolean | No | Whether to create a task when handing over |
| `reactivateEnabled` | boolean | Yes | Whether the agent can be reactivated after handover |
| `sleepTimeUnit` | string (enum: `days`, `hours`, `minutes`) | No | Time unit for reactivation delay (required when reactivateEnabled is true) |
| `sleepTime` | number | No | Time duration before reactivation (required when reactivateEnabled is true) |
| `finalMessage` | string | Yes | Final message sent when handing over to human |
| `tags` | array of string | No | Tags to apply during handover |
| `handoverType` | string (enum: `contactRequest`, `lackOfInformation`, `failedToResolveIssue`, `custom`) | Yes | Type of human handover detection |

### stopBotDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stopBotDetectionType` | string (enum: `Goodbye`, `Custom`) | Yes | Type of stop bot detection - Goodbye or Custom |
| `stopBotTriggerCondition` | string | Yes | Condition that triggers stopping the bot |
| `reactivateEnabled` | boolean | Yes | Whether the bot can be reactivated after being stopped |
| `sleepTimeUnit` | string (enum: `days`, `hours`, `minutes`) | No | Time unit for reactivation delay (required when reactivateEnabled is true) |
| `sleepTime` | number | No | Time duration before reactivation (required when reactivateEnabled is true) |
| `enabled` | boolean | Yes | Whether this action is enabled for the agent |
| `stopBotExamples` | array of string | Yes | Example phrases that trigger stop bot action (minimum 2 required) |
| `finalMessage` | string | Yes | Final message sent when stopping the bot |
| `tags` | array of string | No | Tags to apply when stopping the bot |

### transferBotDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `transferBotType` | string (enum: `Default`, `Custom`) | Yes | Type of transfer - Default or Custom |
| `transferToBot` | string | Yes | ID of the bot/agent to transfer to |
| `enabled` | boolean | Yes | Whether this transfer action is enabled |
| `transferBotTriggerCondition` | string | No | Condition that triggers the transfer (required for Custom type) |
| `transferBotExamples` | array of string | No | Example phrases that trigger transfer (required for Custom type, minimum 2) |

### triggerWorkflowDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `workflowIds` | array of string | Yes | Array of workflow IDs to trigger |
| `triggerCondition` | string | Yes | Condition that triggers the workflow |
| `triggerMessage` | string | No | Optional message to send when triggering the workflow |

### updateActionResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `success` | boolean | Yes | Success status of the request |

### updateContactFieldDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contactFieldId` | string | Yes | ID of the contact field in Contacts Table |
| `description` | string | Yes | Description of the contact field in Contacts Table |
| `contactUpdateExamples` | array of string | No | Contact update examples in Contacts Table. Not required when using standard fields, Monetory or Date Custom fields. Default: `[]` |
