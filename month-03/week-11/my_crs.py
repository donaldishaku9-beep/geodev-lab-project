import geopandas as gpd


def load(path):
    layers = gpd.list_layers(path)
    return gpd.read_file(path, layer=layers["name"].iloc[0])


ward = load("processed/study_area_32632.gpkg")
schools = load("processed/schools_32632.gpkg")
highway = load("processed/Highway_Tudun_Wada_South.gpkg")

for name, layer in [("ward", ward), ("schools", schools), ("highway", highway)]:
    print(name, "| rows:", len(layer), "| type:", layer.geom_type.iloc[0], "| CRS:", layer.crs)

print("Suggested UTM:", ward.estimate_utm_crs())

ward = ward.to_crs(epsg=32632)
schools = schools.to_crs(epsg=32632)
highway = highway.to_crs(epsg=32632)

print("Ward area:", round(ward.area.sum() / 1_000_000, 2), "km2")
print("Highway length:", round(highway.length.sum() / 1000, 2), "km")