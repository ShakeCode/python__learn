import  sys
import platform
import  os
print(str(sys.argv))
print(os.getcwd())
print(platform.platform())
print(sys.path)

import site
print(site.getsitepackages())
