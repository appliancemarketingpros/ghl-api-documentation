# Blogs API

Documentation for Blog public API

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Blogs](#blogs)

## Blogs

### GET `/blogs/posts/url-slug-exists`

**Check url slug**

The "Check url slug" API allows check the blog slug validation which is needed before publishing any blog post. Please use blogs/check-slug.readonly. you can find the POST ID from the post edit url.

**Operation ID:** `check-url-slug-exists`

**Tags:** Blogs

**Required Scopes:** `blogs/check-slug.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `urlSlug` | query | string | Yes |  |
| `locationId` | query | string | Yes |  |
| `postId` | query | string | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `exists` | boolean | Yes | Indicates whether the url slug exists or not |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### PUT `/blogs/posts/{postId}`

**Update Blog Post**

The "Update Blog Post" API allows you update blog post for any given blog site. Please use blogs/post-update.write

**Operation ID:** `update-blog-post`

**Tags:** Blogs

**Required Scopes:** `blogs/post-update.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `locationId` | string | Yes |  |
| `blogId` | string | Yes | You can find the blog id from blog site dashboard link |
| `imageUrl` | string | Yes |  |
| `description` | string | Yes |  |
| `rawHTML` | string | Yes |  |
| `status` | string (enum: `DRAFT`, `PUBLISHED`, `SCHEDULED`, `ARCHIVED`) | Yes |  |
| `imageAltText` | string | Yes |  |
| `categories` | array of string | Yes | This needs to be array of category ids, which you can get from the category get api call. |
| `tags` | array of string | No |  |
| `author` | string | Yes | This needs to be author id, which you can get from the author get api call. |
| `urlSlug` | string | Yes |  |
| `canonicalLink` | string | No |  |
| `publishedAt` | string | Yes | Provide ISO timestamp |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updatedBlogPost` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### POST `/blogs/posts`

**Create Blog Post**

The "Create Blog Post" API allows you create blog post for any given blog site. Please use blogs/post.write

**Operation ID:** `create-blog-post`

**Tags:** Blogs

**Required Scopes:** `blogs/post.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `locationId` | string | Yes |  |
| `blogId` | string | Yes | You can find the blog id from blog site dashboard link |
| `imageUrl` | string | Yes |  |
| `description` | string | Yes |  |
| `rawHTML` | string | Yes |  |
| `status` | string (enum: `DRAFT`, `PUBLISHED`, `SCHEDULED`, `ARCHIVED`) | Yes |  |
| `imageAltText` | string | Yes |  |
| `categories` | array of string | Yes | This needs to be array of category ids, which you can get from the category get api call. |
| `tags` | array of string | No |  |
| `author` | string | Yes | This needs to be author id, which you can get from the author get api call. |
| `urlSlug` | string | Yes |  |
| `canonicalLink` | string | No |  |
| `publishedAt` | string | Yes | Provide ISO timestamp |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/blogs/authors`

**Get all authors**

The "Get all authors" Api return the blog authors for a given location ID. Please use "blogs/author.readonly" 

**Operation ID:** `get-all-blog-authors-by-location`

**Tags:** Blogs

**Required Scopes:** `blogs/author.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes | Location Id |
| `limit` | query | number | Yes | Number of authors to show in the listing |
| `offset` | query | number | Yes | Number of authors to skip in listing |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authors` | array of object | Yes | Array of authors |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/blogs/categories`

**Get all categories**

The "Get all categories" Api return the blog categoies for a given location ID. Please use "blogs/category.readonly" 

**Operation ID:** `get-all-categories-by-location`

**Tags:** Blogs

**Required Scopes:** `blogs/category.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `limit` | query | number | Yes | Number of categories to show in the listing |
| `offset` | query | number | Yes | Number of categories to skip in listing |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `categories` | array of object | Yes | Array of categories |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/blogs/posts/all`

**Get Blog posts by Blog ID**

The "Get Blog posts by Blog ID" API allows you get blog posts for any given blog site using blog ID.Please use blogs/posts.readonly

**Operation ID:** `get-blog-post`

**Tags:** Blogs

**Required Scopes:** `blogs/posts.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `blogId` | query | string | Yes |  |
| `limit` | query | number | Yes |  |
| `offset` | query | number | Yes |  |
| `searchTerm` | query | string | No | search for any post by name |
| `status` | query | string (enum: `PUBLISHED`, `SCHEDULED`, `ARCHIVED`, `DRAFT`) | No |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `blogs` | array of object | Yes | Object containing response data of blog posts |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

### GET `/blogs/site/all`

**Get Blogs by Location ID**

The "Get Blogs by Location ID" API allows you get blogs using Location ID.Please use blogs/list.readonly

**Operation ID:** `get-blogs`

**Tags:** Blogs

**Required Scopes:** `blogs/list.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `locationId` | query | string | Yes |  |
| `skip` | query | number | Yes |  |
| `limit` | query | number | Yes |  |
| `searchTerm` | query | string | No | search for any post by name |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes | Object containing response data of blog |

**`400` - Bad Request**

**`401` - Unauthorized**

**`422` - Unprocessable Entity**

---

## Schemas

### AuthorResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes |  |
| `name` | string | Yes |  |
| `locationId` | string | Yes |  |
| `updatedAt` | string | Yes |  |
| `canonicalLink` | string | Yes |  |

### AuthorsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authors` | array of object | Yes | Array of authors |

### BlogGetResponseWrapperDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | array of object | Yes | Object containing response data of blog |

### BlogPostCreateResponseWrapperDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | object | Yes |  |

### BlogPostGetResponseWrapperDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `blogs` | array of object | Yes | Object containing response data of blog posts |

### BlogPostResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `categories` | array of string | Yes | Array of category IDs associated with the blog post |
| `tags` | array of string | No | Array of tags associated with the blog post |
| `archived` | boolean | Yes | Indicates whether the blog post is archived |
| `_id` | string | Yes | Unique identifier of the blog post |
| `title` | string | Yes | Title of the blog post |
| `description` | string | Yes | Description of the blog post |
| `imageUrl` | string | Yes | URL of the image associated with the blog post |
| `status` | string | Yes | Publication status of the blog post |
| `imageAltText` | string | Yes | Alternative text for the blog post image |
| `urlSlug` | string | Yes | URL slug for the blog post |
| `canonicalLink` | string | No | Canonical link of the blog post |
| `author` | string | No | Identifier of the author of the blog post |
| `publishedAt` | string | Yes | Timestamp when the blog post was published |
| `updatedAt` | string | Yes | Timestamp when the blog post was last updated |

### BlogPostUpdateResponseWrapperDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updatedBlogPost` | object | Yes |  |

### BlogResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes | Unique identifier of the blog |
| `name` | string | Yes | Name of the blog |

### CategoriesResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `categories` | array of object | Yes | Array of categories |

### CategoryResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `_id` | string | Yes |  |
| `label` | string | No |  |
| `locationId` | string | Yes |  |
| `updatedAt` | string | Yes |  |
| `canonicalLink` | string | Yes |  |
| `urlSlug` | string | Yes |  |

### CreateBlogPostParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `locationId` | string | Yes |  |
| `blogId` | string | Yes | You can find the blog id from blog site dashboard link |
| `imageUrl` | string | Yes |  |
| `description` | string | Yes |  |
| `rawHTML` | string | Yes |  |
| `status` | string (enum: `DRAFT`, `PUBLISHED`, `SCHEDULED`, `ARCHIVED`) | Yes |  |
| `imageAltText` | string | Yes |  |
| `categories` | array of string | Yes | This needs to be array of category ids, which you can get from the category get api call. |
| `tags` | array of string | No |  |
| `author` | string | Yes | This needs to be author id, which you can get from the author get api call. |
| `urlSlug` | string | Yes |  |
| `canonicalLink` | string | No |  |
| `publishedAt` | string | Yes | Provide ISO timestamp |

### UpdateBlogPostParams

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | string | Yes |  |
| `locationId` | string | Yes |  |
| `blogId` | string | Yes | You can find the blog id from blog site dashboard link |
| `imageUrl` | string | Yes |  |
| `description` | string | Yes |  |
| `rawHTML` | string | Yes |  |
| `status` | string (enum: `DRAFT`, `PUBLISHED`, `SCHEDULED`, `ARCHIVED`) | Yes |  |
| `imageAltText` | string | Yes |  |
| `categories` | array of string | Yes | This needs to be array of category ids, which you can get from the category get api call. |
| `tags` | array of string | No |  |
| `author` | string | Yes | This needs to be author id, which you can get from the author get api call. |
| `urlSlug` | string | Yes |  |
| `canonicalLink` | string | No |  |
| `publishedAt` | string | Yes | Provide ISO timestamp |

### UrlSlugCheckResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `exists` | boolean | Yes | Indicates whether the url slug exists or not |
