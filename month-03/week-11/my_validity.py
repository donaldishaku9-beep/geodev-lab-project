import geopandas as gpd


def load(path):
    layers = gpd.list_layers(path)
    return gpd.read_file(path, layer=layers["name"].iloc[0])


for name, path in [
    ("ward", "processed/study_area_32632.gpkg"),
    ("grid", "data/processed/school_grid_counts.gpkg"),
    ("uncovered", "data/processed/uncovered_week11.gpkg"),
]:
    layer = load(path)
    before = (~layer.is_valid).sum()
    layer["geometry"] = layer.make_valid()
    after = (~layer.is_valid).sum()
    print(name, "| rows:", len(layer), "| invalid before:", before, "| after:", after)