a=[]
a0=["zero",0][::-1]
a1=["one",1][::-1]
a2=["two",2][::-1]
a3=["three",3][::-1]
a4=["four",4][::-1]
a5=["five",5][::-1]
a6=["six",6][::-1]
a7=["seven",7][::-1]
a8=["eight",8][::-1]
a9=["nine",9][::-1]
a10=["ten",10][::-1]
a11=["eleven",11][::-1]
a12=["twelve",12][::-1]
a13=["thirteen",13][::-1]
a14=["fourteen",14][::-1]
a15=["fifteen",15][::-1]
a16=["sixteen",16][::-1]
a17=["seventeen",17][::-1]
a18=["eightteen",18][::-1]
a19=["nineteen",19][::-1]
a20=["twenty",20][::-1]
a21=["thirty",30][::-1]
a22=["forty",40][::-1]
a23=["fifty",50][::-1]
a24=["sixty",60][::-1]
a25=["seventy",70][::-1]
a26=["eighty",80][::-1]
a27=["ninety",90][::-1]
a28=["tenty",100][::-1]

b=[]
b1=[100,"hundred"]
b2=[1000,"thousand"]
b3=[100000,"hundred thousand"]
b4=[100000,"lakh"]
b5=[1000000,"million"]
b6=[10000000,"crore"]
b7=[1000000000,"billion"]
b8=[1000000000000,"trillion"]


for i in range(1,9):
    b.append(eval(f"b{i}"))

for i in range(0,29):
    a.append(eval(f"a{i}"))
  
def wrd_int(c):
    bm=c.split(" ")
    
    
    stm=""
    
    for ii in bm:
        for aa in range(0,len(a)):
            if ii in a[aa]:
                    if str(stm).isdigit():
                        stm=int(stm)+a[aa][0]
                        stm=str(stm)
                        break
                    else:
                        stm=stm+str(a[aa][0])
                        break
    
       
    
        for bb in range(0,len(b)):  
            if ii in b[bb]:
                if str(stm).isdigit():
                    stm=int(stm)*b[bb][0]
                    break
                else:
                    if str(stm).isdigit():
                        stm=int(stm)*b[bb][0]
                        break
                    else:
                        stm=stm+str(b[bb][0])
                        break
    return int(stm)
                    
print(wrd_int("fifty eight hundred fifty six"))