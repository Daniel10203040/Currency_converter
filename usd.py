class USD:
    def get_value(self):
        return 3.52

    def calculate(self, amount):
        value = self.get_value()
        return amount * value