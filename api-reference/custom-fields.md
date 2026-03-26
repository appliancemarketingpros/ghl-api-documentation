# Custom Fields V2 API

Custom fields are data points that allow you to capture and store specific information tailored to your business requirements. You can create fields across field types like text, numeric, selection options and special fields like date/time or signature

**API Version:** 1.0

## Base URL

- `https://services.leadconnectorhq.com`

## Table of Contents

- [Custom Fields V2](#custom-fields-v2)

## Custom Fields V2

### GET `/custom-fields/{id}`

**Get Custom Field / Folder By Id**


                   Get Custom Field / Folder By Id. 
                  
                    
                                !
                      
                      
                        
                        Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
                        
                      
                  
                

**Operation ID:** `get-custom-field-by-id`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `field` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/custom-fields/{id}`

**Update Custom Field By Id**


     Update Custom Field By Id  
    
      
                  !
        
        
          
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          
        
    
  

**Operation ID:** `update-custom-field`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `name` | string | No | Field name |
| `description` | string | No | Description of the field |
| `placeholder` | string | No | Placeholder text for the field |
| `showInForms` | boolean | Yes | Whether the field should be shown in forms |
| `options` | array of object | No | Options for the field. Important: Providing options will completely replace the existing options array. You must include all existing options alongside any new options you wish to add. Removal of opti... |
| `acceptedFormats` | string (enum: `.pdf`, `.docx`, `.doc`, `.jpg`, `.jpeg`, `.png`, `.gif`, `.csv`, `.xlsx`, `.xls`, `all`) | No | Allowed file formats for uploads. Options include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all |
| `maxFileLimit` | number | No | Maximum file limit for uploads. Applicable only for fields with a data type of FILE_UPLOAD. |

**`options` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | string | Yes | Key of the option (Included in Create and Response, excluded in Update) |
| `label` | string | Yes | Value of the option |
| `url` | string | No | URL associated with the option (Optional, valid only for RADIO type) |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `field` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/custom-fields/{id}`

**Delete Custom Field By Id**


     Delete Custom Field By Id  
    
      
                  !
        
        
          
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          
        
    
  

**Operation ID:** `delete-custom-field`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### GET `/custom-fields/object-key/{objectKey}`

**Get Custom Fields By Object Key**


                   Get Custom Fields By Object Key 
                  
                    
                                !
                      
                      
                        
                        Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
                        
                      
                  
                

**Operation ID:** `get-custom-fields-by-object-key`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.readonly`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `objectKey` | path | string | Yes | key of the Object. Must include "custom_objects." prefix for custom objects. Available on the Custom Objects details Page under settings |
| `locationId` | query | string | Yes |  |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fields` | array of object | No | Custom Fields for the object. |
| `folders` | array of object | No | Custom Fields folder for the object. |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/custom-fields/folder`

**Create Custom Field Folder**


     Create Custom Field Folder  
    
      
                  !
        
        
          
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          
        
    
  

**Operation ID:** `create-custom-field-folder`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `objectKey` | string | Yes | The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `name` | string | Yes | Field name |
| `locationId` | string | Yes | Location Id |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the object |
| `objectKey` | string | Yes | The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `locationId` | string | Yes | Location Id |
| `name` | string | Yes | Field name |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### PUT `/custom-fields/folder/{id}`

**Update Custom Field Folder Name**


     Create Custom Field Folder  
    
      
                  !
        
        
          
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          
        
    
  

**Operation ID:** `update-custom-field-folder`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Field name |
| `locationId` | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the object |
| `objectKey` | string | Yes | The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `locationId` | string | Yes | Location Id |
| `name` | string | Yes | Field name |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### DELETE `/custom-fields/folder/{id}`

**Delete Custom Field Folder**


     Create Custom Field Folder  
    
      
                  !
        
        
          
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          
        
    
  

**Operation ID:** `delete-custom-field-folder`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.write`

**API Version:** `2021-07-28`

#### Parameters

| Parameter | In | Type | Required | Description |
|-----------|-----|------|----------|-------------|
| `id` | path | string | Yes |  |
| `locationId` | query | string | Yes | Location Id |

#### Responses

**`200` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

### POST `/custom-fields/`

**Create Custom Field**


                   Create Custom Field  
                  
                    
                                !
                      
                      
                        
                        Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
                        
                      
                  
                

**Operation ID:** `create-custom-field`

**Tags:** Custom Fields V2

**Required Scopes:** `locations/customFields.write`

**API Version:** `2021-07-28`

#### Request Body

**Required:** Yes

**Content Type:** `application/json`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `name` | string | No | Field name |
| `description` | string | No | Description of the field |
| `placeholder` | string | No | Placeholder text for the field |
| `showInForms` | boolean | Yes | Whether the field should be shown in forms |
| `options` | array of object | No | Options for the field (Optional, valid only for SINGLE_OPTIONS, MULTIPLE_OPTIONS, RADIO, CHECKBOX, TEXTBOX_LIST type) |
| `acceptedFormats` | string (enum: `.pdf`, `.docx`, `.doc`, `.jpg`, `.jpeg`, `.png`, `.gif`, `.csv`, `.xlsx`, `.xls`, `all`) | No | Allowed file formats for uploads. Options include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all |
| `dataType` | string (enum: `TEXT`, `LARGE_TEXT`, `NUMERICAL`, `PHONE`, `MONETORY`, `CHECKBOX`, `SINGLE_OPTIONS`, `MULTIPLE_OPTIONS`, `DATE`, `TEXTBOX_LIST`, `FILE_UPLOAD`, `RADIO`, `EMAIL`) | Yes | Type of field that you are trying to create |
| `fieldKey` | string | Yes | Field key. For Custom Object it's formatted as "custom_object.{objectKey}.{fieldKey}". "custom_object" is a fixed prefix, "{objectKey}" is your custom object's identifier, and "{fieldKey}" is the uniq... |
| `objectKey` | string | Yes | The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `maxFileLimit` | number | No | Maximum file limit for uploads. Applicable only for fields with a data type of FILE_UPLOAD. |
| `allowCustomOption` | boolean | No | Determines if users can add a custom option value different from the predefined options in records for RADIO type fields. A custom value added in one record does not automatically become an option and... |
| `parentId` | string | Yes | ID of the parent folder |

**`options` array item properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | string | Yes | Key of the option (Included in Create and Response, excluded in Update) |
| `label` | string | Yes | Value of the option |
| `url` | string | No | URL associated with the option (Optional, valid only for RADIO type) |

#### Responses

**`201` - Successful response**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `field` | object | No |  |

**`400` - Bad Request**

**`401` - Unauthorized**

---

## Schemas

### CreateCustomFieldsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `name` | string | No | Field name |
| `description` | string | No | Description of the field |
| `placeholder` | string | No | Placeholder text for the field |
| `showInForms` | boolean | Yes | Whether the field should be shown in forms |
| `options` | array of object | No | Options for the field (Optional, valid only for SINGLE_OPTIONS, MULTIPLE_OPTIONS, RADIO, CHECKBOX, TEXTBOX_LIST type) |
| `acceptedFormats` | string (enum: `.pdf`, `.docx`, `.doc`, `.jpg`, `.jpeg`, `.png`, `.gif`, `.csv`, `.xlsx`, `.xls`, `all`) | No | Allowed file formats for uploads. Options include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all |
| `dataType` | string (enum: `TEXT`, `LARGE_TEXT`, `NUMERICAL`, `PHONE`, `MONETORY`, `CHECKBOX`, `SINGLE_OPTIONS`, `MULTIPLE_OPTIONS`, `DATE`, `TEXTBOX_LIST`, `FILE_UPLOAD`, `RADIO`, `EMAIL`) | Yes | Type of field that you are trying to create |
| `fieldKey` | string | Yes | Field key. For Custom Object it's formatted as "custom_object.{objectKey}.{fieldKey}". "custom_object" is a fixed prefix, "{objectKey}" is your custom object's identifier, and "{fieldKey}" is the uniq... |
| `objectKey` | string | Yes | The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `maxFileLimit` | number | No | Maximum file limit for uploads. Applicable only for fields with a data type of FILE_UPLOAD. |
| `allowCustomOption` | boolean | No | Determines if users can add a custom option value different from the predefined options in records for RADIO type fields. A custom value added in one record does not automatically become an option and... |
| `parentId` | string | Yes | ID of the parent folder |

### CreateFolder

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `objectKey` | string | Yes | The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `name` | string | Yes | Field name |
| `locationId` | string | Yes | Location Id |

### CustomFieldSuccessfulResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `field` | object | No |  |

### CustomFieldsResponseDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fields` | array of object | No | Custom Fields for the object. |
| `folders` | array of object | No | Custom Fields folder for the object. |

### CustomFolderDeleteResponseDto

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `succeded` | boolean | Yes |  |
| `id` | string | Yes |  |
| `key` | string | Yes |  |

### ICustomField

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `name` | string | No | Field name |
| `description` | string | No | Description of the field |
| `placeholder` | string | No | Placeholder text for the field |
| `showInForms` | boolean | Yes | Whether the field should be shown in forms |
| `options` | array of object | No | Options for the field (Optional, valid only for SINGLE_OPTIONS, MULTIPLE_OPTIONS, RADIO, CHECKBOX, TEXTBOX_LIST type) |
| `acceptedFormats` | string (enum: `.pdf`, `.docx`, `.doc`, `.jpg`, `.jpeg`, `.png`, `.gif`, `.csv`, `.xlsx`, `.xls`, `all`) | No | Allowed file formats for uploads. Options include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all |
| `id` | string | Yes | Unique identifier of the object |
| `objectKey` | string | Yes | The key for your custom / standard object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `dataType` | string (enum: `TEXT`, `LARGE_TEXT`, `NUMERICAL`, `PHONE`, `MONETORY`, `CHECKBOX`, `SINGLE_OPTIONS`, `MULTIPLE_OPTIONS`, `DATE`, `TEXTBOX_LIST`, `FILE_UPLOAD`, `RADIO`) | Yes | Type of field that you are trying to create |
| `parentId` | string | Yes | ID of the parent folder |
| `fieldKey` | string | Yes | Field key. For Custom Object it's formatted as "custom_object.{objectKey}.{fieldKey}". "custom_object" is a fixed prefix, "{objectKey}" is your custom object's identifier, and "{fieldName}" is the uni... |
| `allowCustomOption` | boolean | No | Determines if users can add a custom option value different from the predefined options in records for RADIO type fields. A custom value added in one record does not automatically become an option and... |
| `maxFileLimit` | number | No | Maximum file limit for uploads |
| `dateAdded` | string | Yes | Date and time when the object was added |
| `dateUpdated` | string | Yes | Date and time when the object was last updated |

### ICustomFieldFolder

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | Yes | Unique identifier of the object |
| `objectKey` | string | Yes | The key for your custom object. This key uniquely identifies the custom object. Example: "custom_object.pet" for a custom object related to pets. |
| `locationId` | string | Yes | Location Id |
| `name` | string | Yes | Field name |

### OptionDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | string | Yes | Key of the option (Included in Create and Response, excluded in Update) |
| `label` | string | Yes | Value of the option |
| `url` | string | No | URL associated with the option (Optional, valid only for RADIO type) |

### UpdateCustomFieldsDTO

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationId` | string | Yes | Location Id |
| `name` | string | No | Field name |
| `description` | string | No | Description of the field |
| `placeholder` | string | No | Placeholder text for the field |
| `showInForms` | boolean | Yes | Whether the field should be shown in forms |
| `options` | array of object | No | Options for the field. Important: Providing options will completely replace the existing options array. You must include all existing options alongside any new options you wish to add. Removal of opti... |
| `acceptedFormats` | string (enum: `.pdf`, `.docx`, `.doc`, `.jpg`, `.jpeg`, `.png`, `.gif`, `.csv`, `.xlsx`, `.xls`, `all`) | No | Allowed file formats for uploads. Options include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all |
| `maxFileLimit` | number | No | Maximum file limit for uploads. Applicable only for fields with a data type of FILE_UPLOAD. |

### UpdateFolder

**Type:** `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Field name |
| `locationId` | string | Yes | Location Id |
