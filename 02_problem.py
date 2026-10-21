def f_to_c(f):
    return 5*(f-32)/9


f = int(input("Enter the temperature in Fahrenheit: "))
print(f_to_c(f))
print (f"{f_to_c(f)} degree celsius")