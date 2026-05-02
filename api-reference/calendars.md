# Calendars API

Documentation for Calendars API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Calendar Groups](#calendar-groups)
- [Calendar Events](#calendar-events)
- [Calendars](#calendars)
- [Appointment Notes](#appointment-notes)
- [Calendar Resources: Rooms & Equipments](#calendar-resources:-rooms-&-equipments)
- [Calendar Notifications](#calendar-notifications)
- [Availability](#availability)

## Calendar Groups

### GET `/calendars/groups`

**Get Groups**

Get all calendar groups in a location.

**Operation ID:** `get-groups`

**Tags:** Calendar Groups

**Required Scopes:** `calendars/groups.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groups` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/calendars/groups`

**Create Calendar Group**

Create Calendar Group

**Operation ID:** `create-calendar-group`

**Tags:** Calendar Groups

**Required Scopes:** `calendars/groups.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `description` | string | Yes |  |
| `slug` | string | Yes |  |
| `isActive` | boolean | No |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `group` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/calendars/groups/validate-slug`

**Validate group slug**

Validate if group slug is available or not.

**Operation ID:** `validate-groups-slug`

**Tags:** Calendar Groups

**Required Scopes:** `calendars/groups.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `slug` | string | Yes | Slug |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `available` | boolean | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/calendars/groups/{groupId}`

**Delete Group**

Delete Group

**Operation ID:** `delete-group`

**Tags:** Calendar Groups

**Required Scopes:** `calendars/groups.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `groupId` | path | string | Yes | Group Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Success |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/groups/{groupId}`

**Update Group**

Update Group by group ID

**Operation ID:** `edit-group`

**Tags:** Calendar Groups

**Required Scopes:** `calendars/groups.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `groupId` | path | string | Yes | Group Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `description` | string | Yes |  |
| `slug` | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `group` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/groups/{groupId}/status`

**Disable Group**

Disable Group

**Operation ID:** `disable-group`

**Tags:** Calendar Groups

**Required Scopes:** `calendars/groups.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `groupId` | path | string | Yes | Group Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isActive` | boolean | Yes | Is Active? |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Success |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Calendar Events

### POST `/calendars/events/appointments`

**Create appointment**

Create appointment

**Operation ID:** `create-appointment`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `ms_teams`, `google`) | No | Meeting location type.  - If `address` is provided in the request body, the `meetingLocationType` defaults to **custom**. |
| `meetingLocationId` | string | No | The unique identifier for the meeting location. - This value can be found in `calendar.locationConfigurations`or `calendar.teamMembers[].locationConfigurations` Default: `default` |
| `overrideLocationConfig` | boolean | No | Flag to override location config - **false** - If only `meetingLocationId` is provided - **true** - If only `meetingLocationType` is provided  |
| `appointmentStatus` | string (enum: `new`, `confirmed`, `cancelled`, `showed`, `noshow`, `invalid`) | No |  |
| `assignedUserId` | string | No | Assigned User Id |
| `description` | string | No | Appointment Description |
| `address` | string | No | Appointment Address |
| `ignoreDateRange` | boolean | No | If set to true, the minimum scheduling notice and date range would be ignored |
| `toNotify` | boolean | No | If set to false, the automations will not run |
| `ignoreFreeSlotValidation` | boolean | No | If true the time slot validation would be avoided for any appointment creation (even the ignoreDateRange) |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. The rrule only be applied if igno... |
| `calendarId` | string | Yes | Calendar Id |
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `startTime` | string | Yes | Start Time |
| `endTime` | string | No | End Time |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendarId` | string | Yes | Calendar Id |
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |
| `title` | string | No | Title |
| `meetingLocationType` | string | No | Meeting Location Type Default: `default` |
| `appointmentStatus` | string (enum: `new`, `confirmed`, `cancelled`, `showed`, `noshow`, `invalid`, `active`, `completed`) | No |  |
| `assignedUserId` | string | No | Assigned User Id |
| `address` | string | No | Appointment Address |
| `isRecurring` | boolean | No | true if the event is recurring otherwise false |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events |
| `id` | string | Yes | Id |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/events/appointments/{eventId}`

**Update Appointment**

Update appointment

**Operation ID:** `edit-appointment`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `eventId` | path | string | Yes | Event Id or Instance id. For recurring appointments send masterEventId to modify original series. |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `ms_teams`, `google`) | No | Meeting location type.  - If `address` is provided in the request body, the `meetingLocationType` defaults to **custom**. |
| `meetingLocationId` | string | No | The unique identifier for the meeting location. - This value can be found in `calendar.locationConfigurations`or `calendar.teamMembers[].locationConfigurations` Default: `default` |
| `overrideLocationConfig` | boolean | No | Flag to override location config - **false** - If only `meetingLocationId` is provided - **true** - If only `meetingLocationType` is provided  |
| `appointmentStatus` | string (enum: `new`, `confirmed`, `cancelled`, `showed`, `noshow`, `invalid`) | No |  |
| `assignedUserId` | string | No | Assigned User Id |
| `description` | string | No | Appointment Description |
| `address` | string | No | Appointment Address |
| `ignoreDateRange` | boolean | No | If set to true, the minimum scheduling notice and date range would be ignored |
| `toNotify` | boolean | No | If set to false, the automations will not run |
| `ignoreFreeSlotValidation` | boolean | No | If true the time slot validation would be avoided for any appointment creation (even the ignoreDateRange) |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. The rrule only be applied if igno... |
| `calendarId` | string | No | Calendar Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendarId` | string | Yes | Calendar Id |
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |
| `title` | string | No | Title |
| `meetingLocationType` | string | No | Meeting Location Type Default: `default` |
| `appointmentStatus` | string (enum: `new`, `confirmed`, `cancelled`, `showed`, `noshow`, `invalid`, `active`, `completed`) | No |  |
| `assignedUserId` | string | No | Assigned User Id |
| `address` | string | No | Appointment Address |
| `isRecurring` | boolean | No | true if the event is recurring otherwise false |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events |
| `id` | string | Yes | Id |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/calendars/events/appointments/{eventId}`

**Get Appointment**

Get appointment by ID

**Operation ID:** `get-appointment`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `eventId` | path | string | Yes | Event Id or Instance id. For recurring appointments send masterEventId to modify original series. |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `event` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/calendars/events`

**Get Calendar Events**

Get Calendar Events

**Operation ID:** `get-calendar-events`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | No | User Id - Owner of an appointment. Either of userId, groupId or calendarId is required |
| `calendarId` | query | string | No | Either of calendarId, userId or groupId is required |
| `groupId` | query | string | No | Either of groupId, calendarId or userId is required |
| `startTime` | query | string | Yes | Start Time (in millis) |
| `endTime` | query | string | Yes | End Time (in millis) |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `events` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/calendars/blocked-slots`

**Get Blocked Slots**

Get Blocked Slots

**Operation ID:** `get-blocked-slots`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `userId` | query | string | No | User Id - Owner of an appointment. Either of userId, groupId or calendarId is required |
| `calendarId` | query | string | No | Either of calendarId, userId or groupId is required |
| `groupId` | query | string | No | Either of groupId, calendarId or userId is required |
| `startTime` | query | string | Yes | Start Time (in millis) |
| `endTime` | query | string | Yes | End Time (in millis) |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `events` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/calendars/events/block-slots`

**Create Block Slot**

Create block slot

**Operation ID:** `create-block-slot`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `calendarId` | string | Yes | Either calendarId or assignedUserId can be set, not both. |
| `assignedUserId` | string | No | Either calendarId or assignedUserId can be set, not both. |
| `locationId` | string | Yes | Location Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `locationId` | string | Yes | Location Id |
| `title` | string | Yes | Title |
| `startTime` | object | Yes | Start Time |
| `endTime` | object | Yes | End Time |
| `calendarId` | string | No | Calendar id |
| `assignedUserId` | string | No | Assigned User Id |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/events/block-slots/{eventId}`

**Update Block Slot**

Update block slot by ID

**Operation ID:** `edit-block-slot`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `eventId` | path | string | Yes | Event Id or Instance id. For recurring appointments send masterEventId to modify original series. |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `calendarId` | string | Yes | Either calendarId or assignedUserId can be set, not both. |
| `assignedUserId` | string | No | Either calendarId or assignedUserId can be set, not both. |
| `locationId` | string | Yes | Location Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `locationId` | string | Yes | Location Id |
| `title` | string | Yes | Title |
| `startTime` | object | Yes | Start Time |
| `endTime` | object | Yes | End Time |
| `calendarId` | string | No | Calendar id |
| `assignedUserId` | string | No | Assigned User Id |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/calendars/events/{eventId}`

**Delete Event**

Delete event by ID

**Operation ID:** `delete-event`

**Tags:** Calendar Events

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `eventId` | path | string | Yes | Event Id or Instance id. For recurring appointments send masterEventId to modify original series. |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeeded` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Calendars

### GET `/calendars/{calendarId}/free-slots`

**Get Free Slots**

Get free slots for a calendar between a date range. Optionally a consumer can also request free slots in a particular timezone and also for a particular user.

**Operation ID:** `get-slots`

**Tags:** Calendars

**Required Scopes:** `calendars.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes | Calendar Id |
| `startDate` | query | number | Yes | Start Date (**⚠️ Important:** Date range cannot be more than 31 days) |
| `endDate` | query | number | Yes | End Date (**⚠️ Important:** Date range cannot be more than 31 days) |
| `timezone` | query | string | No | The timezone in which the free slots are returned |
| `userId` | query | string | No | The user for whom the free slots are returned |
| `userIds` | query | array of string | No | The users for whom the free slots are returned |

#### Responses

**`200` - Availability map keyed by date (YYYY-MM-DD)**

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/{calendarId}`

**Update Calendar**

Update calendar by ID.

**Operation ID:** `update-calendar`

**Tags:** Calendars

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes | Calendar Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notifications` | array of object | No | 🚨 Deprecated! Please use 'Calendar Notifications APIs' instead. |
| `groupId` | string | No | Group Id |
| `teamMembers` | array of object | No | Team members are required for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member. |
| `eventType` | string (enum: `RoundRobin_OptimizeForAvailability`, `RoundRobin_OptimizeForEqualDistribution`) | No |  |
| `name` | string | No |  |
| `description` | string | No |  |
| `slug` | string | No |  |
| `widgetSlug` | string | No |  |
| `widgetType` | string (enum: `default`, `classic`) | No | Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout. Default: `classic` |
| `eventTitle` | string | No |  |
| `eventColor` | string | No |  Default: `#039be5` |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` or `teamMembers[].locationConfigurations.location` instead. |
| `slotDuration` | number | No | This controls the duration of the meeting Default: `30` |
| `slotDurationUnit` | string (enum: `mins`, `hours`) | No | Unit for slot duration. |
| `preBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for pre-buffer. |
| `slotInterval` | number | No | Slot interval reflects the amount of time the between booking slots that will be shown in the calendar. Default: `30` |
| `slotIntervalUnit` | string (enum: `mins`, `hours`) | No | Unit for slot interval. |
| `slotBuffer` | number | No | Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up |
| `preBuffer` | number | No | Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready |
| `appoinmentPerSlot` | number | No |  |
| `appoinmentPerDay` | number | No | Number of appointments that can be booked for a given day |
| `allowBookingAfter` | number | No | Minimum scheduling notice for events |
| `allowBookingAfterUnit` | string (enum: `hours`, `days`, `weeks`, `months`) | No | Unit for minimum scheduling notice |
| `allowBookingFor` | number | No | Minimum number of days/weeks/months for which to allow booking events |
| `allowBookingForUnit` | string (enum: `days`, `weeks`, `months`) | No | Unit for controlling the duration for which booking would be allowed for |
| `openHours` | array of object | No |  |
| `enableRecurring` | boolean | No | Enable recurring appointments for the calendars. Please note that only one member should be added in the calendar to enable this Default: `False` |
| `recurring` | object | No |  |
| `formId` | string | No |  |
| `stickyContact` | boolean | No |  |
| `isLivePaymentMode` | boolean | No |  |
| `autoConfirm` | boolean | No |  |
| `shouldSendAlertEmailsToAssignedMember` | boolean | No |  |
| `alertEmail` | string | No |  |
| `googleInvitationEmails` | boolean | No |  |
| `allowReschedule` | boolean | No |  |
| `allowCancellation` | boolean | No |  |
| `shouldAssignContactToTeamMember` | boolean | No |  |
| `shouldSkipAssigningContactForExisting` | boolean | No |  |
| `notes` | string | No |  |
| `pixelId` | string | No |  |
| `formSubmitType` | string (enum: `RedirectURL`, `ThankYouMessage`) | No |  Default: `ThankYouMessage` |
| `formSubmitRedirectURL` | string | No |  |
| `formSubmitThanksMessage` | string | No |  |
| `availabilityType` | number (enum: `0`, `1`) | No | Determines which availability type to consider: - **1**: Only custom availabilities will be used. - **0**: Only open hours will be used. - **null**: Both the custom availabilities and open hours will ... |
| `availabilities` | array of object | No | This is only to set the custom availability. For standard availability, use the openHours property |
| `guestType` | string (enum: `count_only`, `collect_detail`) | No |  |
| `consentLabel` | string | No |  |
| `calendarCoverImage` | string | No |  |
| `lookBusyConfig` | object | No |  |
| `isActive` | boolean | No |  |

**`notifications` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `email`) | No | Calendar Notification Default: `email` |
| `shouldSendToContact` | boolean | Yes |  |
| `shouldSendToGuest` | boolean | Yes |  |
| `shouldSendToUser` | boolean | Yes |  |
| `shouldSendToSelectedUsers` | boolean | Yes |  |
| `selectedUsers` | string | Yes | Comma separated emails |

**`teamMembers` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | Yes |  |
| `priority` | number (enum: `0`, `0.5`, `1`) | No |  Default: `0.5` |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `teams`, `booker`) | No | 🚨 Deprecated! Use `locationConfigurations.kind` instead. Default: `custom` |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` instead. |
| `isPrimary` | boolean | No | Marks a user as primary. This property is required in case of collective booking calendars. Only one user can be primary. |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar. - *Multiple locations are allowed only when one team member is selected.* - *For **Class booking** and **Collective** calendars, only one location co... |

**`locationConfigurations` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `kind` | string (enum: `custom`, `zoom_conference`, `google_conference`, `inbound_call`, `outbound_call`, `physical`, `booker`, `ms_teams_conference`) | Yes | Type of meeting location. zoom_conference/google_conference/ms_teams_conference is not supported in event calendar type |
| `location` | string | No | Address for meeting location. Not applicable on "zoom_conference", "google_conference" and "ms_teams_conference" kind |

**`openHours` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `daysOfTheWeek` | array of number | Yes |  |
| `hours` | array of object | Yes |  |

**`recurring` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `freq` | string (enum: `DAILY`, `WEEKLY`, `MONTHLY`) | No |  |
| `count` | number | No | Number of recurrences |
| `bookingOption` | string (enum: `skip`, `continue`, `book_next`) | No | This setting contols what to do incase a recurring slot is unavailable |
| `bookingOverlapDefaultStatus` | string (enum: `confirmed`, `new`) | No | This setting contols what to do incase a recurring slot is unavailable |

**`availabilities` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `date` | string | Yes | Formulate the date string in the format of `<YYYY-MM-DD in local timezone>T00:00:00.000Z`. |
| `hours` | array of object | Yes |  |
| `deleted` | boolean | No |  Default: `False` |
| `id` | string | No | The ID of the custom availability object. It is required while updating or deleting the existing custom date availability |

**`lookBusyConfig` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Apply Look Busy Default: `False` |
| `LookBusyPercentage` | number | Yes | Percentage of slots that will be hidden |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendar` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/calendars/{calendarId}`

**Get Calendar**

Get calendar by ID

**Operation ID:** `get-calendar`

**Tags:** Calendars

**Required Scopes:** `calendars.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes | Calendar Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendar` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/calendars/{calendarId}`

**Delete Calendar**

Delete calendar by ID

**Operation ID:** `delete-calendar`

**Tags:** Calendars

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes | Calendar Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/calendars/`

**Get Calendars**

Get all calendars in a location.

**Operation ID:** `get-calendars`

**Tags:** Calendars

**Required Scopes:** `calendars.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `groupId` | query | string | No | Group Id |
| `showDrafted` | query | boolean | No | Show drafted |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendars` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/calendars/`

**Create Calendar**

Create calendar in a location.

**Operation ID:** `create-calendar`

**Tags:** Calendars

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isActive` | boolean | No | Should the created calendar be active or draft Default: `True` |
| `notifications` | array of object | No | 🚨 Deprecated! Please use 'Calendar Notifications APIs' instead. |
| `locationId` | string | Yes |  |
| `groupId` | string | No | Group Id |
| `teamMembers` | array of object | No | Team members are required for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member. |
| `eventType` | string (enum: `RoundRobin_OptimizeForAvailability`, `RoundRobin_OptimizeForEqualDistribution`) | No |  Default: `RoundRobin_OptimizeForAvailability` |
| `name` | string | Yes |  |
| `description` | string | No |  |
| `slug` | string | No |  |
| `widgetSlug` | string | No |  |
| `calendarType` | string (enum: `round_robin`, `event`, `class_booking`, `collective`, `service_booking`, `personal`) | No |  |
| `widgetType` | string (enum: `default`, `classic`) | No | Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout. Default: `classic` |
| `eventTitle` | string | No |  Default: `{{contact.name}}` |
| `eventColor` | string | No |  Default: `#039be5` |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` or `teamMembers[].locationConfigurations.location` instead. |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar |
| `slotDuration` | number | No | This controls the duration of the meeting Default: `30` |
| `slotDurationUnit` | string (enum: `mins`, `hours`) | No | Unit for slot duration. |
| `slotInterval` | number | No | Slot interval reflects the amount of time the between booking slots that will be shown in the calendar. Default: `30` |
| `slotIntervalUnit` | string (enum: `mins`, `hours`) | No | Unit for slot interval. |
| `slotBuffer` | number | No | Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up |
| `slotBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for slot buffer. |
| `preBuffer` | number | No | Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready |
| `preBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for pre-buffer. |
| `appoinmentPerSlot` | number | No | Maximum bookings per slot (per user). Maximum seats per slot in case of Class Booking Calendar. Default: `1` |
| `appoinmentPerDay` | number | No | Number of appointments that can be booked for a given day |
| `allowBookingAfter` | number | No | Minimum scheduling notice for events |
| `allowBookingAfterUnit` | string (enum: `hours`, `days`, `weeks`, `months`) | No | Unit for minimum scheduling notice |
| `allowBookingFor` | number | No | Minimum number of days/weeks/months for which to allow booking events |
| `allowBookingForUnit` | string (enum: `days`, `weeks`, `months`) | No | Unit for controlling the duration for which booking would be allowed for |
| `openHours` | array of object | No | This is only to set the standard availability. For custom availability, use the availabilities property |
| `enableRecurring` | boolean | No | Enable recurring appointments for the calendars. Please note that only one member should be added in the calendar to enable this Default: `False` |
| `recurring` | object | No |  |
| `formId` | string | No |  |
| `stickyContact` | boolean | No |  |
| `isLivePaymentMode` | boolean | No |  |
| `autoConfirm` | boolean | No |  Default: `True` |
| `shouldSendAlertEmailsToAssignedMember` | boolean | No |  |
| `alertEmail` | string | No |  |
| `googleInvitationEmails` | boolean | No |  Default: `False` |
| `allowReschedule` | boolean | No |  Default: `True` |
| `allowCancellation` | boolean | No |  Default: `True` |
| `shouldAssignContactToTeamMember` | boolean | No |  |
| `shouldSkipAssigningContactForExisting` | boolean | No |  |
| `notes` | string | No |  |
| `pixelId` | string | No |  |
| `formSubmitType` | string (enum: `RedirectURL`, `ThankYouMessage`) | No |  Default: `ThankYouMessage` |
| `formSubmitRedirectURL` | string | No |  |
| `formSubmitThanksMessage` | string | No |  |
| `availabilityType` | number (enum: `0`, `1`) | No | Determines which availability type to consider: - **1**: Only custom availabilities will be used. - **0**: Only open hours will be used. - **null**: Both custom availabilities and open hours will be c... |
| `availabilities` | array of object | No | This is only to set the custom availability. For standard availability, use the openHours property |
| `guestType` | string (enum: `count_only`, `collect_detail`) | No |  |
| `consentLabel` | string | No |  |
| `calendarCoverImage` | string | No |  |
| `lookBusyConfig` | object | No |  |

**`notifications` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `email`) | No | Calendar Notification Default: `email` |
| `shouldSendToContact` | boolean | Yes |  |
| `shouldSendToGuest` | boolean | Yes |  |
| `shouldSendToUser` | boolean | Yes |  |
| `shouldSendToSelectedUsers` | boolean | Yes |  |
| `selectedUsers` | string | Yes | Comma separated emails |

**`teamMembers` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | Yes |  |
| `priority` | number (enum: `0`, `0.5`, `1`) | No |  Default: `0.5` |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `teams`, `booker`) | No | 🚨 Deprecated! Use `locationConfigurations.kind` instead. Default: `custom` |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` instead. |
| `isPrimary` | boolean | No | Marks a user as primary. This property is required in case of collective booking calendars. Only one user can be primary. |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar. - *Multiple locations are allowed only when one team member is selected.* - *For **Class booking** and **Collective** calendars, only one location co... |

**`locationConfigurations` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `kind` | string (enum: `custom`, `zoom_conference`, `google_conference`, `inbound_call`, `outbound_call`, `physical`, `booker`, `ms_teams_conference`) | Yes | Type of meeting location. zoom_conference/google_conference/ms_teams_conference is not supported in event calendar type |
| `location` | string | No | Address for meeting location. Not applicable on "zoom_conference", "google_conference" and "ms_teams_conference" kind |

**`openHours` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `daysOfTheWeek` | array of number | Yes |  |
| `hours` | array of object | Yes |  |

**`recurring` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `freq` | string (enum: `DAILY`, `WEEKLY`, `MONTHLY`) | No |  |
| `count` | number | No | Number of recurrences |
| `bookingOption` | string (enum: `skip`, `continue`, `book_next`) | No | This setting contols what to do incase a recurring slot is unavailable |
| `bookingOverlapDefaultStatus` | string (enum: `confirmed`, `new`) | No | This setting contols what to do incase a recurring slot is unavailable |

**`availabilities` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `date` | string | Yes | Formulate the date string in the format of `<YYYY-MM-DD in local timezone>T00:00:00.000Z`. |
| `hours` | array of object | Yes |  |
| `deleted` | boolean | No |  Default: `False` |

**`lookBusyConfig` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Apply Look Busy Default: `False` |
| `LookBusyPercentage` | number | Yes | Percentage of slots that will be hidden |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendar` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Appointment Notes

### GET `/calendars/appointments/{appointmentId}/notes`

**Get Notes**

Get Appointment Notes

**Operation ID:** `get-appointment-notes`

**Tags:** Appointment Notes

**Required Scopes:** `calendars/events.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `limit` | query | number | Yes | Limit of notes to fetch |
| `offset` | query | number | Yes | Offset of notes to fetch |
| `appointmentId` | path | string | Yes | Appointment ID |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notes` | array of object | No |  |
| `hasMore` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/calendars/appointments/{appointmentId}/notes`

**Create Note**

Create Note

**Operation ID:** `create-appointment-note`

**Tags:** Appointment Notes

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `appointmentId` | path | string | Yes | Appointment ID |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No |  |
| `body` | string | Yes | Note body |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `note` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/appointments/{appointmentId}/notes/{noteId}`

**Update Note**

Update Note

**Operation ID:** `update-appointment-note`

**Tags:** Appointment Notes

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `appointmentId` | path | string | Yes | Appointment ID |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No |  |
| `body` | string | Yes | Note body |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `note` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/calendars/appointments/{appointmentId}/notes/{noteId}`

**Delete Note**

Delete Note

**Operation ID:** `delete-appointment-note`

**Tags:** Appointment Notes

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `appointmentId` | path | string | Yes | Appointment ID |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Calendar Resources: Rooms & Equipments

### GET `/calendars/resources/{resourceType}/{id}`

**Get Calendar Resource**

Get calendar resource by ID

**Operation ID:** `get-calendar-resource`

**Tags:** Calendar Resources: Rooms & Equipments

**Required Scopes:** `calendars/resources.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `resourceType` | path | string (enum: `equipments`, `rooms`) | Yes | Calendar Resource Type |
| `id` | path | string | Yes | Calendar Resource ID |

#### Responses

**`200` - Calendar resource fetched**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID of the resource |
| `name` | string | Yes | Name of the resource |
| `resourceType` | string (enum: `equipments`, `rooms`) | Yes |  |
| `isActive` | boolean | Yes | Whether the resource is active |
| `description` | string | No | Description of the resource |
| `quantity` | number | No | Quantity of the resource |
| `outOfService` | number | No | Indicates if the resource is out of service |
| `capacity` | number | No | Capacity of the resource |
| `calendarIds` | array of string | Yes | Calendar IDs |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/resources/{resourceType}/{id}`

**Update Calendar Resource**

Update calendar resource by ID

**Operation ID:** `update-calendar-resource`

**Tags:** Calendar Resources: Rooms & Equipments

**Required Scopes:** `calendars/resources.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `resourceType` | path | string (enum: `equipments`, `rooms`) | Yes | Calendar Resource Type |
| `id` | path | string | Yes | Calendar Resource ID |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | No |  |
| `name` | string | No |  |
| `description` | string | No |  |
| `quantity` | number | No | Quantity of the equipment. |
| `outOfService` | number | No | Quantity of the out of service equipment. |
| `capacity` | number | No | Capacity of the room. |
| `calendarIds` | array of string | No | Service calendar IDs to be mapped with the resource.      One equipment can only be mapped with one service calendar.      One room can be mapped with multiple service calendars. |
| `isActive` | boolean | No |  |

#### Responses

**`200` - Calendar resource updated**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID of the resource |
| `name` | string | Yes | Name of the resource |
| `resourceType` | string (enum: `equipments`, `rooms`) | Yes |  |
| `isActive` | boolean | Yes | Whether the resource is active |
| `description` | string | No | Description of the resource |
| `quantity` | number | No | Quantity of the resource |
| `outOfService` | number | No | Indicates if the resource is out of service |
| `capacity` | number | No | Capacity of the resource |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/calendars/resources/{resourceType}/{id}`

**Delete Calendar Resource**

Delete calendar resource by ID

**Operation ID:** `delete-calendar-resource`

**Tags:** Calendar Resources: Rooms & Equipments

**Required Scopes:** `calendars/resources.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `resourceType` | path | string (enum: `equipments`, `rooms`) | Yes | Calendar Resource Type |
| `id` | path | string | Yes | Calendar Resource ID |

#### Responses

**`200` - Calendar resource deleted**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Success |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/calendars/resources/{resourceType}`

**List Calendar Resources**

List calendar resources by resource type and location ID

**Operation ID:** `fetch-calendar-resources`

**Tags:** Calendar Resources: Rooms & Equipments

**Required Scopes:** `calendars/resources.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `resourceType` | path | string (enum: `equipments`, `rooms`) | Yes | Calendar Resource Type |
| `locationId` | query | string | Yes |  |
| `limit` | query | number | Yes |  |
| `skip` | query | number | Yes |  |

#### Responses

**`200` - Calendar resources listed**

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/calendars/resources/{resourceType}`

**Create Calendar Resource**

Create calendar resource by resource type

**Operation ID:** `create-calendar-resource`

**Tags:** Calendar Resources: Rooms & Equipments

**Required Scopes:** `calendars/resources.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `resourceType` | path | string (enum: `equipments`, `rooms`) | Yes | Calendar Resource Type |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `description` | string | Yes |  |
| `quantity` | number | Yes | Quantity of the equipment. |
| `outOfService` | number | Yes | Quantity of the out of service equipment. |
| `capacity` | number | Yes | Capacity of the room. |
| `calendarIds` | array of string | Yes | Service calendar IDs to be mapped with the resource.      One equipment can only be mapped with one service calendar.      One room can be mapped with multiple service calendars. |

#### Responses

**`201` - Calendar resource created**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID of the resource |
| `name` | string | Yes | Name of the resource |
| `resourceType` | string (enum: `equipments`, `rooms`) | Yes |  |
| `isActive` | boolean | Yes | Whether the resource is active |
| `description` | string | No | Description of the resource |
| `quantity` | number | No | Quantity of the resource |
| `outOfService` | number | No | Indicates if the resource is out of service |
| `capacity` | number | No | Capacity of the resource |
| `calendarIds` | array of string | Yes | Calendar IDs |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Calendar Notifications

### GET `/calendars/{calendarId}/notifications`

**Get notifications**

Get calendar notifications based on query

**Operation ID:** `get-event-notification`

**Tags:** Calendar Notifications

**Required Scopes:** `calendars/events.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes |  |
| `isActive` | query | boolean | No |  |
| `deleted` | query | boolean | No |  |
| `limit` | query | number | No | Number of records to return |
| `skip` | query | number | No | Number of records to skip |

#### Responses

**`200` - Successful response**

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/calendars/{calendarId}/notifications`

**Create notification**

Create Calendar notifications, either one or multiple. All notification settings must be for single calendar only

**Operation ID:** `create-event-notification`

**Tags:** Calendar Notifications

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

#### Responses

**`200` - Successful response**

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/calendars/{calendarId}/notifications/{notificationId}`

**Get notification**

Find Event notification by notificationId

**Operation ID:** `find-event-notification`

**Tags:** Calendar Notifications

**Required Scopes:** `calendars/events.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes |  |
| `notificationId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No | Notification ID |
| `receiverType` | string (enum: `contact`, `guest`, `assignedUser`, `emails`, `phoneNumbers`, `business`) | No |  |
| `additionalEmailIds` | array of string | No |  |
| `additionalPhoneNumbers` | array of string | No |  |
| `channel` | string (enum: `email`, `inApp`, `sms`, `whatsapp`) | No |  |
| `notificationType` | string (enum: `booked`, `confirmation`, `cancellation`, `reminder`, `followup`, `reschedule`) | No |  |
| `isActive` | boolean | No |  |
| `additionalWhatsappNumbers` | array of string | No |  |
| `templateId` | string | No |  |
| `body` | string | No |  |
| `subject` | string | No |  |
| `afterTime` | array of object | No |  |
| `beforeTime` | array of object | No |  |
| `selectedUsers` | array of string | No |  |
| `deleted` | boolean | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/calendars/{calendarId}/notifications/{notificationId}`

**Update notification**

Update Event notification by id

**Operation ID:** `update-event-notification`

**Tags:** Calendar Notifications

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes |  |
| `notificationId` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `receiverType` | string (enum: `contact`, `guest`, `assignedUser`, `emails`, `phoneNumbers`, `business`) | No | Notification recipient type |
| `additionalEmailIds` | array of string | No | Additional email addresses to receive notifications. |
| `additionalPhoneNumbers` | array of string | No | Additional phone numbers to receive notifications. |
| `selectedUsers` | array of string | No | Selected users for in-App and business email notifications. Supports user IDs and special keyword "sub_account_admin" |
| `channel` | string (enum: `email`, `inApp`, `sms`, `whatsapp`) | No | Notification channel |
| `notificationType` | string (enum: `booked`, `confirmation`, `cancellation`, `reminder`, `followup`, `reschedule`) | No | Notification type |
| `isActive` | boolean | No | Is the notification active Default: `True` |
| `deleted` | boolean | No | Marks the notification as deleted (soft delete) Default: `False` |
| `templateId` | string | No | Template ID for email notification |
| `body` | string | No | Body  for email notification. Not necessary for in-App notification |
| `subject` | string | No | Subject  for email notification. Not necessary for in-App notification |
| `afterTime` | array of object | No | Specifies the time after which the follow-up notification should be sent. This is not required for other notification types. |
| `beforeTime` | array of object | No | Specifies the time before which the reminder notification should be sent. This is not required for other notification types. |
| `fromAddress` | string | No | From address for email notification |
| `fromNumber` | string | No | from number for sms notification |
| `fromName` | string | No | From name for email/sms notification |

**`afterTime` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `timeOffset` | number | No |  |
| `unit` | string | No |  |

**`beforeTime` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `timeOffset` | number | No |  |
| `unit` | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Result of delete/update operation |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/calendars/{calendarId}/notifications/{notificationId}`

**Delete Notification**

Delete notification

**Operation ID:** `delete-event-notification`

**Tags:** Calendar Notifications

**Required Scopes:** `calendars/events.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `calendarId` | path | string | Yes |  |
| `notificationId` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Result of delete/update operation |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Availability

### GET `/calendars/schedules/search`

**List user availability schedule**

Retrieve user availability schedules based on various filters including location, calendar, and user. Supports pagination.

**Operation ID:** `getAllSchedules`

**Tags:** Availability

**Required Scopes:** `calendars.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location ID to filter schedules by |
| `userId` | query | string | Yes | User ID to filter schedules by specific user |
| `calendarId` | query | string | No | Calendar ID for filtering schedules by specific calendar |
| `skip` | query | number | No | Number of items to skip for pagination |
| `limit` | query | number | No | Maximum number of items to return (max 500) |

#### Responses

**`200` - Schedules retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedules` | array of object | Yes | Array of schedules |

**`400` - Invalid request parameters**

**`401` - User not authenticated**

---

### GET `/calendars/schedules/{id}`

**Get user availability schedule**

Retrieve a specific schedule by its unique identifier. Returns detailed information including rules, timezone, and associated calendars/users.

**Operation ID:** `getScheduleById`

**Tags:** Availability

**Required Scopes:** `calendars.readonly`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Unique identifier of the schedule |

#### Responses

**`200` - Schedule found and retrieved successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedule` | object | Yes |  |

**`400` - Invalid request parameters**

**`401` - User not authenticated**

**`404` - Schedule with the specified ID was not found**

---

### PUT `/calendars/schedules/{id}`

**Update user availability schedule**

Modify an existing schedule by updating its rules, timezone, and name All fields are optional - only provided fields will be updated.

**Operation ID:** `updateSchedule`

**Tags:** Availability

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Unique identifier of the schedule to update |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Human-readable name for the schedule |
| `rules` | array of object | No | Updated schedule rules defining when the schedule is active |
| `timezone` | string | No | Updated timezone for the schedule (IANA timezone identifier) |

**`rules` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `wday`, `date`) | Yes | Type of schedule rule - weekday (recurring) or date (specific date) |
| `intervals` | array of object | Yes | Time intervals for the rule (e.g., 9 AM to 5 PM) |
| `date` | string | No | Specific date in YYYY-MM-DD format (only for date-type rules) |
| `day` | string (enum: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`) | No | Day of week (only for weekday-type rules) |

#### Responses

**`200` - Schedule updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedule` | object | Yes |  |

**`400` - Invalid request parameters**

**`401` - User not authenticated**

**`404` - Schedule with the specified ID was not found**

**`422` - Validation errors in schedule rules or conflicting data**

---

### DELETE `/calendars/schedules/{id}`

**Delete user availability schedule**

Permanently remove a schedule and all its associated rules. This action cannot be undone.

**Operation ID:** `deleteSchedule`

**Tags:** Availability

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Unique identifier of the schedule to delete |

#### Responses

**`200` - Schedule deleted successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Whether the deletion was successful |

**`400` - Invalid request parameters**

**`401` - User not authenticated**

**`404` - Schedule with the specified ID was not found**

---

### POST `/calendars/schedules`

**Create user availability schedule**

Create new schedule with specified rules, timezone, location, user and calendar associations.

**Operation ID:** `createSchedule`

**Tags:** Availability

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `rules` | array of object | No | Schedule rules defining when the schedule is active |
| `timezone` | string | Yes | Timezone for the schedule (IANA timezone identifier) |
| `locationId` | string | Yes | Location ID where this schedule applies |
| `name` | string | Yes | Human-readable name for the schedule |
| `userId` | string | Yes | User ID associated with the schedule |
| `calendarIds` | array of string | No | Calendar IDs associated with the schedule |

**`rules` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `wday`, `date`) | Yes | Type of schedule rule - weekday (recurring) or date (specific date) |
| `intervals` | array of object | Yes | Time intervals for the rule (e.g., 9 AM to 5 PM) |
| `date` | string | No | Specific date in YYYY-MM-DD format (only for date-type rules) |
| `day` | string (enum: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`) | No | Day of week (only for weekday-type rules) |

#### Responses

**`201` - Schedule created successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedule` | object | Yes |  |

**`400` - Invalid request parameters**

**`401` - User not authenticated**

**`422` - Validation errors in schedule rules or conflicting data**

---

### PUT `/calendars/schedules/{id}/associations/{calendarId}`

**Apply user availability schedule to a calendar**

Associates a calendar with the given schedule by adding the calendarId to a schedule

**Operation ID:** `add-calendar-to-schedule`

**Tags:** Availability

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Unique identifier of the schedule |
| `calendarId` | path | string | Yes | Unique identifier of the team calendar to add to the schedule |

#### Responses

**`200` - Calendar successfully added to schedule**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No |  |

**`400` - Schedule and calendar must belong to the same location**

**`401` - User not authenticated**

**`404` - Schedule or calendar not found**

---

### DELETE `/calendars/schedules/{id}/associations/{calendarId}`

**Remove user availability schedule from a calendar**

Removes the association between a team calendar and the given schedule by removing the calendarId from the schedule

**Operation ID:** `remove-calendar-from-schedule`

**Tags:** Availability

**Required Scopes:** `calendars.write`

**API Version:** `2021-04-15`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes | Unique identifier of the schedule |
| `calendarId` | path | string | Yes | Unique identifier of the calendar to remove from the schedule |

#### Responses

**`200` - Calendar successfully removed from schedule**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No |  |

**`400` - Schedule and calendar must belong to the same location**

**`401` - User not authenticated**

**`404` - Schedule or calendar not found**

---

## Schemas

### AllGroupsSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `groups` | array of object | No |  |

### AppointmentCreateSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `ms_teams`, `google`) | No | Meeting location type.  - If `address` is provided in the request body, the `meetingLocationType` defaults to **custom**. |
| `meetingLocationId` | string | No | The unique identifier for the meeting location. - This value can be found in `calendar.locationConfigurations`or `calendar.teamMembers[].locationConfigurations` Default: `default` |
| `overrideLocationConfig` | boolean | No | Flag to override location config - **false** - If only `meetingLocationId` is provided - **true** - If only `meetingLocationType` is provided  |
| `appointmentStatus` | string (enum: `new`, `confirmed`, `cancelled`, `showed`, `noshow`, `invalid`) | No |  |
| `assignedUserId` | string | No | Assigned User Id |
| `description` | string | No | Appointment Description |
| `address` | string | No | Appointment Address |
| `ignoreDateRange` | boolean | No | If set to true, the minimum scheduling notice and date range would be ignored |
| `toNotify` | boolean | No | If set to false, the automations will not run |
| `ignoreFreeSlotValidation` | boolean | No | If true the time slot validation would be avoided for any appointment creation (even the ignoreDateRange) |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. The rrule only be applied if igno... |
| `calendarId` | string | Yes | Calendar Id |
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `startTime` | string | Yes | Start Time |
| `endTime` | string | No | End Time |

### AppointmentEditSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `ms_teams`, `google`) | No | Meeting location type.  - If `address` is provided in the request body, the `meetingLocationType` defaults to **custom**. |
| `meetingLocationId` | string | No | The unique identifier for the meeting location. - This value can be found in `calendar.locationConfigurations`or `calendar.teamMembers[].locationConfigurations` Default: `default` |
| `overrideLocationConfig` | boolean | No | Flag to override location config - **false** - If only `meetingLocationId` is provided - **true** - If only `meetingLocationType` is provided  |
| `appointmentStatus` | string (enum: `new`, `confirmed`, `cancelled`, `showed`, `noshow`, `invalid`) | No |  |
| `assignedUserId` | string | No | Assigned User Id |
| `description` | string | No | Appointment Description |
| `address` | string | No | Appointment Address |
| `ignoreDateRange` | boolean | No | If set to true, the minimum scheduling notice and date range would be ignored |
| `toNotify` | boolean | No | If set to false, the automations will not run |
| `ignoreFreeSlotValidation` | boolean | No | If true the time slot validation would be avoided for any appointment creation (even the ignoreDateRange) |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. The rrule only be applied if igno... |
| `calendarId` | string | No | Calendar Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |

### AppointmentSchemaResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendarId` | string | Yes | Calendar Id |
| `locationId` | string | Yes | Location Id |
| `contactId` | string | Yes | Contact Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |
| `title` | string | No | Title |
| `meetingLocationType` | string | No | Meeting Location Type Default: `default` |
| `appointmentStatus` | string (enum: `new`, `confirmed`, `cancelled`, `showed`, `noshow`, `invalid`, `active`, `completed`) | No |  |
| `assignedUserId` | string | No | Assigned User Id |
| `address` | string | No | Appointment Address |
| `isRecurring` | boolean | No | true if the event is recurring otherwise false |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events |
| `id` | string | Yes | Id |

### Availability

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `date` | string | Yes | Formulate the date string in the format of `<YYYY-MM-DD in local timezone>T00:00:00.000Z`. |
| `hours` | array of object | Yes |  |
| `deleted` | boolean | No |  Default: `False` |

### BlockSlotCreateRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `calendarId` | string | Yes | Either calendarId or assignedUserId can be set, not both. |
| `assignedUserId` | string | No | Either calendarId or assignedUserId can be set, not both. |
| `locationId` | string | Yes | Location Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |

### BlockSlotEditRequestDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | Title |
| `calendarId` | string | Yes | Either calendarId or assignedUserId can be set, not both. |
| `assignedUserId` | string | No | Either calendarId or assignedUserId can be set, not both. |
| `locationId` | string | Yes | Location Id |
| `startTime` | string | No | Start Time |
| `endTime` | string | No | End Time |

### BlockedSlotSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `locationId` | string | Yes | Location Id |
| `title` | string | Yes | Title |
| `startTime` | object | Yes | Start Time |
| `endTime` | object | Yes | End Time |
| `calendarId` | string | No | Calendar id |
| `assignedUserId` | string | No | Assigned User Id |

### CalendarByIdSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendar` | object | Yes |  |

### CalendarCreateDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isActive` | boolean | No | Should the created calendar be active or draft Default: `True` |
| `notifications` | array of object | No | 🚨 Deprecated! Please use 'Calendar Notifications APIs' instead. |
| `locationId` | string | Yes |  |
| `groupId` | string | No | Group Id |
| `teamMembers` | array of object | No | Team members are required for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member. |
| `eventType` | string (enum: `RoundRobin_OptimizeForAvailability`, `RoundRobin_OptimizeForEqualDistribution`) | No |  Default: `RoundRobin_OptimizeForAvailability` |
| `name` | string | Yes |  |
| `description` | string | No |  |
| `slug` | string | No |  |
| `widgetSlug` | string | No |  |
| `calendarType` | string (enum: `round_robin`, `event`, `class_booking`, `collective`, `service_booking`, `personal`) | No |  |
| `widgetType` | string (enum: `default`, `classic`) | No | Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout. Default: `classic` |
| `eventTitle` | string | No |  Default: `{{contact.name}}` |
| `eventColor` | string | No |  Default: `#039be5` |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` or `teamMembers[].locationConfigurations.location` instead. |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar |
| `slotDuration` | number | No | This controls the duration of the meeting Default: `30` |
| `slotDurationUnit` | string (enum: `mins`, `hours`) | No | Unit for slot duration. |
| `slotInterval` | number | No | Slot interval reflects the amount of time the between booking slots that will be shown in the calendar. Default: `30` |
| `slotIntervalUnit` | string (enum: `mins`, `hours`) | No | Unit for slot interval. |
| `slotBuffer` | number | No | Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up |
| `slotBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for slot buffer. |
| `preBuffer` | number | No | Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready |
| `preBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for pre-buffer. |
| `appoinmentPerSlot` | number | No | Maximum bookings per slot (per user). Maximum seats per slot in case of Class Booking Calendar. Default: `1` |
| `appoinmentPerDay` | number | No | Number of appointments that can be booked for a given day |
| `allowBookingAfter` | number | No | Minimum scheduling notice for events |
| `allowBookingAfterUnit` | string (enum: `hours`, `days`, `weeks`, `months`) | No | Unit for minimum scheduling notice |
| `allowBookingFor` | number | No | Minimum number of days/weeks/months for which to allow booking events |
| `allowBookingForUnit` | string (enum: `days`, `weeks`, `months`) | No | Unit for controlling the duration for which booking would be allowed for |
| `openHours` | array of object | No | This is only to set the standard availability. For custom availability, use the availabilities property |
| `enableRecurring` | boolean | No | Enable recurring appointments for the calendars. Please note that only one member should be added in the calendar to enable this Default: `False` |
| `recurring` | object | No |  |
| `formId` | string | No |  |
| `stickyContact` | boolean | No |  |
| `isLivePaymentMode` | boolean | No |  |
| `autoConfirm` | boolean | No |  Default: `True` |
| `shouldSendAlertEmailsToAssignedMember` | boolean | No |  |
| `alertEmail` | string | No |  |
| `googleInvitationEmails` | boolean | No |  Default: `False` |
| `allowReschedule` | boolean | No |  Default: `True` |
| `allowCancellation` | boolean | No |  Default: `True` |
| `shouldAssignContactToTeamMember` | boolean | No |  |
| `shouldSkipAssigningContactForExisting` | boolean | No |  |
| `notes` | string | No |  |
| `pixelId` | string | No |  |
| `formSubmitType` | string (enum: `RedirectURL`, `ThankYouMessage`) | No |  Default: `ThankYouMessage` |
| `formSubmitRedirectURL` | string | No |  |
| `formSubmitThanksMessage` | string | No |  |
| `availabilityType` | number (enum: `0`, `1`) | No | Determines which availability type to consider: - **1**: Only custom availabilities will be used. - **0**: Only open hours will be used. - **null**: Both custom availabilities and open hours will be c... |
| `availabilities` | array of object | No | This is only to set the custom availability. For standard availability, use the openHours property |
| `guestType` | string (enum: `count_only`, `collect_detail`) | No |  |
| `consentLabel` | string | No |  |
| `calendarCoverImage` | string | No |  |
| `lookBusyConfig` | object | No |  |

### CalendarDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isActive` | boolean | No | Should the created calendar be active or draft Default: `True` |
| `notifications` | array of object | No | 🚨 Deprecated! Please use 'Calendar Notifications APIs' instead. |
| `locationId` | string | Yes |  |
| `groupId` | string | No | Group Id |
| `teamMembers` | array of object | No | Team members are for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member. |
| `eventType` | string (enum: `RoundRobin_OptimizeForAvailability`, `RoundRobin_OptimizeForEqualDistribution`) | No |  Default: `RoundRobin_OptimizeForAvailability` |
| `name` | string | Yes |  |
| `description` | string | No |  |
| `slug` | string | No |  |
| `widgetSlug` | string | No |  |
| `calendarType` | string (enum: `round_robin`, `event`, `class_booking`, `collective`, `service_booking`, `personal`) | No |  |
| `widgetType` | string (enum: `default`, `classic`) | No | Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout. Default: `classic` |
| `eventTitle` | string | No |  Default: `{{contact.name}}` |
| `eventColor` | string | No |  Default: `#039be5` |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` or `teamMembers[].locationConfigurations.location` instead. |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar |
| `slotDuration` | number | No | This controls the duration of the meeting Default: `30` |
| `slotDurationUnit` | string (enum: `mins`, `hours`) | No | Unit for slot duration. |
| `slotInterval` | number | No | Slot interval reflects the amount of time the between booking slots that will be shown in the calendar. Default: `30` |
| `slotIntervalUnit` | string (enum: `mins`, `hours`) | No | Unit for slot interval. |
| `slotBuffer` | number | No | Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up |
| `slotBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for slot buffer. |
| `preBuffer` | number | No | Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready |
| `preBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for pre-buffer. |
| `appoinmentPerSlot` | number | No | Maximum bookings per slot (per user). Maximum seats per slot in case of Class Booking Calendar. Default: `1` |
| `appoinmentPerDay` | number | No | Number of appointments that can be booked for a given day |
| `allowBookingAfter` | number | No | Minimum scheduling notice for events |
| `allowBookingAfterUnit` | string (enum: `hours`, `days`, `weeks`, `months`) | No | Unit for minimum scheduling notice |
| `allowBookingFor` | number | No | Minimum number of days/weeks/months for which to allow booking events |
| `allowBookingForUnit` | string (enum: `days`, `weeks`, `months`) | No | Unit for controlling the duration for which booking would be allowed for |
| `openHours` | array of object | No | This is only to set the standard availability. For custom availability, use the availabilities property |
| `enableRecurring` | boolean | No | Enable recurring appointments for the calendars. Please note that only one member should be added in the calendar to enable this Default: `False` |
| `recurring` | object | No |  |
| `formId` | string | No |  |
| `stickyContact` | boolean | No |  |
| `isLivePaymentMode` | boolean | No |  |
| `autoConfirm` | boolean | No |  Default: `True` |
| `shouldSendAlertEmailsToAssignedMember` | boolean | No |  |
| `alertEmail` | string | No |  |
| `googleInvitationEmails` | boolean | No |  Default: `False` |
| `allowReschedule` | boolean | No |  Default: `True` |
| `allowCancellation` | boolean | No |  Default: `True` |
| `shouldAssignContactToTeamMember` | boolean | No |  |
| `shouldSkipAssigningContactForExisting` | boolean | No |  |
| `notes` | string | No |  |
| `pixelId` | string | No |  |
| `formSubmitType` | string (enum: `RedirectURL`, `ThankYouMessage`) | No |  Default: `ThankYouMessage` |
| `formSubmitRedirectURL` | string | No |  |
| `formSubmitThanksMessage` | string | No |  |
| `availabilityType` | number (enum: `0`, `1`) | No | Determines which availability type to consider: - **1**: Only custom availabilities will be used. - **0**: Only open hours will be used. - **null**: Both custom availabilities and open hours will be c... |
| `availabilities` | array of object | No | This is only to set the custom availability. For standard availability, use the openHours property |
| `guestType` | string (enum: `count_only`, `collect_detail`) | No |  |
| `consentLabel` | string | No |  |
| `calendarCoverImage` | string | No |  |
| `lookBusyConfig` | object | No |  |
| `id` | string | Yes |  |

### CalendarDeleteSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | Yes | Success |

### CalendarEventDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Event Id or Instance id for a recurring event |
| `address` | string | No | Calendar Event address |
| `title` | string | Yes | Calendar Event title |
| `calendarId` | string | Yes | Calendar ID |
| `locationId` | string | Yes | Location ID |
| `contactId` | string | Yes | Contact ID |
| `groupId` | string | Yes | Group ID |
| `appointmentStatus` | string | Yes | Appointment Status |
| `assignedUserId` | string | Yes | AssignedUser - the primary owner of an appointment |
| `users` | array of string | Yes | Users - the secondary owners of an appointment. |
| `notes` | string | No | Notes |
| `description` | string | No | Description |
| `isRecurring` | boolean | No | true if the event is recurring otherwise false |
| `rrule` | string | No | RRULE as per the iCalendar (RFC 5545) specification for recurring events. DTSTART is not required, instance ids are calculated on the basis of startTime of the event. |
| `startTime` | object | Yes | Start Time |
| `endTime` | object | Yes | End Time |
| `dateAdded` | object | Yes | Date Added |
| `dateUpdated` | object | Yes | Date Updated |
| `assignedResources` | array of string | No | Ids of associated resources rooms and/or equipments |
| `createdBy` | object | No |  |
| `masterEventId` | string | No | Master event id for a recurring instance |

### CalendarNotification

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `email`) | No | Calendar Notification Default: `email` |
| `shouldSendToContact` | boolean | Yes |  |
| `shouldSendToGuest` | boolean | Yes |  |
| `shouldSendToUser` | boolean | Yes |  |
| `shouldSendToSelectedUsers` | boolean | Yes |  |
| `selectedUsers` | string | Yes | Comma separated emails |

### CalendarNotificationDeleteResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Result of delete/update operation |

### CalendarNotificationResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | No | Notification ID |
| `receiverType` | string (enum: `contact`, `guest`, `assignedUser`, `emails`, `phoneNumbers`, `business`) | No |  |
| `additionalEmailIds` | array of string | No |  |
| `additionalPhoneNumbers` | array of string | No |  |
| `channel` | string (enum: `email`, `inApp`, `sms`, `whatsapp`) | No |  |
| `notificationType` | string (enum: `booked`, `confirmation`, `cancellation`, `reminder`, `followup`, `reschedule`) | No |  |
| `isActive` | boolean | No |  |
| `additionalWhatsappNumbers` | array of string | No |  |
| `templateId` | string | No |  |
| `body` | string | No |  |
| `subject` | string | No |  |
| `afterTime` | array of object | No |  |
| `beforeTime` | array of object | No |  |
| `selectedUsers` | array of string | No |  |
| `deleted` | boolean | No |  |

### CalendarResourceByIdResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID of the resource |
| `name` | string | Yes | Name of the resource |
| `resourceType` | string (enum: `equipments`, `rooms`) | Yes |  |
| `isActive` | boolean | Yes | Whether the resource is active |
| `description` | string | No | Description of the resource |
| `quantity` | number | No | Quantity of the resource |
| `outOfService` | number | No | Indicates if the resource is out of service |
| `capacity` | number | No | Capacity of the resource |
| `calendarIds` | array of string | Yes | Calendar IDs |

### CalendarResourceResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location ID of the resource |
| `name` | string | Yes | Name of the resource |
| `resourceType` | string (enum: `equipments`, `rooms`) | Yes |  |
| `isActive` | boolean | Yes | Whether the resource is active |
| `description` | string | No | Description of the resource |
| `quantity` | number | No | Quantity of the resource |
| `outOfService` | number | No | Indicates if the resource is out of service |
| `capacity` | number | No | Capacity of the resource |

### CalendarUpdateDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notifications` | array of object | No | 🚨 Deprecated! Please use 'Calendar Notifications APIs' instead. |
| `groupId` | string | No | Group Id |
| `teamMembers` | array of object | No | Team members are required for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member. |
| `eventType` | string (enum: `RoundRobin_OptimizeForAvailability`, `RoundRobin_OptimizeForEqualDistribution`) | No |  |
| `name` | string | No |  |
| `description` | string | No |  |
| `slug` | string | No |  |
| `widgetSlug` | string | No |  |
| `widgetType` | string (enum: `default`, `classic`) | No | Calendar widget type. Choose "default" for "neo" and "classic" for "classic" layout. Default: `classic` |
| `eventTitle` | string | No |  |
| `eventColor` | string | No |  Default: `#039be5` |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` or `teamMembers[].locationConfigurations.location` instead. |
| `slotDuration` | number | No | This controls the duration of the meeting Default: `30` |
| `slotDurationUnit` | string (enum: `mins`, `hours`) | No | Unit for slot duration. |
| `preBufferUnit` | string (enum: `mins`, `hours`) | No | Unit for pre-buffer. |
| `slotInterval` | number | No | Slot interval reflects the amount of time the between booking slots that will be shown in the calendar. Default: `30` |
| `slotIntervalUnit` | string (enum: `mins`, `hours`) | No | Unit for slot interval. |
| `slotBuffer` | number | No | Slot-Buffer is additional time that can be added after an appointment, allowing for extra time to wrap up |
| `preBuffer` | number | No | Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready |
| `appoinmentPerSlot` | number | No |  |
| `appoinmentPerDay` | number | No | Number of appointments that can be booked for a given day |
| `allowBookingAfter` | number | No | Minimum scheduling notice for events |
| `allowBookingAfterUnit` | string (enum: `hours`, `days`, `weeks`, `months`) | No | Unit for minimum scheduling notice |
| `allowBookingFor` | number | No | Minimum number of days/weeks/months for which to allow booking events |
| `allowBookingForUnit` | string (enum: `days`, `weeks`, `months`) | No | Unit for controlling the duration for which booking would be allowed for |
| `openHours` | array of object | No |  |
| `enableRecurring` | boolean | No | Enable recurring appointments for the calendars. Please note that only one member should be added in the calendar to enable this Default: `False` |
| `recurring` | object | No |  |
| `formId` | string | No |  |
| `stickyContact` | boolean | No |  |
| `isLivePaymentMode` | boolean | No |  |
| `autoConfirm` | boolean | No |  |
| `shouldSendAlertEmailsToAssignedMember` | boolean | No |  |
| `alertEmail` | string | No |  |
| `googleInvitationEmails` | boolean | No |  |
| `allowReschedule` | boolean | No |  |
| `allowCancellation` | boolean | No |  |
| `shouldAssignContactToTeamMember` | boolean | No |  |
| `shouldSkipAssigningContactForExisting` | boolean | No |  |
| `notes` | string | No |  |
| `pixelId` | string | No |  |
| `formSubmitType` | string (enum: `RedirectURL`, `ThankYouMessage`) | No |  Default: `ThankYouMessage` |
| `formSubmitRedirectURL` | string | No |  |
| `formSubmitThanksMessage` | string | No |  |
| `availabilityType` | number (enum: `0`, `1`) | No | Determines which availability type to consider: - **1**: Only custom availabilities will be used. - **0**: Only open hours will be used. - **null**: Both the custom availabilities and open hours will ... |
| `availabilities` | array of object | No | This is only to set the custom availability. For standard availability, use the openHours property |
| `guestType` | string (enum: `count_only`, `collect_detail`) | No |  |
| `consentLabel` | string | No |  |
| `calendarCoverImage` | string | No |  |
| `lookBusyConfig` | object | No |  |
| `isActive` | boolean | No |  |

### CalendarsGetSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `calendars` | array of object | No |  |

### CreateCalendarNotificationDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `receiverType` | string (enum: `contact`, `guest`, `assignedUser`, `emails`, `phoneNumbers`, `business`) | Yes | notification recipient type |
| `channel` | string (enum: `email`, `inApp`, `sms`, `whatsapp`) | Yes | Notification channel |
| `notificationType` | string (enum: `booked`, `confirmation`, `cancellation`, `reminder`, `followup`, `reschedule`) | Yes | Notification type |
| `isActive` | boolean | No | Is the notification active Default: `True` |
| `templateId` | string | No | Template ID for email notification. Not necessary for in-App notification |
| `body` | string | No | Body  for email notification. Not necessary for in-App notification |
| `subject` | string | No | Subject  for email notification. Not necessary for in-App notification |
| `afterTime` | array of object | No | Specifies the time after which the follow-up notification should be sent. This is not required for other notification types. |
| `beforeTime` | array of object | No | Specifies the time before which the reminder notification should be sent. This is not required for other notification types. |
| `additionalEmailIds` | array of string | No | Additional email addresses to receive notifications. |
| `additionalPhoneNumbers` | array of string | No | Additional phone numbers to receive notifications. |
| `selectedUsers` | array of string | No | Selected users for in-App and business email notifications. Supports user IDs and special keyword "sub_account_admin" |
| `fromAddress` | string | No | from address for email notification |
| `fromName` | string | No | from name for email/sms notification |
| `fromNumber` | string | No | from number for sms notification |

### CreateCalendarResourceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `description` | string | Yes |  |
| `quantity` | number | Yes | Quantity of the equipment. |
| `outOfService` | number | Yes | Quantity of the out of service equipment. |
| `capacity` | number | Yes | Capacity of the room. |
| `calendarIds` | array of string | Yes | Service calendar IDs to be mapped with the resource.      One equipment can only be mapped with one service calendar.      One room can be mapped with multiple service calendars. |

### CreateScheduleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `rules` | array of object | No | Schedule rules defining when the schedule is active |
| `timezone` | string | Yes | Timezone for the schedule (IANA timezone identifier) |
| `locationId` | string | Yes | Location ID where this schedule applies |
| `name` | string | Yes | Human-readable name for the schedule |
| `userId` | string | Yes | User ID associated with the schedule |
| `calendarIds` | array of string | No | Calendar IDs associated with the schedule |

### CreatedOrUpdatedBy

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No | The ID of the user who created or updated the appointment |
| `source` | string | Yes | The source of the appointment |

### DeleteAppointmentSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### DeleteEventSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeeded` | boolean | No |  |

### DeleteNoteSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No |  |

### GetAllSchedulesResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedules` | array of object | Yes | Array of schedules |

### GetCalendarEventSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `event` | object | No |  |

### GetCalendarEventsSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `events` | array of object | No |  |

### GetCreateUpdateNoteSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `note` | object | No |  |

### GetNoteSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `body` | string | No |  |
| `userId` | string | No |  |
| `dateAdded` | string | No |  |
| `contactId` | string | No |  |
| `createdBy` | object | No |  |

### GetNotesListSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notes` | array of object | No |  |
| `hasMore` | boolean | No |  |

### GroupCreateDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `description` | string | Yes |  |
| `slug` | string | Yes |  |
| `isActive` | boolean | No |  |

### GroupCreateSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `group` | object | No |  |

### GroupDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes |  |
| `name` | string | Yes |  |
| `description` | string | Yes |  |
| `slug` | string | Yes |  |
| `isActive` | boolean | No |  |
| `id` | string | No |  |

### GroupStatusUpdateParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isActive` | boolean | Yes | Is Active? |

### GroupSuccessfulResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Success |

### GroupUpdateDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes |  |
| `description` | string | Yes |  |
| `slug` | string | Yes |  |

### Hour

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `openHour` | number | Yes |  |
| `openMinute` | number | Yes |  |
| `closeHour` | number | Yes |  |
| `closeMinute` | number | Yes |  |

### LocationConfiguration

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `kind` | string (enum: `custom`, `zoom_conference`, `google_conference`, `inbound_call`, `outbound_call`, `physical`, `booker`, `ms_teams_conference`) | Yes | Type of meeting location. zoom_conference/google_conference/ms_teams_conference is not supported in event calendar type |
| `location` | string | No | Address for meeting location. Not applicable on "zoom_conference", "google_conference" and "ms_teams_conference" kind |

### LocationConfigurationResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `kind` | string (enum: `custom`, `zoom_conference`, `google_conference`, `inbound_call`, `outbound_call`, `physical`, `booker`, `ms_teams_conference`) | Yes | Type of meeting location. zoom_conference/google_conference/ms_teams_conference is not supported in event calendar type |
| `location` | string | No | Address for meeting location. Not applicable on "zoom_conference", "google_conference" and "ms_teams_conference" kind |
| `meetingId` | string | No | Unique ID used to select a specific meeting location |

### LookBusyConfiguration

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | Yes | Apply Look Busy Default: `False` |
| `LookBusyPercentage` | number | Yes | Percentage of slots that will be hidden |

### NoteCreatedBySchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |

### NotesDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | No |  |
| `body` | string | Yes | Note body |

### OpenHour

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `daysOfTheWeek` | array of number | Yes |  |
| `hours` | array of object | Yes |  |

### Recurring

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `freq` | string (enum: `DAILY`, `WEEKLY`, `MONTHLY`) | No |  |
| `count` | number | No | Number of recurrences |
| `bookingOption` | string (enum: `skip`, `continue`, `book_next`) | No | This setting contols what to do incase a recurring slot is unavailable |
| `bookingOverlapDefaultStatus` | string (enum: `confirmed`, `new`) | No | This setting contols what to do incase a recurring slot is unavailable |

### ResourceDeleteResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | boolean | No | Success |

### ScheduleIntervalDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `from` | string | Yes | Start time in HH:MM format (24-hour format) |
| `to` | string | Yes | End time in HH:MM format (24-hour format) |

### ScheduleObjectResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the schedule |
| `name` | string | Yes | Human-readable name for the schedule |
| `locationId` | string | Yes | Location ID where this schedule applies |
| `rules` | array of object | Yes | Schedule rules defining when the schedule is active |
| `timezone` | string | Yes | Timezone for the schedule (IANA timezone identifier) |
| `dateAdded` | string | Yes | ISO date string when the schedule was created |
| `dateUpdated` | string | Yes | ISO date string when the schedule was last updated |
| `userId` | string | Yes | User ID associated with the schedule |
| `calendarIds` | array of string | No | Calendar IDs associated with the schedule |
| `deleted` | boolean | Yes | Whether the schedule has been deleted |

### ScheduleResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `schedule` | object | Yes |  |

### ScheduleRuleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `wday`, `date`) | Yes | Type of schedule rule - weekday (recurring) or date (specific date) |
| `intervals` | array of object | Yes | Time intervals for the rule (e.g., 9 AM to 5 PM) |
| `date` | string | No | Specific date in YYYY-MM-DD format (only for date-type rules) |
| `day` | string (enum: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`) | No | Day of week (only for weekday-type rules) |

### SchedulesDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `timeOffset` | number | No |  |
| `unit` | string | No |  |

### SlotsSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `slots` | array of string | Yes |  |

### TeamMember

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | Yes |  |
| `priority` | number (enum: `0`, `0.5`, `1`) | No |  Default: `0.5` |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `teams`, `booker`) | No | 🚨 Deprecated! Use `locationConfigurations.kind` instead. Default: `custom` |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` instead. |
| `isPrimary` | boolean | No | Marks a user as primary. This property is required in case of collective booking calendars. Only one user can be primary. |
| `locationConfigurations` | array of object | No | Meeting location configuration for event calendar. - *Multiple locations are allowed only when one team member is selected.* - *For **Class booking** and **Collective** calendars, only one location co... |

### TeamMemberResponse

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | string | Yes |  |
| `priority` | number (enum: `0`, `0.5`, `1`) | No |  Default: `0.5` |
| `meetingLocationType` | string (enum: `custom`, `zoom`, `gmeet`, `phone`, `address`, `teams`, `booker`) | No | 🚨 Deprecated! Use `locationConfigurations.kind` instead. Default: `custom` |
| `meetingLocation` | string | No | 🚨 Deprecated! Use `locationConfigurations.location` instead. |
| `isPrimary` | boolean | No | Marks a user as primary. This property is required in case of collective booking calendars. Only one user can be primary. |
| `locationConfigurations` | array of object | No | Meeting location configurations |

### UpdateAvailability

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `date` | string | Yes | Formulate the date string in the format of `<YYYY-MM-DD in local timezone>T00:00:00.000Z`. |
| `hours` | array of object | Yes |  |
| `deleted` | boolean | No |  Default: `False` |
| `id` | string | No | The ID of the custom availability object. It is required while updating or deleting the existing custom date availability |

### UpdateCalendarNotificationsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `receiverType` | string (enum: `contact`, `guest`, `assignedUser`, `emails`, `phoneNumbers`, `business`) | No | Notification recipient type |
| `additionalEmailIds` | array of string | No | Additional email addresses to receive notifications. |
| `additionalPhoneNumbers` | array of string | No | Additional phone numbers to receive notifications. |
| `selectedUsers` | array of string | No | Selected users for in-App and business email notifications. Supports user IDs and special keyword "sub_account_admin" |
| `channel` | string (enum: `email`, `inApp`, `sms`, `whatsapp`) | No | Notification channel |
| `notificationType` | string (enum: `booked`, `confirmation`, `cancellation`, `reminder`, `followup`, `reschedule`) | No | Notification type |
| `isActive` | boolean | No | Is the notification active Default: `True` |
| `deleted` | boolean | No | Marks the notification as deleted (soft delete) Default: `False` |
| `templateId` | string | No | Template ID for email notification |
| `body` | string | No | Body  for email notification. Not necessary for in-App notification |
| `subject` | string | No | Subject  for email notification. Not necessary for in-App notification |
| `afterTime` | array of object | No | Specifies the time after which the follow-up notification should be sent. This is not required for other notification types. |
| `beforeTime` | array of object | No | Specifies the time before which the reminder notification should be sent. This is not required for other notification types. |
| `fromAddress` | string | No | From address for email notification |
| `fromNumber` | string | No | from number for sms notification |
| `fromName` | string | No | From name for email/sms notification |

### UpdateCalendarResourceDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | No |  |
| `name` | string | No |  |
| `description` | string | No |  |
| `quantity` | number | No | Quantity of the equipment. |
| `outOfService` | number | No | Quantity of the out of service equipment. |
| `capacity` | number | No | Capacity of the room. |
| `calendarIds` | array of string | No | Service calendar IDs to be mapped with the resource.      One equipment can only be mapped with one service calendar.      One room can be mapped with multiple service calendars. |
| `isActive` | boolean | No |  |

### UpdateScheduleDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | No | Human-readable name for the schedule |
| `rules` | array of object | No | Updated schedule rules defining when the schedule is active |
| `timezone` | string | No | Updated timezone for the schedule (IANA timezone identifier) |

### ValidateGroupSlugPostBody

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `slug` | string | Yes | Slug |

### ValidateGroupSlugSuccessResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `available` | boolean | Yes |  |
