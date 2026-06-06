from sklearn.metrics import silhouette_score

def get_score(model , X) :
    label = model.labels_
    score = silhouette_score(X , label)

    return score