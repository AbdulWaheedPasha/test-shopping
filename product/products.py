
class Product():

    def __init__(self, code: str, price: float, currency: str, created_at: str):
        self._code = code
        self._price = price
        self._currency = currency
        self._created_at = created_at

    def get_code(self) -> str:
        return self._code

    def get_price(self) -> float:
        return self._price

