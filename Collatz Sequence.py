def collatz(number):
    while number != 1:
        if number%2 == 0:
            number = number//2
            print(str(number))
        else:
            number = 3*number + 1
            print(str(number))
    input('Press any key to exit')

print('The Collatz Sequence is defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1.')
print()
print('The sequence is that no matter what value of n, the sequence will always reach 1')
print()
print()
while True:
    while True:
        print('Enter a positive number to perform the Collatz Sequence.')
        print('(No fraction, decimals, zero or negative number)')
        number = input()
        try:
            number = int(number)
            if number <= 0:
                break
            collatz(number)
            number = 1
            break
        except ValueError:
            print()
            print('Please read the instructions.')
    if number == 1:
        break
    print()
    print('Please read the instructions.')
