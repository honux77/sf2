import os

def enc(f):
    import codecs
    BLOCKSIZE = 1024 # or some other, desired size in bytes
    with codecs.open(sourceFileName, "r", "euc-kr") as sourceFile:
        with codecs.open(targetFileName, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)

def changeEncoding(f):
    if os.path.isdir(f):
        files = os.listdir(f)
        print(files)
        for sub in files:
            fullname = ps.path.join(f, sub)
            print(fullname)
    if os.path.isfile():
        print(f + "is a file")

changeEncoding("./")