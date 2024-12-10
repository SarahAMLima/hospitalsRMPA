# Choropleth Map of Hospitals in Porto Alegre, Brazil

This project demonstrates how to create an interactive **choropleth map** using **GeoPandas** and **Plotly Express**. The map visualizes the distribution of hospitals in different zones of Porto Alegre, Brazil, based on a provided GeoJSON file.

---

## **Features**
- Reads and processes geospatial data from a GeoJSON file.
- Assigns a **Coordinate Reference System (CRS)** for consistent mapping.
- Generates a choropleth map where zones are color-coded by the number of hospitals.
- Includes interactivity for users to explore zone details (e.g., code, hospital count).

---

## **Prerequisites**
To run this script, you need to install the following libraries:
- [GeoPandas](https://geopandas.org): `pip install geopandas`
- [Plotly](https://plotly.com/python/): `pip install plotly`

Ensure you have a valid GeoJSON file named `saude_rmpa.geojson` in the working directory. This file should include attributes for:
- **Hospitals**: A numerical field representing the count of hospitals in each zone.
- **Zone Code**: An identifier for each zone.

---

## **Steps to Run**
1. Clone the repository or download the script.
2. Place the `saude_rmpa.geojson` file in the same directory as the script.
3. Execute the script:
   ```bash
   python choropleth_map.py

##**Output**
  ##The interactive map will display:
     ##Zones with a color gradient representing hospital density.
     ##Hover tooltips showing zone codes and hospital counts.
