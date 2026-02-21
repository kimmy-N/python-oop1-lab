# lib/coffee.py

class Coffee:
    def __init__(self, size, price):
        self._size = None  # internal variable for validation
        self.size = size   # use setter for validation
        self.price = price

    # size property with validation
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # tip method
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1