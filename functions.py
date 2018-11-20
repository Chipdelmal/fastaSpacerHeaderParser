import glob


def readFilepaths(experimentPath, extension=".fa"):
    '''
    Returns the paths of all the files that match the extension
    within a given folder.
    '''
    filepaths = glob.glob(experimentPath + "/" + "*" + extension)
    return sorted(filepaths)


def getFilenamesFromPaths(filepaths):
    '''
    Splits the strings of the paths to return only the filenames
    for easier handling.
    '''
    filenames = [None]*len(filepaths)
    for i, path in enumerate(filepaths):
        filenames[i] = path.split("/")[-1]
    return filenames


def getUniqueIdentifiers(filenames, separator="_"):
    '''
    Parses the first part of each filename (up until the separator)
    and returns a list with the deleted repetitions.
    '''
    nonUniqueID = [None]*len(filenames)
    for i, name in enumerate(filenames):
        nonUniqueID[i] = name.split("_")[0]
    uniqueID = set(nonUniqueID)
    return sorted(list(uniqueID))


def checkIdentifierForMatches(filenames, identifier):
    '''
    Checks if the filenames match for the identifier provided (if the
    given identifier is a substring of the filename), and returns a list
    with the matches' indices in the filenames array.
    '''
    matchingIx = []
    for i, name in enumerate(filenames):
        if identifier in filenames[i]:
            matchingIx.append(i)
    return matchingIx


def getIdentifierToFilenamesMatches(filenames, identifiers):
    '''
    Iterates through the identifiers array to return a list of lists with the
    ordered matches to the identifiers provided.
    '''
    matchedIndices = []
    for id in identifiers:
        matchingIndices = checkIdentifierForMatches(filenames, id)
        matchedIndices.append(matchingIndices)
    return matchedIndices


def changeSpacerTagInFile(filepath, filename):
    '''
    Removes unnecesary elements on the filename, to append the tag to
    the "spacer" string, and then performs the replacement to the required
    lines (which start with the character: ">")
    '''
    nametag = filename.replace("_", "").replace("spacer.fa", "")
    returnString = ""
    with open(filepath) as file:
        for i, readLine in enumerate(file):
            readLine = readLine.rstrip('\n\r')
            if ">" in readLine:
                printLine = readLine + "_" + nametag
            else:
                printLine = readLine
            returnString = returnString + printLine + "\n"
    return returnString


def generateExportStringFromMatchedIndices(
    filepaths,
    filenames,
    matchedIndices
):
    '''
    Returns the string with the replaced "spacer" elements (with required
    appended elements).
    '''
    fileString = ""
    for i in matchedIndices:
        fileString = fileString + \
            changeSpacerTagInFile(filepaths[i], filenames[i])
    return fileString


def exportFAFiles(
    outputPath,
    identifiers,
    matchedIndices,
    filepaths,
    filenames
):
    '''
    Performs the whole routine given the elements required for the parsing.
    '''
    for i, identifier in enumerate(identifiers):
        nameFile = outputPath + identifiers[i] + "_CRISPRspacer.fa"
        indicesList = matchedIndices[i]
        with open(nameFile, "w") as file:
            file.write(generateExportStringFromMatchedIndices(
                    filepaths, filenames, indicesList
                )
            )


def parseAndMergeFASTAFilesInPath(path, outputPath):
    '''
    Final wrapper that takes only the paths to do the searches, and
    replacements in the files within the input folder.
    '''
    filepaths = readFilepaths(path, extension=".fa")
    if(len(filepaths) > 0):
        filenames = getFilenamesFromPaths(filepaths)
        identifiers = getUniqueIdentifiers(filenames, separator="_")
        matchedIndices = getIdentifierToFilenamesMatches(
            filenames, identifiers
            )
        exportFAFiles(
            outputPath,
            identifiers,
            matchedIndices,
            filepaths,
            filenames
        )
