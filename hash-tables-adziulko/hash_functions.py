import sys


def h_ascii(key, N):

    if key is None:
        raise TypeError("Key must not be None")

    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_rolling(key, N):
    '''  p a prime number roughly equal to the number of characters in the input alphabet
         m should be a large number, since the probability of two random strings colliding is
           about 1/m. Sometimes m=2^64 is chosen'''

    if key is None:
        raise TypeError("Key must not be None")

    s = 0
    p = 29
    m = 2**64
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N


def random_h_function(key, N):
    """
       Compute a hash of the val string that is in [0 ... N).
    """

    if key is None:
        raise TypeError("Key must not be None")


    hashcode = 0
    for i in range(len(key)):
        hashcode = (71 * hashcode + ord(key[i])) % N
    return hashcode
