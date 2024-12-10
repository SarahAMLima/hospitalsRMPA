#importing the necessary libraries
import geopandas as gpd
import plotly.express as px


#Reading the data using the relative path
gdf: gpd.GeoDataFrame = gpd.read_file('saude_rmpa.geojson')

#to test if the data is being read correctly
#print(gdf)

#assigning a CRS to the project
gdf = gdf.to_crs(4326)

#creating the map/plot
fig = px.choropleth(
    gdf, #Adding the geodataframe
    geojson=gdf.geometry, #creating a cathegory for the shapefile of all the zones
    locations = gdf.index, #creating an index based on locations or zones
    color = 'hospitais', #the color will varry according to the number of hospitals in each zone
    hover_name= 'codigo', #assigning the name of the hover as the cathegory color from our geojson
    title= 'Chloropleth map of hospitals in Porto Alegre, Brazil'
)

fig.update_geos(fitbounds='locations', visible=False)
fig.show()