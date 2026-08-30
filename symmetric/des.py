import secrets

class DES:
    def __init__(self):
        self.ip = [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
        ]
        self.ipi = [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
        ]

        self.PC1 = [
            57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4
        ]
        self.PC2 = [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32
        ]
        self.shift = [
            1, 1, 2, 2,
            2, 2, 2, 2,
            1, 2, 2, 2,
            2, 2, 2, 1
        ]
        self.E = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        ]
        self.S_BOXES = [
            [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
            ],
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
            ],
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
            ],
            [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
            ],
            [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
            ],
            [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
            ],
            [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
            ],
            [
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
            ]
        ]
        self.P = [
            16, 7, 20, 21,
            29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25
        ]

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


    def generate_key(self):
        key= bin(secrets.randbits(64))[2:].zfill(64)
        return key

    def left_shift(self, bits, n):
        return bits[n:]+bits[:n]

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

            row = int(block[0]+block[5],2)
            col = int(block[1:5],2)

            value = self.S_BOXES[i][row][col]

            result += bin(value)[2:].zfill(4)

        return result

    def feistel(self, r, round_key):
        r = self.expand(r)
        r = self.xor(r, round_key)
        r = self.s_box_substitution(r)
        r = self.permute(r, self.P)

        return r        

    def one_round(self, l, r, round_key):
        new_l = r
        new_r = self.xor(l, self.feistel(r, round_key))

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