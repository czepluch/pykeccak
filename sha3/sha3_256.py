from cffi import FFI

seed = ""

ffi = FFI()

lib = ffi.dlopen("./libsha3.so")

ffi.cdef('''
         int sha3_256(uint8_t*, size_t, uint8_t const*, size_t);
         ''')

inpt = ffi.new("uint8_t[]", seed)
outpt = ffi.new("uint8_t[]", 32)
output_length = 32

sha3 = lib.sha3_256(outpt, output_length, inpt, len(inpt))

buf = ffi.buffer(outpt, output_length)

j = buf[:]

print(j)
lib.free(buf[:])
