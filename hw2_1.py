from matplotlib import pyplot as plt

r = 5
b = 50
s_curve_func = lambda r, b, s: (1 - (1 - s**r)**b)
s_list = [i / 10. for i in range(1, 10)]
y_list = map(s_curve_func, [r]*9, [b]*9, s_list)

plt.plot(s_list, y_list)
plt.title('r='+str(r)+',b='+str(b))
plt.show()
