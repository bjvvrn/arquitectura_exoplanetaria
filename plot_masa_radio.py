import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cat_limpio.csv",header=None, names=["name", "metod", "periodo", "radio", "masa"])

R = df["radio"]
M = df["masa"]

rho_e = 5.51

rho = 5.51 * M/R**3 * rho_e

plt.plot( R, M,  ".r")

plt.xlabel("radius")
plt.ylabel("mass")

plt.savefig("masa_radio.png")
plt.show()
