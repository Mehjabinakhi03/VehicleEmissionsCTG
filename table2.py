from matplotlib.gridspec import GridSpec
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create emissions data for Morning and Afternoon
data_morning = {
    "Vehicle Type": ["Bike", "CNG", "Car", "Rickshaw", "Truck", "Bus"],
    "CO₂ (kg)": [40.00, 57.00, 28.60, 5.00, 45.00, 84.00],
    "NOₓ (kg)": [0.20, 0.456, 0.2145, 0.04, 0.45, 0.84],
    "PM (kg)": [0.02, 0.038, 0.0286, 0.006, 0.045, 0.084],
    "Time of Day": "Morning",
}

data_afternoon = {
    "Vehicle Type": ["Bike", "CNG", "Car", "Rickshaw", "Truck", "Bus"],
    "CO₂ (kg)": [12.00, 25.20, 5.60, 6.25, 30.00, 45.60],
    "NOₓ (kg)": [0.06, 0.2016, 0.042, 0.05, 0.30, 0.456],
    "PM (kg)": [0.006, 0.0168, 0.0056, 0.0075, 0.03, 0.0456],
    "Time of Day": "Afternoon",
}

df_morning = pd.DataFrame(data_morning)
df_afternoon = pd.DataFrame(data_afternoon)

df = pd.concat([df_morning, df_afternoon])


df_total = pd.DataFrame(
    {
        "Period": ["Morning", "Afternoon", "Total"],
        "CO₂ (kg)": [259.6, 99.65, 359.25],
        "NOₓ (kg)": [2.201, 0.8506, 3.0516],
        "PM (kg)": [0.172, 0.1115, 0.2835],
    }
)

# Reshape data for plotting
df_melted = df_total.melt(
    id_vars=["Period"], var_name="Pollutant", value_name="Emissions (kg)"
)


pollutants = ["CO₂ (kg)", "NOₓ (kg)", "PM (kg)"]
fig = plt.figure(figsize=(15, 10))
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
sns.barplot(
    data=df,
    x="Vehicle Type",
    y="CO₂ (kg)",
    hue="Time of Day",
    errorbar=None,
    ax=ax1,
    palette="Set2",
)
ax1.set_title("CO₂ Emissions by Vehicle Type", fontsize=14)
ax1.set_xlabel("Vehicle Type", fontsize=12)
ax1.set_ylabel("Emissions (kg)", fontsize=12)
for p in ax1.patches:
    height = p.get_height()
    if height > 0:
        ax1.text(
            p.get_x() + p.get_width() / 2.0,
            height + 0.5,
            f"{int(height)}",
            ha="center",
            fontsize=12,
        )

ax2 = fig.add_subplot(gs[0, 1])
max_y = df["NOₓ (kg)"].max()
ax2.set_ylim(0, max_y * 1.15)
sns.barplot(
    data=df,
    x="Vehicle Type",
    y="NOₓ (kg)",
    hue="Time of Day",
    errorbar=None,
    ax=ax2,
    palette="Set2",
)
ax2.set_title("NOₓ Emissions by Vehicle Type", fontsize=14)
ax2.set_xlabel("Vehicle Type", fontsize=12)
ax2.set_ylabel("Emissions (kg)", fontsize=12)
for p in ax2.patches:
    height = p.get_height()
    if height > 0:
        ax2.text(
            p.get_x() + p.get_width() / 2.0,
            height + 0.001,
            f"{height:.3f}",
            ha="center",
            va="bottom",
            fontsize=12,
            rotation=40,
        )

ax3 = fig.add_subplot(gs[1, 0])
max_y = df["PM (kg)"].max()
ax3.set_ylim(0, max_y * 1.15)
sns.barplot(
    data=df,
    x="Vehicle Type",
    y="PM (kg)",
    hue="Time of Day",
    errorbar=None,
    ax=ax3,
    palette="Set2",
)
ax3.set_title("PM Emissions by Vehicle Type", fontsize=14)
ax3.set_xlabel("Vehicle Type", fontsize=12)
ax3.set_ylabel("Emissions (kg)", fontsize=12)
for p in ax3.patches:
    height = p.get_height()
    if height > 0:
        ax3.text(
            p.get_x() + p.get_width() / 2.0,
            height + 0.001,
            f"{height:.3f}",
            ha="center",
            va="bottom",
            fontsize=12,
            rotation=40,
        )

ax4 = fig.add_subplot(gs[1, 1])
max_y = df_melted["Emissions (kg)"].max()
ax4.set_ylim(0, max_y * 1.15)

sns.barplot(
    data=df_melted,
    x="Period",
    y="Emissions (kg)",
    hue="Pollutant",
    palette="Set2",
    ax=ax4,
)
ax4.set_title("Total Emissions Summary", fontsize=14)
ax4.set_xlabel("Period", fontsize=12)
ax4.set_ylabel("Emissions (kg)", fontsize=12)
ax4.legend(title="Pollutant")
for p in ax4.patches:
    height = p.get_height()
    if height > 0:
        ax4.text(
            p.get_x() + p.get_width() / 2.0,
            height + 0.2,
            f"{height:.2f}",
            ha="center",
            fontsize=12,
            rotation=45,
        )


plt.tight_layout() 
plt.savefig(
    "emissions_summary.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()  