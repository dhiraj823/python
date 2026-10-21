def inch_to_cms(inches):
    return inches * 2.54

n = int(input("Enter the number of inches: "))    

print(f"the corresponding number of centimeters is: {inch_to_cms(n)}")
