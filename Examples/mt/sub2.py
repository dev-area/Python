import subprocess
import sys

proc = subprocess.Popen([sys.executable, 'myapp.py', 'data'],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE)
(output, error) = proc.communicate()
if error != None:
    print("error:", error.decode())
print("output:", output.decode())
