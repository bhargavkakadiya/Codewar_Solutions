def expanded_form(num):
    list = []
    lenn = len(str(num))            #length of input integer
    for i in range(lenn):
        a = 10**(lenn-i-1)
        b = (int(num/a))*a
        num = num % a
        list.append(str(b))
    list = " + ".join(list)
    return


num = 125
expanded_form(num)
