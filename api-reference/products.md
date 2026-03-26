# Products API

Documentation for products API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Products](#products)
- [Prices](#prices)
- [Store](#store)
- [Collections](#collections)
- [Reviews](#reviews)

## Products

### POST `/products/bulk-update`

**Bulk Update Products**

API to bulk update products (price, availability, collections, delete)

**Operation ID:** `bulkUpdate`

**Tags:** Products

**Required Scopes:** `products.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `type` | string (enum: `bulk-update-price`, `bulk-update-availability`, `bulk-update-product-collection`, `bulk-delete-products`, `bulk-update-currency`) | Yes | Type of bulk update operation |
| `productIds` | array of string | Yes | Array of product IDs |
| `filters` | object | No |  |
| `price` | object | No |  |
| `compareAtPrice` | object | No |  |
| `availability` | boolean | No | New availability status |
| `collectionIds` | array of string | No | Array of collection IDs |
| `currency` | string | No | Currency code |

**`filters` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `collectionIds` | array of string | No | Filter by collection IDs |
| `productType` | string | No | Filter by product type |
| `availableInStore` | boolean | No | Filter by availability status |
| `search` | string | No | Filter by search term |

**`price` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `INCREASE_BY_AMOUNT`, `REDUCE_BY_AMOUNT`, `SET_NEW_PRICE`, `INCREASE_BY_PERCENTAGE`, `REDUCE_BY_PERCENTAGE`) | Yes | Type of price update |
| `value` | number | Yes | Value to update (amount or percentage based on type) |
| `roundToWhole` | boolean | No | Round to nearest whole number |

**`compareAtPrice` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `INCREASE_BY_AMOUNT`, `REDUCE_BY_AMOUNT`, `SET_NEW_PRICE`, `INCREASE_BY_PERCENTAGE`, `REDUCE_BY_PERCENTAGE`) | Yes | Type of price update |
| `value` | number | Yes | Value to update (amount or percentage based on type) |
| `roundToWhole` | boolean | No | Round to nearest whole number |

#### Responses

**`201` - Products updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/products/bulk-update/edit`

**Bulk Edit Products and Prices**

API to bulk edit products and their associated prices (max 30 entities)

**Operation ID:** `bulkEdit`

**Tags:** Products

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `products` | array of object | Yes | Array of products to update. Note: The total count includes all prices within each product. |

**`products` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Product ID |
| `name` | string | No | Product name |
| `description` | string | No | Product description |
| `image` | string | No | Product image |
| `availableInStore` | boolean | No | Product availability in store |
| `prices` | array of object | No | Array of price variants for the product |
| `collectionIds` | array of string | No | Collection IDs |
| `isLabelEnabled` | boolean | No | Enable product label |
| `isTaxesEnabled` | boolean | No | Enable taxes |
| `seo` | object | No |  |
| `slug` | string | No | Product URL slug |
| `automaticTaxCategoryId` | string | No | Automatic tax category ID |
| `taxInclusive` | boolean | No | Tax inclusive pricing |
| `taxes` | array of object | No | Product taxes |
| `medias` | array of object | No | Product media |
| `label` | object | No | Product label |

#### Responses

**`201` - Products and prices updated successfully**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Success message |
| `status` | boolean | Yes | Operation status |
| `updatedCount` | number | Yes | Number of products updated |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/products/{productId}`

**Get Product by ID**

The "Get Product by ID" API allows to retrieve information for a specific product using its unique identifier. Use this endpoint to fetch details for a single product based on the provided product ID.

**Operation ID:** `get-product-by-id`

**Tags:** Products

**Required Scopes:** `products.readonly`, `products.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID or the slug of the product that needs to be returned |
| `locationId` | query | string | Yes | location Id |
| `sendWishlistStatus` | query | boolean | No | Parameter which will decide whether to show the wishlisting status of products |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the product. |
| `description` | string | No | product description |
| `variants` | array of object | No | An array of variants for the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `name` | string | Yes | The name of the product. |
| `productType` | string | Yes | The type of the product (e.g., PHYSICAL). |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `createdAt` | string | Yes | The creation timestamp of the product. |
| `updatedAt` | string | Yes | The last update timestamp of the product. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `image` | string | No | The URL for the product image. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | The field indicates whether taxes are enabled for the product or not. Default: `False` |
| `taxes` | array of string | No | An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type `ProductTaxDto`. Please refer to the `ProductTaxDto` for additional details. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `label` | object | No |  |
| `slug` | string | No | The slug of the product by which the product will be navigated |

**`400` - Product not found**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/products/{productId}`

**Delete Product by ID**

The "Delete Product by ID" API allows deleting a specific product using its unique identifier. Use this endpoint to remove a product from the system.

**Operation ID:** `delete-product-by-id`

**Tags:** Products

**Required Scopes:** `products.write`, `products.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID or the slug of the product that needs to be returned |
| `locationId` | query | string | Yes | location Id |
| `sendWishlistStatus` | query | boolean | No | Parameter which will decide whether to show the wishlisting status of products |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | returns true if the product is successfully deleted |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/products/{productId}`

**Update Product by ID**

The "Update Product by ID" API allows modifying information for a specific product using its unique identifier. Use this endpoint to update details for a single product based on the provided product ID.

**Operation ID:** `update-product-by-id`

**Tags:** Products

**Required Scopes:** `products.write`, `products.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID or the slug of the product that needs to be returned |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `description` | string | No | A brief description of the product. |
| `productType` | string (enum: `DIGITAL`, `PHYSICAL`, `SERVICE`, `PHYSICAL/DIGITAL`) | Yes |  |
| `image` | string | No | The URL for the product image. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `medias` | array of object | No | An array of medias for the product. |
| `variants` | array of object | No | An array of variants for the product. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | Are there any taxes attached to the product. If this is true, taxes array cannot be empty. Default: `False` |
| `taxes` | array of string | No | List of ids of Taxes attached to the Product. If taxes are passed, isTaxesEnabled should be true. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `isLabelEnabled` | boolean | No | Is the product label enabled. If this is true, label object cannot be empty. Default: `False` |
| `label` | object | No |  |
| `slug` | string | No | The slug using which the product navigation will be handled |
| `seo` | object | No |  |
| `taxInclusive` | boolean | No | Whether the taxes should be included in the purchase price Default: `False` |
| `prices` | array of string | No | The prices of the product |

**`medias` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the media. |
| `title` | string | No | The title of the media file. |
| `url` | string | Yes | The URL where the media file is stored. |
| `type` | string (enum: `image`, `video`) | Yes | The type of the media file (e.g., image, video will be supporting soon). |
| `isFeatured` | boolean | No | Indicates whether the media is featured. |
| `priceIds` | array of array of any | No | Mongo ObjectIds of the prices for which the media is assigned |

**`variants` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | A unique identifier for the variant. |
| `name` | string | Yes | The name of the variant. |
| `options` | array of object | Yes | An array of options for the variant. |

**`label` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | The content for the product label. |
| `startDate` | string | No | Start date in YYYY-MM-DDTHH:mm:ssZ format |
| `endDate` | string | No | Start date in YYYY-MM-DDTHH:mm:ssZ format |

**`seo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | SEO title |
| `description` | string | No | SEO description |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the product. |
| `description` | string | No | product description |
| `variants` | array of object | No | An array of variants for the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `name` | string | Yes | The name of the product. |
| `productType` | string | Yes | The type of the product (e.g., PHYSICAL). |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `createdAt` | string | Yes | The creation timestamp of the product. |
| `updatedAt` | string | Yes | The last update timestamp of the product. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `image` | string | No | The URL for the product image. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | The field indicates whether taxes are enabled for the product or not. Default: `False` |
| `taxes` | array of string | No | An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type `ProductTaxDto`. Please refer to the `ProductTaxDto` for additional details. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `label` | object | No |  |
| `slug` | string | No | The slug of the product by which the product will be navigated |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/products/`

**Create Product**

The "Create Product" API allows adding a new product to the system. Use this endpoint to create a product with the specified details. Ensure that the required information is provided in the request payload.

**Operation ID:** `create-product`

**Tags:** Products

**Required Scopes:** `products.write`, `products.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `description` | string | No | A brief description of the product. |
| `productType` | string (enum: `DIGITAL`, `PHYSICAL`, `SERVICE`, `PHYSICAL/DIGITAL`) | Yes |  |
| `image` | string | No | The URL for the product image. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `medias` | array of object | No | An array of medias for the product. |
| `variants` | array of object | No | An array of variants for the product. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | Are there any taxes attached to the product. If this is true, taxes array cannot be empty. Default: `False` |
| `taxes` | array of string | No | List of ids of Taxes attached to the Product. If taxes are passed, isTaxesEnabled should be true. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `isLabelEnabled` | boolean | No | Is the product label enabled. If this is true, label object cannot be empty. Default: `False` |
| `label` | object | No |  |
| `slug` | string | No | The slug using which the product navigation will be handled |
| `seo` | object | No |  |
| `taxInclusive` | boolean | No | Whether the taxes should be included in the purchase price Default: `False` |

**`medias` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the media. |
| `title` | string | No | The title of the media file. |
| `url` | string | Yes | The URL where the media file is stored. |
| `type` | string (enum: `image`, `video`) | Yes | The type of the media file (e.g., image, video will be supporting soon). |
| `isFeatured` | boolean | No | Indicates whether the media is featured. |
| `priceIds` | array of array of any | No | Mongo ObjectIds of the prices for which the media is assigned |

**`variants` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | A unique identifier for the variant. |
| `name` | string | Yes | The name of the variant. |
| `options` | array of object | Yes | An array of options for the variant. |

**`label` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | The content for the product label. |
| `startDate` | string | No | Start date in YYYY-MM-DDTHH:mm:ssZ format |
| `endDate` | string | No | Start date in YYYY-MM-DDTHH:mm:ssZ format |

**`seo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | SEO title |
| `description` | string | No | SEO description |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the product. |
| `description` | string | No | product description |
| `variants` | array of object | No | An array of variants for the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `name` | string | Yes | The name of the product. |
| `productType` | string | Yes | The type of the product (e.g., PHYSICAL). |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `createdAt` | string | Yes | The creation timestamp of the product. |
| `updatedAt` | string | Yes | The last update timestamp of the product. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `image` | string | No | The URL for the product image. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | The field indicates whether taxes are enabled for the product or not. Default: `False` |
| `taxes` | array of string | No | An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type `ProductTaxDto`. Please refer to the `ProductTaxDto` for additional details. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `label` | object | No |  |
| `slug` | string | No | The slug of the product by which the product will be navigated |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/products/`

**List Products**

The "List Products" API allows to retrieve a paginated list of products. Customize your results by filtering products based on name or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve product information.

**Operation ID:** `list-invoices`

**Tags:** Products

**Required Scopes:** `products.readonly`, `products.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `limit` | query | number | No | The maximum number of items to be included in a single page of results |
| `offset` | query | number | No | The starting index of the page, indicating the position from which the results should be retrieved. |
| `locationId` | query | string | Yes | LocationId is the id of the sub-account |
| `search` | query | string | No | The name of the product for searching. |
| `collectionIds` | query | string | No | Filter by product category Ids. Supports comma separated values |
| `collectionSlug` | query | string | No | The slug value of the collection by which the collection would be searched |
| `expand` | query | array of string | No | Name of an entity whose data has to be fetched along with product. Possible entities are tax, stripe and paypal. If not mentioned, only ID will be returned in case of taxes |
| `productIds` | query | array of string | No | List of product ids to be fetched. |
| `storeId` | query | string | No | fetch and project products based on the storeId |
| `includedInStore` | query | boolean | No | Separate products by which are included in the store and which are not |
| `availableInStore` | query | boolean | No | If the product is included in the online store |
| `sortOrder` | query | string (enum: `asc`, `desc`) | No | The order of sort which should be applied for the date |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `products` | array of object | Yes | An array of products |
| `total` | array of object | Yes | list products status |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Prices

### POST `/products/{productId}/price`

**Create Price for a Product**

The "Create Price for a Product" API allows adding a new price associated with a specific product to the system. Use this endpoint to create a price with the specified details for a particular product. Ensure that the required information is provided in the request payload.

**Operation ID:** `create-price-for-product`

**Tags:** Prices

**Required Scopes:** `products/prices.write`, `products/prices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID of the product that needs to be used |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price. |
| `currency` | string | Yes | The currency of the price. |
| `amount` | number | Yes | The amount of the price. ( min: 0 ) |
| `recurring` | object | No |  |
| `description` | string | No | A brief description of the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `trialPeriod` | number | No | The trial period duration in days (if applicable). |
| `totalCycles` | number | No | The total number of billing cycles for the price. ( min: 1 ) |
| `setupFee` | number | No | The setup fee for the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `compareAtPrice` | number | No | The compare at price for the price. |
| `locationId` | string | Yes | The unique identifier of the location associated with the price. |
| `userId` | string | No | The unique identifier of the user who created the price. |
| `meta` | object | No |  |
| `trackInventory` | boolean | No | Need to track inventory stock quantity |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |
| `sku` | string | No | The unique identifier of the SKU associated with the price |
| `shippingOptions` | object | No |  |
| `isDigitalProduct` | boolean | No | Is the product a digital product |
| `digitalDelivery` | array of string | No | Digital delivery options |

**`recurring` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `interval` | string (enum: `day`, `month`, `week`, `year`) | Yes | The interval at which the recurring event occurs. |
| `intervalCount` | number | Yes | The number of intervals between each occurrence of the event. |

**`membershipOffers` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `label` | string | Yes | Membership offer label |
| `value` | string | Yes | Membership offer label |
| `_id` | string | Yes | The unique identifier for the membership offer. |

**`meta` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `source` | string (enum: `stripe`, `woocommerce`, `shopify`) | Yes | The source of the price. |
| `sourceId` | string | No | The id of the source of the price from where it is imported |
| `stripePriceId` | string | Yes | The Stripe price ID associated with the price. |
| `internalSource` | string (enum: `agency_plan`, `funnel`, `membership`, `communities`, `gokollab`, `calendar`) | Yes | The internal source of the price. |

**`shippingOptions` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `weight` | object | No |  |
| `dimensions` | object | No |  |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `locationId` | string | No | The unique identifier for the location. |
| `product` | string | No | The unique identifier for the associated product. |
| `userId` | string | No | The unique identifier for the user. |
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price (e.g., one_time). |
| `currency` | string | Yes | The currency code for the price. |
| `amount` | number | Yes | The amount of the price. |
| `recurring` | object | No |  |
| `createdAt` | string | No | The creation timestamp of the price. |
| `updatedAt` | string | No | The last update timestamp of the price. |
| `compareAtPrice` | number | No | The compare-at price for comparison purposes. |
| `trackInventory` | boolean | No | Indicates whether inventory tracking is enabled. |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/products/{productId}/price`

**List Prices for a Product**

The "List Prices for a Product" API allows retrieving a paginated list of prices associated with a specific product. Customize your results by filtering prices or paginate through the list using the provided query parameters.

**Operation ID:** `list-prices-for-product`

**Tags:** Prices

**Required Scopes:** `products/prices.readonly`, `products/prices.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID of the product that needs to be used |
| `limit` | query | number | No | The maximum number of items to be included in a single page of results |
| `offset` | query | number | No | The starting index of the page, indicating the position from which the results should be retrieved. |
| `locationId` | query | string | Yes | The unique identifier for the location. |
| `ids` | query | string | No | To filter the response only with the given price ids, Please provide with comma separated |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `prices` | array of object | Yes | An array of prices |
| `total` | number | Yes |  Default: `Total number of prices available` |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/products/inventory`

**List Inventory**

The "List Inventory API allows the user to retrieve a paginated list of inventory items. Use this endpoint to fetch details for multiple items in the inventory based on the provided query parameters.

**Operation ID:** `get-list-inventory`

**Tags:** Prices

**Required Scopes:** `products/prices.readonly`, `products/prices.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `limit` | query | number | No | The maximum number of items to be included in a single page of results |
| `offset` | query | number | No | The starting index of the page, indicating the position from which the results should be retrieved. |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `search` | query | string | No | Search string for Variant Search |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inventory` | array of object | Yes | List of inventory items |
| `total` | object | Yes | Total count of inventory items |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/products/inventory`

**Update Inventory**

The Update Inventory API allows the user to bulk update the inventory for multiple items. Use this endpoint to update the available quantity and out-of-stock purchase settings for multiple items in the inventory.

**Operation ID:** `update-inventory`

**Tags:** Prices

**Required Scopes:** `products/prices.write`, `products/prices.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `items` | array of object | Yes | Array of items to update in the inventory. |

**`items` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceId` | string | Yes | The unique identifier for the price, in MongoDB ID format. |
| `availableQuantity` | number | No | The available quantity of the item. |
| `allowOutOfStockPurchases` | boolean | No | Whether to continue selling the item when out of stock. |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/products/{productId}/price/{priceId}`

**Get Price by ID for a Product**

The "Get Price by ID for a Product" API allows retrieving information for a specific price associated with a particular product using its unique identifier. Use this endpoint to fetch details for a single price based on the provided price ID and product ID.

**Operation ID:** `get-price-by-id-for-product`

**Tags:** Prices

**Required Scopes:** `products/prices.readonly`, `products/prices.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID of the product that needs to be used |
| `priceId` | path | string | Yes | ID of the price that needs to be returned |
| `locationId` | query | string | Yes | location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `locationId` | string | No | The unique identifier for the location. |
| `product` | string | No | The unique identifier for the associated product. |
| `userId` | string | No | The unique identifier for the user. |
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price (e.g., one_time). |
| `currency` | string | Yes | The currency code for the price. |
| `amount` | number | Yes | The amount of the price. |
| `recurring` | object | No |  |
| `createdAt` | string | No | The creation timestamp of the price. |
| `updatedAt` | string | No | The last update timestamp of the price. |
| `compareAtPrice` | number | No | The compare-at price for comparison purposes. |
| `trackInventory` | boolean | No | Indicates whether inventory tracking is enabled. |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/products/{productId}/price/{priceId}`

**Update Price by ID for a Product**

The "Update Price by ID for a Product" API allows modifying information for a specific price associated with a particular product using its unique identifier. Use this endpoint to update details for a single price based on the provided price ID and product ID.

**Operation ID:** `update-price-by-id-for-product`

**Tags:** Prices

**Required Scopes:** `products/prices.write`, `products/prices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID of the product that needs to be used |
| `priceId` | path | string | Yes | ID of the price that needs to be returned |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price. |
| `currency` | string | Yes | The currency of the price. |
| `amount` | number | Yes | The amount of the price. ( min: 0 ) |
| `recurring` | object | No |  |
| `description` | string | No | A brief description of the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `trialPeriod` | number | No | The trial period duration in days (if applicable). |
| `totalCycles` | number | No | The total number of billing cycles for the price. ( min: 1 ) |
| `setupFee` | number | No | The setup fee for the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `compareAtPrice` | number | No | The compare at price for the price. |
| `locationId` | string | Yes | The unique identifier of the location associated with the price. |
| `userId` | string | No | The unique identifier of the user who created the price. |
| `meta` | object | No |  |
| `trackInventory` | boolean | No | Need to track inventory stock quantity |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |
| `sku` | string | No | The unique identifier of the SKU associated with the price |
| `shippingOptions` | object | No |  |
| `isDigitalProduct` | boolean | No | Is the product a digital product |
| `digitalDelivery` | array of string | No | Digital delivery options |

**`recurring` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `interval` | string (enum: `day`, `month`, `week`, `year`) | Yes | The interval at which the recurring event occurs. |
| `intervalCount` | number | Yes | The number of intervals between each occurrence of the event. |

**`membershipOffers` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `label` | string | Yes | Membership offer label |
| `value` | string | Yes | Membership offer label |
| `_id` | string | Yes | The unique identifier for the membership offer. |

**`meta` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `source` | string (enum: `stripe`, `woocommerce`, `shopify`) | Yes | The source of the price. |
| `sourceId` | string | No | The id of the source of the price from where it is imported |
| `stripePriceId` | string | Yes | The Stripe price ID associated with the price. |
| `internalSource` | string (enum: `agency_plan`, `funnel`, `membership`, `communities`, `gokollab`, `calendar`) | Yes | The internal source of the price. |

**`shippingOptions` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `weight` | object | No |  |
| `dimensions` | object | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `locationId` | string | No | The unique identifier for the location. |
| `product` | string | No | The unique identifier for the associated product. |
| `userId` | string | No | The unique identifier for the user. |
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price (e.g., one_time). |
| `currency` | string | Yes | The currency code for the price. |
| `amount` | number | Yes | The amount of the price. |
| `recurring` | object | No |  |
| `createdAt` | string | No | The creation timestamp of the price. |
| `updatedAt` | string | No | The last update timestamp of the price. |
| `compareAtPrice` | number | No | The compare-at price for comparison purposes. |
| `trackInventory` | boolean | No | Indicates whether inventory tracking is enabled. |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/products/{productId}/price/{priceId}`

**Delete Price by ID for a Product**

The "Delete Price by ID for a Product" API allows deleting a specific price associated with a particular product using its unique identifier. Use this endpoint to remove a price from the system.

**Operation ID:** `delete-price-by-id-for-product`

**Tags:** Prices

**Required Scopes:** `products/prices.write`, `products/prices.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `productId` | path | string | Yes | ID of the product that needs to be used |
| `priceId` | path | string | Yes | ID of the price that needs to be returned |
| `locationId` | query | string | Yes | location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | returns true if the price is successfully deleted |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Store

### GET `/products/store/{storeId}/stats`

**Fetch Product Store Stats**

API to fetch the total number of products, included in the store, and excluded from the store and other stats

**Operation ID:** `get-product-store-stats`

**Tags:** Store

**Required Scopes:** `products.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `storeId` | path | string | Yes | Products related to the store |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `search` | query | string | No | The name of the product for searching. |
| `collectionIds` | query | string | No | Filter by product collection Ids. Supports comma separated values |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `totalProducts` | number | Yes | Total number of products |
| `includedInStore` | number | Yes | Number of products included in the store |
| `excludedFromStore` | number | Yes | Number of products excluded from the store |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/products/store/{storeId}`

**Action to include/exclude the product in store**

API to update the status of products in a particular store

**Operation ID:** `update-store-status`

**Tags:** Store

**Required Scopes:** `products.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `storeId` | path | string | Yes | Products related to the store |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `include`, `exclude`) | Yes | Action to include or exclude the product from the store |
| `productIds` | array of string | Yes | Array of product IDs |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/products/store/{storeId}/priority`

**Update product display priorities in store**

API to set the display priority of products in a store

**Operation ID:** `update-display-priority`

**Tags:** Store

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `storeId` | path | string | Yes | Products related to the store |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `products` | array of array of any | Yes | Array of products with their display priorities |

#### Responses

**`200` - Successfully updated display priorities**

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Collections

### GET `/products/collections`

**Fetch Product Collections**

Internal API to fetch the Product Collections

**Operation ID:** `get-product-collection`

**Tags:** Collections

**Required Scopes:** `products/collection.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `limit` | query | number | No | The maximum number of items to be included in a single page of results |
| `offset` | query | number | No | The starting index of the page, indicating the position from which the results should be retrieved. |
| `altId` | query | string | Yes | Location Id |
| `altType` | query | string (enum: `location`) | Yes | The type of alt. For now it is only LOCATION |
| `collectionIds` | query | string | No | Ids of the collections separated by comma(,) for search purposes |
| `name` | query | string | No | Query to search collection based on names |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of array of any | Yes | Array of Collections |
| `total` | number | Yes | The total count of the collections present, which is useful to calculate the pagination |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/products/collections`

**Create Product Collection**

Create a new Product Collection for a specific location

**Operation ID:** `create-product-collection`

**Tags:** Collections

**Required Scopes:** `products/collection.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id |
| `altType` | string (enum: `location`) | Yes | The type of alt. For now it is only LOCATION |
| `collectionId` | string | No | Unique Identifier of the Product Collection, Mongo Id |
| `name` | string | Yes | Name of the Product Collection |
| `slug` | string | Yes | Slug of the Product Collection which helps in navigation |
| `image` | string | No | The URL of the image that is going to be displayed as the collection Thumbnail |
| `seo` | object | No |  |

**`seo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | The title which will be displayed as an SEO format |
| `description` | string | No | The description which would be displayed in preview purposes |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/products/collections/{collectionId}`

**Get Details about individual product collection**

Get Details about individual product collection

**Operation ID:** `get-product-collection-id`

**Tags:** Collections

**Required Scopes:** `products/collection.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `collectionId` | path | string | Yes | Collection Id |
| `altId` | query | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `status` | boolean | Yes | Status of the operation |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/products/collections/{collectionId}`

**Update Product Collection**

Update a specific product collection with Id :collectionId

**Operation ID:** `update-product-collection`

**Tags:** Collections

**Required Scopes:** `products/collection.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `collectionId` | path | string | Yes | MongoId of the collection |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id |
| `altType` | string (enum: `location`) | Yes | The type of alt. For now it is only LOCATION |
| `name` | string | No | Name of the Product Collection |
| `slug` | string | No | Slug of the Product Collection which helps in navigation |
| `image` | string | No | The URL of the image that is going to be displayed as the collection Thumbnail |
| `seo` | object | No |  |

**`seo` object properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | The title which will be displayed as an SEO format |
| `description` | string | No | The description which would be displayed in preview purposes |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/products/collections/{collectionId}`

**Delete Product Collection**

Delete specific product collection with Id :collectionId

**Operation ID:** `delete-product-collection`

**Tags:** Collections

**Required Scopes:** `products/collection.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `collectionId` | path | string | Yes | MongoId of the collection |
| `altId` | query | string | Yes | Location Id |
| `altType` | query | string (enum: `location`) | Yes | The type of alt. For now it is only LOCATION |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Reviews

### GET `/products/reviews`

**Fetch Product Reviews**

API to fetch the Product Reviews

**Operation ID:** `get-product-reviews`

**Tags:** Reviews

**Required Scopes:** `products.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `limit` | query | number | No | The maximum number of items to be included in a single page of results |
| `offset` | query | number | No | The starting index of the page, indicating the position from which the results should be retrieved. |
| `sortField` | query | string (enum: `createdAt`, `rating`) | No | The field upon which the sort should be applied |
| `sortOrder` | query | string (enum: `asc`, `desc`) | No | The order of sort which should be applied for the sortField |
| `rating` | query | number | No | Key to filter the ratings  |
| `startDate` | query | string | No | The start date for filtering reviews |
| `endDate` | query | string | No | The end date for filtering reviews |
| `productId` | query | string | No | Comma-separated list of product IDs |
| `storeId` | query | string | No | Comma-separated list of store IDs |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of array of any | Yes | Array of Collections |
| `total` | number | Yes | The total count of the collections present, which is useful to calculate the pagination |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/products/reviews/count`

**Fetch Review Count as per status**

API to fetch the Review Count as per status

**Operation ID:** `get-reviews-count`

**Tags:** Reviews

**Required Scopes:** `products.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `rating` | query | number | No | Key to filter the ratings  |
| `startDate` | query | string | No | The start date for filtering reviews |
| `endDate` | query | string | No | The end date for filtering reviews |
| `productId` | query | string | No | Comma-separated list of product IDs |
| `storeId` | query | string | No | Comma-separated list of store IDs |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of array of any | Yes | Array of review status counts |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/products/reviews/{reviewId}`

**Update Product Reviews**

Update status, reply, etc of a particular review

**Operation ID:** `update-product-review`

**Tags:** Reviews

**Required Scopes:** `products.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `reviewId` | path | string | Yes | Review Id |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `productId` | string | Yes | Product Id |
| `status` | string | Yes | Status of the review |
| `reply` | array of object | No | Reply of the review |
| `rating` | number | No | Rating of the product |
| `headline` | string | No | Headline of the Review |
| `detail` | string | No | Detailed Review of the product |

**`reply` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headline` | string | Yes | Headline of the Review |
| `comment` | string | Yes | Detailed Review of the product |
| `user` | object | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### DELETE `/products/reviews/{reviewId}`

**Delete Product Review**

Delete specific product review

**Operation ID:** `delete-product-review`

**Tags:** Reviews

**Required Scopes:** `products.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `reviewId` | path | string | Yes | Review Id |
| `altId` | query | string | Yes | Location Id or Agency Id |
| `altType` | query | string (enum: `location`) | Yes |  |
| `productId` | query | string | Yes | Product Id of the product |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/products/reviews/bulk-update`

**Update Product Reviews**

Update one or multiple product reviews: status, reply, etc.

**Operation ID:** `bulk-update-product-review`

**Tags:** Reviews

**Required Scopes:** `products.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `reviews` | array of object | Yes | Array of Product Reviews |
| `status` | object | Yes | Status of the review |

**`reviews` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `reviewId` | string | Yes | Review Id |
| `productId` | string | Yes | Product Id |
| `storeId` | string | Yes | Store Id |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### BulkEditPriceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Price ID |
| `name` | string | No | Price name |
| `amount` | number | No | Price amount |
| `currency` | string | No | Price currency |
| `compareAtPrice` | number | No | Compare at price |
| `availableQuantity` | number | No | Available quantity |
| `trackInventory` | boolean | No | Track inventory |
| `allowOutOfStockPurchases` | boolean | No | Allow out of stock purchases |
| `sku` | string | No | SKU |
| `trialPeriod` | number | No | Trial period in days |
| `totalCycles` | number | No | Total billing cycles |
| `setupFee` | number | No | Setup fee |
| `shippingOptions` | object | No |  |
| `recurring` | object | No |  |

### BulkEditProductDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Product ID |
| `name` | string | No | Product name |
| `description` | string | No | Product description |
| `image` | string | No | Product image |
| `availableInStore` | boolean | No | Product availability in store |
| `prices` | array of object | No | Array of price variants for the product |
| `collectionIds` | array of string | No | Collection IDs |
| `isLabelEnabled` | boolean | No | Enable product label |
| `isTaxesEnabled` | boolean | No | Enable taxes |
| `seo` | object | No |  |
| `slug` | string | No | Product URL slug |
| `automaticTaxCategoryId` | string | No | Automatic tax category ID |
| `taxInclusive` | boolean | No | Tax inclusive pricing |
| `taxes` | array of object | No | Product taxes |
| `medias` | array of object | No | Product media |
| `label` | object | No | Product label |

### BulkEditRequestDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `products` | array of object | Yes | Array of products to update. Note: The total count includes all prices within each product. |

### BulkEditResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | string | Yes | Success message |
| `status` | boolean | Yes | Operation status |
| `updatedCount` | number | Yes | Number of products updated |

### BulkUpdateDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `type` | string (enum: `bulk-update-price`, `bulk-update-availability`, `bulk-update-product-collection`, `bulk-delete-products`, `bulk-update-currency`) | Yes | Type of bulk update operation |
| `productIds` | array of string | Yes | Array of product IDs |
| `filters` | object | No |  |
| `price` | object | No |  |
| `compareAtPrice` | object | No |  |
| `availability` | boolean | No | New availability status |
| `collectionIds` | array of string | No | Array of collection IDs |
| `currency` | string | No | Currency code |

### BulkUpdateFilters

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `collectionIds` | array of string | No | Filter by collection IDs |
| `productType` | string | No | Filter by product type |
| `availableInStore` | boolean | No | Filter by availability status |
| `search` | string | No | Filter by search term |

### BulkUpdateResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### CollectionSEODto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | The title which will be displayed as an SEO format |
| `description` | string | No | The description which would be displayed in preview purposes |

### CollectionSchema

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the collection |
| `altId` | string | Yes | Location Id to which the collection is associated |
| `name` | string | Yes | Name of the collection |
| `slug` | string | Yes | Slug of the collection with which navigation is established. Special Characters and spacing is not allowed and should be unique |
| `image` | string | Yes | The URL of the image that is going to be displayed as the collection Thumbnail |
| `seo` | object | Yes |  |
| `createdAt` | string | Yes | Date at which the collection was created |

### CountReviewsByStatusResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of array of any | Yes | Array of review status counts |

### CreateCollectionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |

### CreatePriceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price. |
| `currency` | string | Yes | The currency of the price. |
| `amount` | number | Yes | The amount of the price. ( min: 0 ) |
| `recurring` | object | No |  |
| `description` | string | No | A brief description of the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `trialPeriod` | number | No | The trial period duration in days (if applicable). |
| `totalCycles` | number | No | The total number of billing cycles for the price. ( min: 1 ) |
| `setupFee` | number | No | The setup fee for the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `compareAtPrice` | number | No | The compare at price for the price. |
| `locationId` | string | Yes | The unique identifier of the location associated with the price. |
| `userId` | string | No | The unique identifier of the user who created the price. |
| `meta` | object | No |  |
| `trackInventory` | boolean | No | Need to track inventory stock quantity |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |
| `sku` | string | No | The unique identifier of the SKU associated with the price |
| `shippingOptions` | object | No |  |
| `isDigitalProduct` | boolean | No | Is the product a digital product |
| `digitalDelivery` | array of string | No | Digital delivery options |

### CreatePriceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `locationId` | string | No | The unique identifier for the location. |
| `product` | string | No | The unique identifier for the associated product. |
| `userId` | string | No | The unique identifier for the user. |
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price (e.g., one_time). |
| `currency` | string | Yes | The currency code for the price. |
| `amount` | number | Yes | The amount of the price. |
| `recurring` | object | No |  |
| `createdAt` | string | No | The creation timestamp of the price. |
| `updatedAt` | string | No | The last update timestamp of the price. |
| `compareAtPrice` | number | No | The compare-at price for comparison purposes. |
| `trackInventory` | boolean | No | Indicates whether inventory tracking is enabled. |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |

### CreateProductCollectionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id |
| `altType` | string (enum: `location`) | Yes | The type of alt. For now it is only LOCATION |
| `collectionId` | string | No | Unique Identifier of the Product Collection, Mongo Id |
| `name` | string | Yes | Name of the Product Collection |
| `slug` | string | Yes | Slug of the Product Collection which helps in navigation |
| `image` | string | No | The URL of the image that is going to be displayed as the collection Thumbnail |
| `seo` | object | No |  |

### CreateProductDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `description` | string | No | A brief description of the product. |
| `productType` | string (enum: `DIGITAL`, `PHYSICAL`, `SERVICE`, `PHYSICAL/DIGITAL`) | Yes |  |
| `image` | string | No | The URL for the product image. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `medias` | array of object | No | An array of medias for the product. |
| `variants` | array of object | No | An array of variants for the product. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | Are there any taxes attached to the product. If this is true, taxes array cannot be empty. Default: `False` |
| `taxes` | array of string | No | List of ids of Taxes attached to the Product. If taxes are passed, isTaxesEnabled should be true. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `isLabelEnabled` | boolean | No | Is the product label enabled. If this is true, label object cannot be empty. Default: `False` |
| `label` | object | No |  |
| `slug` | string | No | The slug using which the product navigation will be handled |
| `seo` | object | No |  |
| `taxInclusive` | boolean | No | Whether the taxes should be included in the purchase price Default: `False` |

### CreateProductResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the product. |
| `description` | string | No | product description |
| `variants` | array of object | No | An array of variants for the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `name` | string | Yes | The name of the product. |
| `productType` | string | Yes | The type of the product (e.g., PHYSICAL). |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `createdAt` | string | Yes | The creation timestamp of the product. |
| `updatedAt` | string | Yes | The last update timestamp of the product. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `image` | string | No | The URL for the product image. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | The field indicates whether taxes are enabled for the product or not. Default: `False` |
| `taxes` | array of string | No | An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type `ProductTaxDto`. Please refer to the `ProductTaxDto` for additional details. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `label` | object | No |  |
| `slug` | string | No | The slug of the product by which the product will be navigated |

### DefaultCollectionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |
| `status` | boolean | Yes | Status of the operation |

### DefaultPriceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `locationId` | string | No | The unique identifier for the location. |
| `product` | string | No | The unique identifier for the associated product. |
| `userId` | string | No | The unique identifier for the user. |
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price (e.g., one_time). |
| `currency` | string | Yes | The currency code for the price. |
| `amount` | number | Yes | The amount of the price. |
| `recurring` | object | No |  |
| `createdAt` | string | No | The creation timestamp of the price. |
| `updatedAt` | string | No | The last update timestamp of the price. |
| `compareAtPrice` | number | No | The compare-at price for comparison purposes. |
| `trackInventory` | boolean | No | Indicates whether inventory tracking is enabled. |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |

### DefaultProductResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the product. |
| `description` | string | No | product description |
| `variants` | array of object | No | An array of variants for the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `name` | string | Yes | The name of the product. |
| `productType` | string | Yes | The type of the product (e.g., PHYSICAL). |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `createdAt` | string | Yes | The creation timestamp of the product. |
| `updatedAt` | string | Yes | The last update timestamp of the product. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `image` | string | No | The URL for the product image. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | The field indicates whether taxes are enabled for the product or not. Default: `False` |
| `taxes` | array of string | No | An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type `ProductTaxDto`. Please refer to the `ProductTaxDto` for additional details. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `label` | object | No |  |
| `slug` | string | No | The slug of the product by which the product will be navigated |

### DeletePriceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | returns true if the price is successfully deleted |

### DeleteProductCollectionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### DeleteProductResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | returns true if the product is successfully deleted |

### DeleteProductReviewResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### GetInventoryResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inventory` | array of object | Yes | List of inventory items |
| `total` | object | Yes | Total count of inventory items |

### GetPriceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `locationId` | string | No | The unique identifier for the location. |
| `product` | string | No | The unique identifier for the associated product. |
| `userId` | string | No | The unique identifier for the user. |
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price (e.g., one_time). |
| `currency` | string | Yes | The currency code for the price. |
| `amount` | number | Yes | The amount of the price. |
| `recurring` | object | No |  |
| `createdAt` | string | No | The creation timestamp of the price. |
| `updatedAt` | string | No | The last update timestamp of the price. |
| `compareAtPrice` | number | No | The compare-at price for comparison purposes. |
| `trackInventory` | boolean | No | Indicates whether inventory tracking is enabled. |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |

### GetProductResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the product. |
| `description` | string | No | product description |
| `variants` | array of object | No | An array of variants for the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `name` | string | Yes | The name of the product. |
| `productType` | string | Yes | The type of the product (e.g., PHYSICAL). |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `createdAt` | string | Yes | The creation timestamp of the product. |
| `updatedAt` | string | Yes | The last update timestamp of the product. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `image` | string | No | The URL for the product image. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | The field indicates whether taxes are enabled for the product or not. Default: `False` |
| `taxes` | array of string | No | An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type `ProductTaxDto`. Please refer to the `ProductTaxDto` for additional details. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `label` | object | No |  |
| `slug` | string | No | The slug of the product by which the product will be navigated |

### GetProductStatsResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `totalProducts` | number | Yes | Total number of products |
| `includedInStore` | number | Yes | Number of products included in the store |
| `excludedFromStore` | number | Yes | Number of products excluded from the store |

### InventoryItemDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price |
| `name` | string | Yes | Name of the price/variant |
| `availableQuantity` | number | Yes | Available quantity in inventory |
| `sku` | string | Yes | SKU for the product variant |
| `allowOutOfStockPurchases` | boolean | Yes | Whether out of stock purchases are allowed |
| `product` | string | Yes | Product ID this price belongs to |
| `updatedAt` | string | Yes | Last update timestamp |
| `image` | string | No | Product image URL |
| `productName` | string | No | Product name |

### ListCollectionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of array of any | Yes | Array of Collections |
| `total` | number | Yes | The total count of the collections present, which is useful to calculate the pagination |

### ListPricesResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `prices` | array of object | Yes | An array of prices |
| `total` | number | Yes |  Default: `Total number of prices available` |

### ListProductReviewsResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of array of any | Yes | Array of Collections |
| `total` | number | Yes | The total count of the collections present, which is useful to calculate the pagination |

### ListProductsResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `products` | array of object | Yes | An array of products |
| `total` | array of object | Yes | list products status |

### ListProductsStats

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total` | number | Yes | Total number of products |

### MembershipOfferDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `label` | string | Yes | Membership offer label |
| `value` | string | Yes | Membership offer label |
| `_id` | string | Yes | The unique identifier for the membership offer. |

### PriceDimensionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `height` | number | Yes | Height of the price |
| `width` | number | Yes | Width of the price |
| `length` | number | Yes | Length of the price |
| `unit` | string (enum: `cm`, `in`, `m`) | Yes | Unit of the price dimensions |

### PriceMetaDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `source` | string (enum: `stripe`, `woocommerce`, `shopify`) | Yes | The source of the price. |
| `sourceId` | string | No | The id of the source of the price from where it is imported |
| `stripePriceId` | string | Yes | The Stripe price ID associated with the price. |
| `internalSource` | string (enum: `agency_plan`, `funnel`, `membership`, `communities`, `gokollab`, `calendar`) | Yes | The internal source of the price. |

### PriceUpdateField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string (enum: `INCREASE_BY_AMOUNT`, `REDUCE_BY_AMOUNT`, `SET_NEW_PRICE`, `INCREASE_BY_PERCENTAGE`, `REDUCE_BY_PERCENTAGE`) | Yes | Type of price update |
| `value` | number | Yes | Value to update (amount or percentage based on type) |
| `roundToWhole` | boolean | No | Round to nearest whole number |

### ProductCategories

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### ProductLabelDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes | The content for the product label. |
| `startDate` | string | No | Start date in YYYY-MM-DDTHH:mm:ssZ format |
| `endDate` | string | No | Start date in YYYY-MM-DDTHH:mm:ssZ format |

### ProductMediaDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the media. |
| `title` | string | No | The title of the media file. |
| `url` | string | Yes | The URL where the media file is stored. |
| `type` | string (enum: `image`, `video`) | Yes | The type of the media file (e.g., image, video will be supporting soon). |
| `isFeatured` | boolean | No | Indicates whether the media is featured. |
| `priceIds` | array of array of any | No | Mongo ObjectIds of the prices for which the media is assigned |

### ProductReviewDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headline` | string | Yes | Headline of the Review |
| `comment` | string | Yes | Detailed Review of the product |
| `user` | object | Yes |  |

### ProductSEODto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | No | SEO title |
| `description` | string | No | SEO description |

### ProductVariantDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | A unique identifier for the variant. |
| `name` | string | Yes | The name of the variant. |
| `options` | array of object | Yes | An array of options for the variant. |

### ProductVariantOptionDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the option. |
| `name` | string | Yes | The name of the option. |

### RecurringDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `interval` | string (enum: `day`, `month`, `week`, `year`) | Yes | The interval at which the recurring event occurs. |
| `intervalCount` | number | Yes | The number of intervals between each occurrence of the event. |

### ShippingOptionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `weight` | object | No |  |
| `dimensions` | object | No |  |

### UpdateDisplayPriorityBodyDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `products` | array of array of any | Yes | Array of products with their display priorities |

### UpdateInventoryDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `items` | array of object | Yes | Array of items to update in the inventory. |

### UpdateInventoryItemDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceId` | string | Yes | The unique identifier for the price, in MongoDB ID format. |
| `availableQuantity` | number | No | The available quantity of the item. |
| `allowOutOfStockPurchases` | boolean | No | Whether to continue selling the item when out of stock. |

### UpdateInventoryResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### UpdatePriceDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price. |
| `currency` | string | Yes | The currency of the price. |
| `amount` | number | Yes | The amount of the price. ( min: 0 ) |
| `recurring` | object | No |  |
| `description` | string | No | A brief description of the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `trialPeriod` | number | No | The trial period duration in days (if applicable). |
| `totalCycles` | number | No | The total number of billing cycles for the price. ( min: 1 ) |
| `setupFee` | number | No | The setup fee for the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `compareAtPrice` | number | No | The compare at price for the price. |
| `locationId` | string | Yes | The unique identifier of the location associated with the price. |
| `userId` | string | No | The unique identifier of the user who created the price. |
| `meta` | object | No |  |
| `trackInventory` | boolean | No | Need to track inventory stock quantity |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |
| `sku` | string | No | The unique identifier of the SKU associated with the price |
| `shippingOptions` | object | No |  |
| `isDigitalProduct` | boolean | No | Is the product a digital product |
| `digitalDelivery` | array of string | No | Digital delivery options |

### UpdatePriceResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the price. |
| `membershipOffers` | array of object | No | An array of membership offers associated with the price. |
| `variantOptionIds` | array of string | No | An array of variant option IDs associated with the price. |
| `locationId` | string | No | The unique identifier for the location. |
| `product` | string | No | The unique identifier for the associated product. |
| `userId` | string | No | The unique identifier for the user. |
| `name` | string | Yes | The name of the price. |
| `type` | string (enum: `one_time`, `recurring`) | Yes | The type of the price (e.g., one_time). |
| `currency` | string | Yes | The currency code for the price. |
| `amount` | number | Yes | The amount of the price. |
| `recurring` | object | No |  |
| `createdAt` | string | No | The creation timestamp of the price. |
| `updatedAt` | string | No | The last update timestamp of the price. |
| `compareAtPrice` | number | No | The compare-at price for comparison purposes. |
| `trackInventory` | boolean | No | Indicates whether inventory tracking is enabled. |
| `availableQuantity` | number | No | Available inventory stock quantity |
| `allowOutOfStockPurchases` | boolean | No | Continue selling when out of stock |

### UpdateProductCollectionResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### UpdateProductCollectionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id |
| `altType` | string (enum: `location`) | Yes | The type of alt. For now it is only LOCATION |
| `name` | string | No | Name of the Product Collection |
| `slug` | string | No | Slug of the Product Collection which helps in navigation |
| `image` | string | No | The URL of the image that is going to be displayed as the collection Thumbnail |
| `seo` | object | No |  |

### UpdateProductDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | The name of the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `description` | string | No | A brief description of the product. |
| `productType` | string (enum: `DIGITAL`, `PHYSICAL`, `SERVICE`, `PHYSICAL/DIGITAL`) | Yes |  |
| `image` | string | No | The URL for the product image. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `medias` | array of object | No | An array of medias for the product. |
| `variants` | array of object | No | An array of variants for the product. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | Are there any taxes attached to the product. If this is true, taxes array cannot be empty. Default: `False` |
| `taxes` | array of string | No | List of ids of Taxes attached to the Product. If taxes are passed, isTaxesEnabled should be true. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `isLabelEnabled` | boolean | No | Is the product label enabled. If this is true, label object cannot be empty. Default: `False` |
| `label` | object | No |  |
| `slug` | string | No | The slug using which the product navigation will be handled |
| `seo` | object | No |  |
| `taxInclusive` | boolean | No | Whether the taxes should be included in the purchase price Default: `False` |
| `prices` | array of string | No | The prices of the product |

### UpdateProductResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | The unique identifier for the product. |
| `description` | string | No | product description |
| `variants` | array of object | No | An array of variants for the product. |
| `locationId` | string | Yes | The unique identifier for the location. |
| `name` | string | Yes | The name of the product. |
| `productType` | string | Yes | The type of the product (e.g., PHYSICAL). |
| `availableInStore` | boolean | No | Indicates whether the product is available in-store. |
| `createdAt` | string | Yes | The creation timestamp of the product. |
| `updatedAt` | string | Yes | The last update timestamp of the product. |
| `statementDescriptor` | string | No | The statement descriptor for the product. |
| `image` | string | No | The URL for the product image. |
| `collectionIds` | array of string | No | An array of category Ids for the product |
| `isTaxesEnabled` | boolean | No | The field indicates whether taxes are enabled for the product or not. Default: `False` |
| `taxes` | array of string | No | An array of ids of Taxes attached to the Product. If the expand query includes tax, the taxes will be of type `ProductTaxDto`. Please refer to the `ProductTaxDto` for additional details. |
| `automaticTaxCategoryId` | string | No | Tax category ID for Automatic taxes calculation. |
| `label` | object | No |  |
| `slug` | string | No | The slug of the product by which the product will be navigated |

### UpdateProductReviewDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `productId` | string | Yes | Product Id |
| `status` | string | Yes | Status of the review |
| `reply` | array of object | No | Reply of the review |
| `rating` | number | No | Rating of the product |
| `headline` | string | No | Headline of the Review |
| `detail` | string | No | Detailed Review of the product |

### UpdateProductReviewObjectDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `reviewId` | string | Yes | Review Id |
| `productId` | string | Yes | Product Id |
| `storeId` | string | Yes | Store Id |

### UpdateProductReviewsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `reviews` | array of object | Yes | Array of Product Reviews |
| `status` | object | Yes | Status of the review |

### UpdateProductReviewsResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### UpdateProductStoreDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `altId` | string | Yes | Location Id or Agency Id |
| `altType` | string (enum: `location`) | Yes |  |
| `action` | string (enum: `include`, `exclude`) | Yes | Action to include or exclude the product from the store |
| `productIds` | array of string | Yes | Array of product IDs |

### UpdateProductStoreResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | boolean | Yes | Status of api action |
| `message` | string | No | Success message |

### UserDetailsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Name of the customer |
| `email` | string | Yes | Email of the customer |
| `phone` | string | No | Phone no of the customer |
| `isCustomer` | boolean | No | Is the person an admin or customer |

### WeightOptionsDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | number | Yes | Actual weight of the product |
| `unit` | string (enum: `kg`, `lb`, `g`, `oz`) | Yes | Weight unit of the product |
