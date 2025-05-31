from matplotlib.gridspec import GridSpec
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


north_dir = {
    "Time of Day": [
        "Morning",
        "Morning",
        "Morning",
        "Afternoon",
        "Afternoon",
        "Afternoon",
    ],
    "Lane Type": ["U-Turn", "Right", "Left", "U-Turn", "Right", "Left"],
    "Bike": [160, 0, 120, 0, 0, 25],
    "CNG": [0, 0, 120, 0, 0, 10],
    "Car": [0, 0, 40, 0, 0, 10],
    "Bus": [0, 0, 20, 0, 0, 25],
    # "Total Vehicles": [160, 0, 300, 0, 0, 70],
}

north_dir_df = pd.DataFrame(north_dir)

north_dir_df_melted = north_dir_df.melt(
    id_vars=["Time of Day", "Lane Type"], var_name="Vehicle Type", value_name="Count"
)


east_dir_data = {
    "Time of Day": ["Morning", "Morning", "Afternoon", "Afternoon"],
    "Lane Type": ["Right", "Through", "Right", "Through"],
    "Bike": [120, 80, 30, 90],
    "CNG": [100, 120, 85, 18],
    "Car": [40, 0, 5, 0],
    "Rickshaw": [0, 0, 10, 5],
    "Cycle": [0, 0, 0, 15],
    "Truck": [0, 0, 0, 20],
    "Bus": [0, 20, 4, 0],
    # "Total Vehicles": [260, 220, 134, 148],
}


east_dir_df = pd.DataFrame(east_dir_data)

east_dir_df_melted = east_dir_df.melt(
    id_vars=["Time of Day", "Lane Type"], var_name="Vehicle Type", value_name="Count"
)


west_dir_data = {
    "Time of Day": ["Morning", "Morning", "Afternoon", "Afternoon"],
    "Lane Type": ["Left", "Through", "Left", "Through"],
    "Bike": [200, 140, 35, 200],
    "CNG": [140, 120, 35, 20],
    "Car": [0, 40, 3, 0],
    "Rickshaw": [0, 0, 0, 5],
    "Cycle": [20, 20, 5, 0],
    "Truck": [40, 40, 5, 0],
    "Bus": [80, 100, 75, 10],
    # "Total Vehicles": [480, 460, 158, 235]
}

west_dir_df = pd.DataFrame(west_dir_data)

west_dir_df_melted = west_dir_df.melt(
    id_vars=["Time of Day", "Lane Type"], var_name="Vehicle Type", value_name="Count"
)


## -------------------- Plotting -------------------- ##


def add_value_labels(ax):
    """Function to add labels on top of bars, excluding zeros."""
    for p in ax.patches:
        height = p.get_height()
        if height > 0:  # Only annotate non-zero bars
            ax.annotate(
                f"{int(height)}",  # Convert height to integer
                (p.get_x() + p.get_width() / 2, height),  # Position on top of the bar
                ha="center",  # Center alignment
                va="bottom",  # Bottom alignment
                fontsize=12,
                color="black",
            )


fig = plt.figure(figsize=(15, 5))
gs = GridSpec(1, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
sns.barplot(
    data=north_dir_df_melted,
    x="Time of Day",
    y="Count",
    hue="Vehicle Type",
    ax=ax1,
    palette="Set2",
    errorbar=None,
)
ax1.set_title("Northbound Traffic (to the Kaptai Road)", fontsize=14)
ax1.set_xlabel("Time of Day", fontsize=12)
ax1.set_ylabel("Vehicle Count", fontsize=12)
add_value_labels(ax1)
# ax1.grid(axis="y", linestyle="--", alpha=0.7)

ax2 = fig.add_subplot(gs[0, 1])
sns.barplot(
    data=east_dir_df_melted,
    x="Time of Day",
    y="Count",
    hue="Vehicle Type",
    ax=ax2,
    palette="Set2",
    errorbar=None,
)
ax2.set_title("Eastbound Traffic (to the Kalurghat)", fontsize=14)
ax2.set_xlabel("Time of Day", fontsize=12)
ax2.set_ylabel("Vehicle Count", fontsize=12)
add_value_labels(ax2)
# ax2.grid(axis="y", linestyle="--", alpha=0.7)

ax3 = fig.add_subplot(gs[0, 2])
sns.barplot(
    data=west_dir_df_melted,
    x="Time of Day",
    y="Count",
    hue="Vehicle Type",
    ax=ax3,
    palette="Set2",
    errorbar=None,
)
ax3.set_title("Westbound Traffic (to the Chandgaon)", fontsize=14)
ax3.set_xlabel("Time of Day", fontsize=12)
ax3.set_ylabel("Vehicle Count", fontsize=12)
add_value_labels(ax3)
# ax3.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("traffic_table1.png", dpi=300, bbox_inches="tight")
plt.show()
