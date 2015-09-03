from _sha3 import ffi

lib = ffi.dlopen("/home/czepluch/Dropbox/prgrms/ethereum/pypy_sha3/lib/libsha3.so")

output_length = 32
outpt = ffi.new("uint8_t[]", output_length)


def sha3_256(seed):
    inpt = ffi.new("uint8_t[]", str(seed))
    lib.sha3_256(outpt, output_length, inpt, len(seed))
    buf = ffi.buffer(outpt, output_length)
    return buf[:]

printbuf = sha3_256('')
print(printbuf.encode('hex'))
