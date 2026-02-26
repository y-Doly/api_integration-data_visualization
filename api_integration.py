import requests
import matplotlib.pyplot as plt

url = "https://disease.sh/v3/covid-19/historical/India?lastdays=30"
data = requests.get(url).json()

cases = list(data["timeline"]["cases"].values())

plt.plot(cases)
plt.title("COVID Cases in India - Last 30 Days")
plt.show()
