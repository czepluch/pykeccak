
from cffi import FFI

ffi = FFI()
ffi.set_source("_sha3", None)
ffi.cdef('''
         int sha3_256(uint8_t*, size_t, uint8_t const*, size_t);
         ''')

if __name__ == '__main__':
    ffi.compile()
