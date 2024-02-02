print("ceasar cipher")

a=input("enter the text to encrpyt")
k=int(input("enter the key for shift"))
l = list(a)
while(1==1):
    n = int(input("enter the options 1: encrypt 2:decrypt 3;exit"))
    if(n == 1):
            j=0
            for i in l:
              temp = ord(i)
              temp+=k
              if((temp>=122) & i.islower()):
                  temp=96+k
              elif((temp>=90 )& i.isupper()):
                  temp=64+k
              l[j] =chr(temp)
              j+=1
            s=""
            print("encrytped",s.join(l))
    if(n ==2):
            j=0
            for i in l:
              temp = ord(i)
              temp-=k
              if((temp<97) & i.islower()):
                  diff = 97-temp
                  temp=122-diff
              elif((temp<65) & i.isupper()):
                  diff=65-temp
                  temp=90-diff
              l[j] =chr(temp)
              j+=1
            s=""
            print("decrypted",s.join(l))
    if(n==3):
            break
            
    

