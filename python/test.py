# import subprocess
# import inspect

# p = subprocess.Popen("echo 'name'", stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
# print p.communicate()
# print inspect.stack()[0][1]

import re
print re.match(r"ravi.", "ravichandran").group()