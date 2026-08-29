class DES:
    # to do: add fixed matrices for dsa
    self.ip = []

    def permute(self, bits:str, table:list):
        result = ""

        for i in table:
            result += bits[i - 1]

        return result

    def xor(self, a:str, b:str):
        result = ""

        for i in range(len(a)):
            if a[i] == b[i]:
                result += "0"
            else:
                result += "1"

        return result

    def initial_permutation(self, bits):
        self.permute(bits, self.ip)

    def split_block(self, bits:str):
        l = bits[:32]
        r = bits[32:]

        return l, r

    def final_permutation(self):
        pass

    # todo: key generation, shift, round keys
    def generate_key(self):
        pass

    def left_shift(self):
        pass

    def generate_round_keys(self, key):
        pass

    def expand(self, r):
        pass

    def s_box_substitution(self, bits):
        pass

    def feistel(self):
        pass

    def round(self):
        pass

    def encrypt_block(self):
        pass

    def decrypt_block(self):
        pass

    def pad(self):
        pass

    def unpad(self):
        pass


    def text_to_bits(self, text:str):
        bits = ""

        for i in text:
            bits += bin(ord(i))[2:].zfill(8)

        return bits

    def bits_to_text(self, bits):
        pass


    def encrypt(self):
        pass

    def decrypt(self):
        pass