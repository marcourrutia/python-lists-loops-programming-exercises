# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below
for _ in range(10):
    x = random.randint(1, 100)
    my_list.append(x)