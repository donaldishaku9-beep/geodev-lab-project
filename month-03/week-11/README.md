# Week 11: CRS and spatial operations

## What this folder contains
- [area_wrong_and_right.py](./area_wrong_and_right.py): shows the area in degrees against the area in km2 after reprojecting
- [set_vs_to.py](./set_vs_to.py): shows how set_crs moves data to the wrong place and to_crs does not
- [one_point.py](./one_point.py): transforms one coordinate to UTM with pyproj
- [spatial_ops.py](./spatial_ops.py): buffers facilities and counts them per ward
- [coverage_gap.py](./coverage_gap.py): finds the part of each ward more than 2 km from a facility
- [nearest.py](./nearest.py): measures the distance from each ward centre to the nearest facility
- [clip_dissolve.py](./clip_dissolve.py): clips roads to one ward and dissolves wards into an LGA
- [fix_geometry.py](./fix_geometry.py): finds and repairs an invalid polygon
- [my_crs.py](./my_crs.py): checks the CRS of my ward, schools and highway layers and measures them in metres
- [my_count.py](./my_count.py): counts my 47 schools per 1 km grid cell and saves [school_grid_counts.gpkg](../../data/processed/school_grid_counts.gpkg)
- [my_reach.py](./my_reach.py): finds the part of my ward more than 1.5 km from a school, saves [uncovered_week11.gpkg](../../data/processed/uncovered_week11.gpkg) and draws [my_reach_map.png](./my_reach_map.png)
- [my_validity.py](./my_validity.py): counts invalid geometries before and after make_valid

## How to run it
From the repo root, run for example `uv run month-03/week-11/my_reach.py`.

## What I found
I chose EPSG:32632 because Minna is at about 6.5°E, inside UTM zone 32N, and `estimate_utm_crs()` agreed. My ward and school layers were already in 32632. My highway layer was in EPSG:4326, so I reprojected it with `to_crs` before measuring.

My ward is 15.7 km2. My 47 schools were all counted in a 1 km grid of 27 cells. 16 cells have no school, and 16 schools sit in one cell. With a 1.5 km buffer around every school, 2.09 km2 of the ward is uncovered, which is 13.3%. That matches the 13% I found in Month 1 with QGIS. My highway layer is 191.24 km and all of it is inside the ward. I found 0 invalid geometries in my ward, grid and uncovered layers, so make_valid changed nothing.

I chose 1.5 km because it is the distance I used in Month 1, so the two results can be compared.

## Limitation of my method
A 1.5 km buffer is a straight line, but children walk on roads. A river or a missing crossing can make a school much further away than 1.5 km, so my 13.3% is probably too low. My grid cells are also squares over the ward's bounding box, so an empty cell at the edge does not mean an underserved area.

## What went wrong and how I fixed it
I saved the coverage script as `coverage_map.py` instead of `coverage_gap.py`, so I renamed it before committing. My first `git push` also failed with "Could not resolve host" because the laptop had no internet. The commit was safe, and the push worked when the connection came back.