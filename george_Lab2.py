#Stephanie George
#June 24, 2019
#GEOG682 - Lab 2

import processing #import QGIS processing tools
crime = "C:/Users/sgeorge4/Desktop/george_Lab2/Crime/Crime_Incidents_in_2017.shp" #crime incidents shapefile saved as new variable
iface.addVectorLayer(crime, "Crime", "ogr") #crime incidents shapefile added to map

district = "C:/Users/sgeorge4/Desktop/george_Lab2/Police/Police_Districts.shp" #police districts shapefile saved as new variable
iface.addVectorLayer(district, "District", "ogr") #police districts shapefile added to map

processing.runalg("qgis:joinattributesbylocation", 
    crime, district, u'contains', '', 0, 1, 'C:/Users/sgeorge4/Desktop/george_Lab2/final_join.shp')
    
#District 3 had the most crimes in 2017. 5895 crimes occurred there in 2017. 