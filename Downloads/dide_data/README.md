# DiDe / QGIS + PostGIS Analysis README

![DiDe Project](readme_images/img1.png)

## 0) Goal

This project analyzes DiDe event points (especially Cigarette Butt) and bin locations (rubbish / recycle) to understand accessibility and spatial patterns.

Main questions:

- Are cigarette butt reports located within 25m / 50m of a bin?
- Which areas form hotspots (dense clusters)?
- How can PostGIS indexing (GiST / B-tree) speed up queries used in the analysis?

![PostGIS Query Plan](readme_images/img11.png)
*PostGIS query execution plan showing efficient spatial indexing with GiST index*

## 1) Data used

### 1.1 Event data (olaylar)

Source layer: `olaylar_1765259089240` (points)

Contains event attributes such as:

- `olay_turu_id`, `olay_turu_adi`, `olay_turu_good`
- `aciklama`, `photo_urls`, `video_urls`
- `created_by`, `created_by_id`, `created_at`, `event_time`, etc.

**Total Events**: 492  
**Events with Photos**: 488

![Event Data in QGIS](readme_images/img2.png)
*Event data visualization in QGIS with heatmap overlay*

### 1.2 Bin data

We worked with bin-type points and created merged layers:

- `recy_bin_3857`
- `rubbish_bin_3857`
- merged result (all bins): `bins_merged_3857` (points)

### 1.3 Coordinate reference system

For distance-based analysis, we used EPSG:3857 (meters).

Note: One table (`olaylar_1765...`) originally came as EPSG:4326, then we created 3857 versions when needed.

![CRS Configuration](readme_images/img3.png)
*Project CRS set to EPSG:3857 (WGS 84 / Pseudo-Mercator) in QGIS*

## 2) Analysis Workflow

### 2.1 Buffer Analysis

- Created 50m buffers around bin locations (`bins_buffer_50m.gpkg`)
- Identified cigarette butts within 50m of bins
- Identified cigarette butts outside 50m (`cig_butt_outside_50m.gpkg`)

![Buffer Analysis](readme_images/img4.png)
*50m buffer zones around bins with cigarette butt points (teal) within buffer areas*

![Statistical Analysis](readme_images/img12.png)
*Statistical summary of uygun_25m field showing distribution of points within 25m buffers*

### 2.2 Nearest Neighbor Analysis

- Calculated nearest bin for each cigarette butt (`cigg_butt_nearest.gpkg`)
- Created lines connecting hotspots to nearest bins (`hotspot_to_bin_lines.gpkg`)

![Nearest Bin Analysis](readme_images/img13.png)
*Hotspot to nearest bin analysis results showing distances and bin assignments*

### 2.3 Hotspot Detection

- Identified top 3 hotspots (`hotspots_top3.gpkg`)
- Created hotspot centroids (`hotspot_centroids.gpkg`)
- Generated hotspot polygons (`hotspot_poly.gpkg`)
- Created heatmaps at 25m resolution (`heatmap_25m.tif`)

![Hotspot Analysis](readme_images/img9.png)
*Hotspot polygons, centroids, and heatmap visualization showing dense clusters*

![Heatmap Visualization](readme_images/img5.png)
*25m resolution heatmap showing event density across the campus*

![Heatmap Detail](readme_images/img6.png)
*Detailed heatmap view with OpenStreetMap base layer*

### 2.4 Visualization

- HTML summaries: `sum_25.html`, `sum_50.html`
- PDF heatmap: `top3_heatmap.pdf`
- QGIS project: `analiz.qgz`

![QGIS Extract by Location](readme_images/img10.png)
*Extract by Location tool used to identify points within top 3 hotspots*

![Heatmap Layers](readme_images/img7.png)
*Multiple heatmap and event layers displayed in QGIS*

![Event Distribution](readme_images/img8.png)
*Event point distribution overlaid on campus map*

## 3) File Structure

### 3.1 Event Data
- `olaylar_1765259089240.geojson` - Original event data (GeoJSON)
- `olaylar_1765259089240.gpkg` - Event data (GeoPackage)
- `cig_butt_3857.gpkg` - Cigarette butt points in EPSG:3857

### 3.2 Bin Data
- `binpoints.gpkg` - Bin point data
- `bin_points_3857.gpkg` - Bin points in EPSG:3857
- `bins_merged_3857.gpkg` - Merged bin data
- `bins_buffer_50m.gpkg` - 50m buffer zones
- `rubbish_bin_3857.gpkg` - Rubbish bin data
- `recycle_bin_3857.gpkg` - Recycle bin data
- `recy_bin_3857.gpkg` - Alternative recycle bin data

### 3.3 Analysis Results
- `cig_butt_outside_50m.gpkg` - Cigarette butts outside 50m
- `cigg_butt_nearest.gpkg` - Nearest bin assignments
- `cigg_but_nearest_bin.gpkg` - Nearest bin relationships
- `hotspot_poly.gpkg` - Hotspot polygons
- `hotspot_centroids.gpkg` - Hotspot centroids
- `hotspot_counts.gpkg` - Hotspot count data
- `hotspots_top3.gpkg` - Top 3 hotspots
- `hotspot_top3_nearest_bin.gpkg` - Top 3 hotspots nearest bins
- `hotspot_to_bin_lines.gpkg` - Lines from hotspots to bins
- `points_in_top3.gpkg` - Points within top 3 hotspots

### 3.4 Raster Data
- `heatmap_25m.tif` - 25m resolution heatmap
- `hotspot_mask_4.tif` - Hotspot mask

### 3.5 Helper Files
- `216_secimi.gpkg` - Selection data
- `helper_216_binsmerged_50m.gpkg` - Helper analysis file
- `helper_216_within_50m.gpkg` - Helper data within 50m
- `uygun_50m.gpkg` - 50m suitability analysis

### 3.6 Visualization & Reports
- `sum_25.html` - 25m analysis summary
- `sum_50.html` - 50m analysis summary
- `top3_heatmap.pdf` - Top 3 hotspot heatmap report
- `analiz.qgz` - QGIS project file
- `DiDe.qml` - QGIS style file

### 3.7 Uploaded Files
- `uploads/` - User uploads (564 JPG, 2 HEIC, 2 WEBM)

## 4) Technologies Used

- **QGIS** - Geographic Information System analysis
- **PostGIS** - Spatial database extension
- **GeoPackage (.gpkg)** - Vector data format
- **GeoTIFF (.tif)** - Raster data format
- **GeoJSON** - JSON-based geographic data format

## 5) Key Findings

- Analysis of 492 events, primarily cigarette butt reports
- Identification of top 3 hotspot areas
- Distance analysis showing accessibility to bins within 25m/50m
- Spatial patterns revealing areas needing additional bin placement

## 6) Usage

### Opening in QGIS

```bash
# Open QGIS project file
qgis analiz.qgz
```

### Viewing Data

GeoPackage files can be opened with:
- QGIS
- ArcGIS
- Python (geopandas)
- PostGIS

### Accessing Event Photos

Event photos are stored locally in the `uploads/` directory. Each event may have associated photos referenced in the `photo_urls` field of the event data.

## 7) Notes

- All coordinate systems standardized to EPSG:3857 (Web Mercator)
- Buffer analyses performed at 50m distance
- Hotspot analyses focused on top 3 areas
- Photo URLs are stored in the `photo_urls` field of event data

---

**Last Updated**: 2024  
**Project**: DiDe - Spatial Analysis of Cigarette Butt Distribution and Bin Accessibility
