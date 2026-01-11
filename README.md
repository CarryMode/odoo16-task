# Developers Management (Odoo 16)

**Time spent:** approximately 10 hours.

**Use of AI tools:**
AI assistance was used selectively during the development process. Specifically, it was used during installation of odoo16, to help with the creation of XML views, to support the implementation of automated tests due to limited prior experience with testing, and to assist with translating the task requirements.






---



This repository contains a custom Odoo 16 Community module named **developers_management**.
The module provides basic functionality for managing developers and their associated companies.

---

## Features

### Developer Management
- Manage developers with the following fields:
  - Name (unique, required)
  - Type (front-end, backend, fullstack, out-stuff)
  - Global Identification (computed: `name-type`)
  - Phone (hidden when type is `out-stuff`)
  - Email
  - Address
  - Birth Date
  - Job Position
- List and form views for developers
- Search filters by name, phone, and type
- Group developers by type

### Company Management
- Manage companies with:
  - Name
  - Address
  - Linked developers (One2many)
- View companies and their associated developers

### Access Rights
- Only authenticated users can:
  - View developers and companies
  - Create new developers and companies
- No permissions to delete records

---

## Installation

1. Copy the `developers_management` module into your Odoo addons directory:
custom-addons/
└── developers_management

2. Update the apps list in Odoo
3. Install **Developers Management**

---

## Tests

The module includes a minimal test suite to demonstrate functionality.

### Covered Scenarios
- Developer creation
- Computed field (`global_identification`)
- Developer–Company relationship

### Running Tests

Example command:

```bash
odoo-bin -d odoo16 -u developers_management --test-enable --stop-after-init

