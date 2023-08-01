#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))
print(fruit)
y4 = fruit[0:1, :][0]
y3 = fruit[1:2, :][0]
y2 = fruit[2:3, :][0]
y1 = fruit[3:4, :][0]
people = ['Farrah', 'Fred', 'Felicia']
plt.bar(people, y4, 0.5, color='red')
plt.bar(people, y3, 0.5, bottom=y4, color='yellow')
plt.bar(people, y2, 0.5, bottom=y4+y3, color='#ff8000')
plt.bar(people, y1, 0.5, bottom=y4+y3+y2, color='#ffe5b4')
plt.title('Number of Fruit per Person')
plt.legend(['apples', 'bananas', 'oranges', 'peaches'])
plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.show()
