import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # answer = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]

    #df.loc[rows, columns]

    # return answer[["name", "area", "population"]]
    return world.loc[(world['area']>=3000000) | (world["population"]>= 25000000), ["name", "area", "population"]]