class Substitution:
    def _keygen(self,key):
        key = key.upper()

        if len(key) != 26 or len(set(key)) != 26:
            raise ValueError("Key must contain 26 unique letters")


    def encrypt(self, pt:str, key:str):
        ct = ""

        key = self._keygen(key)

        for i in pt:
            if i.isalpha():
                if i.isupper():
                    ct += key[ord(i) - ord('A')]
                else:
                    ct += key[ord(i) - ord('a')].lower()
            else:
                ct += i

        return ct

    def decrypt(self, ct:str, key:str):
        pt = ""

        key = self._keygen(key)

        for i in ct:
            if i.isalpha():
                index = key.index(i.upper())

                if i.isupper():
                    pt += chr(ord('A') + index)
                else:
                    pt += chr(ord('a') + index)
            else:
                pt += i

        return pt