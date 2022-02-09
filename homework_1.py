n=int(input("\n\nFind lucky numbers between 1 and ? : "))
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
range(n)
list_1=(list(range(n+1)))
del list_1[0]
list_2=list_1
print(list_1)
del list_2[1:n+1:2]
print(list_2)
list_3=list_2
del list_3[2:n+1:3]
print(list_3)
list_4=list_3
del list_4[3:n+1:4]
print(list_4)
list_5=list_4
del list_5[4:n+1:5]
print("\n\nLUCKY NUMBERS ARE : ",list_5,"\n\n")