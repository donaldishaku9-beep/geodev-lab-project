import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

table = pd.read_csv("data/raw/schools_xy.csv", encoding="utf-8-sig")
print(table[["X", "Y"]].head(3))

schools = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["X"], table["Y"]),
    crs="EPSG:32632",
)
print(schools.crs)
schools.to_file("data/processed/my_schools_points.gpkg", layer="schools_points")
print("Saved", len(schools), "schools")

area_path = "processed/study_area_32632.gpkg"
area = gpd.read_file(area_path, layer=gpd.list_layers(area_path)["name"].iloc[0])

fig, ax = plt.subplots(figsize=(7, 8))
area.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
schools.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("My schools over the study area")
ax.set_axis_off()

fig.savefig("month-03/week-10/my_points_check.png", dpi=150, bbox_inches="tight")
print("Check map saved")