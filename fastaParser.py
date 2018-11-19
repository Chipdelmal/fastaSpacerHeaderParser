import sys
import functions as parser

PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]
parser.parseAndMergeFASTAFilesInPath(PATH, OUTPUT_PATH)
