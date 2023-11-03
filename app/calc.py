import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y): #Función suma
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):#Función resta
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):#Función multiplicación
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):#Función división
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):#Función potenciación
        self.check_types(x, y)
        return x ** y
    
    def square_root(self, x):#Función raíz cuadrada
        self.check_types(x, 1)
        if x < 0:#valida si los números son positivos para sacarle la raíz
            raise ValueError("Square root is not defined for negative numbers")
        return math.sqrt(x)

    def logarithm(self, x):#Función logarítmo en base 10
        self.check_types(x, 1)
        if x <= 0:#valida si los números son positivos para aplicarle el logarítmo
            raise ValueError("Logarithm is not defined for non-positive numbers")
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result1 = calc.add(2, 2)
    result2 = calc.logarithm(100)
    print(result1, result2)