n = int(input())

if n % 2 != 0:
    # All odd numbers are weird
    print("Weird")
else:
    # Even numbers: check ranges
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
          # n > 20 or n < 2
        print("Not Weird")
