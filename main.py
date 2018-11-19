#############################################################################
# Main routine for the ad hoc fasta files parser
# Description:
#############################################################################

import functions as parser

PATH = "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Data/"
OUTPUT_PATH = "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Out/"

parsers.parseAndMergeFASTAFilesInPath(PATH, OUTPUT_PATH)

filepaths = parser.readFilepaths(PATH, extension=".fa")
filenames = parser.getFilenamesFromPaths(filepaths)
identifiers = parser.getUniqueIdentifiers(filenames, separator="_")
matchedIndices = parser.getIdentifierToFilenamesMatches(filenames, identifiers)
parser.exportFAFiles(
    OUTPUT_PATH,
    identifiers,
    matchedIndices,
    filepaths,
    filenames
)
