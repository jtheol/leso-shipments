import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")


shipments = pd.read_csv("../../data/processed/proc-shipments.csv")

cancellations = pd.read_csv("../../data/processed/proc-cancellations.csv")

# ――――――――――――――――――――――
# VISUALIZING SHIPMENTS
# ――――――――――――――――――――――
# Shipments by State
pal_blue_reversed_ship = sns.color_palette(
    "Blues", n_colors=len(shipments["State"].unique())
)
pal_blue_reversed_ship.reverse()
sns.barplot(
    x=shipments["State"].value_counts().values,
    y=shipments["State"].value_counts().index,
    palette=pal_blue_reversed_ship,
)
plt.title("Number of Shipments by State")
plt.savefig("../visualization/figures/shipments-by-state.png")

# Shipments over time
shipments_time = shipments[["Date Shipped", "Acquisition Value"]].sort_values(
    by="Date Shipped"
)
sns.lineplot(
    data=shipments_time,
    x="Date Shipped",
    y="Acquisition Value",
    color="#83ceff",
    markeredgecolor="black",
    markeredgewidth=1,
    marker="o",
    markersize=6,
    linewidth=2,
)
plt.xticks(rotation=90)
plt.tick_params(axis="x", which="major", labelsize=5)
plt.title("Acquisition Value April - June 2023")
plt.tight_layout()
plt.show()

# ――――――――――――――――――――――――――
# VISUALIZING CANCELLATIONS
# ――――――――――――――――――――――――――
