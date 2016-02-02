#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     GeoLinked App to Facilitate Mappings and Processing
#
# Author:      Holly Tina Ferguson hfergus2@nd.edu
#
# Created:     06/10/2015
# Copyright:   (c) Holly Tina Ferguson 2015
# Licence:     The University of Notre Dame
#-------------------------------------------------------------------------------

# #!/usr/bin/python
import sys
import getopt
import os
from Geo_Link import Geo_Link


def main(argv, inputfile='C:/Users/hfergus2/Desktop/GeoLinked/sample_files/Single_Room_GBXML.xml', outputpath='output.csv'):
    # C:/Users/Holly2012/Desktop/GeoLinked/sample_files
    # C:/Users/hfergus2/Desktop/GeoLinked/sample_files
    print "Main Started"

    # Get the input file
    #inputfile = sys.argv[0]
    #Single_Room_GBXML
    #Single_Room_IFCxml
    mypath = os.path.abspath(inputfile)
    #print "inputfile", mypath, type(inputfile).__name__

    geo_link = Geo_Link()
    geo_link.inputfile = mypath
    geo_link.run()

    #outputfile = open(outputpath) #output.csv in the main folder
    #with open(outputpath, 'r') as f:
        #Add whatever stuff
        #for line in f:
        #    outputfile.write(line)
    #outputfile.close()
    sys.stdout.write("Main Finished")

if __name__ == "__main__":
    #logging.basicConfig()
    main(sys.argv[1:])
    #main(inputfile, outputfile)




