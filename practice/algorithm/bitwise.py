
import math

def getBitwise(n,arr1,arr2):
    arr3=[]
    for i in range(len(arr1)):
        txt=''
        b = arr1[i] | arr2[i] #31
        while(b!=0):
            nmg=b%2 # 1
            b = math.floor(b/2)
            if(nmg==1):
                txt='#'+txt
            elif(nmg==0):
                txt=' '+txt
        arr3.append(txt)
    return arr3

print( getBitwise(5,[9,20,28,18,11],[30,1,21,17,28]) )


