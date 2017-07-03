@SET PATH=%PATH%;"C:\Python27"
@SET PYTHONPATH=C:\Python27\Lib

@ASSOC .py=Python.File
@ASSOC .pyc=Python.CompiledFile
@ASSOC .pyo=Python.CompiledFile
@ASSOC .pyw=Python.NoConFile

@FTYPE Python.CompiledFile="C:\Python27\python.exe" "%%1" %%*
@FTYPE Python.File="C:\Python27\python.exe" "%%1" %%*
@FTYPE Python.NoConFile="C:\Python27\pythonw.exe" "%%1" %%*
@SET PATHEXT=.py;%PATHEXT%


