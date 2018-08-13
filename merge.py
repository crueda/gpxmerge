#-*- coding: UTF-8 -*-

from os import listdir
from xml.dom.minidom import parse, parseString

out = open("merged.gpx","w")
out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
out.write('<gpx xmlns:gpxdata="http://www.cluetrust.com/XML/GPXDATA/1/0" xmlns:gpxext="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns="http://www.topografix.com/GPX/1/1" creator="tapiriik-sync">\n')
out.write('<metadata><name>Cycling</name></metadata>\n')

for fichero_gpx in listdir("./gpx"):
    #if fichero_gpx.find('Cycling') > -1 and fichero_gpx.find('2018-08') > -1:
    if fichero_gpx.find('Cycling') > -1:
        print (fichero_gpx)
        xml = parse('./gpx/' + fichero_gpx)
        trks = xml.getElementsByTagName("trk")
        for trk in trks:
            trk.writexml(out)

out.write('</gpx>\n')
out.close()