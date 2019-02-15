# Matthías Ólafur

# 2.
def linearLeit(listi,finna):
    for x in range(len(listi)):
        if listi[x] == finna:
            return x
    return -1

listi = [8,5,3,7,1,9,2,6]
print("Staða 1: ",linearLeit(listi,4))
print("Staða 1: ",linearLeit(listi,2))


# 3.
def binaryLeit(listi,finna):
    midja = len(listi)//2
    if midja == 0:
        return -1
    if listi[midja] == finna:
        return midja
    for x in range(midja):
        if listi[x] == finna:
            return x
    re = binaryLeit(listi[midja+1:len(listi)],finna)
    if re == -1:
        return -1
    else:
        return re + midja + 1



listi = [1,2,3,5,6,7,8,9]
print("Binary",binaryLeit(listi,10))
print("Binary",binaryLeit(listi,6))

# 5.
def insertRett(listi,tala):
    if len(listi) == 0 or tala >= listi[len(listi)-1]:
        listi.append(tala)
        return listi
    midja = len(listi)//2
    if listi[midja] >= tala:
        for x in range(midja+1):
            if listi[x] >= tala:
                if (x == midja+1):
                    listi.append(tala)
                nyr = listi[0:x]
                nyr.append(tala)
                if (x == midja+1):
                    return nyr
                for x in listi[x:len(listi)]:
                    nyr.append(x)
                return nyr
    return listi[0:midja+1] + insertRett(listi[midja+1:len(listi)],tala)

listi = []
listi = insertRett(listi,3)
print("Very nice3\t",listi)

listi = [2,5,9,12,16,18,22,23]
print("listi\t\t",listi)
listi = insertRett(listi,3)
print("Very nice3\t",listi)
listi = insertRett(listi,19)
print("Very nice19\t",listi)
listi = insertRett(listi,19)
print("Very nice19\t",listi)
listi = insertRett(listi,26)
print("Very nice26\t",listi)
listi = insertRett(listi,1)
print("Very nice1\t",listi)

# tré
#           5
#       4       7
#      3       6  8
