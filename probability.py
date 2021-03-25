import numpy as np
import matplotlib.pyplot as pyplot

apple = 500
orange = 500

apple_weight = 150 + 50 * np.random.randn(apple)
orange_weight = 130 + 50 * np.random.randn(orange)

pyplot.hist([apple_weight, orange_weight], stacked=True, color=['r', 'b'])
pyplot.show()
