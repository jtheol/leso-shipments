import os
import re

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

pd.options.display.float_format = "{:2f}".format

shipments = pd.read_excel(
    "../../data/raw/q3fy23-ShipmentsCancellations.xlsx", sheet_name="SHIPMENTS"
)

cancellations = pd.read_excel(
    "../../data/raw/q3fy23-ShipmentsCancellations.xlsx", sheet_name="CANCELLATIONS"
)

shipments.info()
shipments[["Quantity", "Acquisition Value"]].describe()
shipments.isnull().sum()

cancellations.info()
cancellations[["Quantity", "Acquisition Value"]].describe()
cancellations.isnull().sum()
cancellations.dropna(axis=0, how="any", inplace=True)
cancellations.reset_index(drop=True)


shipments.to_csv("../../data/processed/proc-shipments.csv", index=False)
cancellations.to_csv("../../data/processed/proc-cancellations.csv", index=False)
