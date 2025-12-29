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




