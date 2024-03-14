class Checkout:
    def __init__(self):
        self.prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.special_offers = {'A': (3, 130), 'B': (2, 45)}
        self.cart = {}

    def scan(self, items):
        for item in items:
            if item in self.cart:
                self.cart[item] += 1
            else:
                self.cart[item] = 1

    def calculate_total(self):
        total = 0
        for item, quantity in self.cart.items():
            total += self.calculate_item_price(item, quantity)
        return total

    def calculate_item_price(self, item, quantity):
        if item in self.special_offers:
            special_quantity, special_price = self.special_offers[item]
            special_offer_count = quantity // special_quantity
            remaining_quantity = quantity % special_quantity
            return special_offer_count * special_price + remaining_quantity * self.prices[item]
        else:
            return quantity * self.prices[item]


# Example usage:
def run_checkout(items):
    checkout = Checkout()
    checkout.scan(items)
    total_price = checkout.calculate_total()
    return total_price


# Test cases
test_cases = [
    ("", 0),
    ("A", 50),
    ("AB", 80),
    ("CDBA", 115),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 230),
    ("AAAAAA", 260),
    ("AAAB", 160),
    ("AAABB", 175),
    ("AAABBD", 190),
    ("DABABA", 190)
]

for items, expected_price in test_cases:
    assert run_checkout(items) == expected_price

print("All test cases passed successfully!")
