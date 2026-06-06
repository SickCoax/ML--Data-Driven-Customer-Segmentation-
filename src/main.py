import pandas as pd
from train import get_cluster
from evaluate import get_score
import os
import sys

csv_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "dataset",
    "Online Retail.csv"
)

df = pd.read_csv(csv_path)

model , X = get_cluster(df) 

score = get_score(model , X)

print(f"Score : {score}")