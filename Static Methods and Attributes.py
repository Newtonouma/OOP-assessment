class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

result1 = Calculator.add(5, 3)
print(f"Result 1: {result1}")
print(f"Add method called {Calculator.count} times")

result2 = Calculator.add(10, 7)
print(f"Result 2: {result2}")
print(f"Add method called {Calculator.count} times")

result3 = Calculator.add(2, 6)
print(f"Result 3: {result3}")
print(f"Add method called {Calculator.count} times")
