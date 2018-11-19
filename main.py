#############################################################################
# Main routine for the ad hoc fasta files parser
# Description:
#############################################################################

import functions as parser

PATH = "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Data"

filepaths = parser.readFilepaths(PATH, extension=".fa")
filenames = parser.getFilenamesFromPaths(filepaths)
identifiers = parser.getUniqueIdentifiers(filenames, separator="_")
matchedIndices = parser.getIdentifierToFilenamesMatches(filenames, identifiers)


file = open(filepaths[0], "r")
read=file.read()
read.replace(">spacer","")
