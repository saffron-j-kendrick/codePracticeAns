import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores.sort_values(by="score", ascending=False, inplace=True)
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    
    return scores[["score", "rank"]]


if __name__ == "__main__":
    scores = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "score": [3, 2, 1, 4, 5]})

    print(order_scores(scores))