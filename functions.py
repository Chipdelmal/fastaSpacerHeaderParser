import glob


def readFilepaths(experimentPath, extension=".fa"):
    filepaths = glob.glob(experimentPath + "/" + "*" + extension)
    return sorted(filepaths)


def getFilenamesFromPaths(filepaths):
    filenames = [None]*len(filepaths)
    for i, path in enumerate(filepaths):
        filenames[i] = path.split("/")[-1]
    return filenames


def getUniqueIdentifiers(filenames, separator="_"):
    nonUniqueID = [None]*len(filenames)
    for i, name in enumerate(filenames):
        nonUniqueID[i] = name.split("_")[0]
    uniqueID = set(nonUniqueID)
    return sorted(list(uniqueID))


def checkIdentifierForMatches(filenames, identifier):
    matchingIx = []
    for i, name in enumerate(filenames):
        if identifier in filenames[i]:
            matchingIx.append(i)
    return matchingIx


def getIdentifierToFilenamesMatches(filenames, identifiers):
    matchedIndices = []
    for id in identifiers:
        matchingIndices = checkIdentifierForMatches(filenames, id)
        matchedIndices.append(matchingIndices)
    return matchedIndices


def changeSpacerTagInFile(filepath, filename):
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
    for i, identifier in enumerate(identifiers):
        nameFile = outputPath + identifiers[i] + "_CRISPRspacer.fa"
        indicesList = matchedIndices[i]
        with open(nameFile, "w") as file:
            file.write(generateExportStringFromMatchedIndices(
                    filepaths, filenames, indicesList
                )
            )


def parseAndMergeFASTAFilesInPath(path, outputPath):
    filepaths = readFilepaths(path, extension=".fa")
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
