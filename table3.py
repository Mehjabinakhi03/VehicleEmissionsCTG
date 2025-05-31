import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame for total emissions
df_total = pd.DataFrame({
    "Period": ["Morning", "Afternoon", "Total"],
    "CO₂ (kg)": [259.6, 99.65, 359.25],
    "NOₓ (kg)": [2.201, 0.8506, 3.0516],
    "PM (kg)": [0.172, 0.1115, 0.2835]
})

# Reshape data for plotting
df_melted = df_total.melt(id_vars=["Period"], var_name="Pollutant", value_name="Emissions (kg)")

# Plot
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=df_melted, x="Period", y="Emissions (kg)", hue="Pollutant",
                 palette=["#1f77b4", "#ff7f0e", "#2ca02c"])  # Colors for CO₂, NOₓ, PM

# Customize plot
plt.title("Total Emissions Comparison (Morning vs. Afternoon)")
plt.xlabel("Period")
plt.ylabel("Emissions (kg)")
plt.legend(title="Pollutant")

# Add labels on top of bars
for p in ax.patches:
    height = p.get_height()
    if height > 0:
        ax.text(p.get_x() + p.get_width() / 2., height + 0.01, f'{height:.2f}', 
                ha='center', fontsize=9, fontweight='bold')

# Show plot
plt.show()
