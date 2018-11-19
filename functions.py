# I wanna merge (for example)
# MN184_CRISPR3spacer.fa and MN184_CRISPR4spacer.fa
# into MN184_CRISPRspacer.fa
# with sequence names each annotated.
#
# Now, the sequence name looks like
# >spacer1
# >spacer2
# ......
#
# I wanna change it into (for MN184)
# >spacer1_MN184CRISPR3
# >spacer2_MN184CRISPR4

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
