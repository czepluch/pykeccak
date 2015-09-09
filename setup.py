from setuptools import setup, Extension

pypy_sha3 = Extension('pypy-sha3',
                      sources=['lib/sha3.c'],
                      depends=['lib/compiler.h', 'lib/sha3.h'],
                      extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"])


setup(name="pypy-sha3",
      version='0.1',
      description="Keccak sha3-256 hashing for PyPy2",
      author="Jacob Stenum Czepluch",
      author_email="j.czepluch@gmail.com",
      url="https://github.com/czepluch/pypy_sha3",
      ext_modules=[pypy_sha3],
      setup_requires=["cffi>=1.0.0"],
      cffi_modules=["sha3_256/sha3_build.py:ffi"],
      install_requires=["cffi>=1.0.0"],
      )
from cffi import FFI

ffi = FFI()

ffi.set_source("_sha3", None)
ffi.cdef('''
         int sha3_256(uint8_t*, size_t, uint8_t const*, size_t);
         ''')

if __name__ == '__main__':
    ffi.compile()
