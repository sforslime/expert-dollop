"""
My answers to the technical interview questions based on the data in 'python_class_question.html'.
Ayodele Opadiran
"""

from bs4 import BeautifulSoup
from collections import Counter
import statistics

# Read the HTML file
with open('python_class_question.html', 'r') as file:
    html = file.read()

# Parse and extract colors
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')

colors = []
for row in rows[1:]:  
    cells = row.find_all('td')
    if len(cells) > 1:
        day_colors = cells[1].text.split(',')
        for color in day_colors:
            colors.append(color.strip())

# Fix typos
colors = ['BLUE' if c == 'BLEW' else c for c in colors]
colors = ['ASH' if c == 'ARSH' else c for c in colors]

# Count colors
color_count = Counter(colors)

# 1.  Which color of shirt is the mean color?
mean_color = color_count.most_common(1)[0][0]
print(f"1. Mean color: {mean_color}")

# 2.  Which color is mostly worn throughout the week?
most_worn = color_count.most_common(1)[0]
print(f"2. Most worn color: {most_worn[0]} ({most_worn[1]} times)")

# 3.  Which color is the median?
sorted_colors = sorted(colors)
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index]
print(f"3. Median color: {median_color}")

# 4. Get the variance of the colors
frequencies = list(color_count.values())
variance = statistics.variance(frequencies)
print(f"4. Variance: {variance:.2f}")

# 5. If a colour is chosen at random, what is the probability that the color is red?
total = len(colors)
red_count = color_count['RED']
probability = red_count / total
print(f"5. Probability of RED: {probability:.4f} ({probability*100:.2f}%)")

# 6. Save the colours and their frequencies in postgresql database
# In this case, print out the SQL commands you would need to run to save the data.
print("\n6. PostgreSQL statements:")
print("CREATE TABLE colors (color VARCHAR(20), frequency INT);")
for color, freq in color_count.items():
    print(f"INSERT INTO colors VALUES ('{color}', {freq});")

# 7. write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1
    if numbers[index] == target:
        return index
    return recursive_search(numbers, target, index + 1)

numbers = [5, 12, 7, 23, 45, 8, 19, 34]
user_number = int(input("\n7. Enter a number to search: "))
result = recursive_search(numbers, user_number)
if result != -1:
    print(f"   Found at position {result}")
else:
    print(f"   Not found in list")

# 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
from random import randint

binary = ''.join([str(randint(0, 1)) for i in range(4)])
decimal = int(binary, 2)
print(f"\n8. Random binary: {binary}")
print(f"   Base 10: {decimal}")

# 9. Write a program to sum the first 50 fibonacci sequence.
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for i in range(n):
        total += a
        a, b = b, a + b
    return total

fib_sum = fibonacci_sum(50)
print(f"\n9. Sum of first 50 Fibonacci numbers: {fib_sum}")





