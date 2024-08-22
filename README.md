# Product Catalog API

## Overview

The Product Catalog API is a RESTful API designed to manage a product catalog. It supports CRUD operations, real-time inventory updates, product search, and popularity calculation based on sales.

## Features

- **Product Management**: Create, read, update, and delete products.
- **Product Search**: Search for products by name, description, and category.
- **Inventory Management**: Real-time updates to inventory counts.
- **Popularity Calculation**: Calculate product popularity based on sales.

## Requirements

- Python
- Django
- Django REST Framework
- Docker
- Docker Compose

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kadiyalove/product_management.git

2. **Docker Commands**
   ```bash
   docker-compose up --build

3. **Apply Migrations**
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate

4. **Access the Application**
   Open your browser and navigate to http://localhost:8000 to access the API.


   - Review the API documentation here: http://localhost:8000/redoc/
   - Test the API functionality here: http://localhost:8000/swagger/


