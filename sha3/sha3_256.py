import sys
from cffi import FFI
import rlp
from rlp.utils import decode_hex, encode_hex

ffi = FFI()
lib = ffi.dlopen("/home/czepluch/Dropbox/prgrms/ethereum/pypy_sha3/lib/libsha3.so")

ffi.cdef('''
         int sha3_256(uint8_t*, size_t, uint8_t const*, size_t);
         ''')
seed = ''
output_length = 32
inpt = ffi.new("uint8_t[]", str(seed))
outpt = ffi.new("uint8_t[]", output_length)
lib.sha3_256(outpt, output_length, inpt, len(seed))

buf = ffi.buffer(outpt, output_length)
printbuf = buf[:]
print(printbuf.encode('hex'))
