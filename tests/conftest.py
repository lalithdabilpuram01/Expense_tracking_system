import os
import sys


project_root = os.path.join(os.path.dirname(__file__),'..')
print("project root : ",project_root)
sys.path.insert(0,project_root)
print("**file**",project_root)