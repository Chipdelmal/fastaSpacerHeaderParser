#
#

import functions as parser

PATH = "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Data"
filepaths = parser.readFilepaths(PATH,extension=".fa")
parser.getFilenamesFromPaths(filepaths)
