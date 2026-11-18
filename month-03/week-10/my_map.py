import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

schools_path = "processed/schools_32632.gpkg"
ward_path = "processed/study_area_32632.gpkg"

schools = gpd.read_file(schools_path, layer=gpd.list_layers(schools_path)["name"].iloc[0])
ward = gpd.read_file(ward_path, layer=gpd.list_layers(ward_path)["name"].iloc[0])

table = pd.read_csv(
    "mydata.csv",
    encoding="utf-8-sig",
    usecols=["uniq_id", "pop_sum"],
    dtype={"uniq_id": str},
)
schools["uniq_id"] = schools["uniq_id"].astype(str)
schools = schools.merge(table, on="uniq_id", how="left")
print("Schools with population:", schools["pop_sum"].notna().sum(), "of", len(schools))
print("CRS match:", schools.crs == ward.crs)

fig, ax = plt.subplots(figsize=(8, 8))
ward.plot(ax=ax, color="#f2f2f2", edgecolor="black", linewidth=1)
schools.plot(
    ax=ax,
    column="pop_sum",
    cmap="viridis",
    markersize=45,
    edgecolor="white",
    linewidth=0.5,
    legend=True,
    legend_kwds={"label": "Population within 1.5 km (WorldPop)", "shrink": 0.7},
)
ax.set_title("Schools in Tudun Wada South ward, Minna")
ax.set_xlabel("Easting (m, EPSG:32632)")
ax.set_ylabel("Northing (m, EPSG:32632)")
plt.tight_layout()
plt.savefig("month-03/week-10/my_map.png", dpi=150)
print("Map saved: month-03/week-10/my_map.png")