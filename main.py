import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def rsa():
    print("\n--- RSA ---")
    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))
    if not is_prime(p) or not is_prime(q):
        print("Ошибка: p или q не простые числа!")
        return
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while math.gcd(e, phi) != 1:
        e += 1

    d = 1
    while (e * d) % phi != 1:
        d += 1

    print(f"Открытый ключ: (e={e}, n={n})")
    print(f"Закрытый ключ: (d={d}, n={n})")

    m = int(input("Введите число m для шифрования (m < n): "))
    if m >= n:
        print("Ошибка: m должно быть меньше n!")
        return

    c = (m ** e) % n
    print(f"Зашифрованное сообщение: {c}")

    m2 = (c ** d) % n
    print(f"Расшифрованное сообщение: {m2}")

def main():
    print("Простая утилита: RSA и Diffie-Hellman")
    rsa()

if __name__ == '__main__':
    main()
