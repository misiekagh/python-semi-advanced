import time
def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %f sec' % (method.__name__, args, kw, te-ts))
        return result

    return timed
