class Vector2D:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: 'Vector2D'):
        """Сложение векторов"""
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __mul__(self, scalar: int):
        """Умножение вектора на скаляр"""
        return Vector2D(self.x * scalar, self.y * scalar)
