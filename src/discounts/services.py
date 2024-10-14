
from abc import ABC, abstractmethod
from typing import List
from .models import Item, ItemWithDiscount


class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass


class ProviderADiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.95


class ProviderBDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.90
    

class ProviderCDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.85


class ProvideDDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.75
    

class Discount:

    @staticmethod
    def get_discount_strategy(provider: str) -> DiscountStrategy:
        if provider == 'A':
            return ProviderADiscount()
        elif provider == 'B':
            return ProviderBDiscount()
        elif provider == 'C':
            return ProviderCDiscount()
        elif provider == 'D':
            return ProvideDDiscount()
        else:
            raise ValueError(f"Invalid provider {provider}")


class PriceCalculatorService:

    def calculate_final_prices(
            self, items: List[Item]) -> List[ItemWithDiscount]:
        
        result = []
        for item in items:
            discount_strategy = Discount.get_discount_strategy(item.provider)
            discounted_price = discount_strategy.apply_discount(
                item.unitPrice
                )
            result.append(
                ItemWithDiscount(
                    sku=item.sku, unitPriceWithDiscount=round(
                        discounted_price, 2)))
        return result
