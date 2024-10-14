from pydantic import BaseModel, Field
from typing import List


# Define Item body model
class Item(BaseModel):
    sku: str = Field(..., json_schema_extra={'example': "2606"})
    unitPrice: float = Field(..., json_schema_extra={'example': 153.21})
    provider: str = Field(..., json_schema_extra={'example': "A"})


# Define response body model
class ItemWithDiscount(BaseModel):
    sku: str
    unitPriceWithDiscount: float


# Define API endpoint models
class ItemListRequest(BaseModel):
    items: List[Item]


# Define API endpoint response item model
class ItemListResponse(BaseModel):
    items: List[ItemWithDiscount]


# Define API endpoint response provider model
class ProvidersList(BaseModel):
    providers: List[str]
