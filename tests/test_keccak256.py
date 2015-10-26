from keccak import sha3_256
from keccak import sha3_512


def s256(seed):
    return sha3_256(seed).hexdigest()


def s512(seed):
    return sha3_512(seed).hexdigest()


def test_empty_string():
    assert s256('') == 'c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'
    assert s512('') == '0eab42de4c3ceb9235fc91acffe746b29c29a8c366b7c60e4e67c466f36a4304c00fa9caf9d87976ba469bcbe06713b435f091ef2769fb160cdab33d3670680e'


def test_short_string():
    """test for string `hello`"""
    assert s256('hello') == '1c8aff950685c2ed4bc3174f3472287b56d9517b9c948127319a09a7a36deac8'
    assert s512('hello') ==  '52fa80662e64c128f8389c9ea6c73d4c02368004bf4463491900d11aaadca39d47de1b01361f207c512cfa79f0f92c3395c67ff7928e3f5ce3e3c852b392f976'


def test_update():
    k = sha3_256()
    assert k.seed == ''

    k.update('')
    assert k.seed == ''

    k.update("foo")
    assert k.seed == "foo"

    k.update(" bar")
    assert k.seed == "foo bar"
