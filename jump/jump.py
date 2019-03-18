
def jump(key, buckets):
    """implementation of consistent hashing algorithm
    this algorithm described on this http://arxiv.org/abs/1406.2294
    """
    result = -1
    i = 0
    while i < buckets:
        result = i
        key *= 2862933555777941757 + 1
        i = (result + 1) * ((1 << 31)/(divv(key, 33)) + 1)
    return result

def divv(x, times):
    for i in range(times):
        x /= 2
    return x 