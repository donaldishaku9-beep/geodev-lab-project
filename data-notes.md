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
  study area, but usable. Raster does not fully cover the ward's thin northern spike and 
  southern tail after clipping — this reflects the ~1km resolution being 
  coarser than these narrow parts of the ward shape, not a clipping error. 
  Population for those slivers should be treated as unavailable, not zero.

  
  ## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Tudun Wada South, extracted from GRID3 wards
- - Ward boundary and schools layer reprojected to EPSG:32632 (UTM Zone 32N) — corrected from an initial error using zone 31N. Minna/Chanchaga sits at ~6.55°E, which falls within zone 32N's range (6°–12°E), not 31N (0°–6°E).
- Population raster re-clipped and reprojected to EPSG:32632
- Area check: Tudun Wada South = 15.69 km²
- Population raster clipped to study area (still in EPSG:4326)
- Area check: Tudun Wada South = 15.687km², there is no published figure to match with
- Working files are stored in data/processed file, while raw files are untouched.

## Quality notes

### Ward boundary
- Completeness: full national coverage, Niger State included, no gaps observed
- Fitness for purpose: authoritative source, well suited for defining the study area

### Schools
- Completeness: 47 features within Tudun Wada South; OSM had zero for the same 
  area (mapping gap, not absence of schools)
- Fitness for purpose: UBEC-sourced via GRID3, more authoritative than OSM here

### Population
- Completeness: full raster coverage except two narrow ward slivers (see note above)
- Fitness for purpose: modeled, not measured; 1km resolution is coarse for a 
  single small ward, so results should be read as indicative, not precise
