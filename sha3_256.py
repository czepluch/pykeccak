import os
from _sha3 import ffi

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'build/lib.linux-x86_64-2.7/pypy-sha3.pypy-26.so')
lib = ffi.dlopen(filename)

output_length = 32
outpt = ffi.new("uint8_t[]", output_length)


def sha3_256(seed):
    inpt = ffi.new("uint8_t[]", str(seed))
    lib.sha3_256(outpt, output_length, inpt, len(seed))
    buf = ffi.buffer(outpt, output_length)
    return buf[:]

printbuf = sha3_256('')
print(printbuf.encode('hex'))
