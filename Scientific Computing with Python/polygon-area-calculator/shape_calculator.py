############################
# @author Jack Steussie    #
# @email jsteussi@ucsd.edu #
############################

class Rectangle:
    '''Rectangle class that represents a rectangle with width and height'''

    def __init__(self, width, height):
        ''' Constructor for class Rectangle. Takes width and height as input.

        @param self: Rectangle class instance self-reference
        @param width: width of the rectangle to be instantiated
        @param height: height of the rectangle to be instantiated
        @return: None
        '''
        self.width = width
        self.height = height

    def __str__(self):
        ''' Creates string representation of any instance of Rectangle.

        @param self: Rectangle class instance self-reference
        @return: string representation of this instance of Rectangle
        '''
        return 'Rectangle(width=' + str(self.width) + ', height=' + \
            str(self.height) + ')'
        
    def set_width(self, width):
        ''' Sets the width of the rectangle to input width.

        @param self: Rectangle class instance self-reference
        @param width: new width value of Rectangle instance
        @return: None
        '''
        self.width = width
        
    def set_height(self, height):
        ''' Sets the height of the rectangle to input height.

        @param self: Rectangle class instance self-reference
        @param height: new height value of Rectangle instance
        @return: None
        '''
        self.height = height
        
    def get_area(self):
        ''' Returns the area of the input Rectangle 
            instance (width * height).

        @param self: Rectangle class instance self-reference
        @return: the area of the given instance of Rectangle
        '''
        return self.width * self.height
        
    def get_perimeter(self):
        ''' Returns the perimeter of the input Rectangle 
            instance (2 * width + 2 * height).

        @param self: Rectangle class instance self-reference
        @return: the perimeter of the given instance of Rectangle
        '''
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        ''' Returns the diagonal of the input Rectangle
            instance ((width ** 2 + height ** 2) ** .5).
        
        @param self: Rectangle class instance self-reference
        @return: the diagonal of the given instance of Rectangle
        '''
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        ''' Returns the shape of the given instance of the Rectangle class
            with lines of *'s.
        
        @param self: Rectangle class instance self-reference
        @return: string that, when printed, is the shape of the given rectangle
        '''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        output = str()
        for i in range(0, self.height):
            for j in range(0, self.width):
                output += '*'

            output += '\n'
        
        return output
    
    def get_amount_inside(self, shape):
        ''' Takes a shape (of class Rectangle or subclass Square) as input
            and returns how many times the input shape could fit inside 
            this instance of a shape (with no rotations).

        @param self: Rectangle class instance self-reference
        @param shape: object of type Rectangle or any of its children
        @return: the amount of times the input shape can fit inside given shape 
        '''
        max_width = self.width // shape.width
        max_height = self.height // shape.height
        return max_width * max_height

class Square(Rectangle):
    '''Subclass of Rectangle that represents a square with a certain length.'''

    def __init__(self, length):
        ''' Constructor for class Square. Takes a length as input.

        @param self: Square class instance self-reference
        @param length: the length of one side of the square
        @return: None
        '''
        super().__init__(length, length)
    
    def __str__(self):
        ''' Creates string representation of any instance of Square.

        @param self: Square class instance self-reference
        @return: string representation of this instance of Square
        '''
        return 'Square(side=' + str(self.height) + ')'
    
    def set_side(self, side):
        ''' Sets the side length of the given instance of Square.

        @param self: Square class instance self-reference
        @param side: new side length value
        @return: None
        '''
        self.width = side
        self.height = side
    
    def set_width(self, side):
        ''' Sets the width of the given instance of Square.

        @param self: Square class instance self-reference
        @param side: new width length value
        @return: None
        '''
        self.width = side
        self.height = side
    
    def set_height(self, side):
        ''' Sets the height of the given instance of Square.

        @param self: Square class instance self-reference
        @param side: new height length value
        @return: None
        '''
        self.width = side
        self.height = side