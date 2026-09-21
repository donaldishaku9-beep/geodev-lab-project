# My project brief

## The question
Where are the gaps in school coverage in Brighter area, Chanchaga LGA, Minna, Niger State, relative to where people actually live?

## Why it matters
Mapping school locations alone shows what exists, but not whether it's actually adequate. Comparing school locations against population distribution reveals underserved pockets — areas with real population density but no nearby school. This kind of analysis could inform where new schools are most needed, or simply give residents and local planners a clearer picture of access in the area. I also live in this area, so I can sanity-check the results against what I actually see on the ground.

## The data I need
- School locations — GRID3 NGA Schools (POI)
- Ward boundaries for Chanchaga LGA — GRID3 Operational Wards v3.0
- Population distribution — WorldPop gridded population estimates (~1km resolution)

## Where each dataset comes from
- GRID3 NGA Schools (POI) — https://data.grid3.org — downloaded as the national file, clipped to Tudun Wada South ward. Note: OpenStreetMap (amenity=school) was tried first but returned zero results for this ward, a genuine OSM mapping gap; GRID3 was used instead as a more complete source.
- GRID3 Operational Wards v3.0 — https://data.grid3.org (Niger State is included in this dataset)
- WorldPop population — https://hub.worldpop.org (Nigeria population, 2026 estimate, ~1km resolution GeoTIFF)

## What I would build
A map showing school locations overlaid with population density across Brighter area and its surrounding wards, highlighting populated zones that fall outside a reasonable walking distance (e.g. 1–2 km) from any school. Over time, this could become a simple tool that flags underserved areas as new population or school data becomes available.
