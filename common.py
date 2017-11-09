#!/usr/bin/env python2

def random_mod(m):
    x = ord(os.urandom(1)[0])
    while x>=m:
        x = ord(os.urandom(1)[0])
    return m

def xor_str(s1,s2):
    "xor two strings of equal size"
    return "".join([chr(ord(c1)^ord(c2)) for c1,c2 in zip(s1,s2)])

def null_padding(s,n):
    "either truncate or padd with null bytes"
    if len(s)<=n:
        return s + ("\0"*(n-len(s)))
    else:
        return s[:n]

def shiftr_i32(x, n):
    "shift integer n right by b bits"
    return (x & 0xffffffff) >> n

def rotr_i32(x, n):
    "Rotate integer n right bn b bits"
    return (((x & 0xffffffff) >> (n & 31)) | (x << (32 - (n & 31)))) & 0xffffffff

