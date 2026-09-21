# Data notes

## Ward boundary — Tudun Wada South
- Source: GRID3 Operational Wards v3.0 — https://data.grid3.org
- Features: 5,872 features
- Key columns: ward_name, lga_name, state
- Geometry type: Polygon
- Notes: no obvious gaps
  
## School locations — GRID3
- Source: GRID3 NGA Schools (POI dataset) — https://data.grid3.org
- Downloaded: national file, clipped to Tudun Wada South ward boundary
- Features: 47 features
- Geometry type: Point
- Notes: OpenStreetMap (amenity=school) returned zero results for this ward, 
  even after broadening the query to all amenity tags — a genuine OSM mapping 
  gap in this area rather than an actual absence of schools. GRID3's POI 
  schools dataset (UBEC-sourced) provides full coverage instead and is used 
  as the primary school data source going forward.

## Population — WorldPop
- Source: WorldPop Nigeria population estimates — https://hub.worldpop.org
- Format: GeoTIFF, ~1km resolution (30 arc-seconds)
- Year: 2026 estimate
- Projection: WGS84 (geographic)
- Notes: 100m resolution version was not available/accessible; using the 
  1km resolution product instead. Coarser than ideal for a single-ward 
  study area, but usable.
  
  ## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Tudun Wada South, extracted from GRID3 wards
- Ward boundary and schools layer reprojected to EPSG:32631 (UTM 31N)
- Population raster clipped to study area (still in EPSG:4326)
- Area check: Tudun Wada South = 15.687km²
