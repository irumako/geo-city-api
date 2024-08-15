# Aiohttp REST API Service
This is a REST API service built using aiohttp and asyncpg for managing a list of cities, including functionalities like creating, retrieving, deleting, and finding the nearest cities based on geographic coordinates.

## Features
- CRUD Operations: Create, Read, Update, Delete cities in a PostgreSQL database.
- Nearest Cities: Find the two nearest cities to a given geographic point (latitude and longitude).
- External API Integration: Fetch city data from the Ninja API.

## Getting Started
### Prerequisites
- Python 3.8+
- Docker
- API key for the Ninja API (for fetching city data)

### Installation
1. **Clone the Repository:**

    ```
    git clone https://github.com/irumako/geo-city-api.git
    cd geo-city-api
   ```
2. **Create a Virtual Environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

4. **Create .env file:**

    ```
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_DB=db_name
    POSTGRES_SERVER=localhost
    
    API_TOKEN=token
    ```
    
### Running the Service
#### **Start the Server:**
```
make run # With Poetry `make run_poetry
```

#### **API Endpoints:**

- Create City: Fetch and store city data.

   `POST /cities?name=<city_name>`
- Get All Cities: Retrieve all cities in the database.
 
   `GET /cities`
- Get City by ID: Retrieve a city by its ID.
  
  `GET /cities/{id}`
- Delete City by ID: Delete a city by its ID.
  
  `DELETE /cities/{id}`
- Nearest Cities: Get the two nearest cities to the provided latitude and longitude.

   `GET cities/nearest?latitude=<lat>&longitude=<lon>`