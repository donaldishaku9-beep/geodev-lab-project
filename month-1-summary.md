# Month 1 summary

## Question
Where are the gaps in school coverage in Tudun Wada South ward, Chanchaga LGA, 
Minna, Niger State, relative to where people actually live?

## Operation
Buffered 47 GRID3 schools by 1.5km (dissolved into one shape), then took the 
difference against the Tudun Wada South ward boundary to isolate areas beyond 
walking distance of any school. All layers in EPSG:32632 (UTM Zone 32N).

## Expected
Most of the ward covered within 1.5km, with a small uncovered pocket or two 
at the edges.

## Got
2.11 km² (about 13%) of the ward's 15.69 km² falls outside 1.5km of a school — 
concentrated in the ward's southern tail. The remaining 87% is within walking 
distance of at least one school.

## What surprised me
- OpenStreetMap had zero schools mapped in this ward at all — a genuine OSM 
  coverage gap. GRID3's POI schools dataset (UBEC-sourced) was used instead, 
  and had full coverage (47 schools).
- The population raster (1km resolution) couldn't fully resolve the ward's 
  narrow northern spike and southern tail — some slivers had no population 
  pixel at all, since they're narrower than the raster's resolution.
- I initially used the wrong UTM zone (31N instead of 32N) for this area — 
  Minna sits at ~6.55°E, just east of the 31N/32N boundary at 6°E, an easy 
  mistake to make without checking.

## Limitations, stated plainly
- Straight-line (Euclidean) distance was used, not actual travel distance 
  along roads — a location 1.4km away across difficult terrain may be harder 
  to reach than this analysis suggests.
- Population is modelled (WorldPop), not measured, and at 1km resolution is 
  coarse for a ward this size (15.69 km²).
- I have not yet calculated how many people (not just how much area) fall 
  within the uncovered zone — only a visual/qualitative sense from the 
  population layer.

## What I still need
- Road network data, to calculate actual travel distance rather than 
  straight-line distance
- A population sum (not just area) within the uncovered polygon, to know how 
  many people are actually affected
- Higher-resolution population data (100m), if it becomes accessible
