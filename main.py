from fastapi import FastAPI
from endpoints import stores

app = FastAPI()

# Only include stores router
app.include_router(stores.router)