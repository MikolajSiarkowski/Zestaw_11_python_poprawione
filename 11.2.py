import random
def saveL(L):
    for i in range(len(L)):
        f.write(str(i)+" "+str(L[i])+"\n")
    f.write("\n\n")

def selectsort(L, left, right):
    for i in range(left, right):
        saveL(L)
        k = i
        for j in range(i+1, right+1):  
            if L[j] < L[k]:
                k = j        
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item
    saveL(L)

filepath="data.txt"
f=open(filepath,"w")
L=[]
for i in range(50):
    L.append(i)
random.shuffle(L)
print("lista przed sortowaniem:\n",L)
selectsort(L,0,49)
print("\nlista po sortowaniu:\n",L)
f.close()


