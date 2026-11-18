import geopandas as gpd

path = "processed/schools_32632.gpkg"
layers = gpd.list_layers(path)
print(layers)

layer = gpd.read_file(path, layer=layers["name"].iloc[0])

print(layer.head())
print("Rows and columns:", layer.shape)
print(layer.geom_type.value_counts())
print("CRS:", layer.crs)
print("Bounds:", layer.total_bounds)