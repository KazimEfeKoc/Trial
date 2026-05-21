'''How to create Class and
Instances'''
class Circle(object):

    #constructor : It is a special method to initialize some data attributes.
    #In this case @radius and @color are the parameters.
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


RedCircle = Circle(5,"Blue")

for num in range(2,10):
    if num == 4:
        continue
    print(num)

import pandas as pd

data = {
    "name": ["Efe", "Sameera", "Kazim"],
    "age": [18,20,25],
    "city": ["Berlin", "Antalya", "Lahore"]
}

df = pd.DataFrame(data)

print(df)
