import processing #import QGIS processing tools
sample = "C:/Temp/sample.shp" #save shapefile as new variable
iface.addVectorLayer(sample,"sample","ogr") #add shapefile to map
#run fixed distance buffer processing tool
processing.runalg("qgis:fixeddistancebuffer", 
    {'INPUT':sample,'DISTANCE':50,'SEGMENTS':5,'DISSOLVE':False,'OUTPUT':'C:/Temp/samp_buff.shp'})
#add new buffers to the map
iface.addVectorLayer( "C:/Temp/samp_buff.shp","buff","ogr")
    