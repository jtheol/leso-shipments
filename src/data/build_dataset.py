import os
import re
import string

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from nltk.corpus import stopwords

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
shipments

cancellations.info()
cancellations[["Quantity", "Acquisition Value"]].describe()
cancellations.isnull().sum()
cancellations.dropna(axis=0, how="any", inplace=True)
cancellations.reset_index(drop=True)


# ――――――――――――――――――――――――――――――――――――――――――――――
# CLEANING JUSTIFICATIONS AND REASONS CANCELLED
# ――――――――――――――――――――――――――――――――――――――――――――――
def clean_text(text: pd.Series) -> pd.Series:
    """Used to clean text for both shipment justifications and cancellations.

    Args:
        text (pd.Series): Column from dataframe containing text to be cleaned.

    Returns:
        pd.Series: Resulting column after text has been cleaned.
    """

    text = text.str.lower()
    text = text.str.translate(str.maketrans("", "", string.punctuation))

    # Cleaning stop words
    stop_words = set(stopwords.words("english"))
    text = text.apply(
        lambda x: " ".join(w for w in x.split(" ") if w not in stop_words)
    )

    # Removing numbers
    text = text.str.replace(r"\d+", "", regex=True)

    text = text.str.replace("\n", "")

    return text


# Shipments Justifications (shipments)
shipments["cleaned_justification"] = clean_text(shipments["Justification"])

# Reasons Cancelled (cancellations)
cancellations["cleaned_justification"] = clean_text(cancellations["Justification"])
cancellations["cleaned_reason_cancelled"] = clean_text(
    cancellations["Reason Cancelled"]
)

shipments.to_csv("../../data/processed/proc-shipments.csv", index=False)
cancellations.to_csv("../../data/processed/proc-cancellations.csv", index=False)
