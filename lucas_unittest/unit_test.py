"""write a simple calculator so has add subtract multiply divide"""

class Calculator:

    # rases Keyword
    def add(self, a:int, b:int):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Must be two integers.")
        return a + b

    def multiply(self, a, b):
        return a * b
