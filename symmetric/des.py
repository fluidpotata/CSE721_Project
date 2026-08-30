import secrets

class DES:
    # to do: add fixed matrices for dsa
    ip = []
    ipi = []
    PC1 = []
    PC2 = []
    shift = []
    E = []
    S_BOXES = []

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
        return self.permute(bits, self.ip)

    def split_block(self, bits:str):
        l = bits[:32]
        r = bits[32:]

        return l, r

    def final_permutation(self, bits):
        return self.permute(bits, self.ipi)

    # todo: key generation, shift, round keys
    def generate_key(self):
        key= bin(secrets.randbits(64))[2:].zfill(64)
        return key

    def left_shift(self, bits, n):
        return bits[n:]+bits[n]

    def generate_round_keys(self, key):
        round_keys = []
        key = self.permute(key, self.PC1)

        c = key[:28]
        d = key[28:]

        for i in range(16):
            c = self.left_shift(c, self.shift[i])
            d = self.left_shift(d, self.shift[i])

            combined = c+d

            round_key = self.permute(combined, self.PC2)
            round_keys.append(round_key)

        return round_keys

    def expand(self, r):
        return self.permute(r, self.E)

    def s_box_substitution(self, bits):
        result = ""
        for i in range(8): #48 bits divided into  6 so 8 loop
            block = bits[i*6:(i+1)*6] #0-6,6-12,12-18...

            row = int(block[0]+block[5])
            col = int(block[1:5])

            value = self.S_BOXES[i][row][col]

            result += bin(value)[2:].zfill(4)

        return result

    def feistel(self, r, round_key):
        r = self.expand(r)
        r = self.xor(r, round_key)
        r = self.s_box_substitution(r)
        r = self.permute(r, self.P)

        return r        

    def one_round(self, l, r):
        new_l = r
        new_r = self.xor(l, self.feistel(r))

        return new_l, new_r

    def encrypt_block(self, block, round_keys):
        block = self.initial_permutation(block)
        l,r = self.split_block(block)

        for i in range(16):
            l,r = self.one_round(l,r,round_keys[i])

        block = r+l

        block = self.final_permutation(block)

        return block

    def decrypt_block(self, block, round_keys):
        block = self.initial_permutation(block)
        l,r = self.split_block(block)

        for i in range(16):
            l,r = self.one_round(l,r,round_keys[15-i])

        block = r+l

        block = self.final_permutation(block)

        return block

    def pad(self, pt):
        padding_bit = 8 - (len(pt)%8)
        for i in range(padding_bit):
            pt+=chr(padding_bit)
        return pt

    def unpad(self, pt):
        padding_bit = ord(pt[-1])
        return pt[:-padding_bit]


    def text_to_bits(self, text:str):
        bits = ""

        for i in text:
            bits += bin(ord(i))[2:].zfill(8)

        return bits

    def bits_to_text(self, bits):
        text = ""

        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            text += chr(int(byte, 2))

        return text


    def encrypt(self, pt):
        key = self.generate_key()
        round_keys = self.generate_round_keys(key)

        pt = self.pad(pt)
        bits = self.text_to_bits(pt)

        ct = ""

        for i in range(0, len(bits), 64):
            block = bits[i:i+64]
            ct+=self.encrypt_block(block, round_keys)

        return ct, key, round_keys


    def decrypt(self, ct, key):
        round_keys = self.generate_round_keys(key)

        bits = ""

        for i in range(0, len(ct), 64):
            block = ct[i:i+64]
            bits += self.decrypt_block(block, round_keys)

        pt = self.bits_to_text(bits)
        pt = self.unpad(pt)

        return pt