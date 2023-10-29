# ------------------ IMPORTS ------------------


import pygame
from render.colors import Color

# ------------------ GLOBAL VARIABLES ------------------

# This line initializes the pygame.font module, 
# which is used for showing text in the graphics window.
pygame.font.init()


# ------------------ CLASSES AND FUNCTIONS ------------------


class NodeType:
    '''
    This block of code defines an enumeration class NodeType which has three values INPUT, HIDDEN, 
    and OUTPUT
    . This class is used to represent the type of neural network nodes.'''
    INPUT = 0
    HIDDEN = 1
    OUTPUT = 2


class Node:
    """
    This block of code defines a class Node which represents a single node in the neural network. 
    The __init__ method initializes the properties of the node, such as its id, coordinates, 
    type, label, and index. The draw method is used to draw the node on the screen. 
    The get_color method calculates the color of the node based on its type and other properties.
    """
    RADIUS = 20
    SPACING = 5
    LAYER_SPACING = 100
    CONNECTION_WIDTH = 1
    FONT = pygame.font.SysFont("comicsans", 15)

    def __init__(self, id: int, x: int, y: int, type: NodeType, colors: list[Color], label: str = "", index: int = 0):
        self.id = id
        self.x = x
        self.y = y
        self.type = type
        self.colors = colors
        self.label = label
        self.index = index
        self.inputs = [0, 0, 0, 0, 0]
        self.output = None

    def draw(self, screen: pygame.Surface):
        """
This is the draw() method of the Node class, which is responsible for showing the node on the screen.

First, it calls the get_color() method of the same class to determine the color scheme for the node.
 This color scheme is stored in the color_scheme variable.

Next, it draws two circles on the screen using the pygame.draw.circle() function. 

The first circle is drawn using the color scheme's first color (which represents the outer edge of the node), 
and the second circle is drawn using the second color (which represents the inner fill of the node).

The center of the circles is located at the (x, y) position of the node, and the radius 
of the circles is set to Node.RADIUS (which is a constant value of 20).

If the node is not of type NodeType.HIDDEN, it then generates a pygame.Surface object containing the label text 
using the Node.FONT.render() function. This text surface is stored in the text variable.

Finally, it blits (i.e., draws) the label text onto the screen using the screen.blit() function. The position of the text is set to the right side of the node if it is an input node (self.type-1), and the left side of the node if it is an output node (-self.type). The Node.RADIUS + 5 term is added as spacing between the node and the label, and the text.get_height()/2 term is subtracted to vertically center the text. The text color is set to Color.BLACK.
        """
        color_scheme = self.get_color()

        pygame.draw.circle(
            screen, color_scheme[0], (self.x, self.y), Node.RADIUS)
        pygame.draw.circle(
            screen, color_scheme[1], (self.x, self.y), Node.RADIUS - 2)

        if self.type != NodeType.HIDDEN:
            text = Node.FONT.render(self.label, 1, Color.BLACK)
            screen.blit(text, (self.x + (self.type-1) * ((text.get_width()
                            if not self.type else 0) + Node.RADIUS + 5), self.y - text.get_height()/2))

    def get_color(self):
        if self.type == NodeType.INPUT:
            v = self.inputs[self.index]
            ratio = 1 - (min(v / 100, 1))
        elif self.type == NodeType.OUTPUT:
            ratio = 1 if self.index == self.output else 0
        else:
            ratio = 0

        color = [[0, 0, 0], [0, 0, 0]]
        for i in range(3):
            color[0][i] = int(ratio * (self.colors[1][i] -
                            self.colors[3][i]) + self.colors[3][i])
            color[1][i] = int(ratio * (self.colors[0][i] -
                            self.colors[2][i]) + self.colors[2][i])
        return color


class Connection:
    def __init__(self, input, output, wt):
        self.input = input
        self.output = output
        self.wt = wt

    def draw(self, screen):
        color = Color.GREEN if self.wt >= 0 else Color.RED
        width = int(abs(self.wt * Node.CONNECTION_WIDTH))
        pygame.draw.line(screen, color, (self.input.x + Node.RADIUS,
                         self.input.y), (self.output.x - Node.RADIUS, self.output.y), width)
"""
This code defines a class called Connection that represents a connection between two Node objects in a neural network.
 The __init__ method initializes the Connection object with an input node, an output node, and a weight for the connection.

The draw method takes in a screen parameter which is a Pygame surface and draws the connection between the input and output nodes
 as a line on the screen. The color of the line is determined based on the weight of the connection. If the weight is positive, 
 the color of the line is green, otherwise, it is red. The width of the line is proportional to the absolute value of the weight, 
 and it is scaled by a constant factor Node.CONNECTION_WIDTH.

To draw the line, the method uses the pygame.draw.line function, which takes in the screen parameter, a color,
 the starting and ending points of the line, and the line width. The starting point of the line is at the center 
 of the input node, which is represented by (self.input.x + Node.RADIUS, self.input.y), and the ending point of
   the line is at the center of the output node, which is represented by (self.output.x - Node.RADIUS, self.output.y).
   """