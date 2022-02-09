a=(input("\n\nEnter First Word : ").lower())
b=(input("\n\nEnter Second Word : ").lower())
c=[]
d=""
e=""
f=""
aa=set(a)
bb=set(b)
c.extend([sorted(aa&bb),sorted(aa-bb),sorted(bb-aa)])
for i in c[0]:
    d=d+i
for j in c[1]:
    e=e+j
for k in c[2]:
    f=f+k
c=[d,e,f]
print("\n",c,"\n")