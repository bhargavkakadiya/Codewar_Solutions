key = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
       'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14',
       'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21',
       'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
evalu = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    check1 = list(text.lower())
    l = len(check1)
    list1=[]
    for i in range(l-1):
        if check1[i] in list(evalu):
           list1.append(check1[i])
       
    list3=[]
    for i in range(len(list1)):
        n = list1[i]
        list3.append(key[n])

    string1 = ' '.join(list3)
    return string1

#return ' '.join(key[x] for x in [i for i in list(text.lower()) if i in list(evalu)])

if __name__ == "__main__":
    print(alphabet_position("The sunset sets at twelve o' clock."))
