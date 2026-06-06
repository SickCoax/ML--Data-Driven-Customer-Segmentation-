from sklearn.cluster import KMeans
from preprocessing import process_X

def get_cluster(df) :

    X = process_X(df)

    k = 4   # Found the optimal value of "k" at K_Optimization notebook

    model = KMeans(
        n_clusters = k ,
        n_init = 10 ,
        random_state = 42
    )

    model.fit(X)

    return model , X