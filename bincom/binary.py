""" 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10. """

from random import randint

binary = ''.join([str(randint(0, 1)) for i in range(4)])
decimal = int(binary, 2)
print(f"\n8. Random binary: {binary}")
print(f"   Base 10: {decimal}")
