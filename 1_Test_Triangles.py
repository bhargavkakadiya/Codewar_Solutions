def is_triangle(a, b, c):
    if a < b+c and b < a+c and c < a + b:
        print ("true")
        return True
    else:
        print ("False")
        return False
