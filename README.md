# User Management API

This API, built using FastAPI, MongoDB, and Docker, manages user information and implements translation functionality using langchain and OpenAI.


## set OPENAI API key
Please add the variable `OPENAI_API_KEY=your_key` to your `.env` file to use this application.

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
* http://127.0.0.1:8000/chain/playground/
  * langchin翻譯頁面

## TODO
* Unit testing
* add Nginx
* More asyncio example scenarios
* API validation
* Run GitHub Actions