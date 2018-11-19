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


nameFile = identifiers[0] + "_CRISPRspacer.fa"
indicesList = matchedIndices[0]
open()
generateExportStringFromMatchedIndices(indicesList)

def generateExportStringFromMatchedIndices(matchedIndices):
    fileString = ""
    for i in indicesList:
        fileString = fileString + \
            parser.changeSpacerTagInFile(filepaths[i], filenames[i])
    return fileString
