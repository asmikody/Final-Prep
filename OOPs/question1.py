from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def process_payment(self):
        pass  # Must be implemented by subclasses

# Interface
class Discountable(ABC):
    @abstractmethod
    def apply_discount(self, discount_percent):
        pass  # Must be implemented by subclasses

# CreditCard class implementing both PaymentMethod and Discountable
class CreditCard(PaymentMethod, Discountable):
    def process_payment(self):
        print(f"Processing credit card payment of ${self.amount}")

    def apply_discount(self, discount_percent):
        discount_amount = self.amount * (discount_percent / 100)
        self.amount -= discount_amount
        print(f"Applied {discount_percent}% discount. New amount: ${self.amount:.2f}")

# PayPal class implementing both PaymentMethod and Discountable
class PayPal(PaymentMethod, Discountable):
    def process_payment(self):
        print(f"Processing PayPal payment of ${self.amount}")

    def apply_discount(self, discount_percent):
        discount_amount = self.amount * (discount_percent / 100)
        self.amount -= discount_amount
        print(f"Applied {discount_percent}% discount. New amount: ${self.amount:.2f}")

# Example usage
payment1 = CreditCard(100)
payment1.apply_discount(10)
payment1.process_payment()

payment2 = PayPal(200)
payment2.apply_discount(5)
payment2.process_payment()
