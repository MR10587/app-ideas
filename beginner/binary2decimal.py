binary = int(input("Enter binary number to convert: "))

number_of_digits = len(str(binary))

decimal = 0

i = number_of_digits

for digit in str(binary):
    decimal += int(digit) * 2 ** (i - 1)
    i -= 1
    
print(decimal)