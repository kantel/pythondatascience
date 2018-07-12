import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

baby_name = ["Alice", "Charles", "Diana", "Edward"]
number_birth = [96, 155, 66, 272]
dataset = list(zip(baby_name, number_birth))

df = pd.DataFrame(data = dataset, columns = ["Name", "Anzahl"])
df["Anzahl"].plot()
plt.show()