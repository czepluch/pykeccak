from keccak import sha3_256


def sha3(seed):
    return sha3_256(seed).encode('hex')


def test_empty_string():
    assert sha3('') == 'c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'


def test_short_string():
    """test for string `hello`"""
    assert sha3('hello') == '1c8aff950685c2ed4bc3174f3472287b56d9517b9c948127319a09a7a36deac8'
