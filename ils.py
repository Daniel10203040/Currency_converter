class ILS:
    def get_value(self):
        return 0.28

    def calculate(self, amount):
        value = self.get_value()
        return amount * value