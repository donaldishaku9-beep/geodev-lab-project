import geopandas as gpd
import matplotlib.pyplot as plt


def load(path):
    layers = gpd.list_layers(path)
    return gpd.read_file(path, layer=layers["name"].iloc[0])


ward = load("processed/study_area_32632.gpkg").to_crs(epsg=32632)
schools = load("processed/schools_32632.gpkg").to_crs(epsg=32632)
highway = load("processed/Highway_Tudun_Wada_South.gpkg").to_crs(epsg=32632)

reach = schools[["geometry"]].copy()
reach["geometry"] = reach.buffer(1500)
reach = reach.dissolve()

uncovered = gpd.overlay(ward[["geometry"]], reach, how="difference")
ward_km2 = ward.area.sum() / 1_000_000
uncovered_km2 = uncovered.area.sum() / 1_000_000
print("Ward area:", round(ward_km2, 2), "km2")
print("Uncovered area:", round(uncovered_km2, 2), "km2")
print("Uncovered share:", round(uncovered_km2 / ward_km2 * 100, 1), "%")

uncovered.to_file(
    "data/processed/uncovered_week11.gpkg", layer="uncovered", driver="GPKG"
)

clipped = gpd.clip(highway, ward)
print("Highway length, whole layer:", round(highway.length.sum() / 1000, 2), "km")
print("Highway length inside ward:", round(clipped.length.sum() / 1000, 2), "km")

fig, ax = plt.subplots(figsize=(8, 8))
ward.plot(ax=ax, color="#f2f2f2", edgecolor="black", linewidth=1)
uncovered.plot(ax=ax, color="#d7301f", alpha=0.75)
schools.plot(ax=ax, color="black", markersize=14)
ax.set_title("Red: more than 1.5 km from a school, Tudun Wada South")
ax.set_xlabel("Easting (m, EPSG:32632)")
ax.set_ylabel("Northing (m, EPSG:32632)")
plt.tight_layout()
plt.savefig("month-03/week-11/my_reach_map.png", dpi=150)
print("Map saved: month-03/week-11/my_reach_map.png")