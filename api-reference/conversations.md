# Conversations API

Documentation for Conversations API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Search](#search)
- [Conversations](#conversations)
- [Preference Management](#preference-management)
- [Email](#email)
- [Messages](#messages)
- [Providers](#providers)

## Search

### GET `/conversations/search`

**Search Conversations**

Returns a list of all conversations matching the search criteria along with the sort and filter options selected.

**Operation ID:** `search-conversation`

**Tags:** Search

**Required Scopes:** `conversations.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `contactId` | query | string | No | Contact Id |
| `assignedTo` | query | string | No | User IDs that conversations are assigned to. Multiple IDs can be provided as comma-separated values. Use "unassigned" to fetch conversations not assigned to any user. |
| `followers` | query | string | No | User IDs of followers to filter conversations by. Multiple IDs can be provided as comma-separated values. |
| `mentions` | query | string | No | User Id of the mention. Multiple values are comma separated. |
| `query` | query | string | No | Search paramater as a string |
| `sort` | query | string (enum: `asc`, `desc`) | No | Sort paramater - asc or desc |
| `startAfterDate` | query | any | No | Search to begin after the specified date - should contain the sort value of the last document |
| `id` | query | string | No | Id of the conversation |
| `limit` | query | number | No | Limit of conversations - Default is 20 |
| `lastMessageType` | query | string (enum: `TYPE_CALL`, `TYPE_SMS`, `TYPE_RCS`, `TYPE_EMAIL`, `TYPE_SMS_REVIEW_REQUEST`, `TYPE_WEBCHAT`, `TYPE_SMS_NO_SHOW_REQUEST`, `TYPE_CAMPAIGN_SMS`, `TYPE_CAMPAIGN_CALL`, `TYPE_CAMPAIGN_EMAIL`, `TYPE_CAMPAIGN_VOICEMAIL`, `TYPE_FACEBOOK`, `TYPE_CAMPAIGN_FACEBOOK`, `TYPE_CAMPAIGN_MANUAL_CALL`, `TYPE_CAMPAIGN_MANUAL_SMS`, `TYPE_GMB`, `TYPE_CAMPAIGN_GMB`, `TYPE_REVIEW`, `TYPE_INSTAGRAM`, `TYPE_WHATSAPP`, `TYPE_CUSTOM_SMS`, `TYPE_CUSTOM_EMAIL`, `TYPE_CUSTOM_PROVIDER_SMS`, `TYPE_CUSTOM_PROVIDER_EMAIL`, `TYPE_IVR_CALL`, `TYPE_ACTIVITY_CONTACT`, `TYPE_ACTIVITY_INVOICE`, `TYPE_ACTIVITY_PAYMENT`, `TYPE_ACTIVITY_OPPORTUNITY`, `TYPE_LIVE_CHAT`, `TYPE_LIVE_CHAT_INFO_MESSAGE`, `TYPE_ACTIVITY_APPOINTMENT`, `TYPE_FACEBOOK_COMMENT`, `TYPE_INSTAGRAM_COMMENT`, `TYPE_CUSTOM_CALL`, `TYPE_INTERNAL_COMMENT`, `TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG`, `TYPE_TIKTOK`, `TYPE_TIKTOK_COMMENT`, `TYPE_ACTIVITY_WHATSAPP`, `TYPE_FORM_SUBMISSION`, `TYPE_SMS_REACTION`) | No | Type of the last message in the conversation as a string |
| `lastMessageAction` | query | string (enum: `automated`, `manual`) | No | Action of the last outbound message in the conversation as string. |
| `lastMessageDirection` | query | string (enum: `inbound`, `outbound`) | No | Direction of the last message in the conversation as string. |
| `status` | query | string (enum: `all`, `read`, `unread`, `starred`, `recents`) | No | The status of the conversation to be filtered - all, read, unread, starred  |
| `sortBy` | query | string (enum: `last_manual_message_date`, `last_message_date`, `score_profile`, `overdue_at`, `due_at`) | No | The sorting of the conversation to be filtered as - manual messages or all messages |
| `sortScoreProfile` | query | string | No | Id of score profile on which sortBy.ScoreProfile should sort on |
| `scoreProfile` | query | string | No | Id of score profile on which conversations should get filtered out, works with scoreProfileMin & scoreProfileMax |
| `scoreProfileMin` | query | number | No | Minimum value for score |
| `scoreProfileMax` | query | number | No | Maximum value for score |
| `startDate` | query | number | No | Start date filter for dateAdded field (Unix timestamp in milliseconds) |
| `endDate` | query | number | No | End date filter for dateAdded field (Unix timestamp in milliseconds) |

#### Responses

**`200` - Successfully fetched the conversations**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversations` | array of object | Yes | The list of all conversations found for the given query |
| `total` | number | Yes | Total Number of results found for the given query |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Conversations

### GET `/conversations/{conversationId}`

**Get Conversation**

Get the conversation details based on the conversation ID

**Operation ID:** `get-conversation`

**Tags:** Conversations

**Required Scopes:** `conversations.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `conversationId` | path | string | Yes | Conversation ID as string |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contactId` | string | Yes | Unique identifier of the contact associated with this conversation |
| `locationId` | string | Yes | Unique identifier of the business location where this conversation takes place |
| `deleted` | boolean | Yes | Flag indicating if this conversation has been moved to trash/deleted |
| `inbox` | boolean | Yes | Flag indicating if this conversation is currently in the main inbox view |
| `type` | number | Yes | Communication channel type for this conversation: 1 (Phone), 2 (Email), 3 (Facebook Messenger), 4 (Review), 5 (Group SMS), 6 (Internal Chat - coming soon) |
| `unreadCount` | number | Yes | Number of messages in this conversation that have not been read by the user |
| `assignedTo` | string | No | Unique identifier of the team member currently responsible for handling this conversation |
| `id` | string | Yes | Unique identifier for this specific conversation thread |
| `starred` | boolean | No | Flag indicating if this conversation has been marked as important/starred by the user |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/conversations/{conversationId}`

**Update Conversation**

Update the conversation details based on the conversation ID

**Operation ID:** `update-conversation`

**Tags:** Conversations

**Required Scopes:** `conversations.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `conversationId` | path | string | Yes | Conversation ID as string |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `unreadCount` | number | No | Count of unread messages in the conversation |
| `starred` | boolean | No | Starred status of the conversation. |
| `feedback` | object | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Boolean value as the API response. |
| `conversation` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/conversations/{conversationId}`

**Delete Conversation**

Delete the conversation details based on the conversation ID

**Operation ID:** `delete-conversation`

**Tags:** Conversations

**Required Scopes:** `conversations.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `conversationId` | path | string | Yes | Conversation ID as string |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Boolean value as the API response. |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/`

**Create Conversation**

Creates a new conversation with the data provided

**Operation ID:** `create-conversation`

**Tags:** Conversations

**Required Scopes:** `conversations.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `contactId` | string | Yes | Contact ID as string |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates whether the API request was successful. |
| `conversation` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Preference Management

### GET `/conversations/preferences/custom-subtypes`

**Get All Custom Subtypes**

Get all custom subtypes for a location

**Operation ID:** `get-all-custom-subtypes`

**Tags:** Preference Management

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/preferences/custom-subtypes`

**Create Custom Subtype**

Create a new custom subtype for a location. Requires agency or account admin role.

**Operation ID:** `create-custom-subtype`

**Tags:** Preference Management

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the custom subtype (max 100 characters) |
| `description` | string | No | Description of the custom subtype (max 100 characters) |
| `channel` | string (enum: `email`, `sms`) | Yes | Communication channel |
| `language` | string | Yes | Language code |

#### Responses

**`200` - Successful response**

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/conversations/preferences/custom-subtypes/{id}`

**Update Custom Subtype**

Update or archive a custom subtype. Requires agency or account admin role.

**Operation ID:** `update-custom-subtype`

**Tags:** Preference Management

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Custom Subtype Id |
| `locationId` | query | string | Yes | Location Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the custom subtype (max 100 characters) |
| `description` | string | No | Description of the custom subtype (max 100 characters) |
| `archived` | boolean | No | Whether the custom subtype is archived |
| `resubscription_legal_form_id` | string | No | Resubscription legal form ID (optional when archiving) |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/conversations/preferences/unsubscriptions/status`

**Get Contact Unsubscription Status**

Get all subscription statuses for a contact (all emails or specific email)

**Operation ID:** `get-contact-unsubscription-status`

**Tags:** Preference Management

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `contactId` | query | string | Yes | Contact Id |
| `email` | query | string | No | Email address (optional - if not provided, gets all emails for contact) |

#### Responses

**`200` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/preferences/unsubscriptions/user-change`

**User Subscription Change**

Process subscription change initiated by a user (admin/agent). Supports individual custom subscription changes and resub all functionality. Legal forms are automatically created for user-initiated resubscribe actions on custom subscriptions.

**Operation ID:** `user-subscription-change`

**Tags:** Preference Management

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `email` | string | Yes | Email address |
| `subscription_action` | object | Yes |  |
| `legal_reason` | string | No | Legal reason for the change (required only for resubscribe and resub_all actions) |
| `legal_description` | string | No | Legal description/details |

**`subscription_action` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `default`, `custom`, `resub_all`) | Yes | Type of subscription action |
| `subtype_name` | string (enum: `One on One`) | No | Subscription type name (required for default types: "One on One") |
| `subtype_id` | string | No | Custom subscription type ID (required for custom types) |
| `subtype_status` | string (enum: `subscribed`, `unsubscribed`) | Yes | Subscription status |

#### Responses

**`200` - Successful response**

**`201` - **

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Email

### GET `/conversations/messages/email/{id}`

**Get email by Id**

Get email by Id

**Operation ID:** `get-email-by-id`

**Tags:** Email

#### Responses

**`200` - Email object for the id given.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `altId` | string | No | External Id |
| `threadId` | string | Yes | Message Id or thread Id |
| `locationId` | string | Yes |  |
| `contactId` | string | Yes |  |
| `conversationId` | string | Yes |  |
| `dateAdded` | string | Yes |  |
| `subject` | string | No |  |
| `body` | string | Yes |  |
| `direction` | string (enum: `inbound`, `outbound`) | Yes |  |
| `status` | string (enum: `pending`, `scheduled`, `sent`, `delivered`, `read`, `undelivered`, `connected`, `failed`, `opened`) | No |  |
| `contentType` | string | Yes |  |
| `attachments` | array of string | No | An array of attachment URLs. |
| `provider` | string | No |  |
| `from` | string | Yes | Name and Email Id of the sender |
| `to` | array of string | Yes | List of email Ids of the receivers |
| `cc` | array of string | No | List of email Ids of the people in the cc field |
| `bcc` | array of string | No | List of email Ids of the people in the bcc field |
| `replyToMessageId` | string | No | In case of reply, email message Id of the reply to email |
| `source` | string (enum: `workflow`, `bulk_actions`, `campaign`, `api`, `app`) | No | Email source |
| `conversationProviderId` | string | No | Conversation provider ID |

---

### DELETE `/conversations/messages/email/{emailMessageId}/schedule`

**Cancel a scheduled email message.**

Post the messageId for the API to delete a scheduled email message. 

**Operation ID:** `cancel-scheduled-email-message`

**Tags:** Email

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `emailMessageId` | path | string | Yes | Email Message Id |

#### Responses

**`200` - The scheduled email message was cancelled successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | number | Yes | HTTP Status code of the request |
| `message` | string | Yes | Error message of the request |

---

## Messages

### GET `/conversations/messages/export`

**Export messages by location ID**

Export messages for a specific location with cursor-based pagination support. Response includes messageType (string), source, and subType fields. The channel parameter is optional - if not provided, all non-email message types will be returned including activity messages (opportunity updates, appointments, etc.).

**Operation ID:** `export-messages-by-location`

**Tags:** Messages

**Required Scopes:** `conversations/message.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location ID to filter messages by |
| `limit` | query | number | No | Number of messages to return per page |
| `cursor` | query | string | No | Cursor for pagination. Pass the nextCursor from previous response to get next page. |
| `sortBy` | query | string (enum: `createdAt`, `updatedAt`) | No | Field to sort by |
| `sortOrder` | query | string (enum: `asc`, `desc`) | No | Sort order |
| `conversationId` | query | string | No | Filter messages by conversation ID |
| `contactId` | query | string | No | Filter messages by contact ID |
| `channel` | query | string (enum: `Call`, `SMS`, `Email`, `WhatsApp`, `Instagram`, `Facebook`) | No | Filter by message channel. If not provided, all non-email message types will be returned including activity messages (opportunity updates, appointments, etc.) |
| `startDate` | query | string | No | Start date to filter messages by |
| `endDate` | query | string | No | End date to filter messages by |

#### Responses

**`200` - List of messages for the location with pagination details.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `messages` | array of object | Yes | Array of messages |
| `nextCursor` | string | No | Cursor for fetching next page. Null if no more results. |
| `total` | number | Yes | Total number of messages matching the query |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/conversations/messages/{id}`

**Get message by message id**

Get message by message id.

**Operation ID:** `get-message`

**Tags:** Messages

**Required Scopes:** `conversations/message.readonly`

**API Version:** `2021-04-15`

#### Responses

**`200` - Message object for the id given.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `type` | number | Yes |  |
| `messageType` | string (enum: `TYPE_CALL`, `TYPE_SMS`, `TYPE_RCS`, `TYPE_EMAIL`, `TYPE_SMS_REVIEW_REQUEST`, `TYPE_WEBCHAT`, `TYPE_SMS_NO_SHOW_REQUEST`, `TYPE_CAMPAIGN_SMS`, `TYPE_CAMPAIGN_CALL`, `TYPE_CAMPAIGN_EMAIL`, `TYPE_CAMPAIGN_VOICEMAIL`, `TYPE_FACEBOOK`, `TYPE_CAMPAIGN_FACEBOOK`, `TYPE_CAMPAIGN_MANUAL_CALL`, `TYPE_CAMPAIGN_MANUAL_SMS`, `TYPE_GMB`, `TYPE_CAMPAIGN_GMB`, `TYPE_REVIEW`, `TYPE_INSTAGRAM`, `TYPE_WHATSAPP`, `TYPE_CUSTOM_SMS`, `TYPE_CUSTOM_EMAIL`, `TYPE_CUSTOM_PROVIDER_SMS`, `TYPE_CUSTOM_PROVIDER_EMAIL`, `TYPE_IVR_CALL`, `TYPE_ACTIVITY_CONTACT`, `TYPE_ACTIVITY_INVOICE`, `TYPE_ACTIVITY_PAYMENT`, `TYPE_ACTIVITY_OPPORTUNITY`, `TYPE_LIVE_CHAT`, `TYPE_LIVE_CHAT_INFO_MESSAGE`, `TYPE_ACTIVITY_APPOINTMENT`, `TYPE_FACEBOOK_COMMENT`, `TYPE_INSTAGRAM_COMMENT`, `TYPE_CUSTOM_CALL`, `TYPE_INTERNAL_COMMENT`, `TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG`, `TYPE_TIKTOK`, `TYPE_TIKTOK_COMMENT`, `TYPE_ACTIVITY_WHATSAPP`, `TYPE_FORM_SUBMISSION`, `TYPE_SMS_REACTION`) | Yes | Type of the message as a string |
| `locationId` | string | Yes |  |
| `contactId` | string | Yes |  |
| `conversationId` | string | Yes |  |
| `dateAdded` | string | Yes |  |
| `body` | string | No |  |
| `direction` | string (enum: `inbound`, `outbound`) | Yes |  |
| `status` | string (enum: `connected`, `delivered`, `failed`, `opened`, `pending`, `read`, `scheduled`, `sent`, `undelivered`, `clicked`, `opt_out`, `queued`) | No |  |
| `contentType` | string | Yes |  |
| `attachments` | array of string | No | An array of attachment URLs. Attachments will be empty for Call and Voicemails, type 1 and 10. Please use get call recording API to fetch call recording and voicemails. |
| `meta` | object | No |  |
| `source` | string (enum: `workflow`, `bulk_actions`, `campaign`, `api`, `app`) | No | Message source |
| `userId` | string | No | User Id |
| `conversationProviderId` | string | No | Conversation Provider Id |
| `chatWidgetId` | string | No | Chat Widget Id |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/conversations/{conversationId}/messages`

**Get messages by conversation id**

Get messages by conversation id.

**Operation ID:** `get-messages`

**Tags:** Messages

**Required Scopes:** `conversations/message.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `conversationId` | path | string | Yes | Conversation ID as string |
| `lastMessageId` | query | string | No | Message ID of the last message in the list as a string |
| `limit` | query | number | No | Number of messages to be fetched from the conversation. Default limit is 20 |
| `type` | query | string (enum: `TYPE_CALL`, `TYPE_SMS`, `TYPE_RCS`, `TYPE_EMAIL`, `TYPE_FACEBOOK`, `TYPE_GMB`, `TYPE_INSTAGRAM`, `TYPE_WHATSAPP`, `TYPE_ACTIVITY_APPOINTMENT`, `TYPE_ACTIVITY_CONTACT`, `TYPE_ACTIVITY_INVOICE`, `TYPE_ACTIVITY_PAYMENT`, `TYPE_ACTIVITY_OPPORTUNITY`, `TYPE_LIVE_CHAT`, `TYPE_INTERNAL_COMMENTS`, `TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG`, `TYPE_TIKTOK`, `TYPE_ACTIVITY_WHATSAPP`, `TYPE_FORM_SUBMISSION`) | No | Types of message to fetched separated with comma |

#### Responses

**`200` - List of messages for the conversation id of the given type.**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `lastMessageId` | string | Yes | Id of the last message in the messages array |
| `nextPage` | boolean | Yes | Next page value true indicates only 20 message is in the response. Rest of the messages are in the next page. Please use the lastMessageId value in the query to get the next page messages |
| `messages` | array of object | Yes | Array of messages |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/messages`

**Send a new message**

Post the necessary fields for the API to send a new message.

**Operation ID:** `send-a-new-message`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `SMS`, `RCS`, `Email`, `WhatsApp`, `IG`, `FB`, `Custom`, `Live_Chat`, `TIKTOK`) | Yes | Type of message being sent |
| `subType` | object | Yes | Type of message being sent |
| `contactId` | string | Yes | ID of the contact receiving the message |
| `appointmentId` | string | No | ID of the associated appointment |
| `attachments` | array of string | No | Array of attachment URLs |
| `emailFrom` | string | No | Email address to send from |
| `emailCc` | array of string | No | Array of CC email addresses |
| `emailBcc` | array of string | No | Array of BCC email addresses |
| `html` | string | No | HTML content of the message |
| `message` | string | No | Text content of the message |
| `subject` | string | No | Subject line for email messages |
| `replyMessageId` | string | No | ID of message being replied to |
| `templateId` | string | No | ID of message template |
| `threadId` | string | No | ID of message thread. For email messages, this is the message ID that contains multiple email messages in the thread |
| `scheduledTimestamp` | number | No | UTC Timestamp (in seconds) at which the message should be scheduled |
| `conversationProviderId` | string | No | ID of conversation provider |
| `emailTo` | string | No | Email address to send to, if different from contact's primary email. This should be a valid email address associated with the contact. |
| `customSubtypeId` | string | No | Custom subtype ID for email unsubscription preferences. Only applies to email messages. |
| `emailReplyMode` | string (enum: `reply`, `reply_all`) | No | Mode for email replies |
| `fromNumber` | string | No | Phone number used as the sender number for outbound messages |
| `toNumber` | string | No | Recipient phone number for outbound messages |
| `forward` | object | No |  |
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |
| `usesNativeSchedulingAi` | boolean | No | Whether the scheduled email uses native AI for the email scheduling  |
| `optimizationPeriod` | string (enum: `24h`, `48h`, `72h`) | No | Optimization period in hours (24h, 48h, or 72h) |

**`forward` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isForwarded` | boolean | Yes | Specify if this is a forwarded email |
| `forwardWholeThread` | boolean | No | Specify if forwarding the whole thread or just a single email |
| `messageId` | string | No | Message ID of the email thread being forwarded (source) - REQUIRED for forwarding |
| `emailMessageId` | string | No | Email Message ID of the specific email being forwarded (source) - Required for single email forward, ignored for thread forward |
| `sourceContactId` | string | No | Contact ID where the forwarded email originated from (source) - Auto-populated if not provided |
| `sourceConversationId` | string | No | Conversation ID where the forwarded email originated from (source) - Auto-populated if not provided |
| `toEmail` | string | No | Email address to forward to (destination) |
| `recipientContactId` | string | No | Contact ID of recipient when forwarding (destination) |
| `recipientConversationId` | string | No | Conversation ID of recipient when forwarding (destination) |

#### Responses

**`200` - Created the message**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation ID. |
| `emailMessageId` | string | No | This contains the email message id (only for Email type). Use this ID to send inbound replies to GHL to create a threaded email. |
| `messageId` | string | Yes | This is the main Message ID |
| `messageIds` | array of string | No | When sending via the GMB channel, we will be returning list of `messageIds` instead of single `messageId`. |
| `msg` | string | No | Additional response message when sending a workflow message |
| `forwardData` | object | No |  |
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/messages/inbound`

**Add an inbound message**

Post the necessary fields for the API to add a new inbound message. 

**Operation ID:** `add-an-inbound-message`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `SMS`, `RCS`, `Email`, `WhatsApp`, `GMB`, `IG`, `FB`, `Custom`, `WebChat`, `Live_Chat`, `Call`, `IVR_Call`, `Campaign_Call`, `Campaign_VoiceMail`, `TIKTOK`, `ALL_IN_ONE_CHAT`, `FORM_SUBMISSION`) | Yes | Message Type |
| `attachments` | array of string | No | Array of attachments |
| `message` | string | No | Message Body |
| `conversationId` | string | Yes | Conversation Id |
| `contactId` | string | Yes | Contact Id |
| `conversationProviderId` | string | Yes | Conversation Provider Id |
| `html` | string | No | HTML Body of Email |
| `subject` | string | No | Subject of the Email |
| `emailFrom` | string | No | Email address to send from. This field is associated with the contact record and cannot be dynamically changed. |
| `emailTo` | string | No | Recipient email address. This field is associated with the contact record and cannot be dynamically changed. |
| `emailCc` | array of string | No | List of email address to CC |
| `emailBcc` | array of string | No | List of email address to BCC |
| `emailMessageId` | string | No | Send the email message id for which this email should be threaded. This is for replying to a specific email |
| `altId` | string | No | external mail provider's message id |
| `direction` | object | No | Message direction, if required can be set manually, default is outbound Default: `outbound` |
| `date` | string | No | Date of the inbound message |
| `call` | object | No |  |

**`call` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `to` | string | No | Phone number of the receiver |
| `from` | string | No | Phone number of the dialer |
| `status` | string (enum: `pending`, `completed`, `answered`, `busy`, `no-answer`, `failed`, `canceled`, `voicemail`) | No | Call status |

#### Responses

**`200` - Created the message**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |
| `conversationId` | string | Yes | Conversation ID. |
| `messageId` | string | Yes | This is the main Message ID |
| `message` | string | Yes |  |
| `contactId` | string | No |  |
| `dateAdded` | string | No |  |
| `emailMessageId` | string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/messages/outbound`

**Add an external outbound call**

Post the necessary fields for the API to add a new outbound call.

**Operation ID:** `add-an-outbound-message`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `Call`) | Yes | Message Type |
| `attachments` | array of string | No | Array of attachments |
| `conversationId` | string | Yes | Conversation Id |
| `conversationProviderId` | string | Yes | Conversation Provider Id |
| `altId` | string | No | external mail provider's message id |
| `date` | string | No | Date of the outbound message |
| `call` | object | No |  |

**`call` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `to` | string | No | Phone number of the receiver |
| `from` | string | No | Phone number of the dialer |
| `status` | string (enum: `pending`, `completed`, `answered`, `busy`, `no-answer`, `failed`, `canceled`, `voicemail`) | No | Call status |

#### Responses

**`200` - Created the message**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |
| `conversationId` | string | Yes | Conversation ID. |
| `messageId` | string | Yes | This is the main Message ID |
| `message` | string | Yes |  |
| `contactId` | string | No |  |
| `dateAdded` | string | No |  |
| `emailMessageId` | string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/messages/review-reply`

**Send a review reply to Google My Business**

Post a reply to a customer review on Google My Business

**Operation ID:** `send-review-reply`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation ID (must have reviewId) |
| `locationId` | string | Yes | Location ID |
| `message` | string | Yes | Review reply message text |

#### Responses

**`200` - Review reply sent successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation ID. |
| `emailMessageId` | string | No | This contains the email message id (only for Email type). Use this ID to send inbound replies to GHL to create a threaded email. |
| `messageId` | string | Yes | This is the main Message ID |
| `messageIds` | array of string | No | When sending via the GMB channel, we will be returning list of `messageIds` instead of single `messageId`. |
| `msg` | string | No | Additional response message when sending a workflow message |
| `forwardData` | object | No |  |
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/conversations/messages/{messageId}/schedule`

**Cancel a scheduled message.**

Post the messageId for the API to delete a scheduled message. 

**Operation ID:** `cancel-scheduled-message`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `messageId` | path | string | Yes | Message Id |

#### Responses

**`200` - The scheduled message was cancelled successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | number | Yes | HTTP Status code of the request |
| `message` | string | Yes | Error message of the request |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/conversations/messages/upload`

**Upload file attachments**

Post the necessary fields for the API to upload files. The files need to be a buffer with the key "fileAttachment".  The allowed file types are: 
 JPGJPEGPNGMP4MPEGZIPRARPDFDOCDOCXTXTMP3WAV  The API will return an object with the URLs

**Operation ID:** `upload-file-attachments`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `multipart/form-data`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation Id |
| `contactId` | string | Yes | Contact Id |
| `locationId` | string | Yes |  |
| `attachmentUrls` | array of string | Yes |  |
| `chatServiceSid` | string | No | Twilio chat service SID for group SMS uploads |
| `isGroupSms` | string | No | Flag to indicate group SMS upload flow. When true, only 1 file upload is allowed per request. |

#### Responses

**`200` - Uploaded the file successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadedFiles` | object | Yes |  |
| `twilioMediaSids` | array of string | No | Twilio media SIDs for group SMS (when isGroupSms=true) |

**`400` - Bad Request**

**`401` - Unauthorized**

**`413` - Payload Too Large**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | number (enum: `400`, `413`, `415`) | Yes | HTTP Status code of the request |
| `message` | string | Yes | Error message of the request |

**`415` - Unsupported Media Type**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | number (enum: `400`, `413`, `415`) | Yes | HTTP Status code of the request |
| `message` | string | Yes | Error message of the request |

---

### POST `/conversations/messages/upload/initiate`

**Initiate file upload to GCS**

Generates a signed URL for direct file upload to Google Cloud Storage. Returns a signed URL valid for 15 minutes. Upload file via PUT request, then call /complete to finalize.

**Operation ID:** `initiate-file-upload`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID |
| `conversationId` | string | Yes | Conversation ID |
| `filename` | string | Yes | Original filename with extension |
| `contentType` | string | Yes | MIME type of the file |
| `fileSize` | number | No | File size in bytes (optional, for pre-validation) |
| `channel` | string | Yes | Channel type for size limits (WHATSAPP for 100MB limit, others for 5MB) |

#### Responses

**`200` - Signed URL generated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadUrl` | string | Yes | Signed URL for direct upload to GCS. Use PUT request with file content. |
| `uploadId` | string | Yes | Unique upload ID for tracking and completing the upload |
| `filePath` | string | Yes | File path in GCS bucket (needed for confirmation endpoint) |
| `expiresAt` | number | Yes | URL expiration timestamp (Unix milliseconds) |
| `maxFileSize` | number | Yes | Maximum allowed file size in bytes |

**`400` - Bad Request - Invalid parameters**

**`401` - Unauthorized**

**`413` - File size exceeds maximum allowed limit**

---

### POST `/conversations/messages/upload/complete`

**Complete file upload**

Validates the uploaded file in GCS and returns the public URL. Call this endpoint after successfully uploading the file to the signed URL.

**Operation ID:** `complete-file-upload`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadId` | string | Yes | Upload ID from request response |
| `filePath` | string | Yes | File path from request response |
| `locationId` | string | Yes | Location ID |
| `conversationId` | string | Yes | Conversation ID |
| `filename` | string | Yes | Original filename (for response mapping) |

#### Responses

**`200` - Upload completed successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadedFiles` | object | Yes | Map of filename to public URL |
| `metadata` | object | Yes | File metadata |

**`400` - Bad Request - Invalid parameters**

**`401` - Unauthorized**

**`404` - File not found in storage - upload may have failed or URL expired**

---

### PUT `/conversations/messages/{messageId}/status`

**Update message status**

Post the necessary fields for the API to update message status.

**Operation ID:** `update-message-status`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `messageId` | path | string | Yes | Message Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |
| `error` | object | No |  |
| `emailMessageId` | string | No | Email message Id |
| `recipients` | array of string | No | Email delivery status for additional email recipients. |

**`error` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | string | Yes | Error Code |
| `type` | string | Yes | Error Type |
| `message` | string | Yes | Error Message |

#### Responses

**`200` - Created the message**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation ID. |
| `emailMessageId` | string | No | This contains the email message id (only for Email type). Use this ID to send inbound replies to GHL to create a threaded email. |
| `messageId` | string | Yes | This is the main Message ID |
| `messageIds` | array of string | No | When sending via the GMB channel, we will be returning list of `messageIds` instead of single `messageId`. |
| `msg` | string | No | Additional response message when sending a workflow message |
| `forwardData` | object | No |  |
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/conversations/messages/{messageId}/attachments`

**Add message attachments**

Set attachments on an existing message (replaces existing). Maximum 5 URLs. Supported for TYPE_CUSTOM_CALL (34) and TYPE_CALL (1) with subType EXTERNAL_CALL.

**Operation ID:** `add-message-attachments`

**Tags:** Messages

**Required Scopes:** `conversations/message.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `messageId` | path | string | Yes | Message Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `attachments` | array of string | Yes | Array of attachment URLs to set on the message (replaces existing). Maximum 5 URLs. |

#### Responses

**`200` - Successfully set message attachments**

**`400` - Bad Request**

**`401` - Unauthorized**

**`403` - Message type does not support attachment updates**

**`404` - Message not found**

---

### GET `/conversations/messages/{messageId}/locations/{locationId}/recording`

**Get Recording by Message ID**

Get the recording for a message by passing the message id

**Operation ID:** `get-message-recording`

**Tags:** Messages

**Required Scopes:** `conversations/message.readonly`, `conversations/message.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID as string |
| `messageId` | path | string | Yes | Message ID as string |

#### Responses

**`200` - Gives the attached recording to the message**

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/conversations/locations/{locationId}/messages/{messageId}/transcription`

**Get transcription by Message ID**

Get the recording transcription for a message by passing the message id

**Operation ID:** `get-message-transcription`

**Tags:** Messages

**Required Scopes:** `conversations/message.readonly`, `conversations/message.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID as string |
| `messageId` | path | string | Yes | Message ID as string |

#### Responses

**`200` - Gives the attached recording transcription to the message**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaChannel` | number | Yes | Media channel describes the user interaction channel |
| `sentenceIndex` | number | Yes | Index of the sentence in the transcription |
| `startTime` | number | Yes | Start time of the sentence in milliseconds |
| `endTime` | number | Yes | End time of the sentence in milliseconds |
| `transcript` | string | Yes | Transcript of the sentence |
| `confidence` | number | Yes | Confidence of the transcription |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/conversations/locations/{locationId}/messages/{messageId}/transcription/download`

**Download transcription by Message ID**

Download the recording transcription for a message by passing the message id

**Operation ID:** `download-message-transcription`

**Tags:** Messages

**Required Scopes:** `conversations/message.readonly`, `conversations/message.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | path | string | Yes | Location ID as string |
| `messageId` | path | string | Yes | Message ID as string |

#### Responses

**`200` - Downloads the attached transcription of the message**

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Providers

### POST `/conversations/providers/live-chat/typing`

**Agent/Ai-Bot is typing a message indicator for live chat**

Agent/AI-Bot will call this when they are typing a message in live chat message

**Operation ID:** `live-chat-agent-typing`

**Tags:** Providers

**Required Scopes:** `conversations/livechat.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `isTyping` | string | Yes | Typing status |
| `visitorId` | string | Yes | visitorId is the Unique ID assigned to each Live chat visitor. visitorId will be added soon in <a href="https://highlevel.stoplight.io/docs/integrations/00c5ff21f0030-get-contact" target="_blank">GET ... |
| `conversationId` | string | Yes | Conversation Id |

#### Responses

**`201` - Show typing indicator for live chat**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AddMessageAttachmentsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `attachments` | array of string | Yes | Array of attachment URLs to set on the message (replaces existing). Maximum 5 URLs. |

### CallDataDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `to` | string | No | Phone number of the receiver |
| `from` | string | No | Phone number of the dialer |
| `status` | string (enum: `pending`, `completed`, `answered`, `busy`, `no-answer`, `failed`, `canceled`, `voicemail`) | No | Call status |

### CancelScheduledResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | number | Yes | HTTP Status code of the request |
| `message` | string | Yes | Error message of the request |

### CompleteFileUploadDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadId` | string | Yes | Upload ID from request response |
| `filePath` | string | Yes | File path from request response |
| `locationId` | string | Yes | Location ID |
| `conversationId` | string | Yes | Conversation ID |
| `filename` | string | Yes | Original filename (for response mapping) |

### CompleteFileUploadResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadedFiles` | object | Yes | Map of filename to public URL |
| `metadata` | object | Yes | File metadata |

### ConversationCreateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the conversation |
| `dateUpdated` | string | Yes | Date when the conversation was last updated |
| `dateAdded` | string | Yes | Date when the conversation was created |
| `deleted` | boolean | Yes | Flag indicating if this conversation has been deleted |
| `contactId` | string | Yes | Unique identifier of the contact associated with this conversation |
| `locationId` | string | Yes | Unique identifier of the business location where this conversation takes place |
| `lastMessageDate` | string | Yes | Date of the last message in the conversation |
| `assignedTo` | string | No | Unique identifier of the team member assigned to this conversation |

### ConversationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No | Contact ID as string |
| `locationId` | string | Yes | Location ID as string |
| `contactId` | string | Yes | Contact ID as string |
| `assignedTo` | string | No | Assigned User ID as string |
| `userId` | string | No | User ID as string |
| `lastMessageBody` | string | No | Last message body as string |
| `lastMessageDate` | string | No | Last message date as UTC |
| `lastMessageType` | string (enum: `TYPE_CALL`, `TYPE_SMS`, `TYPE_RCS`, `TYPE_EMAIL`, `TYPE_SMS_REVIEW_REQUEST`, `TYPE_WEBCHAT`, `TYPE_SMS_NO_SHOW_REQUEST`, `TYPE_CAMPAIGN_SMS`, `TYPE_CAMPAIGN_CALL`, `TYPE_CAMPAIGN_EMAIL`, `TYPE_CAMPAIGN_VOICEMAIL`, `TYPE_FACEBOOK`, `TYPE_CAMPAIGN_FACEBOOK`, `TYPE_CAMPAIGN_MANUAL_CALL`, `TYPE_CAMPAIGN_MANUAL_SMS`, `TYPE_GMB`, `TYPE_CAMPAIGN_GMB`, `TYPE_REVIEW`, `TYPE_INSTAGRAM`, `TYPE_WHATSAPP`, `TYPE_CUSTOM_SMS`, `TYPE_CUSTOM_EMAIL`, `TYPE_CUSTOM_PROVIDER_SMS`, `TYPE_CUSTOM_PROVIDER_EMAIL`, `TYPE_IVR_CALL`, `TYPE_ACTIVITY_CONTACT`, `TYPE_ACTIVITY_INVOICE`, `TYPE_ACTIVITY_PAYMENT`, `TYPE_ACTIVITY_OPPORTUNITY`, `TYPE_LIVE_CHAT`, `TYPE_LIVE_CHAT_INFO_MESSAGE`, `TYPE_ACTIVITY_APPOINTMENT`, `TYPE_FACEBOOK_COMMENT`, `TYPE_INSTAGRAM_COMMENT`, `TYPE_CUSTOM_CALL`, `TYPE_INTERNAL_COMMENT`, `TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG`, `TYPE_TIKTOK`, `TYPE_TIKTOK_COMMENT`, `TYPE_ACTIVITY_WHATSAPP`, `TYPE_FORM_SUBMISSION`, `TYPE_SMS_REACTION`) | No | Type of the last message sent/received in the conversation. |
| `unreadCount` | number | No | Count of unread messages in the conversation |
| `inbox` | boolean | No | Inbox status of the conversation. |
| `starred` | boolean | No | Starred status of the conversation. |
| `deleted` | boolean | Yes | Deleted status of the conversation. |

### ConversationSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Conversation Id |
| `contactId` | string | Yes | Contact Id |
| `locationId` | string | Yes | Location Id |
| `lastMessageBody` | string | Yes | Content of the most recent message in the conversation |
| `lastMessageType` | string (enum: `TYPE_CALL`, `TYPE_SMS`, `TYPE_RCS`, `TYPE_EMAIL`, `TYPE_SMS_REVIEW_REQUEST`, `TYPE_WEBCHAT`, `TYPE_SMS_NO_SHOW_REQUEST`, `TYPE_CAMPAIGN_SMS`, `TYPE_CAMPAIGN_CALL`, `TYPE_CAMPAIGN_EMAIL`, `TYPE_CAMPAIGN_VOICEMAIL`, `TYPE_FACEBOOK`, `TYPE_CAMPAIGN_FACEBOOK`, `TYPE_CAMPAIGN_MANUAL_CALL`, `TYPE_CAMPAIGN_MANUAL_SMS`, `TYPE_GMB`, `TYPE_CAMPAIGN_GMB`, `TYPE_REVIEW`, `TYPE_INSTAGRAM`, `TYPE_WHATSAPP`, `TYPE_CUSTOM_SMS`, `TYPE_CUSTOM_EMAIL`, `TYPE_CUSTOM_PROVIDER_SMS`, `TYPE_CUSTOM_PROVIDER_EMAIL`, `TYPE_IVR_CALL`, `TYPE_ACTIVITY_CONTACT`, `TYPE_ACTIVITY_INVOICE`, `TYPE_ACTIVITY_PAYMENT`, `TYPE_ACTIVITY_OPPORTUNITY`, `TYPE_LIVE_CHAT`, `TYPE_LIVE_CHAT_INFO_MESSAGE`, `TYPE_ACTIVITY_APPOINTMENT`, `TYPE_FACEBOOK_COMMENT`, `TYPE_INSTAGRAM_COMMENT`, `TYPE_CUSTOM_CALL`, `TYPE_INTERNAL_COMMENT`, `TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG`, `TYPE_TIKTOK`, `TYPE_TIKTOK_COMMENT`, `TYPE_ACTIVITY_WHATSAPP`, `TYPE_FORM_SUBMISSION`, `TYPE_SMS_REACTION`) | Yes | Channel/type of the most recent message (SMS, Email, Call, etc) |
| `type` | string (enum: `TYPE_PHONE`, `TYPE_EMAIL`, `TYPE_FB_MESSENGER`, `TYPE_REVIEW`, `TYPE_GROUP_SMS`) | Yes | Primary channel/type of the conversation (Phone, Email, etc) |
| `unreadCount` | number | Yes | Number of unread messages in this conversation |
| `fullName` | string | Yes | Complete name of the contact (first and last name) |
| `contactName` | string | Yes | Alternative display name for the contact - used when full name is not available |
| `email` | string | Yes | Primary email address of the contact |
| `phone` | string | Yes | Primary phone number of the contact |

### CreateConversationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `contactId` | string | Yes | Contact ID as string |

### CreateConversationSuccessResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Indicates whether the API request was successful. |
| `conversation` | object | Yes |  |

### CreateCustomSubtypeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the custom subtype (max 100 characters) |
| `description` | string | No | Description of the custom subtype (max 100 characters) |
| `channel` | string (enum: `email`, `sms`) | Yes | Communication channel |
| `language` | string | Yes | Language code |

### CreateLiveChatMessageFeedbackResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |

### DeleteConversationSuccessfulResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Boolean value as the API response. |

### ErrorDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | string | Yes | Error Code |
| `type` | string | Yes | Error Type |
| `message` | string | Yes | Error Message |

### ExportMessagesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `messages` | array of object | Yes | Array of messages |
| `nextCursor` | string | No | Cursor for fetching next page. Null if no more results. |
| `total` | number | Yes | Total number of messages matching the query |

### ForwardConfigDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isForwarded` | boolean | Yes | Specify if this is a forwarded email |
| `forwardWholeThread` | boolean | No | Specify if forwarding the whole thread or just a single email |
| `messageId` | string | No | Message ID of the email thread being forwarded (source) - REQUIRED for forwarding |
| `emailMessageId` | string | No | Email Message ID of the specific email being forwarded (source) - Required for single email forward, ignored for thread forward |
| `sourceContactId` | string | No | Contact ID where the forwarded email originated from (source) - Auto-populated if not provided |
| `sourceConversationId` | string | No | Conversation ID where the forwarded email originated from (source) - Auto-populated if not provided |
| `toEmail` | string | No | Email address to forward to (destination) |
| `recipientContactId` | string | No | Contact ID of recipient when forwarding (destination) |
| `recipientConversationId` | string | No | Conversation ID of recipient when forwarding (destination) |

### ForwardResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `forwardWholeThread` | boolean | No | Whether the entire thread was forwarded |
| `messageId` | string | No | Message ID of the forwarded message (source) |
| `emailMessageId` | string | No | Email Message ID of the forwarded email (source) |
| `sourceContactId` | string | No | Contact ID where the forwarded email originated from (source) |
| `sourceConversationId` | string | No | Conversation ID where the forwarded email originated from (source) |
| `forwardToEmail` | string | No | Email address the message was forwarded to (destination) |
| `recipientContactId` | string | No | Contact ID of the recipient of the forwarded email (destination) |
| `recipientConversationId` | string | No | Conversation ID of the recipient of the forwarded email (destination) |

### GetConversationByIdResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contactId` | string | Yes | Unique identifier of the contact associated with this conversation |
| `locationId` | string | Yes | Unique identifier of the business location where this conversation takes place |
| `deleted` | boolean | Yes | Flag indicating if this conversation has been moved to trash/deleted |
| `inbox` | boolean | Yes | Flag indicating if this conversation is currently in the main inbox view |
| `type` | number | Yes | Communication channel type for this conversation: 1 (Phone), 2 (Email), 3 (Facebook Messenger), 4 (Review), 5 (Group SMS), 6 (Internal Chat - coming soon) |
| `unreadCount` | number | Yes | Number of messages in this conversation that have not been read by the user |
| `assignedTo` | string | No | Unique identifier of the team member currently responsible for handling this conversation |
| `id` | string | Yes | Unique identifier for this specific conversation thread |
| `starred` | boolean | No | Flag indicating if this conversation has been marked as important/starred by the user |

### GetConversationSuccessfulResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Boolean value as the API response. |
| `conversation` | object | Yes |  |

### GetEmailMessageResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `altId` | string | No | External Id |
| `threadId` | string | Yes | Message Id or thread Id |
| `locationId` | string | Yes |  |
| `contactId` | string | Yes |  |
| `conversationId` | string | Yes |  |
| `dateAdded` | string | Yes |  |
| `subject` | string | No |  |
| `body` | string | Yes |  |
| `direction` | string (enum: `inbound`, `outbound`) | Yes |  |
| `status` | string (enum: `pending`, `scheduled`, `sent`, `delivered`, `read`, `undelivered`, `connected`, `failed`, `opened`) | No |  |
| `contentType` | string | Yes |  |
| `attachments` | array of string | No | An array of attachment URLs. |
| `provider` | string | No |  |
| `from` | string | Yes | Name and Email Id of the sender |
| `to` | array of string | Yes | List of email Ids of the receivers |
| `cc` | array of string | No | List of email Ids of the people in the cc field |
| `bcc` | array of string | No | List of email Ids of the people in the bcc field |
| `replyToMessageId` | string | No | In case of reply, email message Id of the reply to email |
| `source` | string (enum: `workflow`, `bulk_actions`, `campaign`, `api`, `app`) | No | Email source |
| `conversationProviderId` | string | No | Conversation provider ID |

### GetMessageResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes |  |
| `type` | number | Yes |  |
| `messageType` | string (enum: `TYPE_CALL`, `TYPE_SMS`, `TYPE_RCS`, `TYPE_EMAIL`, `TYPE_SMS_REVIEW_REQUEST`, `TYPE_WEBCHAT`, `TYPE_SMS_NO_SHOW_REQUEST`, `TYPE_CAMPAIGN_SMS`, `TYPE_CAMPAIGN_CALL`, `TYPE_CAMPAIGN_EMAIL`, `TYPE_CAMPAIGN_VOICEMAIL`, `TYPE_FACEBOOK`, `TYPE_CAMPAIGN_FACEBOOK`, `TYPE_CAMPAIGN_MANUAL_CALL`, `TYPE_CAMPAIGN_MANUAL_SMS`, `TYPE_GMB`, `TYPE_CAMPAIGN_GMB`, `TYPE_REVIEW`, `TYPE_INSTAGRAM`, `TYPE_WHATSAPP`, `TYPE_CUSTOM_SMS`, `TYPE_CUSTOM_EMAIL`, `TYPE_CUSTOM_PROVIDER_SMS`, `TYPE_CUSTOM_PROVIDER_EMAIL`, `TYPE_IVR_CALL`, `TYPE_ACTIVITY_CONTACT`, `TYPE_ACTIVITY_INVOICE`, `TYPE_ACTIVITY_PAYMENT`, `TYPE_ACTIVITY_OPPORTUNITY`, `TYPE_LIVE_CHAT`, `TYPE_LIVE_CHAT_INFO_MESSAGE`, `TYPE_ACTIVITY_APPOINTMENT`, `TYPE_FACEBOOK_COMMENT`, `TYPE_INSTAGRAM_COMMENT`, `TYPE_CUSTOM_CALL`, `TYPE_INTERNAL_COMMENT`, `TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG`, `TYPE_TIKTOK`, `TYPE_TIKTOK_COMMENT`, `TYPE_ACTIVITY_WHATSAPP`, `TYPE_FORM_SUBMISSION`, `TYPE_SMS_REACTION`) | Yes | Type of the message as a string |
| `locationId` | string | Yes |  |
| `contactId` | string | Yes |  |
| `conversationId` | string | Yes |  |
| `dateAdded` | string | Yes |  |
| `body` | string | No |  |
| `direction` | string (enum: `inbound`, `outbound`) | Yes |  |
| `status` | string (enum: `connected`, `delivered`, `failed`, `opened`, `pending`, `read`, `scheduled`, `sent`, `undelivered`, `clicked`, `opt_out`, `queued`) | No |  |
| `contentType` | string | Yes |  |
| `attachments` | array of string | No | An array of attachment URLs. Attachments will be empty for Call and Voicemails, type 1 and 10. Please use get call recording API to fetch call recording and voicemails. |
| `meta` | object | No |  |
| `source` | string (enum: `workflow`, `bulk_actions`, `campaign`, `api`, `app`) | No | Message source |
| `userId` | string | No | User Id |
| `conversationProviderId` | string | No | Conversation Provider Id |
| `chatWidgetId` | string | No | Chat Widget Id |

### GetMessageTranscriptionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaChannel` | number | Yes | Media channel describes the user interaction channel |
| `sentenceIndex` | number | Yes | Index of the sentence in the transcription |
| `startTime` | number | Yes | Start time of the sentence in milliseconds |
| `endTime` | number | Yes | End time of the sentence in milliseconds |
| `transcript` | string | Yes | Transcript of the sentence |
| `confidence` | number | Yes | Confidence of the transcription |

### GetMessagesByConversationResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `lastMessageId` | string | Yes | Id of the last message in the messages array |
| `nextPage` | boolean | Yes | Next page value true indicates only 20 message is in the response. Rest of the messages are in the next page. Please use the lastMessageId value in the query to get the next page messages |
| `messages` | array of object | Yes | Array of messages |

### InitiateFileUploadDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID |
| `conversationId` | string | Yes | Conversation ID |
| `filename` | string | Yes | Original filename with extension |
| `contentType` | string | Yes | MIME type of the file |
| `fileSize` | number | No | File size in bytes (optional, for pre-validation) |
| `channel` | string | Yes | Channel type for size limits (WHATSAPP for 100MB limit, others for 5MB) |

### InitiateFileUploadResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadUrl` | string | Yes | Signed URL for direct upload to GCS. Use PUT request with file content. |
| `uploadId` | string | Yes | Unique upload ID for tracking and completing the upload |
| `filePath` | string | Yes | File path in GCS bucket (needed for confirmation endpoint) |
| `expiresAt` | number | Yes | URL expiration timestamp (Unix milliseconds) |
| `maxFileSize` | number | Yes | Maximum allowed file size in bytes |

### MessageMeta

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `callDuration` | string | No | Call duration in seconds |
| `callStatus` | string (enum: `pending`, `completed`, `answered`, `busy`, `no-answer`, `failed`, `canceled`, `voicemail`) | No | Call status - can be pending, completed, answered, busy, no-answer, failed, canceled, or voicemail |
| `email` | object | No | meta will contain email, for message type 3 (email). messageIds is list of all email message ids under the message thread |

### ProcessMessageBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `SMS`, `RCS`, `Email`, `WhatsApp`, `GMB`, `IG`, `FB`, `Custom`, `WebChat`, `Live_Chat`, `Call`, `IVR_Call`, `Campaign_Call`, `Campaign_VoiceMail`, `TIKTOK`, `ALL_IN_ONE_CHAT`, `FORM_SUBMISSION`) | Yes | Message Type |
| `attachments` | array of string | No | Array of attachments |
| `message` | string | No | Message Body |
| `conversationId` | string | Yes | Conversation Id |
| `contactId` | string | Yes | Contact Id |
| `conversationProviderId` | string | Yes | Conversation Provider Id |
| `html` | string | No | HTML Body of Email |
| `subject` | string | No | Subject of the Email |
| `emailFrom` | string | No | Email address to send from. This field is associated with the contact record and cannot be dynamically changed. |
| `emailTo` | string | No | Recipient email address. This field is associated with the contact record and cannot be dynamically changed. |
| `emailCc` | array of string | No | List of email address to CC |
| `emailBcc` | array of string | No | List of email address to BCC |
| `emailMessageId` | string | No | Send the email message id for which this email should be threaded. This is for replying to a specific email |
| `altId` | string | No | external mail provider's message id |
| `direction` | object | No | Message direction, if required can be set manually, default is outbound Default: `outbound` |
| `date` | string | No | Date of the inbound message |
| `call` | object | No |  |

### ProcessMessageResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes |  |
| `conversationId` | string | Yes | Conversation ID. |
| `messageId` | string | Yes | This is the main Message ID |
| `message` | string | Yes |  |
| `contactId` | string | No |  |
| `dateAdded` | string | No |  |
| `emailMessageId` | string | No |  |

### ProcessOutboundMessageBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `Call`) | Yes | Message Type |
| `attachments` | array of string | No | Array of attachments |
| `conversationId` | string | Yes | Conversation Id |
| `conversationProviderId` | string | Yes | Conversation Provider Id |
| `altId` | string | No | external mail provider's message id |
| `date` | string | No | Date of the outbound message |
| `call` | object | No |  |

### SendConversationResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversations` | array of object | Yes | The list of all conversations found for the given query |
| `total` | number | Yes | Total Number of results found for the given query |

### SendMessageBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `SMS`, `RCS`, `Email`, `WhatsApp`, `IG`, `FB`, `Custom`, `Live_Chat`, `TIKTOK`) | Yes | Type of message being sent |
| `subType` | object | Yes | Type of message being sent |
| `contactId` | string | Yes | ID of the contact receiving the message |
| `appointmentId` | string | No | ID of the associated appointment |
| `attachments` | array of string | No | Array of attachment URLs |
| `emailFrom` | string | No | Email address to send from |
| `emailCc` | array of string | No | Array of CC email addresses |
| `emailBcc` | array of string | No | Array of BCC email addresses |
| `html` | string | No | HTML content of the message |
| `message` | string | No | Text content of the message |
| `subject` | string | No | Subject line for email messages |
| `replyMessageId` | string | No | ID of message being replied to |
| `templateId` | string | No | ID of message template |
| `threadId` | string | No | ID of message thread. For email messages, this is the message ID that contains multiple email messages in the thread |
| `scheduledTimestamp` | number | No | UTC Timestamp (in seconds) at which the message should be scheduled |
| `conversationProviderId` | string | No | ID of conversation provider |
| `emailTo` | string | No | Email address to send to, if different from contact's primary email. This should be a valid email address associated with the contact. |
| `customSubtypeId` | string | No | Custom subtype ID for email unsubscription preferences. Only applies to email messages. |
| `emailReplyMode` | string (enum: `reply`, `reply_all`) | No | Mode for email replies |
| `fromNumber` | string | No | Phone number used as the sender number for outbound messages |
| `toNumber` | string | No | Recipient phone number for outbound messages |
| `forward` | object | No |  |
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |
| `usesNativeSchedulingAi` | boolean | No | Whether the scheduled email uses native AI for the email scheduling  |
| `optimizationPeriod` | string (enum: `24h`, `48h`, `72h`) | No | Optimization period in hours (24h, 48h, or 72h) |

### SendMessageResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation ID. |
| `emailMessageId` | string | No | This contains the email message id (only for Email type). Use this ID to send inbound replies to GHL to create a threaded email. |
| `messageId` | string | Yes | This is the main Message ID |
| `messageIds` | array of string | No | When sending via the GMB channel, we will be returning list of `messageIds` instead of single `messageId`. |
| `msg` | string | No | Additional response message when sending a workflow message |
| `forwardData` | object | No |  |
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |

### SendReviewReplyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation ID (must have reviewId) |
| `locationId` | string | Yes | Location ID |
| `message` | string | Yes | Review reply message text |

### StartAfterArrayNumberSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `startAfterDate` | array of string | No | Search to begin after the specified date - should contain the sort value of the last document |

### StartAfterNumberSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `startAfterDate` | number | No | Search to begin after the specified date - should contain the sort value of the last document |

### SubscriptionActionDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `default`, `custom`, `resub_all`) | Yes | Type of subscription action |
| `subtype_name` | string (enum: `One on One`) | No | Subscription type name (required for default types: "One on One") |
| `subtype_id` | string | No | Custom subscription type ID (required for custom types) |
| `subtype_status` | string (enum: `subscribed`, `unsubscribed`) | Yes | Subscription status |

### UpdateConversationDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID as string |
| `unreadCount` | number | No | Count of unread messages in the conversation |
| `starred` | boolean | No | Starred status of the conversation. |
| `feedback` | object | No |  |

### UpdateCustomSubtypeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Name of the custom subtype (max 100 characters) |
| `description` | string | No | Description of the custom subtype (max 100 characters) |
| `archived` | boolean | No | Whether the custom subtype is archived |
| `resubscription_legal_form_id` | string | No | Resubscription legal form ID (optional when archiving) |

### UpdateMessageStatusDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | string (enum: `delivered`, `failed`, `pending`, `read`) | Yes | Message status |
| `error` | object | No |  |
| `emailMessageId` | string | No | Email message Id |
| `recipients` | array of string | No | Email delivery status for additional email recipients. |

### UploadFilesDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversationId` | string | Yes | Conversation Id |
| `contactId` | string | Yes | Contact Id |
| `locationId` | string | Yes |  |
| `attachmentUrls` | array of string | Yes |  |
| `chatServiceSid` | string | No | Twilio chat service SID for group SMS uploads |
| `isGroupSms` | string | No | Flag to indicate group SMS upload flow. When true, only 1 file upload is allowed per request. |

### UploadFilesErrorResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | number (enum: `400`, `413`, `415`) | Yes | HTTP Status code of the request |
| `message` | string | Yes | Error message of the request |

### UploadFilesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `uploadedFiles` | object | Yes |  |
| `twilioMediaSids` | array of string | No | Twilio media SIDs for group SMS (when isGroupSms=true) |

### UserSubscriptionChangeDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `email` | string | Yes | Email address |
| `subscription_action` | object | Yes |  |
| `legal_reason` | string | No | Legal reason for the change (required only for resubscribe and resub_all actions) |
| `legal_description` | string | No | Legal description/details |

### UserTypingBody

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `isTyping` | string | Yes | Typing status |
| `visitorId` | string | Yes | visitorId is the Unique ID assigned to each Live chat visitor. visitorId will be added soon in <a href="https://highlevel.stoplight.io/docs/integrations/00c5ff21f0030-get-contact" target="_blank">GET ... |
| `conversationId` | string | Yes | Conversation Id |
