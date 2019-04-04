import inspect
import sys


# https://kb.froglogic.com/display/KB/Article+-+Using+Squish+functions+in+your+own+Python+modules+or+packages

def importSquishSymbols(import_into_module=None):
    if import_into_module is None:
        frame = inspect.stack()[1]
        fn = frame[1]
        mn = "PageObjects." + inspect.getmodulename(fn)
        import_into_module = sys.modules[mn]
    squish_module = sys.modules["squish"]
    for n in dir(squish_module):
        setattr(import_into_module, n, getattr(squish_module, n))
    setattr(import_into_module, "test", sys.modules["test"])
    setattr(import_into_module, "testData", sys.modules["testData"])
    setattr(import_into_module, "object", sys.modules["object"])
    setattr(import_into_module, "objectMap", sys.modules["objectMap"])
    setattr(import_into_module, "squishinfo", sys.modules["squishinfo"])
