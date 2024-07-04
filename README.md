# User Management API

This API is built using FastAPI and is used for managing user information, including user creation and retrieval operations.

## Using Docker
``` sh
docker compose up --build
```

## Local Development
* Start MongoDB Container
``` sh
docker pull mongo
```

* Start FastAPI Application

``` sh
docker run -d --name mongodb -p 27017:27017 mongo
uvicorn app.main:app --reload
```
## Documentation URLs
* http://127.0.0.1:8000/docs
* http://127.0.0.1:8000/redoc
* http://127.0.0.1:8000/openapi.json

## TODO
* Unit testing
* add Nginx
* More asyncio example scenarios
* API validation
* Run GitHub Actions