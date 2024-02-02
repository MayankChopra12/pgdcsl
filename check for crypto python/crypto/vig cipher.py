print("vigenere cipher")

a=input("enter the text to encrpyt")
k=input("enter the key ")
k_list=[]
h= 0
for i in k:
    k_list.append(abs(97-ord(i)))
    
j=0
l = list(k)
new_l=[]
new_d=[]
while(1==1):
    n = int(input("enter the options 1: encrypt 2:decrypt 3;exit"))
    if(n == 1):
            for i in l:
                for k in k_list:
                    temp = ord(i)
                    temp+=k
                    if((temp>=122) & i.islower()):
                        temp=96+k
                    elif((temp>=90 )& i.isupper()):
                        temp=64+k
                    new_l.append(chr(temp))
                    j+=1
            s=""
            print("encrytped",s.join(new_l))
    if(n ==2):
            j=0
            for i in l:
                for k in k_list:
                    temp = ord(i)
                    temp-=k
                    if((temp<97) & i.islower()):
                        diff = 97-temp
                        temp=122-diff
                    elif((temp<65) & i.isupper()):
                        diff=65-temp
                        temp=90-diff
                    new_d.append(chr(temp))
                    j+=1
            s=""
            print("decrypted",s.join(new_d))
    if(n==3):
            break
         
