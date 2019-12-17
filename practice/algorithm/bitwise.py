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
        if(len(txt) < 6):
            txt = txt.rjust(6, ' ')
        arr3.append(txt)
    return arr3
print( getBitwise(5,[9,20,28,18,11],[30,1,21,17,28]) )
print( getBitwise(6,[46,33,33,22,31,1],[27,56,19,14,14,1]) )