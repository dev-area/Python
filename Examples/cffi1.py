from cffi import FFI

ffi = FFI()

ffi.cdef("""
int add(int, int);
""")

C = ffi.verify("""
int add(int a, int b) {
return a + b; }
""")

print (C.add(21, 21))
