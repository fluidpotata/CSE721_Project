class Caeser:
    def encrypt(self, pt:str, key:int):
        ct = ""
        for i in pt:
            ct += chr(ord(i)+key)
        
        return ct

    def decrypt(self, ct:str, key:int):
        pt = ""
        for i in ct:
            pt += chr(ord(i)-key)

        return pt