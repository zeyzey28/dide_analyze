# DiDe / QGIS + PostGIS Analysis README

## 0) Goal

This project analyzes DiDe event points (especially Cigarette Butt) and bin locations (rubbish / recycle) to understand accessibility and spatial patterns.

Main questions:

- Are cigarette butt reports located within 25m / 50m of a bin?
- Which areas form hotspots (dense clusters)?
- How can PostGIS indexing (GiST / B-tree) speed up queries used in the analysis?

## 1) Data used

### 1.1 Event data (olaylar)

Source layer: `olaylar_1765259089240` (points)

Contains event attributes such as:

- `olay_turu_id`, `olay_turu_adi`, `olay_turu_good`
- `aciklama`, `photo_urls`, `video_urls`
- `created_by`, `created_by_id`, `created_at`, `event_time`, etc.

![QGIS attribute table showing event data with columns: olay_id, created_by, created_by_id, created_at, event_time, hour, weekday_name, date_only](readme_images/event_data_table.png)

*Figure: Sample records from the `olaylar_1765259089240` event data table showing 234 total features with various attributes including user IDs, timestamps, and event metadata.*

### 1.2 Bin data

I worked with bin-type points and created merged layers:

- `recy_bin_3857`
- `rubbish_bin_3857`
- merged result (all bins): `bins_merged_3857` (points)

![QGIS attribute table showing joined layer with bin data including olay_turu_adi (Recycle bin, Rubbish bin), olay_turu_id, olay_turu_good, and pt_count fields](readme_images/bin_data_table.png)

*Figure: Joined layer attribute table showing bin data with event types (Recycle bin, Rubbish bin), event type IDs, and point counts. This represents the merged bin dataset used in the analysis.*

### 1.3 Coordinate reference system

For distance-based analysis, I used EPSG:3857 (meters).

Note: One table (`olaylar_1765...`) originally came as EPSG:4326, then I created 3857 versions when needed.

## 2) Preprocessing & layer preparation in QGIS

### 2.1 Filtering event type: Cigarette Butt

From `olaylar_1765259089240` I filtered the event type:

- `olay_turu_adi = 'Cigarette Butt'` (or `olay_turu_id = 3`)

Saved as a new layer:

- `cig_butt_3857` (points)

### 2.2 Preparing bins layer

I combined rubbish + recycle bins into one dataset:

- Output layer: `bins_merged_3857`

## 3) Distance threshold analysis (25m & 50m)

Goal: Separate cigarette butt events into inside vs outside distance thresholds from bins.

### 3.1 Create buffers around bins

I created bin buffers to model reachable distance:

- `bins_buffer_25m`
- `bins_buffer_50m`

QGIS tool:

- Vector → Geoprocessing Tools → Buffer
- Distance: 25m and 50m (separately)
- Dissolve (optional depending on workflow)

### 3.2 Points inside buffer (within distance)

I selected cigarette butt points that fall inside buffers:

- Inside 25m → `cig_butt_within_25m`
- Inside 50m → `cig_butt_within_50m`

QGIS tool options:

- Select by Location
- "Select features from" = cigarette butt layer
- "Where the features" = within / intersects
- "By comparing to" = `bins_buffer_25m` / `bins_buffer_50m`
- Then Export → Save Selected Features As…

### 3.3 Points outside buffer (not within distance)

I also extracted points outside (coverage gap):

- `cig_butt_outside_25m`
- `cig_butt_outside_50m`

Method:

- Select inside first, then invert selection, export as outside.

![Distance threshold analysis visualization showing 50m buffers (pink polygons) and suitable cigarette butt points (cyan) within 50m of bins](readme_images/distance_analysis_50m.png)

*Figure: QGIS visualization of 50m buffer zones around bins (pink polygons) and cigarette butt events within suitable distance (cyan points). The map shows Hacettepe University Beytepe Campus with EPSG:3857 coordinate system.*

### Interpretation

- **Inside distance**: bins exist nearby → problem may be cleaning/behavior.
- **Outside distance**: accessibility problem → indicates need for better bin placement.

## 4) Nearest bin assignment (Nearest neighbor join)

Goal: For each cigarette butt point, assign the nearest bin and distance.

### 4.1 Nearest hub (or distance to nearest)

I used a nearest-neighbor tool to link each event to the closest bin:

- Output layer: `cigg_butt_nearest`
  (contains nearest bin reference + distance fields)

QGIS tool:

- Processing Toolbox → Vector analysis
- "Distance to nearest hub" OR "Join attributes by nearest"
- Input: cigarette butt points
- Hubs / target: `bins_merged_3857`

### 4.2 "Suitable bins" outputs (25m / 50m)

I created final "suitable within threshold" result layers:

- `uygun_25m` — ...
- `uygun_50m` — `cigg_butt_nearest`

These layers represent filtered/processed sets that are used in final reporting and maps.

## 5) Hotspot / clustering analysis

Goal: Identify areas where cigarette butt events concentrate strongly.

### 5.1 Create density surface (heatmap)

Heatmap output: `heatmap_25m` (or your heatmap layer)

QGIS tool:

- Heatmap (Kernel density estimation)

![QGIS map showing heatmap visualization with red gradient indicating density of cigarette butt events, overlaid on OpenStreetMap base layer](readme_images/heatmap_25m.png)

*Figure: Kernel density estimation heatmap (`heatmap_25m`) showing concentration of cigarette butt events. Darker red areas indicate higher event density (hotspots). The map uses EPSG:3857 coordinate system.*

### 5.2 Hotspot polygons & centroid points

I extracted top dense regions:

- `hotspot_poly` (polygons)
- `hotspot_centroids` (points)

Then I calculated counts / ranking:

- `hotspot_counts`
- `hotspots_top3` — `hotspot_counts`
- `points_in_top3`
- `hotspot_top3_nearest_bin`

![QGIS comprehensive view showing heatmap, event points, buffer zones, and suitable points on Hacettepe University Beytepe Campus map](readme_images/comprehensive_analysis_view.png)

*Figure: Comprehensive QGIS visualization showing multiple analysis layers: heatmap (red gradient), event points (red dots), 50m buffer zones (pink polygons), and suitable points within 50m (cyan). This integrated view demonstrates the relationship between hotspot areas, bin accessibility, and event distribution.*

### Interpretation

Top3 hotspot zones show where cigarette butt events are systematically frequent.

These zones are candidates for targeted interventions (more bins, signage, cleaning schedule).

## 6) PostGIS database storage (saving all layers)

Goal: Store both teacher-provided data + my derived layers in PostGIS.

### 6.1 Create a new database

Database name: `dide`

### 6.2 Import layers into PostGIS (via QGIS DB Manager)

Tool:

- Database → DB Manager → Import Layer/File…

I imported:

- `olaylar_1765259089240`
- `bins_merged_3857`
- `cigg_butt_nearest`
- `cig_butt_outside_50m`
- `hotspot_centroids`
- `hotspot_counts`
- `hotspots_top3`
- `uygun_50m` ...
  (and other derived layers)

After importing, I confirmed geometry tables using:

```sql
SELECT f_table_name, f_geometry_column, srid, type
FROM geometry_columns;
```

## 7) Indexing demo (GiST + B-tree) with EXPLAIN ANALYZE

Goal: Show how indexing speeds up DiDe-like spatial queries.

### 7.1 Why GiST? (Spatial index)

Spatial queries like `ST_DWithin` benefit from GiST index on `geom`.

Create GiST indexes:

```sql
CREATE INDEX IF NOT EXISTS idx_cig_geom_gist
ON public.cigg_butt_nearest
USING GIST (geom);

CREATE INDEX IF NOT EXISTS idx_bin_geom_gist
ON public.bins_merged_3857
USING GIST (geom);
```

Update statistics:

```sql
ANALYZE public.cigg_butt_nearest;
ANALYZE public.bins_merged_3857;
```

### 7.2 Query tested

I tested a typical query:
"Count cigarette butt points that have at least one bin within 50m"

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT count(*) AS cig_within_50m
FROM public.cigg_butt_nearest c
WHERE EXISTS (
  SELECT 1
  FROM public.bins_merged_3857 b
  WHERE b.geom && ST_Expand(c.geom, 50)
    AND ST_DWithin(c.geom, b.geom, 50)
);
```

### 7.3 Result interpretation

Without spatial index, the plan tends to show:

- Seq Scan (slow for large datasets)

With GiST index, I observed:

- Index Scan using `idx_bin_geom_gist` ...

This confirms the spatial index is being used.

![PostgreSQL EXPLAIN ANALYZE query plan showing Index Scan using idx_bin_geom_gist with execution time of 5.454 ms](readme_images/explain_analyze_gist.png)

*Figure: Query execution plan from `EXPLAIN (ANALYZE, BUFFERS)` showing the use of GiST spatial index (`idx_bin_geom_gist`) on `bins_merged_3857`. The plan shows Index Scan operations with Index Condition using `ST_Expand` and Filter using `ST_DWithin`, confirming efficient spatial index utilization. Execution time: 5.454 ms.*

I recorded execution times during tests (example measurements):

- Step A: 0.073s
- Step C: 0.187s

(times vary depending on cache, dataset size, and machine conditions)

### 7.4 B-tree note (non-spatial)

B-tree is useful for standard fields (e.g., filtering by `created_by`, ids, timestamps), but not for geometry distance checks.

Example B-tree index:

```sql
CREATE INDEX IF NOT EXISTS idx_events_created_by
ON public.olaylar_1765259089240 (created_by);
```

## 8) Helper selection (helper_id = 216)

I selected helper 216 by checking their contributed dataset and verifying it is consistent and usable for analysis.

I filtered the events table by:

- `created_by = 216`

This produced a subset of 16 events, with meaningful descriptions and photo URLs.

This subset was used as a reference contributor sample for interpreting event patterns and checking proximity logic.

### Reasoning

Helper 216's contributions are structured, include media references, and represent different event categories (bins, cigarette butt, full rubbish). This makes the helper suitable as a "reliable contributor" for demonstrating analysis logic.

## 9) Outputs (main layers)

Key outputs generated:

- `bins_merged_3857`
- `bins_buffer_25m`, `bins_buffer_50m`
- `cig_butt_within_25m`, `cig_butt_within_50m`
- `cig_butt_outside_25m`, `cig_butt_outside_50m`
- `cigg_butt_nearest`
- `uygun_25m` ..., `uygun_50m` ...
- `hotspot_poly`, `hotspot_centroids`
- `hotspot_counts`, `hotspots_top3`, `points_in_top3`, `hotspot_top3_nearest_bin`

## 10) Conclusion

Using distance thresholds (25m/50m), nearest-bin assignment, and hotspot extraction, I identified both:

- areas that are already served by bins (behavior/maintenance issue),
- and coverage gaps where bin accessibility may be insufficient.

The PostGIS indexing demo confirms that spatial indexing (GiST) is critical for scalable distance-based analysis.
