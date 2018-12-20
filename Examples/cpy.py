import ctypes

ml = ctypes.cdll.LoadLibrary("./libsimp.so")

print(ml.add(2,4))

