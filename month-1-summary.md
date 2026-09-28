# Month 1 summary

## Question
Where are the gaps in school coverage in Tudun Wada South ward, Chanchaga LGA, 
Minna, relative to population?

## Operation
Buffered 47 GRID3 schools by 1.5km (dissolved), then took the difference against 
the ward boundary to find uncovered areas. All layers in EPSG:32632.

## What I got
[Describe what the uncovered map shows — which edges/areas are outside 1.5km of a school]

## Limitations
- Population data is 1km resolution (coarse for a single ward)
- CRS was initially set incorrectly to zone 31N and corrected to 32632 
  (Minna sits at ~6.55°E, in zone 32N's range)
- OSM had no school data for this ward; GRID3 was used instead
