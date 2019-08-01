import itertools as it

def chunkify(a, k):
    return it.zip_longest(*[iter(a)]*k)

