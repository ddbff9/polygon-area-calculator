class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    pass
  
  def __str__(self):
    width = self.width
    height = self.height
    output = self.__class__.__name__ + f"(width={width}, height={height})"
    return output
    
  def set_height(self, height):
    self.height = height
    return height
  
  def set_width(self, width):
    self.width = width
    return width
  
  def get_area(self):
    width = self.width
    height = self.height

    area = width * height
    return area
  
  def get_perimeter(self):
    width = self.width
    height = self.height

    perimeter = (2 * width) + (2 * height)
    return perimeter

  def get_diagonal(self):
    width = self.width
    height = self.height

    diagonal = (width ** 2 + height ** 2) ** .5
    return diagonal
  
  def get_amount_inside(self, shape):
    return(self.width//shape.width * self.height//shape.height)

  def get_picture(self):
    picture = ""
    if self.width > 50:
      return "Too big for picture."
      exit
    if self.height > 50:
      return "Too big for picture."
      exit

    for lines in range(self.height):
      line = "*" * self.width + "\n"
      picture += str(line)
    return picture
class Square(Rectangle):
  def __init__(self, side):
    super().__init__(width=side, height=side)
    self.side = side  
    
  def __str__(self):
    side = self.side
  
    output = self.__class__.__name__ + f"(side={side})"
    return output

  def set_side(self, side):
    self.side = side
    super().__init__(width=side, height=side)
    
  def set_width(self, side):
    self.side = side
    super().set_width(width=side)
  
  def set_height(self, side):
    self.side = side
    super().set_height(height=side)

# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))