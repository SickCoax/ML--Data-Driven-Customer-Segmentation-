import pandas as pd
from train import get_cluster
from evaluate import get_score

df = pd.read_csv(r"C:\Users\sailj\OneDrive\文档\GitHub\Data-Driven Customer Segmentation\dataset\Online Retail.csv")

model , X = get_cluster(df) 

score = get_score(model , X)

print(f"Score : {score}")