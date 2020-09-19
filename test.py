import olefile

assert olefile.isOleFile('blank.hwp')

with olefile.OleFileIO('blank.hwp') as ole:
    ole.dumpdirectory()
