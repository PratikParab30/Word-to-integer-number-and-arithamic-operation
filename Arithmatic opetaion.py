import WrdNumCnv as wnc
import re

aa="fifty six thousand plus thirty"  #here you can set your varible and operatore
ad=[]
b=r"((plus)|(minus)|(divid)|(multiply))"

a=re.search(b,aa)
nd=0
if a:
    if re.search(r"plus",aa):
        af=aa.split("plus")
        for i in af:
            nd=nd+wnc.wrd_int(i)
else:
    nd=wnc.wrd_int(aa)        
print(f'answer is : {nd}')
            
        