#Rules:
# z < x < y
# x^2 + y^2 = 1 + z^4
# No common factors


import doctest

candidate = 1;
y = 1;

#Test for common factors
def commonFactors(lower, upper):
    if(lower%2 == 0 and upper%2 == 0):
        return True;
    if(upper%lower == 0):
        return True;
    for i in range(2, upper):
        if(upper%i == 0 and lower%i == 0):
            return True;
    return False;
    

#Produce x, y, and z so that z < x < y
while(candidate != 70):
    for x in range(2, y):
        if(commonFactors(x, y)):
            break;
        for z in range(2, x):
            if(commonFactors(z, x) or commonFactors(z, y)):
                break;
            if((x**2+y**2) == (1+z**4)):
                print("{} {} {} {}".format(candidate, x, y, z));
                candidate = candidate + 1;
    y = y + 1;
    
if __name__ == "__main__":
    doctest.testmod()
