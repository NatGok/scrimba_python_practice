
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used

# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f


num1 = float(input('Enter first number: '))
mode = input('Enter math operation(+,-,*,/): ')
num2 = float(input('Enter second number: '))

if mode == '+':
    print(f'Answer is: {num1 + num2}')
elif mode == '-':
    print(f'Answer is: {num1 - num2}')
elif mode == '*':
    print(f'Answer is: {num1 * num2}')
elif mode == '/':
    print(f'Answer is: {num1 / num2}')
else:
    print('Input error!')