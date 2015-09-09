import sha3_256

def empty_string():
    assert sha3_256('').encode('hex') == 'c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'
