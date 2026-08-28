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


    # todo: key generation, shift, round keys




def text_to_bits(text:str):
    bits = ""

    for i in text:
        bits += bin(ord(i))[2:].zfill(8)

    return bits