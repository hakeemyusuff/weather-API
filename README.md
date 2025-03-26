# Weather API Wrapper Service

This is a simple Weather API wrapper service that fetches weather data from a third-party API (Visual Crossing) and returns the data in JSON format. The project is part of the [roadmap.sh backend projects](https://roadmap.sh/projects/weather-api-wrapper-service) and is built using Django Rest Framework (DRF).

## Features

- Fetches weather data from Visual Crossing API.
- Implements in-memory caching using Redis to improve performance.
- Rate limiting to prevent API abuse.
- Supports different unit groups (metric, imperial, etc.).
- Swagger UI documentation using drf-yasg.

## Technologies Used

- **Django Rest Framework (DRF)** – For building the API.
- **Redis** – For caching API responses to reduce redundant external requests.
- **Gunicorn** – For WSGI application serving in production.
- **drf-yasg** – For API documentation with Swagger UI.
- **Requests** – For making HTTP requests to the third-party weather API.

## Setup Instructions

### Prerequisites

- Python 3.12+
- Redis (running locally or using a managed service)
- A free API key from [Visual Crossing](https://www.visualcrossing.com/weather-api)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/weather-api-wrapper.git
   cd weather-api-wrapper
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   Create a `.env` file in the project root and add:
   ```env
   key=YOUR_VISUAL_CROSSING_API_KEY
   REDIS_URL=redis://localhost:6379/1
   ```

### Running the Project locally

1. Start Redis:
   ```sh
   redis-server
   ```
2. Run the Django server:
   ```sh
   python manage.py runserver
   ```
3. Access the API at:
   - `http://127.0.0.1:8000/weather/{location}`
   - Swagger UI: `http://127.0.0.1:8000/doc/swagger/`

## API Endpoints

- **GET /weather/{location}** - Fetches the weather data for the given location.

