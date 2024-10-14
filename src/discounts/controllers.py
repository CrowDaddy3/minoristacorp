from fastapi import APIRouter, HTTPException
from .models import ItemListRequest, ItemListResponse
from .services import PriceCalculatorService


router = APIRouter()

price_service = PriceCalculatorService()  # Create an instance of the class

@router.post("/calculate_price",
             response_model=ItemListResponse,
             status_code=200,
             tags=["Pricing"]
             )
def calculate_prices(request: ItemListRequest):
    """
    Calculate the price of the items with discount
    """
    try:
        items_with_discounts = price_service.calculate_final_prices(
            request.items)
        return  ItemListResponse(items=items_with_discounts)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
