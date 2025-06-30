import math

# Проверка простоты числа

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#  RSA

def rsa():
    print("\n--- RSA ---")
    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))
    if not is_prime(p) or not is_prime(q):
        print("Ошибка: p или q не простые числа!")
        return
    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбор открытой экспоненты e
    e = 2
    while math.gcd(e, phi) != 1:
        e += 1

    # Поиск закрытой экспоненты d
    d = 1
    while (e * d) % phi != 1:
        d += 1

    print(f"Открытый ключ: (e={e}, n={n})")
    print(f"Закрытый ключ: (d={d}, n={n})")

    m = int(input("Введите число m для шифрования (m < n): "))
    if m >= n:
        print("Ошибка: m должно быть меньше n!")
        return

    # Шифрование
    c = (m ** e) % n
    print(f"Зашифрованное сообщение: {c}")

    # Дешифрование
    m2 = (c ** d) % n
    print(f"Расшифрованное сообщение: {m2}")

# функция Диффи-Хеллмана

def diffie():
    print("\n--- Диффи-Хелман ---")
    p = int(input("Введите простое число p: "))
    if not is_prime(p):
        print("Ошибка: p не простое число!")
        return
    g = int(input("Введите генератор g: "))
    a = int(input("Сторона A: введите секретное число a: "))
    b = int(input("Сторона B: введите секретное число b: "))

    A = (g ** a) % p
    B = (g ** b) % p
    print(f"A отправляет B: {A}")
    print(f"B отправляет A: {B}")

    s1 = (B ** a) % p
    s2 = (A ** b) % p
    print(f"Секрет, вычисленный A: {s1}")
    print(f"Секрет, вычисленный B: {s2}")

    if s1 == s2:
        print("Успех: секреты совпадают!")
    else:
        print("Ошибка: секреты не совпадают...")

# Запуск

def main():
    print("Простая утилита: RSA и Diffie-Hellman")
    rsa()
    diffie()

if __name__ == '__main__':
    main()
