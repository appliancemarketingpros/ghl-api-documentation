# GoHighLevel API Documentation

Comprehensive API documentation for the GoHighLevel (HighLevel) platform, converted to Markdown format for easy reference and integration.

> **Source:** This documentation is automatically synced from the [official GoHighLevel API V2 documentation](https://marketplace.gohighlevel.com/docs/) and the [GoHighLevel API docs repository](https://github.com/GoHighLevel/highlevel-api-docs). It is checked for updates daily via GitHub Actions.

## Table of Contents

### Authentication & OAuth

- [Overview](docs/oauth/Overview.md)
- [Scopes](docs/oauth/Scopes.md)
- [Authorization](docs/oauth/Authorization.md)
- [External Billing](docs/oauth/Billing.md)
- [External Authentication](docs/oauth/ExternalAuthentication.md)
- [Webhook Authentication](docs/oauth/WebhookAuthentication.md)
- [FAQs](docs/oauth/Faqs.md)

### API Reference

| API | Description | Documentation |
|-----|-------------|---------------|
| Agencies | 0 endpoints | [Agencies API](api-reference/agencies.md) |
| Associations | 10 endpoints | [Associations API](api-reference/associations.md) |
| Blogs | 7 endpoints | [Blogs API](api-reference/blogs.md) |
| Businesses | 5 endpoints | [Businesses API](api-reference/businesses.md) |
| Calendars | 34 endpoints | [Calendars API](api-reference/calendars.md) |
| Campaigns | 1 endpoints | [Campaigns API](api-reference/campaigns.md) |
| Companies | 1 endpoints | [Companies API](api-reference/companies.md) |
| Contacts | 32 endpoints | [Contacts API](api-reference/contacts.md) |
| Conversations | 19 endpoints | [Conversations API](api-reference/conversations.md) |
| Courses | 1 endpoints | [Courses API](api-reference/courses.md) |
| Custom Fields V2 | 8 endpoints | [Custom Fields V2 API](api-reference/custom-fields.md) |
| Custom Menus | 5 endpoints | [Custom Menus API](api-reference/custom-menus.md) |
| LC Email | 1 endpoints | [LC Email API](api-reference/email-isv.md) |
| Emails | 5 endpoints | [Emails API](api-reference/emails.md) |
| Forms | 3 endpoints | [Forms API](api-reference/forms.md) |
| Funnels | 7 endpoints | [Funnels API](api-reference/funnels.md) |
| Invoices | 41 endpoints | [Invoices API](api-reference/invoices.md) |
| Trigger Links | 6 endpoints | [Trigger Links API](api-reference/links.md) |
| Sub-Accounts (Locations) | 29 endpoints | [Sub-Accounts (Locations) API](api-reference/locations.md) |
| Marketplace | 7 endpoints | [Marketplace API](api-reference/marketplace.md) |
| Media Library | 7 endpoints | [Media Library API](api-reference/medias.md) |
| OAuth 2.0 | 3 endpoints | [OAuth 2.0 API](api-reference/oauth.md) |
| Objects | 9 endpoints | [Objects API](api-reference/objects.md) |
| Opportunities | 10 endpoints | [Opportunities API](api-reference/opportunities.md) |
| Payments | 24 endpoints | [Payments API](api-reference/payments.md) |
| Phone System | 2 endpoints | [Phone System API](api-reference/phone-system.md) |
| Products | 27 endpoints | [Products API](api-reference/products.md) |
| Proposals & Estimates | 4 endpoints | [Proposals & Estimates API](api-reference/proposals.md) |
| SaaS API | 22 endpoints | [SaaS API API](api-reference/saas-api.md) |
| Snapshots | 4 endpoints | [Snapshots API](api-reference/snapshots.md) |
| Social Media Posting | 40 endpoints | [Social Media Posting API](api-reference/social-media-posting.md) |
| Store | 18 endpoints | [Store API](api-reference/store.md) |
| Surveys | 2 endpoints | [Surveys API](api-reference/surveys.md) |
| Users | 7 endpoints | [Users API](api-reference/users.md) |
| Voice AI | 11 endpoints | [Voice AI API](api-reference/voice-ai.md) |
| Workflows | 1 endpoints | [Workflows API](api-reference/workflows.md) |

### Webhook Events

- [AppInstall](docs/webhook-events/AppInstall.md)
- [AppUninstall](docs/webhook-events/AppUninstall.md)
- [AppointmentCreate](docs/webhook-events/AppointmentCreate.md)
- [AppointmentDelete](docs/webhook-events/AppointmentDelete.md)
- [AppointmentUpdate](docs/webhook-events/AppointmentUpdate.md)
- [AssociationCreate](docs/webhook-events/AssociationCreate.md)
- [AssociationDelete](docs/webhook-events/AssociationDelete.md)
- [AssociationUpdate](docs/webhook-events/AssociationUpdate.md)
- [CampaignStatusUpdate](docs/webhook-events/CampaignStatusUpdate.md)
- [ContactCreate](docs/webhook-events/ContactCreate.md)
- [ContactDelete](docs/webhook-events/ContactDelete.md)
- [ContactDndUpdate](docs/webhook-events/ContactDndUpdate.md)
- [ContactTagUpdate](docs/webhook-events/ContactTagUpdate.md)
- [ContactUpdate](docs/webhook-events/ContactUpdate.md)
- [ConversationUnreadWebhook](docs/webhook-events/ConversationUnreadWebhook.md)
- [InboundMessage](docs/webhook-events/InboundMessage.md)
- [InvoiceCreate](docs/webhook-events/InvoiceCreate.md)
- [InvoiceDelete](docs/webhook-events/InvoiceDelete.md)
- [InvoicePaid](docs/webhook-events/InvoicePaid.md)
- [InvoicePartiallyPaid](docs/webhook-events/InvoicePartiallyPaid.md)
- [InvoiceSent](docs/webhook-events/InvoiceSent.md)
- [InvoiceUpdate](docs/webhook-events/InvoiceUpdate.md)
- [InvoiceVoid](docs/webhook-events/InvoiceVoid.md)
- [LCEmailStats](docs/webhook-events/LCEmailStats.md)
- [LocationCreate](docs/webhook-events/LocationCreate.md)
- [LocationUpdate](docs/webhook-events/LocationUpdate.md)
- [NoteCreate](docs/webhook-events/NoteCreate.md)
- [NoteDelete](docs/webhook-events/NoteDelete.md)
- [NoteUpdate](docs/webhook-events/NoteUpdate.md)
- [ObjectSchemaCreate](docs/webhook-events/ObjectSchemaCreate.md)
- [ObjectSchemaUpdate](docs/webhook-events/ObjectSchemaUpdate.md)
- [OpportunityAssignedToUpdate](docs/webhook-events/OpportunityAssignedToUpdate.md)
- [OpportunityCreate](docs/webhook-events/OpportunityCreate.md)
- [OpportunityDelete](docs/webhook-events/OpportunityDelete.md)
- [OpportunityMonetaryValueUpdate](docs/webhook-events/OpportunityMonetaryValueUpdate.md)
- [OpportunityStageUpdate](docs/webhook-events/OpportunityStageUpdate.md)
- [OpportunityStatusUpdate](docs/webhook-events/OpportunityStatusUpdate.md)
- [OpportunityUpdate](docs/webhook-events/OpportunityUpdate.md)
- [OrderCreate](docs/webhook-events/OrderCreate.md)
- [OrderStatusUpdate](docs/webhook-events/OrderStatusUpdate.md)
- [OutboundMessage](docs/webhook-events/OutboundMessage.md)
- [PlanChange](docs/webhook-events/PlanChange.md)
- [PriceCreate](docs/webhook-events/PriceCreate.md)
- [PriceDelete](docs/webhook-events/PriceDelete.md)
- [PriceUpdate](docs/webhook-events/PriceUpdate.md)
- [ProductCreate](docs/webhook-events/ProductCreate.md)
- [ProductDelete](docs/webhook-events/ProductDelete.md)
- [ProductUpdate](docs/webhook-events/ProductUpdate.md)
- [ProviderOutboundMessage](docs/webhook-events/ProviderOutboundMessage.md)
- [RecordCreate](docs/webhook-events/RecordCreate.md)
- [RecordDelete](docs/webhook-events/RecordDelete.md)
- [RecordUpdate](docs/webhook-events/RecordUpdate.md)
- [RelationCreate](docs/webhook-events/RelationCreate.md)
- [RelationDelete](docs/webhook-events/RelationDelete.md)
- [TaskComplete](docs/webhook-events/TaskComplete.md)
- [TaskCreate](docs/webhook-events/TaskCreate.md)
- [TaskDelete](docs/webhook-events/TaskDelete.md)
- [UserCreate](docs/webhook-events/UserCreate.md)

### Marketplace Modules

- [ConversationProviders](docs/marketplace-modules/ConversationProviders.md)
- [CustomJs](docs/marketplace-modules/CustomJs.md)
- [shared_secret_customJS_customPages](docs/marketplace-modules/shared_secret_customJS_customPages.md)

### Other Documentation

- [Country List](docs/other/Country.md)

## Quick Start

### Base URL

All API requests should be made to:

```
https://services.leadconnectorhq.com
```

### Authentication

The GoHighLevel API uses **OAuth 2.0** for authentication. See the [OAuth Overview](docs/oauth/Overview.md) for details.

### Example Request

```bash
curl -X GET \
  https://services.leadconnectorhq.com/contacts/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Version: 2021-07-28"
```

## Contributing

This documentation is maintained by [Appliance Marketing Pros](https://github.com/appliancemarketingpros). For official API issues, please refer to the [GoHighLevel API docs repository](https://github.com/GoHighLevel/highlevel-api-docs).

## License

This documentation is provided for reference purposes. GoHighLevel and HighLevel are trademarks of HighLevel Inc.
