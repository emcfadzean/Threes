#Rules:
# z < x < y
# x^2 + y^2 = 1 + z^4
# No common factors


import doctest

candidate = 1;
#Produce x, y, and z so that z < x < y
for y in range(1, 100):
    for x in range(1, y):
        for z in range(1, x):
            print("{} {} {} {}".format(candidate, x, y, z));
            candidate = candidate + 1;
    
if __name__ == "__main__":
    doctest.testmod()
