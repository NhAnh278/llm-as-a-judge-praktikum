import json
from pathlib import Path

import pandas as pd
from scipy.stats import pearsonr, spearmanr


def load_json(path):
    """
    Load a JSON file.
    """
    path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_data(path):
    """
    Load ratings from one LLM judge model/human ratings.

    This function can be adjusted later depending on the exact file structure.
    """
    data = load_json(path)
    return pd.DataFrame(data)


def merge_ratings(human_df, model_df, on_columns):
    """
    Merge human ratings and model ratings.

    Example:
    on_columns = ["doc_id", "language"]
    """
    return pd.merge(human_df, model_df, on=on_columns, how="inner")


def compute_correlations(df, human_col, model_col):
    """
    Compute Pearson, Spearman, and Kendall correlations
    between human ratings and model ratings.
    """
    clean_df = df[[human_col, model_col]].dropna()

    pearson_corr, pearson_p = pearsonr(clean_df[human_col], clean_df[model_col])
    spearman_corr, spearman_p = spearmanr(clean_df[human_col], clean_df[model_col])

    return {
        "pearson": pearson_corr,
        "pearson_p": pearson_p,
        "spearman": spearman_corr,
        "spearman_p": spearman_p,
    }


def save_dataframe(df, path):
    """
    Save a DataFrame as CSV.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)