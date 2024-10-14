import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from src.discounts.services import PriceCalculatorService
from src.discounts.models import Item
from src.main import app 

# Inicializa el TestClient
client = TestClient(app)

# Pruebas para PriceCalculatorService
@pytest.fixture
def price_calculator_service():
    return PriceCalculatorService()

def test_calculate_final_prices(price_calculator_service):
    items = [Item(sku="2626", unitPrice=123.4, provider="A")]
    result = price_calculator_service.calculate_final_prices(items)
    assert result[0].unitPriceWithDiscount == 117.23

def test_invalid_provider(price_calculator_service):
    items = [Item(sku="2626", unitPrice=123.4, provider="Z")]
    with pytest.raises(ValueError):
        price_calculator_service.calculate_final_prices(items)

@pytest.mark.parametrize(
    "sku, unitPrice, provider, expected_error",
    [
        (
            None, 123.4, "A",
            "Input should be a valid string"
        ),  # sku es None
        (
            "2626", None, "A",
            "Input should be a valid number"
        ),  # unitPrice es None
        (   "2626", 123.4, None,
            "Input should be a valid string"
        ),  # provider es None
    ]
)
def test_none_values(sku, unitPrice, provider, expected_error):
    with pytest.raises(ValidationError) as excinfo:
        Item(sku=sku, unitPrice=unitPrice, provider=provider)
    
    assert expected_error in str(excinfo.value)
    

def test_api_endpoint():
    response = client.get("/api/v1/calculate_price") 
    assert response.status_code == 405
    assert response.status_code != 200
    assert response.json() == {"detail":"Method Not Allowed"}
