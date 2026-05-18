import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = products.melt(
    id_vars=["product_id"],              # keep this column
    value_vars=["store1", "store2", "store3"],  # turn these columns into rows
    var_name="store",                    # old column name
    value_name="price"                   # old value
)

    return result.dropna(subset=["price"])