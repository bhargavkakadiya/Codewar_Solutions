#kyu=6
#Build a pile of cubes
def find_nb(m):
    for n in range(int(m/10)):
        a=sum(n**3 for n in range(1,n+1))
        if a==m:
            return print(n)
    return -1



find_nb(4183059834009)
