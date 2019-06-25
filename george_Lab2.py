#Stephanie George
#June 24, 2019
#GEOG682 - Lab 2

import processing #import QGIS processing tools
crime = "C:/Users/sgeorge4/Desktop/george_Lab2/Crime/Crime_Incidents_in_2017.shp" #save shapefile as new variable
iface.addVectorLayer(crime, "Crime", "ogr") #add shapefile to map
district = "C:/Users/sgeorge4/Desktop/george_Lab2/Police/Police_Districts.shp"
iface.addVectorLayer(district, "District", "ogr")
#run fixed distance buffer processing tool
#processing.runalg("qgis:fixeddistancebuffer", 
#    {'INPUT':sample,'DISTANCE':50,'SEGMENTS':5,'DISSOLVE':False,'OUTPUT':'C:/temp/Lab2/samp_buff.shp'})
#add new buffers to the map
#iface.addVectorLayer( "C:/temp/Lab2/samp_buff.shp","buff","ogr")
#processing.runalg("qgis:joinattributestable",
  #  {'INPUT_LAYER': district, 'INPUT_LAYER_2': crime, 'TABLE_FIELD': district, 
    #'OUTPUT_LAYER': 'C:/Users/sgeorge4/Desktop/george_Lab2/final_join.shp'})
    
processing.runalg("qgis:joinattributesbylocation",
    crime, district, u'contains', '', 0, 1, 'C:/Users/sgeorge4/Desktop/george_Lab2/final_join.shp')
    
#District 3 had the most crimes in 2017. 5895 crimes occurred there in 2017. 