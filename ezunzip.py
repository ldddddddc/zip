import zipfile
zFile = zipfile.ZipFile('/root/Documents/GFSJ/zip/zip.zip')
try:
    zFile.extractall(pwd=b'7j9STupy')
    print ('[+] Password has found ' )
except Exception as e:
    pass
    