import hashlib
import random

g = 2
# print(f'Base: {g}')
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
# print(f'Numero primo: {p}')

a = random.getrandbits(256)
# print(f'\nLlave privada de Alice: {a}')
b = random.getrandbits(256)
# print(f'Llave privada de Bob: {b}')
e = random.getrandbits(256)
# print(f'Llave privada de Eve: {e}')

# print('\nIntecambio de llaves')
A = pow(g, a, p)
B = pow(g, b, p)
E = pow(g, e, p)
# print(A)
# print(B)
# print(E)

# print('\nModular Inverso')
# s1 = pow(A, b, p)
# s2 = pow(B, a, p)

# print(s1)
# print(s2)

alice_eve = pow(A, e, p)
eve_alice = pow(E, a, p)

if eve_alice == alice_eve:
    shared_key = hashlib.sha256(str(eve_alice).encode()).hexdigest()
    print(f'Llave secreta compartida por Alice y Bob (Eve): {shared_key}')
else:
    print('Las llaves secretas no son iguales')
    
bob_eve = pow(B, e, p)
eve_bob = pow(E, b, p)

if eve_bob == bob_eve:
    shared_key = hashlib.sha256(str(eve_bob).encode()).hexdigest()
    print(f'Llave secreta compartida por Bob y Alice (Eve): {shared_key}')
else:
    print('Las llaves secretas no son iguales')
    

if bob_eve == alice_eve:
    shared_key = hashlib.sha256(str(bob_eve).encode()).hexdigest()
    print(f'Llave secreta compartida por Bob y Alice: {shared_key}')
else:
    print('Las llaves secretas no son iguales')