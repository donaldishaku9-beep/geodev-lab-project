# Week 10: GeoPandas, layers as tables

## What this folder contains
- [explore_pandas.py](./explore_pandas.py): first look at the ward population table
- [filter_sort.py](./filter_sort.py): filters, sorts and adds a column to the ward table
- [explore_layer.py](./explore_layer.py): opens the wards layer and runs the layer checklist
- [geom_props.py](./geom_props.py): looks inside one ward geometry
- [csv_to_points.py](./csv_to_points.py): turns the facility CSV into a point layer
- [join_population.py](./join_population.py): joins population to the wards after cleaning names
- [make_map.py](./make_map.py): draws [facilities_map.png](./facilities_map.png)
- [save_outputs.py](./save_outputs.py): saves a GeoPackage layer and [wards_table.csv](./wards_table.csv)
- [my_explore.py](./my_explore.py): runs the layer checklist on my Minna schools layer
- [my_points.py](./my_points.py): turns my school coordinates from [schools_xy.csv](../../data/raw/schools_xy.csv) into points and plots them over my ward as [my_points_check.png](./my_points_check.png)
- [my_join.py](./my_join.py): joins population to my 47 schools on `uniq_id` and prints the match counts
- [my_join.py](./my_join.py): joins population from `mydata.csv` to my 47 schools on `uniq_id` and prints the match counts
- [my_map.py](./my_map.py): draws my schools over the ward, coloured by population, and saves [my_map.png](./my_map.png)

## How to run it
From the repository root:

uv run month-03/week-10/join_population.py

Every script runs the same way, with its own file name at the end.

## What I found
The first population join matched 9 of 12 wards. After cleaning the names in code, it matched all 12. My own schools layer has 47 points in EPSG:32632, and its bounds fall around Minna, where I expected them.
My join matched 47 of 47 schools on the first try. I checked that `uniq_id` had no duplicates and that the row count stayed at 47 after the join.

## What went wrong and how I fixed it
Before the week started, uv failed to build my project because the `src` folder from Month 2 had never been uploaded, and a broken `.venv` blocked the rebuild. I copied `src` back in, deleted the broken `.venv` and let uv rebuild it.