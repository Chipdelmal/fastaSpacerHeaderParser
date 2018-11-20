#############################################################################
# Bash routine for the fastaParser process
# Description: Read the specifications for the objective of the script.
#   First argument should be the path where the FA files are stored.
#   Second argument is the path where the merged FA files will be saved.
#############################################################################

import sys
import functions as parser

PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]
parser.parseAndMergeFASTAFilesInPath(PATH, OUTPUT_PATH)
