# Users API

Documentation for users API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Search](#search)
- [Users](#users)

## Search

### GET `/users/search`

**Search Users**

Search Users

**Operation ID:** `search-users`

**Tags:** Search

**Required Scopes:** `users.readonly`, `users.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `companyId` | query | string | Yes | Company ID in which the search needs to be performed |
| `query` | query | string | No | The search term for the user is matched based on the user full name, email or phone |
| `skip` | query | string | No | No of results to be skipped before returning the result |
| `limit` | query | string | No | No of results to be limited before returning the result |
| `locationId` | query | string | No | Location ID in which the search needs to be performed |
| `type` | query | string | No | Type of the users to be filtered in the search |
| `role` | query | string | No | Role of the users to be filtered in the search |
| `ids` | query | string | No | List of User IDs to be filtered in the search |
| `sort` | query | string | No | The field on which sort is applied in which the results need to be sorted. Default is based on the first and last name |
| `sortDirection` | query | string | No | The direction in which the results need to be sorted |
| `enabled2waySync` | query | boolean | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `users` | array of object | No |  |
| `count` | number | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/users/search/filter-by-email`

**Filter Users by Email**

Filter users by company ID, deleted status, and email array

**Operation ID:** `filter-users-by-email`

**Tags:** Search

**Required Scopes:** `users.readonly`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes | Company ID to filter users |
| `emails` | string | Yes | Comma-separated list of email addresses to filter users |
| `deleted` | boolean | No | Filter deleted users Default: `False` |
| `skip` | string | No | No of results to be skipped before returning the result Default: `0` |
| `limit` | string | No | No of results to be limited before returning the result Default: `25` |
| `projection` | string | No | Projection fields to return. Use "all" for all fields, or specify comma-separated field names. Default returns only id and email |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `users` | array of object | No |  |
| `count` | number | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Users

### GET `/users/{userId}`

**Get User**

Get User

**Operation ID:** `get-user`

**Tags:** Users

**Required Scopes:** `users.readonly`, `users.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `userId` | path | string | Yes | User Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `extension` | string | No |  |
| `permissions` | object | No |  |
| `scopes` | string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No |  |
| `roles` | object | No |  |
| `lcPhone` | object | No | LC Phone Inbound Phone Numbers |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/users/{userId}`

**Update User**

Update User

**Operation ID:** `update-user`

**Tags:** Users

**Required Scopes:** `users.write`, `users.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No | Email update is no longer supported due to security reasons. |
| `password` | string | No |  |
| `phone` | string | No |  |
| `type` | string | No |  |
| `role` | string | No |  |
| `companyId` | string | No | Company/Agency Id. Required for Agency Level access |
| `locationIds` | array of string | No |  |
| `permissions` | object | No |  |
| `scopes` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Scopes allowed for users. Only scopes that have been passed will be enabled. If passed empty all the scopes will be get disabled |
| `scopesAssignedToOnly` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Assigned Scopes allowed for users. Only scopes that have been passed will be enabled. If passed empty all the assigned scopes will be get disabled |
| `profilePhoto` | string | No |  |
| `twilioPhone` | object | No | Per-location inbound Twilio number in E.164 format, keyed by location id (Call and Voicemail Inbound Number for direct Twilio, not LC Phone). Replacement semantics: if you send twilioPhone in the requ... |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

**`permissions` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignsEnabled` | boolean | No |  Default: `True` |
| `campaignsReadOnly` | boolean | No |  Default: `False` |
| `contactsEnabled` | boolean | No |  Default: `True` |
| `workflowsEnabled` | boolean | No |  Default: `True` |
| `workflowsReadOnly` | boolean | No |  Default: `False` |
| `triggersEnabled` | boolean | No |  Default: `True` |
| `funnelsEnabled` | boolean | No |  Default: `True` |
| `websitesEnabled` | boolean | No |  Default: `False` |
| `opportunitiesEnabled` | boolean | No |  Default: `True` |
| `dashboardStatsEnabled` | boolean | No |  Default: `True` |
| `bulkRequestsEnabled` | boolean | No |  Default: `True` |
| `appointmentsEnabled` | boolean | No |  Default: `True` |
| `reviewsEnabled` | boolean | No |  Default: `True` |
| `onlineListingsEnabled` | boolean | No |  Default: `True` |
| `phoneCallEnabled` | boolean | No |  Default: `True` |
| `conversationsEnabled` | boolean | No |  Default: `True` |
| `assignedDataOnly` | boolean | No |  Default: `False` |
| `adwordsReportingEnabled` | boolean | No |  Default: `False` |
| `membershipEnabled` | boolean | No |  Default: `False` |
| `facebookAdsReportingEnabled` | boolean | No |  Default: `False` |
| `attributionsReportingEnabled` | boolean | No |  Default: `False` |
| `settingsEnabled` | boolean | No |  Default: `True` |
| `tagsEnabled` | boolean | No |  Default: `True` |
| `leadValueEnabled` | boolean | No |  Default: `True` |
| `marketingEnabled` | boolean | No |  Default: `True` |
| `agentReportingEnabled` | boolean | No |  Default: `True` |
| `botService` | boolean | No |  Default: `False` |
| `socialPlanner` | boolean | No |  Default: `True` |
| `bloggingEnabled` | boolean | No |  Default: `True` |
| `invoiceEnabled` | boolean | No |  Default: `True` |
| `affiliateManagerEnabled` | boolean | No |  Default: `True` |
| `contentAiEnabled` | boolean | No |  Default: `True` |
| `refundsEnabled` | boolean | No |  Default: `True` |
| `recordPaymentEnabled` | boolean | No |  Default: `True` |
| `cancelSubscriptionEnabled` | boolean | No |  Default: `True` |
| `paymentsEnabled` | boolean | No |  Default: `True` |
| `communitiesEnabled` | boolean | No |  Default: `True` |
| `exportPaymentsEnabled` | boolean | No |  Default: `True` |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `extension` | string | No |  |
| `permissions` | object | No |  |
| `scopes` | string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No |  |
| `roles` | object | No |  |
| `lcPhone` | object | No | LC Phone Inbound Phone Numbers |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/users/{userId}`

**Delete User**

Delete User

**Operation ID:** `delete-user`

**Tags:** Users

**Required Scopes:** `users.write`, `users.write`

**API Version:** `2021-07-28`

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |
| `message` | string | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/users/`

**Get User by Location**

> **DEPRECATED**: This endpoint is deprecated and may be removed in future versions.

Deprecated. Use `GET /users/search` instead. Pass `locationId` as a query parameter to filter results by location, along with the required `companyId` and other search filters as needed.

**Operation ID:** `get-user-by-location`

**Tags:** Users

**Required Scopes:** `users.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `users` | array of object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/users/`

**Create User**

Create User

**Operation ID:** `create-user`

**Tags:** Users

**Required Scopes:** `users.write`, `users.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes |  |
| `firstName` | string | Yes |  |
| `lastName` | string | Yes |  |
| `email` | string | Yes |  |
| `password` | string | Yes |  |
| `phone` | string | No |  |
| `type` | string | Yes |  |
| `role` | string | Yes |  |
| `locationIds` | array of string | Yes |  |
| `permissions` | object | No |  |
| `scopes` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Scopes allowed for users. Only scopes that have been passed will be enabled. Note:- If passed empty all the scopes will be get disabled |
| `scopesAssignedToOnly` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Assigned Scopes allowed for users. Only scopes that have been passed will be enabled. If passed empty all the assigned scopes will be get disabled |
| `profilePhoto` | string | No |  |
| `twilioPhone` | object | No | Per-location inbound Twilio number in E.164 format, keyed by location id (Call and Voicemail Inbound Number for direct Twilio, not LC Phone). Replacement semantics: if you send twilioPhone in the requ... |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

**`permissions` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignsEnabled` | boolean | No |  Default: `True` |
| `campaignsReadOnly` | boolean | No |  Default: `False` |
| `contactsEnabled` | boolean | No |  Default: `True` |
| `workflowsEnabled` | boolean | No |  Default: `True` |
| `workflowsReadOnly` | boolean | No |  Default: `False` |
| `triggersEnabled` | boolean | No |  Default: `True` |
| `funnelsEnabled` | boolean | No |  Default: `True` |
| `websitesEnabled` | boolean | No |  Default: `False` |
| `opportunitiesEnabled` | boolean | No |  Default: `True` |
| `dashboardStatsEnabled` | boolean | No |  Default: `True` |
| `bulkRequestsEnabled` | boolean | No |  Default: `True` |
| `appointmentsEnabled` | boolean | No |  Default: `True` |
| `reviewsEnabled` | boolean | No |  Default: `True` |
| `onlineListingsEnabled` | boolean | No |  Default: `True` |
| `phoneCallEnabled` | boolean | No |  Default: `True` |
| `conversationsEnabled` | boolean | No |  Default: `True` |
| `assignedDataOnly` | boolean | No |  Default: `False` |
| `adwordsReportingEnabled` | boolean | No |  Default: `False` |
| `membershipEnabled` | boolean | No |  Default: `False` |
| `facebookAdsReportingEnabled` | boolean | No |  Default: `False` |
| `attributionsReportingEnabled` | boolean | No |  Default: `False` |
| `settingsEnabled` | boolean | No |  Default: `True` |
| `tagsEnabled` | boolean | No |  Default: `True` |
| `leadValueEnabled` | boolean | No |  Default: `True` |
| `marketingEnabled` | boolean | No |  Default: `True` |
| `agentReportingEnabled` | boolean | No |  Default: `True` |
| `botService` | boolean | No |  Default: `False` |
| `socialPlanner` | boolean | No |  Default: `True` |
| `bloggingEnabled` | boolean | No |  Default: `True` |
| `invoiceEnabled` | boolean | No |  Default: `True` |
| `affiliateManagerEnabled` | boolean | No |  Default: `True` |
| `contentAiEnabled` | boolean | No |  Default: `True` |
| `refundsEnabled` | boolean | No |  Default: `True` |
| `recordPaymentEnabled` | boolean | No |  Default: `True` |
| `cancelSubscriptionEnabled` | boolean | No |  Default: `True` |
| `paymentsEnabled` | boolean | No |  Default: `True` |
| `communitiesEnabled` | boolean | No |  Default: `True` |
| `exportPaymentsEnabled` | boolean | No |  Default: `True` |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `extension` | string | No |  |
| `permissions` | object | No |  |
| `scopes` | string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No |  |
| `roles` | object | No |  |
| `lcPhone` | object | No | LC Phone Inbound Phone Numbers |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### CreateUserDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes |  |
| `firstName` | string | Yes |  |
| `lastName` | string | Yes |  |
| `email` | string | Yes |  |
| `password` | string | Yes |  |
| `phone` | string | No |  |
| `type` | string | Yes |  |
| `role` | string | Yes |  |
| `locationIds` | array of string | Yes |  |
| `permissions` | object | No |  |
| `scopes` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Scopes allowed for users. Only scopes that have been passed will be enabled. Note:- If passed empty all the scopes will be get disabled |
| `scopesAssignedToOnly` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Assigned Scopes allowed for users. Only scopes that have been passed will be enabled. If passed empty all the assigned scopes will be get disabled |
| `profilePhoto` | string | No |  |
| `twilioPhone` | object | No | Per-location inbound Twilio number in E.164 format, keyed by location id (Call and Voicemail Inbound Number for direct Twilio, not LC Phone). Replacement semantics: if you send twilioPhone in the requ... |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

### DeleteUserSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | No |  |
| `message` | string | No |  |

### FilterByEmailDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `companyId` | string | Yes | Company ID to filter users |
| `emails` | string | Yes | Comma-separated list of email addresses to filter users |
| `deleted` | boolean | No | Filter deleted users Default: `False` |
| `skip` | string | No | No of results to be skipped before returning the result Default: `0` |
| `limit` | string | No | No of results to be limited before returning the result Default: `25` |
| `projection` | string | No | Projection fields to return. Use "all" for all fields, or specify comma-separated field names. Default returns only id and email |

### LocationSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `users` | array of object | No |  |

### PermissionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignsEnabled` | boolean | No |  Default: `True` |
| `campaignsReadOnly` | boolean | No |  Default: `False` |
| `contactsEnabled` | boolean | No |  Default: `True` |
| `workflowsEnabled` | boolean | No |  Default: `True` |
| `workflowsReadOnly` | boolean | No |  Default: `False` |
| `triggersEnabled` | boolean | No |  Default: `True` |
| `funnelsEnabled` | boolean | No |  Default: `True` |
| `websitesEnabled` | boolean | No |  Default: `False` |
| `opportunitiesEnabled` | boolean | No |  Default: `True` |
| `dashboardStatsEnabled` | boolean | No |  Default: `True` |
| `bulkRequestsEnabled` | boolean | No |  Default: `True` |
| `appointmentsEnabled` | boolean | No |  Default: `True` |
| `reviewsEnabled` | boolean | No |  Default: `True` |
| `onlineListingsEnabled` | boolean | No |  Default: `True` |
| `phoneCallEnabled` | boolean | No |  Default: `True` |
| `conversationsEnabled` | boolean | No |  Default: `True` |
| `assignedDataOnly` | boolean | No |  Default: `False` |
| `adwordsReportingEnabled` | boolean | No |  Default: `False` |
| `membershipEnabled` | boolean | No |  Default: `False` |
| `facebookAdsReportingEnabled` | boolean | No |  Default: `False` |
| `attributionsReportingEnabled` | boolean | No |  Default: `False` |
| `settingsEnabled` | boolean | No |  Default: `True` |
| `tagsEnabled` | boolean | No |  Default: `True` |
| `leadValueEnabled` | boolean | No |  Default: `True` |
| `marketingEnabled` | boolean | No |  Default: `True` |
| `agentReportingEnabled` | boolean | No |  Default: `True` |
| `botService` | boolean | No |  Default: `False` |
| `socialPlanner` | boolean | No |  Default: `True` |
| `bloggingEnabled` | boolean | No |  Default: `True` |
| `invoiceEnabled` | boolean | No |  Default: `True` |
| `affiliateManagerEnabled` | boolean | No |  Default: `True` |
| `contentAiEnabled` | boolean | No |  Default: `True` |
| `refundsEnabled` | boolean | No |  Default: `True` |
| `recordPaymentEnabled` | boolean | No |  Default: `True` |
| `cancelSubscriptionEnabled` | boolean | No |  Default: `True` |
| `paymentsEnabled` | boolean | No |  Default: `True` |
| `communitiesEnabled` | boolean | No |  Default: `True` |
| `exportPaymentsEnabled` | boolean | No |  Default: `True` |

### RoleSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | No |  |
| `role` | string | No |  |
| `locationIds` | array of string | No |  |
| `restrictSubAccount` | boolean | No |  |

### SearchUserSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `users` | array of object | No |  |
| `count` | number | No |  |

### UpdateUserDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No | Email update is no longer supported due to security reasons. |
| `password` | string | No |  |
| `phone` | string | No |  |
| `type` | string | No |  |
| `role` | string | No |  |
| `companyId` | string | No | Company/Agency Id. Required for Agency Level access |
| `locationIds` | array of string | No |  |
| `permissions` | object | No |  |
| `scopes` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Scopes allowed for users. Only scopes that have been passed will be enabled. If passed empty all the scopes will be get disabled |
| `scopesAssignedToOnly` | array of string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No | Assigned Scopes allowed for users. Only scopes that have been passed will be enabled. If passed empty all the assigned scopes will be get disabled |
| `profilePhoto` | string | No |  |
| `twilioPhone` | object | No | Per-location inbound Twilio number in E.164 format, keyed by location id (Call and Voicemail Inbound Number for direct Twilio, not LC Phone). Replacement semantics: if you send twilioPhone in the requ... |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

### UserSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `extension` | string | No |  |
| `permissions` | object | No |  |
| `scopes` | string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No |  |
| `roles` | object | No |  |
| `deleted` | boolean | No |  |
| `lcPhone` | object | No | LC Phone Inbound Phone Numbers |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |

### UserSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | No |  |
| `name` | string | No |  |
| `firstName` | string | No |  |
| `lastName` | string | No |  |
| `email` | string | No |  |
| `phone` | string | No |  |
| `extension` | string | No |  |
| `permissions` | object | No |  |
| `scopes` | string (enum: `campaigns.readonly`, `campaigns.write`, `calendars.readonly`, `calendars/events.write`, `calendars/groups.write`, `calendars.write`, `contacts.write`, `contacts/bulkActions.write`, `workflows.readonly`, `workflows.write`, `triggers.write`, `funnels.write`, `forms.write`, `surveys.write`, `quizzes.write`, `websites.write`, `medias.write`, `medias.readonly`, `opportunities.write`, `opportunities/leadValue.readonly`, `opportunities/bulkActions.write`, `reporting/phone.readonly`, `reporting/adwords.readonly`, `reporting/facebookAds.readonly`, `reporting/attributions.readonly`, `prospecting/auditReport.write`, `reporting/reports.readonly`, `reporting/agent.readonly`, `reporting/reports.write`, `reporting/stats.export`, `payments.write`, `payments/records.write`, `payments/orders.readonly`, `payments/orders.export`, `payments/orders.import`, `payments/orders.collectPayment`, `payments/subscriptions.readonly`, `payments/subscriptions.write`, `payments/subscriptions.update`, `payments/subscriptions.export`, `payments/subscriptions.pauseResumeCancel`, `payments/subscriptions.sharePaymentMethod`, `payments/transactions.readonly`, `payments/transactions.export`, `payments/transactions.import`, `payments/transactions.refund`, `payments/transactions.viewReceipts`, `payments/taxesSettings.readonly`, `payments/settings.readonly`, `payments/taxesSettings.updateInclusiveExclusive`, `payments/taxesSettings.manageRates`, `payments/taxesSettings.configureAutomatic`, `products.readonly`, `products.write`, `products.delete`, `products.duplicate`, `products.bulkActions`, `payments/settings.write`, `payments/settings.configureReceipt`, `payments/settings.configureSubscription`, `invoices.write`, `invoices.readonly`, `invoices/schedule.readonly`, `invoices/schedule.write`, `invoices/template.readonly`, `invoices/template.write`, `reputation/review.write`, `reputation/listing.write`, `reputation/reviewsAIAgents.write`, `reputation/gbp.write`, `conversations.write`, `conversations.readonly`, `conversations/message.readonly`, `conversations/message.write`, `contentAI.write`, `dashboard/stats.readonly`, `locations/tags.write`, `locations/tags.readonly`, `marketing.write`, `eliza.write`, `settings.write`, `socialplanner/post.write`, `socialplanner/account.readonly`, `socialplanner/account.write`, `socialplanner/category.readonly`, `socialplanner/category.write`, `socialplanner/csv.readonly`, `socialplanner/csv.write`, `socialplanner/group.write`, `socialplanner/hashtag.readonly`, `socialplanner/hashtag.write`, `socialplanner/oauth.readonly`, `socialplanner/oauth.write`, `socialplanner/post.readonly`, `socialplanner/recurring.readonly`, `socialplanner/recurring.write`, `socialplanner/review.readonly`, `socialplanner/review.write`, `socialplanner/rss.readonly`, `socialplanner/rss.write`, `socialplanner/search.readonly`, `socialplanner/setting.readonly`, `socialplanner/setting.write`, `socialplanner/stat.readonly`, `socialplanner/tag.readonly`, `socialplanner/tag.write`, `socialplanner/filters.readonly`, `socialplanner/medias.readonly`, `socialplanner/medias.write`, `socialplanner/watermarks.readonly`, `socialplanner/watermarks.write`, `socialplanner/metatag.readonly`, `socialplanner/facebook.readonly`, `socialplanner/linkedin.readonly`, `socialplanner/twitter.readonly`, `socialplanner/notification.readonly`, `socialplanner/notification.write`, `socialplanner/snapshot.readonly`, `socialplanner/snapshot.write`, `marketing/affiliate.write`, `blogs.write`, `membership.write`, `communities.write`, `gokollab.write`, `certificates.write`, `certificates.readonly`, `adPublishing.write`, `adPublishing.readonly`, `prospecting.write`, `prospecting.readonly`, `prospecting/reports.readonly`, `private-integration-location.readonly`, `private-integration-location.write`, `private-integration-company.readonly`, `private-integration-company.write`, `native-integrations.readonly`, `native-integrations.write`, `wordpress.write`, `wordpress.read`, `custom-menu-link.write`, `qrcodes.write`, `users/team-management.write`, `users/team-management.readonly`, `loginas.write`, `users-sso-login-management.write`, `users-sso-login-management.readonly`, `sso-config.write`, `snapshots/api.readonly`, `snapshots/api.create`, `snapshots/api.edit`, `snapshots/api.push`, `snapshots/api.refresh`, `snapshots/api.share`, `snapshots/api.delete`, `internaltools.location-transfer.write`, `internaltools.location-transfer.readonly`, `affiliateportal.write`, `affiliateportal.readonly`, `companies.write`, `internaltools.billing.write`, `internaltools.billing.readonly`, `internaltools.billing-common.readonly`, `internaltools.billing-common.write`, `voice-ai-agents.write`, `voice-ai-agents.readonly`, `voice-ai-common.readonly`, `voice-ai-common.write`, `voice-ai-agent-goals.readonly`, `voice-ai-agent-goals.write`, `voice-ai-dashboard.readonly`, `agency/launchpad.write`, `agency/launchpad.readonly`, `launchpad/location.write`, `launchpad/location.readonly`, `text-ai-agents.write`, `text-ai-agent-goals.readonly`, `text-ai-agent-goals.write`, `text-ai-agent-training.write`, `text-ai-agents-dashboard.readonly`, `locations.create`, `locations.delete`, `locations.export.list`, `locations.features-limits.manage`, `locations.pause-resume`, `locations.agency-subaccounts.manage`, `locations.billing.manage`, `locations.details.manage`, `audit-logs.readonly`, `audit-logs.export`) | No |  |
| `roles` | object | No |  |
| `lcPhone` | object | No | LC Phone Inbound Phone Numbers |
| `platformLanguage` | string (enum: `en_US`, `es`, `fr_CA`, `fr_FR`, `nl`, `de`, `pt_PT`, `pt_BR`, `it`, `sv`, `da`, `fi`, `no`) | No | Platform language preference for the user |
