#############################################################################
# Main routine for the ad hoc fasta files parser
# Description: Read the specifications for the objective of the script.
#   This routine runs from a python terminal, for the bash version, open
#   "fastaParser.py"
#############################################################################

import sys
import functions as parser

PATH = "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Data/"
OUTPUT_PATH = "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Out/"

parser.parseAndMergeFASTAFilesInPath(PATH, OUTPUT_PATH)
