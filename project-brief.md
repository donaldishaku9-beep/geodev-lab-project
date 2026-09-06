# My project brief

## The question
Where are the gaps in school coverage in Brighter area, Chanchaga LGA, Minna, Niger State, relative to where people actually live?

## Why it matters
Mapping school locations alone shows what exists, but not whether it's actually adequate. Comparing school locations against population distribution reveals underserved pockets — areas with real population density but no nearby school. This kind of analysis could inform where new schools are most needed, or simply give residents and local planners a clearer picture of access in the area. I also live in this area, so I can sanity-check the results against what I actually see on the ground.

## The data I need
- School locations — OpenStreetMap (amenity=school), extracted via QuickOSM
- Ward boundaries for Chanchaga LGA — GRID3 Operational Wards v3.0
- Population distribution — WorldPop gridded population estimates (100m resolution)

## Where each dataset comes from
- OpenStreetMap schools — extracted via the QuickOSM plugin in QGIS, querying amenity=school within my area of interest
- GRID3 Operational Wards v3.0 — https://data.grid3.org (Niger State is included in this dataset)
- WorldPop population — https://worldpop.org (Nigeria population, most recent year available)

## What I would build
A map showing school locations overlaid with population density across Brighter area and its surrounding wards, highlighting populated zones that fall outside a reasonable walking distance (e.g. 1–2 km) from any school. Over time, this could become a simple tool that flags underserved areas as new population or school data becomes available.
