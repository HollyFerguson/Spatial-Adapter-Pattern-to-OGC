#-------------------------------------------------------------------------------
# Name:        Geo_Link.py
# Purpose:     Start program to process geometry data
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
from file_type import file_type
from term_mapping import term_mapping
from UBO_structure import UBO_structure
from filled_UBO_graph import filled_UBO_graph
from OGCtemplate import OGCtemplate
from OGCtemplate2 import OGCtemplate2
from OGCqueryNfill import OGCqueryNfill


class Geo_Link():
    # Input parameters
    inputfile = ""


    def run(self):
        """
        Main run function
        """
        self.process_schemas()

        return None


    def process_schemas(self):
        """
        Main Processing Function
        """

        # Send file type and return respective term mapping between it and the UBO
        # Also find the source app that created this particular gbXML (use to lift to ontology later)
        step1 = file_type()
        this_file_type, SourceDetials = step1.schema_type(self.inputfile)
        #print "this_file_type", this_file_type

        # Send file type and return respective term mapping between it and the UBO
        step2 = term_mapping()
        mapDict = step2.get_mapping(this_file_type)

        # Retrieve the UBO empty structure to fill with the values from the input file
        step3 = UBO_structure()
        UBOgraphStructure = step3.pull_graph_structure()

        # Use mapping and the UBO structure to fill the UBO with geometry data
        step3 = filled_UBO_graph()
        UBO_filled, base = step3.fill_graph(this_file_type, mapDict, UBOgraphStructure, self.inputfile)

        # Setup ISO/OGC GeoSPARQL File Template...from: http://www.opengeospatial.org/standards/geosparql
        # Also uses the OGC simple feature documentation (both pdfs in sample_files folder)
        # States that the file type is RDF/XML encoded geometry data, in GeoSPARQL format)
        step4 = OGCtemplate2()
        OGC_RDF_header, OGC_file_parts = step4.createOGCtemplate2(base)
        #step4 = OGCtemplate()
        #OGC_RDF_header, OGC_file_parts = step4.createOGCtemplate(base)

        # Query UBO for data based on map, process coordinates into OGC format, use answers to fill OGC RDF file for output
        step5 = OGCqueryNfill()
        stuff = step5.processUBOforOGC(UBO_filled, base, OGC_RDF_header, OGC_file_parts)

        # Use UBO_filled to answer queries for data within to create respective ISO/OGC GeoSPARQL File

        return 0
