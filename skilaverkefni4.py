# Matthías Ólafur

# 2.
print("\n--------- Dæmi 2 ---------\n")
def linearLeit(listi,finna):
    for x in range(len(listi)):
        if listi[x] == finna:
            return x
    return -1
listi = [8,5,3,7,1,9,2,6]
print("Staða 4: ",linearLeit(listi,4))
print("Staða 2: ",linearLeit(listi,2))


# 3.
print("\n--------- Dæmi 3 ---------\n")
def binaryLeit(listi,finna):
    midja = len(listi)//2
    if midja == 0:
        if listi[midja] == finna:
            return midja
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



listi = [1,2,3,5,6,7,8,9,10]
print("Binary staða 10:",binaryLeit(listi,10))
print("Binary staða 11:",binaryLeit(listi,11))
print("Binary staða 9:",binaryLeit(listi,9))
print("Binary staða 6:",binaryLeit(listi,6))
print("Binary staða 1:",binaryLeit(listi,1))

# 5.
print("\n--------- Dæmi 5 ---------\n")
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
print("Listinn\t",listi)
listi = insertRett(listi,3)
print("Listinn\t",listi)
listi = insertRett(listi,19)
print("Listinn\t",listi)
listi = insertRett(listi,19)
print("Listinn\t",listi)
listi = insertRett(listi,26)
print("Listinn\t",listi)
listi = insertRett(listi,1)
print("Listinn\t",listi)


# 6
print("\n--------- Dæmi 6 ---------\n")
class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None
    def insert(self,v):
        if self.value == v:
            return False
        elif self.value > v:
            if self.left:
                return self.left.insert(v)
            else:
                self.left = Node(v)
                return True
        else:
            if self.right:
                return self.right.insert(v)
            else:
                self.right = Node(v)
                return True
class Tree:
    def __init__(self):
        self.root = None
    def insert(self,v):
        if self.root:
            return self.root.insert(v)
        else:
            self.root = Node(v)
            return True

def finna(tre,data):
    if tre.root:
        return finnaN(tre.root,data)
    return False
def finnaN(root,data):
    if root.value and root.value == data:
        return True
    if root.left:
        if finnaN(root.left,data):
            return True
    if root.right:
        return finnaN(root.right,data)
    return False
print("\n------ Tré 1 ------\n")
t = Tree()
print("Insert 7:",t.insert(7))
print("Insert 3:",t.insert(3))
print("Insert 1:",t.insert(1))
print("Insert 6:",t.insert(6))
print("Insert 8:",t.insert(8))
print("Insert 5:",t.insert(5))
print("Insert 10:",t.insert(10))
print("Insert 9:",t.insert(9))
print("Insert 1:",t.insert(1))
print("Insert 2:",t.insert(2))
print()
print("Finnst 7: ",finna(t,7))
print("Finnst 3: ",finna(t,3))
print("Finnst 1: ",finna(t,1))
print("Finnst 2: ",finna(t,2))
print("Finnst 6: ",finna(t,6))
print("Finnst 5: ",finna(t,5))
print("Finnst 8: ",finna(t,8))
print("Finnst 9: ",finna(t,9))
print("Finnst 10: ",finna(t,10))
print()
print("Finnst 0: ",finna(t,0))
print("Finnst 12: ",finna(t,12))
print("Finnst 4: ",finna(t,4))
print()
print("Finnst: ",finna(t,7))


t2 = Tree()
print()
print("\n------ Tré 2 ------\n")
print("Finnst 7: ",finna(t2,7))

print("\n-------------------\n")
