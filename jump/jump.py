def jump(key, buckets):
    """implementation of consistent hashing algorithm
    this algorithm described on this http://arxiv.org/abs/1406.2294
    """
    result = -1
    i = 0
    while i < buckets:
        result = i
        key = (key * int(2862933555777941757) + 1) & 0xffffffffffffffff
        i = int(((result + 1) * (1 << 31))/((key >> 33) + 1))
    return result