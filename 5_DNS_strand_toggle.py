def DNA_strand(dna):
    n=[]
    for i in range(len(dna)):
        if dna[i]=='A':
            n.append('T')
            break
        elif dna[i]=='T':
            n.append('A')
            break
        elif dna[i]=='C':
            n.append('G')
            break
        else:
            n.append('C')
            break
    print(n)
    return n

DNA_strand('ATTG')