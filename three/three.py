"""A library dedicated to the beauty of the number three.

"""

# Numbers

def three():
    return 3


def squared():
    return 9


def cubed():
    return 27


def dozen():
    return 36


def binary():
    return bin(3)


def factorial():
    return 6


def is_three(x):
    return x == three()


def filter(items):
    return [item for item in items if is_three(item)]


def map(items):
    return [three() for item in items]


def reduce(items):
    return three()


# Language

def letters():
    return ['t', 'h', 'r', 'e', 'e']


def spanish():
    return 'tres'


def german():
    return 'drei'


def french():
    return 'drois'


def italian():
    return 'tre'


# Currency

def dollars():
    return '$3.00'


def cents():
    return '$0.03'


# Rule of Threes

def rule_of():
    return 'Things that come in 3s are inherently more appealing.'

  
def is_appealing(items):
    return len(items) == 3


# Novelty 

def musketeers():
    return ['Athos', 'Aramis', 'Porthos']


def stooges():
    return ['Larry', 'Curly', 'Moe']


def wise_men():
    return ['Melchior', 'Caspar', 'Balthazar']


def little_pigs():
    """Returns a list of the materials used in the story 'Three Little Pigs'"""
    return ['Straw', 'Sticks', 'Bricks']


def blind_mice():
    """Returns the names of the three blind mice in shrek"""
    return ['Forder', 'Gorder', 'Horder']


# Food

def leches():
    return ['Condensed', 'Evaporated', 'Heavy cream']


def peas():
    return 'As close as three peas in a pod'


# Misc

def string():
    return '3'

def force_three(func):
    def inner(*args, **kwargs):
        return 3
    return inner
