import pandas as pd
import geopandas as gpd

path = "processed/schools_32632.gpkg"
schools = gpd.read_file(path, layer=gpd.list_layers(path)["name"].iloc[0])
table = pd.read_csv(
    "mydata.csv",
    encoding="utf-8-sig",
    usecols=["uniq_id", "pop_sum", "pop_mean"],
    dtype={"uniq_id": str},
)

schools["uniq_id"] = schools["uniq_id"].astype(str)
print("Schools:", len(schools), "| Table rows:", len(table))
print("Duplicate keys in table:", table["uniq_id"].duplicated().sum())

first_try = schools.merge(table, on="uniq_id", how="left")
matched = first_try["pop_sum"].notna().sum()
print("Matched on first try:", matched, "of", len(schools))


def clean_key(value):
    return str(value).strip()


schools["join_key"] = schools["uniq_id"].apply(clean_key)
table["join_key"] = table["uniq_id"].apply(clean_key)

joined = schools.merge(
    table[["join_key", "pop_sum", "pop_mean"]], on="join_key", how="left"
)
matched = joined["pop_sum"].notna().sum()
print("Matched after cleaning:", matched, "of", len(schools))
print("Rows after join:", len(joined))
print(joined[["name", "pop_sum", "pop_mean"]].head())