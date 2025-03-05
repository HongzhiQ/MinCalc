import pandas as pd
import numpy as np


file_path = "all_data.xlsx"
data = pd.read_excel(file_path)


data = data.applymap(lambda x: str(x).replace("\n", " ") if isinstance(x, str) else x)



def split_data(df, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    np.random.seed(42)
    shuffled_indices = np.random.permutation(len(df))

    train_size = int(len(df) * train_ratio)
    val_size = int(len(df) * val_ratio)

    train_indices = shuffled_indices[:train_size]
    val_indices = shuffled_indices[train_size:train_size + val_size]
    test_indices = shuffled_indices[train_size + val_size:]

    train_set = df.iloc[train_indices]
    val_set = df.iloc[val_indices]
    test_set = df.iloc[test_indices]

    return train_set, val_set, test_set


train_data, val_data, test_data = split_data(data)


train_data.to_csv("train_data.tsv", sep="\t", index=False)
val_data.to_csv("val_data.tsv", sep="\t", index=False)
test_data.to_csv("test_data.tsv", sep="\t", index=False)

print("success！")
