# Simple CRUD API

This project is designed for managing products and their characteristics. It allows you to create, update, delete, and read products stored in the database.

## Technologies
- **FastAPI**: Web framework for building APIs.
- **Alembic**: Database migration tool.
- **Pydantic**: Data validation and parsing.
- **PostgreSQL**: Database for storing product data.
- **Docker**: Containerization for the application.

## Setup and Running with Docker

### Prerequisites:
Make sure Docker and Docker Compose are installed on your machine. If you don't have them installed, you can download and install Docker from [here](https://www.docker.com/get-started).

### Steps to run the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KravchenkoSerhiii/simple-crud-api

2. **Set up the .env file**
    Create .env file in the root directory of the project based on the template below:
    
   ```bash
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=my_database
    DB_USER=my_user
    DB_PASSWORD=my_password

3. **Build and start the containers:**
    Run the following command to build and start the containers:

    ```bash
   docker-compose up --build

This command will build the Docker images (if not already built) and start the application and database containers.

4. **Check if the server is running:**
    After starting the containers, you can check if the API is running by visiting http://localhost:8000 in your browser.

## Features
Create Products: You can create new products with their characteristics.

Read Products: You can read the details of products in the database.

Update Products: You can update the information of existing products.

Delete Products: You can delete products from the database.
