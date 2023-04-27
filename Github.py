#Weight connversion from kg to lbs
weight=(input("Enter weight: "))
if weight.isnumeric():
    value=input("(K)g or (L)bs: ")
    if value.upper()=="K":
        converted=(float(weight)*2.20)
        print("Weight in lbs: ",converted)
    elif value.upper()=="L":
        converted=(float(weight)/2.20)
        print("Weight in kg: ",converted)
    else:
        print("Invalid value")
else:
    print("Number only allowed")