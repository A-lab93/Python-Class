years = int(input("enter number of years:"))
unit = input("""select your choice:
1 - days
2 - weeks 
3 - hours""" ) 

if unit == "1":
    print(years*365) 
elif unit == "2":
    print(years*52) 
elif unit == "3":
    print(years*365*24) 
else:
    print("pick the right choice")         