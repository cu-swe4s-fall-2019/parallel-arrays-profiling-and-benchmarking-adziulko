import sys
import hash_functions
import time
import random
import argparse

def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val

class LPHashTable:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0
        self.keys = []

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None

class ChainHashTable:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        self.T[start_hash].append((key,value))
        self.M += 1
        return True

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        for k,v in self.T[start_hash]:
            if key == k:
                return v
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of hash tables',
                                     prog='hash_tables')

    parser.add_argument('--table_size', type=int,
                        help='Size of hash table', required=True)
    parser.add_argument('--hash_method', type=str,
                        help='Algorithm of choice: ascii, rolling, random', required=True)
    parser.add_argument('--collision_strategy', type=str,
                        help='Collision strategy', required=True)
    parser.add_argument('--file_name', type=str,
                        help='Name of the input file', required=True)
    parser.add_argument('--key', type=int,
                        help='Keys to add', required=True)


    args = parser.parse_args()

    N = args.table_size
    hash_alg = args.hash_method
    collision_strategy = args.collision_strategy
    data_file_name = args.file_name
    keys_to_add = args.key


    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_ascii)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_rolling)

    elif hash_alg == 'python':
        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.random_h_function)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.random_h_function)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.insert(l, l)
        t1 = time.time()
        print('insert', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break


    for v in V:
        t0 = time.time()
        r = ht.find(v)
        t1 = time.time()
        print('search', t1 - t0)
