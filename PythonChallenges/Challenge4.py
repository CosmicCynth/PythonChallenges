#Write a function that takes the base and height of a triangle and return its area.

def TriArea(base,height):
    Answer = base * height / 2
    return Answer

print(("Area: " + str(TriArea(5,5))))