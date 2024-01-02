# fast-api-demo


FastAPI Docuemntation https://fastapi.tiangolo.com/

## Run
- `uvicorn app.main:app --reload`
- go to http://localhost:8000/

## Usage
Using with httpie

Add item
`http localhost:8000/items value=test`

Get items
`http localhost:8000/items`

Get item by id
`http localhost:8000/items/1`
