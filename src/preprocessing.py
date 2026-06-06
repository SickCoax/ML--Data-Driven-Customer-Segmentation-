import pandas as pd
from sklearn.preprocessing import StandardScaler


def process_X(df) :
    
    df = df.drop(["Description"] , axis= 1)
    df = df.dropna(subset=["CustomerID"])

    df = df[df["Quantity"] > 0]

    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]


    df = df.drop(["InvoiceDate" , "UnitPrice" , "Country"] , axis=1) 

    df = df.groupby("CustomerID").agg({
        "TotalPrice" : ["max" , "sum"] ,
        "Quantity" : "sum" ,
        "StockCode" : "nunique",
        "InvoiceNo" : "nunique"
    })

    df = df.reset_index()
    df.columns = ['_'.join(col).strip('_') for col in df.columns]

    df = df.rename(columns={    
        "InvoiceNo_nunique" : "Frequency",
        "StockCode_nunique" : "Distinct_Product"
    })

    df["Avg_Product_Price"] = df["TotalPrice_sum"] / df["Quantity_sum"]

    X = df.drop(["CustomerID"] , axis=1)

    scaler = StandardScaler()

    X_arr= scaler.fit_transform(X)
    
    X = pd.DataFrame(X_arr , columns= X.columns)

    return X
