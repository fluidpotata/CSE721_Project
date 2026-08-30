import secrets


class ECC:

    # y² = x³ + ax + b (mod p)

    def __init__(self, p, a, b, G, n):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n

        if not self.is_on_curve(G):
            raise ValueError("G is not on the curve")


    def extended_gcd(self, a, b):
        if b == 0:
            return a, 1, 0

        gcd, x1, y1 = self.extended_gcd(b, a % b)

        x = y1
        y = x1 - (a // b) * y1

        return gcd, x, y

    def mod_inverse(self, x):
        x %= self.p

        gcd, inv, _ = self.extended_gcd(x, self.p)

        if gcd != 1:
            raise ValueError("Modular inverse doesnt exist")

        return inv % self.p


    def is_on_curve(self, P):
        if P is None:
            return True

        x, y = P

        left = (y * y) % self.p
        right = (x ** 3 + self.a * x + self.b) % self.p

        return left == right

    def point_neg(self, P):
        if P is None:
            return None

        x, y = P

        return x, (-y) % self.p


    def point_add(self, P, Q):
        if P is None:
            return Q

        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and (y1 + y2) % self.p == 0:
            return None

        if P == Q:
            if y1 % self.p == 0:
                return None

            numerator = (3 * x1 * x1 + self.a) % self.p
            denominator = (2 * y1) % self.p

        else:
            numerator = (y2 - y1) % self.p
            denominator = (x2 - x1) % self.p

        slope = (
            numerator *
            self.mod_inverse(denominator)
        ) % self.p

        x3 = (
            slope * slope
            - x1
            - x2
        ) % self.p

        y3 = (
            slope * (x1 - x3)
            - y1
        ) % self.p

        R = (x3, y3)

        if not self.is_on_curve(R):
            raise ValueError("Point addition produced invalid point")

        return R


    def scalar_mult(self, k, P):
        if k == 0 or P is None:
            return None

        result = None
        current = P

        while k > 0:
            if k & 1:
                result = self.point_add(result, current)

            current = self.point_add(current, current)

            k >>= 1

        return result


    def list_multiples(self, P=None):
        if P is None:
            P = self.G

        points = []

        current = None

        for i in range(1, self.n + 1):
            current = self.point_add(current, P)

            points.append((i, current))

            if current is None:
                break

        return points


    def generate_private_key(self):
        return secrets.randbelow(self.n - 1) + 1


    def generate_public_key(self, private_key):
        return self.scalar_mult(private_key, self.G)


    def generate_keys(self):
        private_key = self.generate_private_key()
        public_key = self.generate_public_key(private_key)

        return private_key, public_key


    def ecdh(self, alice_private, bob_private):
        alice_public = self.scalar_mult(
            alice_private,
            self.G
        )

        bob_public = self.scalar_mult(
            bob_private,
            self.G
        )

        alice_shared = self.scalar_mult(
            alice_private,
            bob_public
        )

        bob_shared = self.scalar_mult(
            bob_private,
            alice_public
        )

        if alice_shared != bob_shared:
            raise ValueError("ECDH key exchange failed")

        return {
            "alice_private": alice_private,
            "alice_public": alice_public,
            "bob_private": bob_private,
            "bob_public": bob_public,
            "shared_key": alice_shared
        }