from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
datafreym = pd.read_csv(BASE / "tokopedia_products_with_review.csv")
print(datafreym.shape)
print(datafreym.columns.tolist())
df = datafreym.copy()
columns = ["discounted_price", "review_rating"]
df = df[columns].copy()

df[["discounted_price", "review_rating"]].info()      # sesuaikan nama kolom lu
df[["discounted_price", "review_rating"]].isna().mean()
df["review_rating"].value_counts().sort_index()
df["discounted_price"].describe()



