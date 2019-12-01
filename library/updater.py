import requests
class updater(object):
    def __new__(cls, SHA512HASH=None, Version=None):
        cls.__init__(cls, SHA512HASH, Version)
        return cls.main(cls)
    def __init__(self, SHA512HASH=None, Version=None):
        if SHA512HASH != None:
            self.SHA512HASH = SHA512HASH
            self.VERSION = Version
        else:
            raise IOError("No SHA-512 Hash given")
    def main(self):
        self.GET(self)
        self.PARSE(self)
        self.PARSE_DATA(self)
        self.CURRENTARRAY = self.find_element(self)
        self.CURRENT_VERSION = self.CURRENTARRAY[1]
        self.TYPE = self.CURRENTARRAY[len(self.CURRENTARRAY) - 1]
        try:
            return eval("self.S"+str(self.TYPE)+"(self)")
        except:
            raise TypeError("No Type Found in Manifest")
    def GET(self):
        self.RESPONSE = requests.get('https://www.dropbox.com/s/q179icv5j6o5t6h/MANIFEST.txt?dl=1')
    def PARSE(self):
        self.DATA = self.RESPONSE.content.decode("ISO-8859-1").replace("\r", "").replace("\t", "").split("\n")
    def PARSE_DATA(self):
        for x in range(len(self.DATA)):
            self.DATA[x] = self.DATA[x].split("!")
            self.DATA[x].append(len(self.DATA[x]))
    def find_element(self):
        TEMP = None
        for x in range(len(self.DATA)):
            if self.DATA[x][0] == self.SHA512HASH:
                TEMP = self.DATA[x]
        if TEMP != None:
            return TEMP
        else:
            raise IOError("No SHA-512 Hash Found")
    def S2(self):
        if self.VERSION == self.CURRENT_VERSION:
            return True
        else:
            return False
    def S3(self):
        return






