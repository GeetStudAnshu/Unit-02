#WAP to implement the use of hashtables by calculating a key's hash value.

def hash_key( key, i):
    return key % i

i = 7

print(f'The hash value for 3 is {hash_key(3,i)}')
print(f'The hash value for 2 is {hash_key(2,i)}')
print(f'The hash value for 9 is {hash_key(9,i)}')
print(f'The hash value for 11 is {hash_key(11,i)}')
print(f'The hash value for 7 is {hash_key(7,i)}')