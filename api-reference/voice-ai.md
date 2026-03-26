# Voice AI API

Documentation for Voice AI API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Agents](#agents)
- [Dashboard](#dashboard)
- [Actions](#actions)

## Agents

### POST `/voice-ai/agents`

**Create Agent**

Create a new voice AI agent configuration and settings

**Operation ID:** `create-agent`

**Tags:** Agents

**Required Scopes:** `voice-ai-agents.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | No | Unique identifier for the location where this agent will operate |
| `agentName` | string | No | Display name for the voice AI agent, between 1-40 characters. Default: "My Agent {random 3 digit number}" |
| `businessName` | string | No | Name of the business this agent represents. Default: Uses location name |
| `welcomeMessage` | string | No | Initial greeting spoken when the agent answers calls. Default: Auto generated |
| `agentPrompt` | string | No | Custom instructions defining the agent's behavior and personality. Default: Basic prompt generated automatically |
| `voiceId` | string | No | Identifier for the speech synthesis voice from available voice options. Default: Auto generated |
| `language` | string (enum: `en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, `nl-NL`, `multi`) | No | Language code for the agent's speech and understanding. Default: "en-US" |
| `patienceLevel` | string (enum: `low`, `medium`, `high`) | No | Tolerance level for caller response delays. Default: "high" |
| `maxCallDuration` | number | No | Maximum call duration in seconds, between 180-900 (3-15 minutes). Default: 300 seconds (5 minutes) |
| `sendUserIdleReminders` | boolean | No | Enables automatic reminders when callers are silent. Default: true |
| `reminderAfterIdleTimeSeconds` | number | No | Seconds to wait before sending idle reminders, between 1-20. Default: 8 seconds |
| `inboundNumber` | string | No | Phone number for receiving inbound calls to this agent. Default: null |
| `numberPoolId` | string | No | Identifier for the number pool managing phone number allocation. Default: null |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs to trigger automatically when calls end. Default: [] |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals defining when the agent accepts calls, organized by day of week. Default: [] (available 24/7) |
| `timezone` | string | No | IANA timezone identifier affecting working hours and scheduling. Default: Location timezone |
| `isAgentAsBackupDisabled` | boolean | No | Prevents this agent from being used as a fallback option. Default: false (Available as backup agent) |
| `translation` | object | No |  |

**`sendPostCallNotificationTo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `admins` | boolean | Yes | Enables post-call notifications to all admin users in the location. Default: true |
| `allUsers` | boolean | Yes | Enables post-call notifications to all users in the location. Default: false |
| `contactAssignedUser` | boolean | Yes | Enables post-call notifications to the user assigned to the contact. Default: false |
| `specificUsers` | array of string | Yes | Array of specific user IDs to receive post-call notifications. Default: [] |
| `customEmails` | array of string | Yes | Array of custom email addresses to receive post-call notifications. Default: [] |

**`agentWorkingHours` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dayOfTheWeek` | number (enum: `1`, `2`, `3`, `4`, `5`, `6`, `7`) | Yes | Day of the week for this working hours configuration (Monday=1 to Sunday=7) |
| `intervals` | array of object | Yes | Array of time intervals when the agent is available on this day |

**`translation` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Enables language translation for agent conversations. Default: false |
| `language` | string | No | Target language code for translation (e.g., "es" for Spanish, "fr" for French). |

#### Responses

**`201` - Agent created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created agent |
| `locationId` | string | Yes | Unique identifier for the location where this agent operates |
| `agentName` | string | Yes | Display name of the voice AI agent |
| `businessName` | string | Yes | Name of the business this agent represents |
| `welcomeMessage` | string | Yes | Greeting message spoken when the agent answers calls |
| `agentPrompt` | string | Yes | Custom instructions defining the agent's behavior |
| `voiceId` | string | Yes | Identifier for the speech synthesis voice being used |
| `language` | string | Yes | Language code for the agent's speech and understanding |
| `patienceLevel` | string | Yes | Current tolerance level for caller response delays |
| `maxCallDuration` | number | Yes | Maximum call duration in seconds, between 180-900 |
| `sendUserIdleReminders` | boolean | Yes | Indicates whether automatic idle reminders are enabled |
| `reminderAfterIdleTimeSeconds` | number | Yes | Seconds to wait before sending idle reminders, between 1-20 |
| `inboundNumber` | string | No | Phone number for receiving inbound calls |
| `numberPoolId` | string | No | Identifier for the number pool managing this agent's phone allocation |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs triggered automatically when calls end |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals when the agent accepts calls, organized by day of week |
| `timezone` | string | Yes | IANA timezone identifier for working hours and scheduling |
| `isAgentAsBackupDisabled` | boolean | Yes | Indicates whether this agent is excluded from backup scenarios |
| `translation` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/voice-ai/agents`

**List Agents**

Retrieve a paginated list of agents for given location.

**Operation ID:** `get-agents`

**Tags:** Agents

**Required Scopes:** `voice-ai-agents.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `page` | query | number | No | Page number starting from 1 |
| `pageSize` | query | number | No | Number of items per page |
| `locationId` | query | string | Yes | Location ID |
| `query` | query | string | No | Query |

#### Responses

**`200` - Agent list retrieved successfully.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `page` | number | Yes | Page number starting from 1 |
| `pageSize` | number | Yes | Number of items per page |
| `agents` | array of object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PATCH `/voice-ai/agents/{agentId}`

**Patch Agent**

Partially update an existing voice AI agent

**Operation ID:** `patch-agent`

**Tags:** Agents

**Required Scopes:** `voice-ai-agents.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes | Unique agent identifier |
| `locationId` | query | string | Yes | Location ID |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agentName` | string | No | Display name for the voice AI agent, between 1-40 characters. Default: "My Agent {random 3 digit number}" |
| `businessName` | string | No | Name of the business this agent represents. Default: Uses location name |
| `welcomeMessage` | string | No | Initial greeting spoken when the agent answers calls. Default: Auto generated |
| `agentPrompt` | string | No | Custom instructions defining the agent's behavior and personality. Default: Basic prompt generated automatically |
| `voiceId` | string | No | Identifier for the speech synthesis voice from available voice options. Default: Auto generated |
| `language` | string (enum: `en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, `nl-NL`, `multi`) | No | Language code for the agent's speech and understanding. Default: "en-US" |
| `patienceLevel` | string (enum: `low`, `medium`, `high`) | No | Tolerance level for caller response delays. Default: "high" |
| `maxCallDuration` | number | No | Maximum call duration in seconds, between 180-900 (3-15 minutes). Default: 300 seconds (5 minutes) |
| `sendUserIdleReminders` | boolean | No | Enables automatic reminders when callers are silent. Default: true |
| `reminderAfterIdleTimeSeconds` | number | No | Seconds to wait before sending idle reminders, between 1-20. Default: 8 seconds |
| `inboundNumber` | string | No | Phone number for receiving inbound calls to this agent. Default: null |
| `numberPoolId` | string | No | Identifier for the number pool managing phone number allocation. Default: null |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs to trigger automatically when calls end. Default: [] |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals defining when the agent accepts calls, organized by day of week. Default: [] (available 24/7) |
| `timezone` | string | No | IANA timezone identifier affecting working hours and scheduling. Default: Location timezone |
| `isAgentAsBackupDisabled` | boolean | No | Prevents this agent from being used as a fallback option. Default: false (Available as backup agent) |
| `translation` | object | No |  |

**`sendPostCallNotificationTo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `admins` | boolean | Yes | Enables post-call notifications to all admin users in the location. Default: true |
| `allUsers` | boolean | Yes | Enables post-call notifications to all users in the location. Default: false |
| `contactAssignedUser` | boolean | Yes | Enables post-call notifications to the user assigned to the contact. Default: false |
| `specificUsers` | array of string | Yes | Array of specific user IDs to receive post-call notifications. Default: [] |
| `customEmails` | array of string | Yes | Array of custom email addresses to receive post-call notifications. Default: [] |

**`agentWorkingHours` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dayOfTheWeek` | number (enum: `1`, `2`, `3`, `4`, `5`, `6`, `7`) | Yes | Day of the week for this working hours configuration (Monday=1 to Sunday=7) |
| `intervals` | array of object | Yes | Array of time intervals when the agent is available on this day |

**`translation` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Enables language translation for agent conversations. Default: false |
| `language` | string | No | Target language code for translation (e.g., "es" for Spanish, "fr" for French). |

#### Responses

**`200` - Agent updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created agent |
| `locationId` | string | Yes | Unique identifier for the location where this agent operates |
| `agentName` | string | Yes | Display name of the voice AI agent |
| `businessName` | string | Yes | Name of the business this agent represents |
| `welcomeMessage` | string | Yes | Greeting message spoken when the agent answers calls |
| `agentPrompt` | string | Yes | Custom instructions defining the agent's behavior |
| `voiceId` | string | Yes | Identifier for the speech synthesis voice being used |
| `language` | string | Yes | Language code for the agent's speech and understanding |
| `patienceLevel` | string | Yes | Current tolerance level for caller response delays |
| `maxCallDuration` | number | Yes | Maximum call duration in seconds, between 180-900 |
| `sendUserIdleReminders` | boolean | Yes | Indicates whether automatic idle reminders are enabled |
| `reminderAfterIdleTimeSeconds` | number | Yes | Seconds to wait before sending idle reminders, between 1-20 |
| `inboundNumber` | string | No | Phone number for receiving inbound calls |
| `numberPoolId` | string | No | Identifier for the number pool managing this agent's phone allocation |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs triggered automatically when calls end |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals when the agent accepts calls, organized by day of week |
| `timezone` | string | Yes | IANA timezone identifier for working hours and scheduling |
| `isAgentAsBackupDisabled` | boolean | Yes | Indicates whether this agent is excluded from backup scenarios |
| `translation` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/voice-ai/agents/{agentId}`

**Get Agent**

Retrieve detailed configuration and settings for a specific voice AI agent

**Operation ID:** `get-agent`

**Tags:** Agents

**Required Scopes:** `voice-ai-agents.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes | Unique agent identifier |
| `locationId` | query | string | Yes | Location ID |

#### Responses

**`200` - Agent details retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created agent |
| `locationId` | string | Yes | Unique identifier for the location where this agent operates |
| `agentName` | string | Yes | Display name of the voice AI agent |
| `businessName` | string | Yes | Name of the business this agent represents |
| `welcomeMessage` | string | Yes | Greeting message spoken when the agent answers calls |
| `agentPrompt` | string | Yes | Custom instructions defining the agent's behavior |
| `voiceId` | string | Yes | Identifier for the speech synthesis voice being used |
| `language` | string | Yes | Language code for the agent's speech and understanding |
| `patienceLevel` | string | Yes | Current tolerance level for caller response delays |
| `maxCallDuration` | number | Yes | Maximum call duration in seconds, between 180-900 |
| `sendUserIdleReminders` | boolean | Yes | Indicates whether automatic idle reminders are enabled |
| `reminderAfterIdleTimeSeconds` | number | Yes | Seconds to wait before sending idle reminders, between 1-20 |
| `inboundNumber` | string | No | Phone number for receiving inbound calls |
| `numberPoolId` | string | No | Identifier for the number pool managing this agent's phone allocation |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs triggered automatically when calls end |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals when the agent accepts calls, organized by day of week |
| `timezone` | string | Yes | IANA timezone identifier for working hours and scheduling |
| `isAgentAsBackupDisabled` | boolean | Yes | Indicates whether this agent is excluded from backup scenarios |
| `translation` | object | No |  |
| `actions` | array of object | Yes | Raw actions configured for this agent with complete actionParameters structure |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/voice-ai/agents/{agentId}`

**Delete Agent**

Delete a voice AI agent and all its configurations

**Operation ID:** `delete-agent`

**Tags:** Agents

**Required Scopes:** `voice-ai-agents.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `agentId` | path | string | Yes | Unique agent identifier |
| `locationId` | query | string | Yes | Location ID |

#### Responses

**`204` - Agent deleted successfully**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Dashboard

### GET `/voice-ai/dashboard/call-logs`

**List Call Logs**

Returns call logs for Voice AI agents scoped to a location. Supports filtering by agent, contact, call type, action types, and date range (interpreted in the provided IANA timezone). Also supports sorting and 1-based pagination.

**Operation ID:** `get-call-logs`

**Tags:** Dashboard

**Required Scopes:** `voice-ai-dashboard.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location identifier. Filters results to this location. |
| `agentId` | query | string | No | Agent identifier. When provided, returns logs for this agent only. |
| `contactId` | query | string | No | Contact IDs (comma-separated) to filter by. |
| `callType` | query | string (enum: `LIVE`, `TRIAL`) | No | Call type filter. |
| `startDate` | query | number | No | Start date filter (Unix timestamp). Must be less than endDate. Both startDate and endDate must be provided together. |
| `endDate` | query | number | No | End date filter (Unix timestamp). Must be greater than startDate. Both startDate and endDate must be provided together. |
| `actionType` | query | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`, `KNOWLEDGE_BASE`) | No | Action type filter for call logs (comma-separated ACTION_TYPE values) |
| `sortBy` | query | string (enum: `duration`, `createdAt`) | No | Field to sort by. Defaults to newest if omitted. |
| `sort` | query | string (enum: `ascend`, `descend`) | No | Sort direction. Applies only when sortBy is provided. |
| `page` | query | number | No | Page number (1-based). |
| `pageSize` | query | number | No | Page size (max 50). |

#### Responses

**`200` - Successfully retrieved call logs**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `page` | number | Yes | Page number starting from 1 |
| `pageSize` | number | Yes | Number of items per page |
| `callLogs` | array of object | Yes | Array of call logs |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/voice-ai/dashboard/call-logs/{callId}`

**Get Call Log**

Returns a call log by callId.

**Operation ID:** `getCallLog`

**Tags:** Dashboard

**Required Scopes:** `voice-ai-dashboard.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `callId` | path | string | Yes | Call ID |
| `locationId` | query | string | Yes | Location ID |

#### Responses

**`200` - Successfully retrieved call log**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the call |
| `contactId` | string | No | Associated contact ID |
| `agentId` | string | Yes | Agent ID associated with the call |
| `isAgentDeleted` | boolean | Yes | Whether the agent is deleted |
| `fromNumber` | string | No | Caller phone number |
| `createdAt` | string | Yes | Timestamp when the call was created |
| `duration` | number | Yes | Call duration in seconds |
| `trialCall` | boolean | Yes | Whether this call was a trial call |
| `executedCallActions` | array of object | Yes | Actions performed during the call |
| `summary` | string | Yes | Call summary |
| `transcript` | string | Yes | Call transcript |
| `translation` | object | No |  |
| `extractedData` | object | No |  |
| `messageId` | string | No | Message identifier associated with the call |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Actions

### POST `/voice-ai/actions`

**Create Agent Action**

Create a new action for a voice AI agent. Actions define specific behaviors and capabilities for the agent during calls.

**Operation ID:** `create-action`

**Tags:** Actions

**Required Scopes:** `voice-ai-agent-goals.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agentId` | string | Yes | Agent ID to attach the action to |
| `locationId` | string | Yes | Location ID |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

#### Responses

**`201` - Action created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created action |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/voice-ai/actions/{actionId}`

**Update Agent Action**

Update an existing action for a voice AI agent. Modifies the behavior and configuration of an agent action.

**Operation ID:** `update-action`

**Tags:** Actions

**Required Scopes:** `voice-ai-agent-goals.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `actionId` | path | string | Yes | Unique identifier for the action |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agentId` | string | Yes | Agent ID to attach the action to |
| `locationId` | string | Yes | Location ID |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

#### Responses

**`200` - Action updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created action |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/voice-ai/actions/{actionId}`

**Get Agent Action**

Retrieve details of a specific action by its ID. Returns the action configuration including actionParameters.

**Operation ID:** `get-action`

**Tags:** Actions

**Required Scopes:** `voice-ai-agent-goals.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `actionId` | path | string | Yes | Unique identifier for the action |
| `locationId` | query | string | Yes | Location ID |

#### Responses

**`200` - Action details retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the action |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/voice-ai/actions/{actionId}`

**Delete Agent Action**

Delete an existing action from a voice AI agent. This permanently removes the action and its configuration.

**Operation ID:** `delete-action`

**Tags:** Actions

**Required Scopes:** `voice-ai-agent-goals.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `actionId` | path | string | Yes | Unique identifier for the action |
| `locationId` | query | string | Yes | Location ID |
| `agentId` | query | string | Yes | Agent ID the action is attached to |

#### Responses

**`204` - Action deleted successfully**

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AgentActionResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for this action |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

### AgentCreationRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | No | Unique identifier for the location where this agent will operate |
| `agentName` | string | No | Display name for the voice AI agent, between 1-40 characters. Default: "My Agent {random 3 digit number}" |
| `businessName` | string | No | Name of the business this agent represents. Default: Uses location name |
| `welcomeMessage` | string | No | Initial greeting spoken when the agent answers calls. Default: Auto generated |
| `agentPrompt` | string | No | Custom instructions defining the agent's behavior and personality. Default: Basic prompt generated automatically |
| `voiceId` | string | No | Identifier for the speech synthesis voice from available voice options. Default: Auto generated |
| `language` | string (enum: `en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, `nl-NL`, `multi`) | No | Language code for the agent's speech and understanding. Default: "en-US" |
| `patienceLevel` | string (enum: `low`, `medium`, `high`) | No | Tolerance level for caller response delays. Default: "high" |
| `maxCallDuration` | number | No | Maximum call duration in seconds, between 180-900 (3-15 minutes). Default: 300 seconds (5 minutes) |
| `sendUserIdleReminders` | boolean | No | Enables automatic reminders when callers are silent. Default: true |
| `reminderAfterIdleTimeSeconds` | number | No | Seconds to wait before sending idle reminders, between 1-20. Default: 8 seconds |
| `inboundNumber` | string | No | Phone number for receiving inbound calls to this agent. Default: null |
| `numberPoolId` | string | No | Identifier for the number pool managing phone number allocation. Default: null |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs to trigger automatically when calls end. Default: [] |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals defining when the agent accepts calls, organized by day of week. Default: [] (available 24/7) |
| `timezone` | string | No | IANA timezone identifier affecting working hours and scheduling. Default: Location timezone |
| `isAgentAsBackupDisabled` | boolean | No | Prevents this agent from being used as a fallback option. Default: false (Available as backup agent) |
| `translation` | object | No |  |

### AgentWorkingHoursDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dayOfTheWeek` | number (enum: `1`, `2`, `3`, `4`, `5`, `6`, `7`) | Yes | Day of the week for this working hours configuration (Monday=1 to Sunday=7) |
| `intervals` | array of object | Yes | Array of time intervals when the agent is available on this day |

### AppointmentBookingActionParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendarId` | string | Yes | Calendar ID to book appointments in |
| `daysOfOfferingDates` | number | Yes | Number of days ahead to offer booking dates |
| `slotsPerDay` | number | Yes | Number of available slots per day |
| `hoursBetweenSlots` | number | Yes | Hours between available slots |

### CallActionSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `actionId` | string | No | Action ID reference |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Action type |
| `actionName` | string | Yes | Action name |
| `description` | string | No | Action description |
| `actionParameters` | object | object | object | object | object | object | object | object | No | Action parameters - structure varies by actionType |
| `executedAt` | string | No | When the action was executed |
| `triggerReceivedAt` | string | No | When the trigger was received |

### CallLogDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the call |
| `contactId` | string | No | Associated contact ID |
| `agentId` | string | Yes | Agent ID associated with the call |
| `isAgentDeleted` | boolean | Yes | Whether the agent is deleted |
| `fromNumber` | string | No | Caller phone number |
| `createdAt` | string | Yes | Timestamp when the call was created |
| `duration` | number | Yes | Call duration in seconds |
| `trialCall` | boolean | Yes | Whether this call was a trial call |
| `executedCallActions` | array of object | Yes | Actions performed during the call |
| `summary` | string | Yes | Call summary |
| `transcript` | string | Yes | Call transcript |
| `translation` | object | No |  |
| `extractedData` | object | No |  |
| `messageId` | string | No | Message identifier associated with the call |

### CallLogsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `page` | number | Yes | Page number starting from 1 |
| `pageSize` | number | Yes | Number of items per page |
| `callLogs` | array of object | Yes | Array of call logs |

### CallTransferActionParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `triggerPrompt` | string | Yes | When to trigger this action during the call |
| `transferToType` | string (enum: `number`) | Yes | Type of transfer destination (currently only "number" is supported) |
| `transferToValue` | string | Yes | Phone number to transfer to. Must start with +, include country code, contain only numbers, and be 11-16 characters long (e.g., +12345678901). |
| `triggerMessage` | string | No | Message to tell the caller before transferring |
| `hearWhisperMessage` | boolean | No | Whether to play whisper message to the receiving party |

### CreateActionResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created action |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

### CreateAgentResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created agent |
| `locationId` | string | Yes | Unique identifier for the location where this agent operates |
| `agentName` | string | Yes | Display name of the voice AI agent |
| `businessName` | string | Yes | Name of the business this agent represents |
| `welcomeMessage` | string | Yes | Greeting message spoken when the agent answers calls |
| `agentPrompt` | string | Yes | Custom instructions defining the agent's behavior |
| `voiceId` | string | Yes | Identifier for the speech synthesis voice being used |
| `language` | string | Yes | Language code for the agent's speech and understanding |
| `patienceLevel` | string | Yes | Current tolerance level for caller response delays |
| `maxCallDuration` | number | Yes | Maximum call duration in seconds, between 180-900 |
| `sendUserIdleReminders` | boolean | Yes | Indicates whether automatic idle reminders are enabled |
| `reminderAfterIdleTimeSeconds` | number | Yes | Seconds to wait before sending idle reminders, between 1-20 |
| `inboundNumber` | string | No | Phone number for receiving inbound calls |
| `numberPoolId` | string | No | Identifier for the number pool managing this agent's phone allocation |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs triggered automatically when calls end |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals when the agent accepts calls, organized by day of week |
| `timezone` | string | Yes | IANA timezone identifier for working hours and scheduling |
| `isAgentAsBackupDisabled` | boolean | Yes | Indicates whether this agent is excluded from backup scenarios |
| `translation` | object | No |  |

### CreateSingleActionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agentId` | string | Yes | Agent ID to attach the action to |
| `locationId` | string | Yes | Location ID |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

### CustomActionApiDetailsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `url` | string | Yes | API endpoint URL |
| `method` | string (enum: `POST`, `GET`) | Yes | HTTP method |
| `authenticationRequired` | boolean | No | Whether authentication is required |
| `authenticationValue` | string | No | Authentication token or API key (required if authenticationRequired is true) |
| `headers` | array of object | No | HTTP headers to include |
| `parameters` | array of object | No | API parameters to send |

### CustomActionHeaderDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | string | Yes | HTTP header name |
| `value` | string | Yes | HTTP header value |

### CustomActionParameterDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Parameter name |
| `description` | string | No | Parameter description |
| `type` | string | No | Parameter type |
| `example` | string | No | Example parameter value |

### CustomActionParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `triggerPrompt` | string | Yes | When to call the custom API |
| `triggerMessage` | string | No | Message to tell the caller |
| `apiDetails` | object | Yes |  |
| `selectedPaths` | array of string | No | Selected response paths to extract from API response. Required: at least 1 value if the method is GET. Should be empty if the method is POST. |

### DataExtractionActionParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contactFieldId` | string | Yes | ID of the contact field to be updated with the extracted data |
| `description` | string | Yes | Description of what data to extract |
| `examples` | array of string | Yes | Example values to help Agent understand the expected format. At least one example is required, maximum 5 examples allowed. |
| `overwriteExistingValue` | boolean | No | Whether to overwrite existing field value if already set, default is false Default: `False` |

### ExtractedDataSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### GetActionResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the action |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

### GetAgentResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created agent |
| `locationId` | string | Yes | Unique identifier for the location where this agent operates |
| `agentName` | string | Yes | Display name of the voice AI agent |
| `businessName` | string | Yes | Name of the business this agent represents |
| `welcomeMessage` | string | Yes | Greeting message spoken when the agent answers calls |
| `agentPrompt` | string | Yes | Custom instructions defining the agent's behavior |
| `voiceId` | string | Yes | Identifier for the speech synthesis voice being used |
| `language` | string | Yes | Language code for the agent's speech and understanding |
| `patienceLevel` | string | Yes | Current tolerance level for caller response delays |
| `maxCallDuration` | number | Yes | Maximum call duration in seconds, between 180-900 |
| `sendUserIdleReminders` | boolean | Yes | Indicates whether automatic idle reminders are enabled |
| `reminderAfterIdleTimeSeconds` | number | Yes | Seconds to wait before sending idle reminders, between 1-20 |
| `inboundNumber` | string | No | Phone number for receiving inbound calls |
| `numberPoolId` | string | No | Identifier for the number pool managing this agent's phone allocation |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs triggered automatically when calls end |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals when the agent accepts calls, organized by day of week |
| `timezone` | string | Yes | IANA timezone identifier for working hours and scheduling |
| `isAgentAsBackupDisabled` | boolean | Yes | Indicates whether this agent is excluded from backup scenarios |
| `translation` | object | No |  |
| `actions` | array of object | Yes | Raw actions configured for this agent with complete actionParameters structure |

### GetAgentsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of items |
| `page` | number | Yes | Page number starting from 1 |
| `pageSize` | number | Yes | Number of items per page |
| `agents` | array of object | Yes |  |

### InCallDataExtractionActionParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contactFieldId` | string | Yes | ID of the contact field to be updated with the extracted data |
| `description` | string | Yes | Description of what data to extract |
| `examples` | array of string | Yes | Example values to help Agent understand the expected format. At least one example is required, maximum 5 examples allowed. |
| `overwriteExistingValue` | boolean | No | Whether to overwrite existing field value if already set, default is false Default: `False` |

### IntervalDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `startHour` | number | Yes | Starting hour of the working interval in 24-hour format (0-23) |
| `endHour` | number | Yes | Ending hour of the working interval in 24-hour format (0-23) |
| `startMinute` | number | Yes | Starting minute of the working interval (0-59) |
| `endMinute` | number | Yes | Ending minute of the working interval (0-59) |

### KnowledgeBaseParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `triggerPrompt` | string | No | When to query the knowledge base |
| `triggerMessage` | string | Yes | Message to tell the caller |
| `knowledgeBaseId` | string | Yes | Knowledge base ID to query |
| `parameters` | array of object | No | Additional parameters for the knowledge base query |

### PatchAgentDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agentName` | string | No | Display name for the voice AI agent, between 1-40 characters. Default: "My Agent {random 3 digit number}" |
| `businessName` | string | No | Name of the business this agent represents. Default: Uses location name |
| `welcomeMessage` | string | No | Initial greeting spoken when the agent answers calls. Default: Auto generated |
| `agentPrompt` | string | No | Custom instructions defining the agent's behavior and personality. Default: Basic prompt generated automatically |
| `voiceId` | string | No | Identifier for the speech synthesis voice from available voice options. Default: Auto generated |
| `language` | string (enum: `en-US`, `pt-BR`, `es`, `fr`, `de`, `it`, `nl-NL`, `multi`) | No | Language code for the agent's speech and understanding. Default: "en-US" |
| `patienceLevel` | string (enum: `low`, `medium`, `high`) | No | Tolerance level for caller response delays. Default: "high" |
| `maxCallDuration` | number | No | Maximum call duration in seconds, between 180-900 (3-15 minutes). Default: 300 seconds (5 minutes) |
| `sendUserIdleReminders` | boolean | No | Enables automatic reminders when callers are silent. Default: true |
| `reminderAfterIdleTimeSeconds` | number | No | Seconds to wait before sending idle reminders, between 1-20. Default: 8 seconds |
| `inboundNumber` | string | No | Phone number for receiving inbound calls to this agent. Default: null |
| `numberPoolId` | string | No | Identifier for the number pool managing phone number allocation. Default: null |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs to trigger automatically when calls end. Default: [] |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals defining when the agent accepts calls, organized by day of week. Default: [] (available 24/7) |
| `timezone` | string | No | IANA timezone identifier affecting working hours and scheduling. Default: Location timezone |
| `isAgentAsBackupDisabled` | boolean | No | Prevents this agent from being used as a fallback option. Default: false (Available as backup agent) |
| `translation` | object | No |  |

### PatchAgentResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created agent |
| `locationId` | string | Yes | Unique identifier for the location where this agent operates |
| `agentName` | string | Yes | Display name of the voice AI agent |
| `businessName` | string | Yes | Name of the business this agent represents |
| `welcomeMessage` | string | Yes | Greeting message spoken when the agent answers calls |
| `agentPrompt` | string | Yes | Custom instructions defining the agent's behavior |
| `voiceId` | string | Yes | Identifier for the speech synthesis voice being used |
| `language` | string | Yes | Language code for the agent's speech and understanding |
| `patienceLevel` | string | Yes | Current tolerance level for caller response delays |
| `maxCallDuration` | number | Yes | Maximum call duration in seconds, between 180-900 |
| `sendUserIdleReminders` | boolean | Yes | Indicates whether automatic idle reminders are enabled |
| `reminderAfterIdleTimeSeconds` | number | Yes | Seconds to wait before sending idle reminders, between 1-20 |
| `inboundNumber` | string | No | Phone number for receiving inbound calls |
| `numberPoolId` | string | No | Identifier for the number pool managing this agent's phone allocation |
| `callEndWorkflowIds` | array of string | No | Array of workflow IDs triggered automatically when calls end |
| `sendPostCallNotificationTo` | object | No |  |
| `agentWorkingHours` | array of object | No | Time intervals when the agent accepts calls, organized by day of week |
| `timezone` | string | Yes | IANA timezone identifier for working hours and scheduling |
| `isAgentAsBackupDisabled` | boolean | Yes | Indicates whether this agent is excluded from backup scenarios |
| `translation` | object | No |  |

### PatienceLevel

Tolerance level for caller response delays. Default: "high"

**Type:** `string`

**Possible Values:**

- `low`
- `medium`
- `high`

### SMSParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `triggerPrompt` | string | Yes | When to send the SMS |
| `triggerMessage` | string | Yes | Message to tell the caller |
| `messageBody` | string | Yes | SMS message content to send |

### SendPostCallNotificationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `admins` | boolean | Yes | Enables post-call notifications to all admin users in the location. Default: true |
| `allUsers` | boolean | Yes | Enables post-call notifications to all users in the location. Default: false |
| `contactAssignedUser` | boolean | Yes | Enables post-call notifications to the user assigned to the contact. Default: false |
| `specificUsers` | array of string | Yes | Array of specific user IDs to receive post-call notifications. Default: [] |
| `customEmails` | array of string | Yes | Array of custom email addresses to receive post-call notifications. Default: [] |

### SendPostCallNotificationSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `admins` | boolean | No | Send notifications to admins |
| `allUsers` | boolean | No | Send notifications to all users |
| `contactAssignedUser` | boolean | No | Send notifications to contact assigned user |
| `specificUsers` | array of string | No | Specific user IDs to notify |
| `customEmails` | array of string | No | Custom email addresses to notify |

### TranslationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Enables language translation for agent conversations. Default: false |
| `language` | string | No | Target language code for translation (e.g., "es" for Spanish, "fr" for French). |

### TranslationSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | No | Whether translation is enabled |
| `language` | string | No | Translation language code |

### UpdateActionResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the created action |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

### UpdateSingleActionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `agentId` | string | Yes | Agent ID to attach the action to |
| `locationId` | string | Yes | Location ID |
| `actionType` | string (enum: `CALL_TRANSFER`, `DATA_EXTRACTION`, `IN_CALL_DATA_EXTRACTION`, `WORKFLOW_TRIGGER`, `SMS`, `APPOINTMENT_BOOKING`, `CUSTOM_ACTION`) | Yes | Type of action |
| `name` | string | Yes | Human-readable name for this action |
| `actionParameters` | object | object | object | object | object | object | object | Yes | Action parameters - structure varies by actionType |

### VoiceAILanguage

Language code for the agent's speech and understanding. Default: "en-US"

**Type:** `string`

**Possible Values:**

- `en-US`
- `pt-BR`
- `es`
- `fr`
- `de`
- `it`
- `nl-NL`
- `multi`

### WorkflowTriggerParameters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `triggerPrompt` | string | Yes | When to trigger this workflow |
| `triggerMessage` | string | Yes | Message to tell the caller |
| `workflowId` | string | Yes | Workflow ID to trigger |
