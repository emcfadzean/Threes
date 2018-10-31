#Rules:
# z < x < y
# x^2 + y^2 = 1 + z^4
# No common factors


import doctest

def check(x, y, z):
    sizeOrder(x,y,z);
    print("{} {} {}".format(x,y,z));

# z < x < y
def sizeOrder(x, y, z):
    """
    Checks to see if inputs match the following condition: z < x < y
    >>> sizeOrder(1,2,3)
    False
    >>> sizeOrder(2,3,1)
    True
    >>> sizeOrder(1,1,1)
    False
    """
    if (z >= x or x >= y):
        return False;
    else:
        return True;

with open("primes.txt", "r") as file:
    for line in file:
        for word in line.split():
            print(word);
    
if __name__ == "__main__":
    doctest.testmod()
