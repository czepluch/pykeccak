from distutils.core import setup, Extension

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
      ext_modules=[pypy_sha3]
      )
