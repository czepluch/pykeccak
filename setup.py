from setuptools import setup, Extension
from cffi import FFI

pykeccak = Extension('pykeccak',
                      sources=['lib/sha3.c'],
                      depends=['lib/compiler.h', 'lib/sha3.h'],
                      extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"]
                     )


setup(name="pykeccak",
      version='0.1',
      description="Keccak 256 hashing for PyPy2",
      author="Jacob Stenum Czepluch",
      author_email="j.czepluch@gmail.com",
      url="https://github.com/czepluch/pykeccak",
      ext_modules=[pykeccak],
      install_requires=["cffi>=1.2.1"],
      setup_requires=["cffi>=1.2.1"],
      )

# cffi specific setup.
ffi = FFI()

ffi.set_source("_keccak", None)
ffi.cdef('''
         int sha3_256(uint8_t*, size_t, uint8_t const*, size_t);
         ''')

if __name__ == '__main__':
    ffi.compile()
