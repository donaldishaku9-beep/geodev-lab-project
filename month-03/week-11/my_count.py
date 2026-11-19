import geopandas as gpd
from shapely.geometry import box


def load(path):
    layers = gpd.list_layers(path)
    return gpd.read_file(path, layer=layers["name"].iloc[0])


ward = load("processed/study_area_32632.gpkg").to_crs(epsg=32632)
schools = load("processed/schools_32632.gpkg").to_crs(epsg=32632)

size = 1000
minx, miny, maxx, maxy = ward.total_bounds
cells = []
x = minx
while x < maxx:
    y = miny
    while y < maxy:
        cells.append(box(x, y, x + size, y + size))
        y += size
    x += size

grid = gpd.GeoDataFrame(geometry=cells, crs=ward.crs)
grid = grid[grid.intersects(ward.union_all())].reset_index(drop=True)
grid["cell_id"] = grid.index
print("Grid cells touching the ward:", len(grid))

joined = gpd.sjoin(
    schools, grid[["cell_id", "geometry"]], how="inner", predicate="within"
)
counts = joined.groupby("cell_id").size().rename("school_count").reset_index()
grid = grid.merge(counts, on="cell_id", how="left")
grid["school_count"] = grid["school_count"].fillna(0).astype(int)

print("Cells with no school:", (grid["school_count"] == 0).sum())
print(grid.sort_values("school_count", ascending=False).head(3)[["cell_id", "school_count"]])
print("Total counted:", grid["school_count"].sum(), "of", len(schools))

grid.to_file("data/processed/school_grid_counts.gpkg", layer="school_grid", driver="GPKG")
print("Saved data/processed/school_grid_counts.gpkg")