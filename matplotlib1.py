import matplotlib.pyplot as plt
import matplotlib.style as style

x = [1, 2, 3, 4, 5, 6]
y = [7, 5, 6, 7, 8, 9]

x2 = [1, 2, 3, 4, 5, 6]
y2 = [3, 6, 5, 7, 8, 6]

len(x)

style.use('dark_background')
plt.plot(x, y, label='Line One')
plt.plot(x2, y2, label='Line Two')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Chart')

plt.legend()
plt.show()
