import pandas as pd


RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def clean_books(df):

    df = df.copy()

    # Price

    df["price_gbp"] = pd.to_numeric(
    df["price"]
    .astype(str)
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip(),
    errors="coerce"
    )


# Median imputation for invalid/missing prices 
    if df["price_gbp"].isna().any(): 
        df["price_gbp"] = df["price_gbp"].fillna( 
            df["price_gbp"].median() 
        )

    
    # Rating
    df["rating"] = (
        df["star_rating"]
        .astype(str)
        .str.strip()
        .map(RATING_MAP)
    )

    # Median imputation for invalid/missing ratings 
    if df["rating"].isna().any(): 
        df["rating"] = df["rating"].fillna( 
            df["rating"].median() 
            ).round().astype(int)

    # Availability
    df["in_stock"] = (
        df["availability"]
        .astype(str)
        .str.contains(
            "In stock",
            case=False,
            na=False
        )
    )

    # Fixed project exchange rate
    df["price_inr"] = (
        df["price_gbp"] * 105.50
    )

    return df