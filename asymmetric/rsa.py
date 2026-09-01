import math
import secrets


class RSA:

    def __init__(self, key_size=512):
        self.key_size = key_size

        self.p = None
        self.q = None

        self.public_key = None
        self.private_key = None


    def is_probable_prime(self, n, rounds=40):
        # Miller-Rabin test
        if n < 2:
            return False

        if n == 2 or n == 3:
            return True

        if n % 2 == 0:
            return False

        d = n - 1
        s = 0

        while d % 2 == 0:
            d //= 2
            s += 1

        for i in range(rounds):
            a = secrets.randbelow(n - 3) + 2

            x = pow(a, d, n)

            if x == 1 or x == n - 1:
                continue

            for j in range(s - 1):
                x = pow(x, 2, n)

                if x == n - 1:
                    break

            else:
                return False

        return True

    def generate_prime(self, bits):
        while True:
            candidate = secrets.randbits(bits)
            candidate |= (1 << (bits - 1))

            candidate |= 1

            if self.is_probable_prime(candidate):
                return candidate


    def generate_keys(self):
        half_bits = self.key_size // 2

        while True:
            self.p = self.generate_prime(half_bits)
            self.q = self.generate_prime(half_bits)

            if self.p == self.q:
                continue

            n = self.p * self.q

            if n.bit_length() != self.key_size:
                continue

            phi = (self.p - 1) * (self.q - 1)

            e = 65537

            if math.gcd(e, phi) != 1:
                continue

            d = pow(e, -1, phi)

            self.public_key = (e, n)
            self.private_key = (d, n)

            return self.public_key, self.private_key


    def text_to_int(self, text):
        data = text.encode("utf-8")
        return int.from_bytes(data, byteorder="big")


    def int_to_text(self, value):
        length = (value.bit_length() + 7) // 8
        data = value.to_bytes(length, byteorder="big")
        return data.decode("utf-8")


    def encrypt_int(self, message, public_key):
        e, n = public_key
        ciphertext = pow(message, e, n)

        return ciphertext


    def decrypt_int(self, ciphertext, private_key):
        d, n = private_key
        message = pow(ciphertext, d, n)

        return message


    def encrypt(self, plaintext, public_key=None):
        if public_key is None:
            public_key = self.public_key

        message = self.text_to_int(plaintext)

        ciphertext = self.encrypt_int(message, public_key)

        return ciphertext


    def decrypt(self, ciphertext, private_key=None):
        if private_key is None:
            private_key = self.private_key

        message = self.decrypt_int(ciphertext, private_key)

        plaintext = self.int_to_text(message)

        return plaintext


    def factorization_attack(self, public_key=None, max_attempts=100000):
        if public_key is None:
            public_key = self.public_key

        if public_key is None:
            raise ValueError("Public key not available.")

        e, n = public_key

        attempts = 0

        if n % 2 == 0:
            p = 2
            q = n // 2

        else:
            p = None
            q = None

            divisor = 3

            while divisor * divisor <= n:

                attempts += 1

                if attempts >= max_attempts:
                    return {
                        "success": False,
                        "message": "Factorization failed within attempt limit.",
                        "attempts": attempts
                    }

                if n % divisor == 0:
                    p = divisor
                    q = n // divisor
                    break

                divisor += 2

        if p is None:
            return {
                "success": False,
                "message": "Factors not found.",
                "attempts": attempts
            }

        # Reconstruct phi(n)
        phi = (p - 1) * (q - 1)

        # Recover private exponent
        d = pow(e, -1, phi)

        recovered_private_key = (d, n)

        return {
            "success": True,
            "p": p,
            "q": q,
            "private_key": recovered_private_key,
            "attempts": attempts
        }