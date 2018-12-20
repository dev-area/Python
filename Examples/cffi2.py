from cffi import FFI

ffi = FFI()


ffi.cdef("""
    int add(int, int);
""")

C = ffi.dlopen("./libsimp.so")

print(C.add(2,3))
