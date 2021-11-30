class Calculator:

    def add(self, a, b):
        self.a = a
        self.b = b
        return a+b
    def subtract(self, a, b):
        self.a = a
        self.b = b
        return a-b
    def multiply(self, a, b):
        self.a = a
        self.b = b
        return a*b
    
    def divide(self, a, b):
        self.a = a
        self.b = b
        try:
            return a/b
        except ZeroDivisionError as exception:
            print(f'An error occurred: {exception}')