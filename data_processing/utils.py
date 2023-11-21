from pathlib import Path

def getPath(targetDir, globStr, targetDirList=None):
    if targetDirList is None:
        targetDirList = list()

    childDirList = list(targetDir.iterdir())
    for childDir in childDirList:
        if childDir.is_dir():
            targetDirList = getPath(childDir, globStr, targetDirList)

    targetList = list(targetDir.glob(globStr))

    if len(targetList) > 0:
        targetDirList = targetDirList+targetList
        return targetDirList
    else:
        return targetDirList