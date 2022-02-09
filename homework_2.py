n=int(input("\n\nMake a list from 1 to 'x'\n\nPlease Enter 'x' : "))
r=int(input("\nHow many digits do you want to shift?\nEnter positive value to shift --->\nEnter negative value to shift <---\n:"))
lst=(list(range(1, n+1)))
if abs(r)<=len(lst):
    a=lst[-r:]+lst[:-r]
    del lst[-r:]
    print(a)      
else:
    print("Shifting value can not be bigger than the lenght of list !")       