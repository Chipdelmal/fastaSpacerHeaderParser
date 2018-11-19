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
    """
    Description:
    In:
    Out:
    """
    filepaths = sorted(
        glob.glob(
            experimentPath + "/" + "*" + extension
        )
    )
    return filepaths

def getFilenamesFromPaths(filepaths):
    """
    Description:
    In:
    Out:
    """
    filenames=[None]*len(filepaths)
    for i, path in enumerate(filepaths):
        filenames[i]=path.split("/")[-1]
    return filenames
