from typing import List
from fastapi import FastAPI
from .discounts.controllers import router


app = FastAPI(
    title="MinoristaCoop API",
    description="API for calculating final prices with discount",
    version="1.0.0",
    openapi_tags=[{"name": "Pricing", "description": "Operatios for calculating prices"},
                  {"name": "Providers", "description": "Get all providers"}],
)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome, visit /docs for more information"}


PROVIDERS = ["A", "B", "C", "D"]

@app.get("/providers", response_model=List[str], summary="Obtener lista de proveedores", tags=["Providers"])
def get_providers():
    """
    Return a List of all the Providers: A, B, C, D.
    """
    return PROVIDERS

app.include_router(router, prefix="/api/v1")