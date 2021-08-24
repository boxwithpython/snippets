class Vector2D:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __mul__(self, scalar: int):
        """Умножение вектора на скаляр"""
        if isinstance(scalar, int):
            return Vector2D(self.x * scalar, self.y * scalar)
        else:
            return NotImplemented
