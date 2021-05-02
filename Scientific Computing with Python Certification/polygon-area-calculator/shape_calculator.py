class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width={:d}, height={:d})'.format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        if shape.height > self.height or shape.width > self.width:
            return 0
        return (self.height // shape.height) * (self.width // shape.width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return 'Square(side={:d})'.format(self.height)

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side