

def stupid_chain(*iters):
    store= []
    for item in iters:
        for thing in item:
            store.append(thing)

    return store


def lazy_chain(*iters):
    for item in iters:
        for thing in item:
            yield thing


def chain(*iters):
    for i in iters:
        yield from i


assert list(lazy_chain("abc", [1,2,3,])) == stupid_chain("abc", [1,2,3,])
assert list(chain("abc", [1,2,3,])) == stupid_chain("abc", [1,2,3,])

