import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pressure = 1003.5

pre_eruption_data_file = "pre_eruption_data.csv"
imminent_eruption_data_file = "imminent_eruption_data.csv"

pre_eruption_df = pd.read_csv(pre_eruption_data_file)
imminent_eruption_df = pd.read_csv(imminent_eruption_data_file)

def calculate_absolute_humidity(temperature, relative_humidity):
    e = 6.112 * np.exp((17.67 * temperature) / (temperature + 243.5))
    absolute_humidity = (0.622 * e) / (pressure - (0.378 * e))
    return absolute_humidity


pre_eruption_df["Absolute_Humidity"] = calculate_absolute_humidity(pre_eruption_df["Temperature"], pre_eruption_df["Relative_Humidity"])
imminent_eruption_df["Absolute_Humidity"] = calculate_absolute_humidity(imminent_eruption_df["Temperature"], imminent_eruption_df["Relative_Humidity"])
pre_eruption_df["Gas_Increase_Rate"] = (imminent_eruption_df["Gas_Concentration"] - pre_eruption_df["Gas_Concentration"]) / pre_eruption_df["Gas_Concentration"]

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(pre_eruption_df["Gas_Increase_Rate"], label="Gas Increase Rate", color='blue')
plt.title("Gas Increase Rate Over Time")
plt.xlabel("Time")
plt.ylabel("Gas Increase Rate")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(pre_eruption_df["Absolute_Humidity"], label="Absolute Humidity", color='green')
plt.title("Absolute Humidity Over Time")
plt.xlabel("Time")
plt.ylabel("Absolute Humidity")
plt.legend()

plt.tight_layout()
plt.show()
