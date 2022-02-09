sent=str(input("\n\nWrite Something :").lower())
say={}
lst=[]
lsttek=[]
lstson=()
son=[]
alp=('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','ğ','ü','ç','ö','ş','ı')
lst=[letter for letter in sent.lower()]
for i in lst:
    if i in alp:
        lsttek.append(i)
lsttek=set(lsttek[: ])      
for j in (sorted (lsttek)):
    say=lst.count(j)
    lstson=(j,say)
    son.append(lstson)
print("\n",son,"\n")