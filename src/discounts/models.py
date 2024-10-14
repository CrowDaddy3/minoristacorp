from pydantic import BaseModel, Field
from typing import List


class Item(BaseModel):
    sku: str = Field(..., json_schema_extra={'example': "2606"})
    unitPrice: float = Field(..., json_schema_extra={'example': 153.21})
    provider: str = Field(..., json_schema_extra={'example': "A"})


class ItemWithDiscount(BaseModel):
    sku: str
    unitPriceWithDiscount: float


class ItemListRequest(BaseModel):
    items: List[Item]


class ItemListResponse(BaseModel):
    items: List[ItemWithDiscount]


class ProvidersList(BaseModel):
    providers: List[str]
