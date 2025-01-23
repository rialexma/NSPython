import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

def hex_cde(code):
    code = code[:8] + '-' + code[8:]
    code = code[:13] + '-' + code[13:]
    code = code[:18] + '-' + code[18:]
    code = code[:23] + '-' + code[23:]
    return code
    

GUID = input()
result = hex_cde(GUID)

print(GUID)
print(result)