Stephanie George
GEOG682 Final
August 4, 2019 

import processing

crime = "E:/682Final/Crimes_Incidents_in_2017.csv"
iface.addVectorLayer(crime, "Crime", "ogr")
wards = "E:/682Final/Ward_from_2012.csv"
iface.addVectorLayer(wards, "Wards", "ogr") 
shots = "E:/682Final/Shot_Spotter_Gun_Shots.csv"
iface.addVectorLayer(shots, "Shots", "ogr") 

