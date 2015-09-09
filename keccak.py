import os
import glob
from _keccak import ffi

# Use relative path to generated shared object
dir = os.path.dirname(__file__)
filepath = glob.glob('build/*/*.so')
filename = os.path.join(dir, filepath[0])
# Open the shared object to use with ffi
lib = ffi.dlopen(filename)

# Length of the output of sha256
output_length = 32
# ffi definition of the output uint array
outpt = ffi.new("uint8_t[]", output_length)


# SHA3-256 hashing using the Keccak standard
def sha3_256(seed):
    inpt = ffi.new("uint8_t[]", str(seed))
    lib.sha3_256(outpt, output_length, inpt, len(seed))
    buf = ffi.buffer(outpt, output_length)
    return buf[:]

# bf = sha3_256('')
# print(bf.encode('hex'))
