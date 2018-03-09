#kyu=7
def square_digits(num):
    a=[]
    for i in range(len(str(num))):
        a.append(str((int(str(num)[i]))**2))
    return int("".join(a))


#OR
#   def square_digits(num):
#        return int(''.join(str(int(d)**2) for d in str(num)))