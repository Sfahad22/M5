# Shaik Fahad
# Oct 22, 2024

# This program works on the integers form 1 to 51

for num in range (1,51):
    if num %3 == 0 and num %5 ==0:
        print("Divisible by both")
    elif num %3 == 0:
        print("Divisible by three")
    elif num % 5 == 0:
        print("Divisble by five")
    else:
        print(num)