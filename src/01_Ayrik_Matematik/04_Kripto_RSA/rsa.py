import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2 - temp1 * x1
        y = y2 - temp1 * y1
        
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        
    if temp_phi == 1:
        return d + phi
    
    return d

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    
    # 1 < e < phi ve gcd(e, phi) = 1 olacak şekilde e seç
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        
    # d * e = 1 (mod phi) olacak şekilde d hesapla
    # Bu adim karmasik oklid algoritmasi (extended euclidean) gerektirir
    # Basitlik icin brute-library kullanilabilir ama burada manuel basit bir 
    # implementasyon yerine sembolik bir fonksiyon kullanacagiz.
    # Not: Yukaridaki inverse fonksiyonu hatali olabilir, 
    # Python 3.8+ pow(e, -1, phi) bunu dogrudan yapar.
    
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    print("--- Basit RSA Implementasyonu ---")
    p = 61
    q = 53
    # Gerçek hayatta bu sayılar devasa olmalıdır
    
    public, private = generate_keypair(p, q)
    print(f"Public Key: {public}")
    print(f"Private Key: {private}")
    
    message = "Hello Math"
    print(f"Orjinal Mesaj: {message}")
    
    encrypted_msg = encrypt(public, message)
    print(f"Şifreli Mesaj: {encrypted_msg}")
    
    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Çözülen Mesaj: {decrypted_msg}")
