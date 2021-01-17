import sys
from pathlib import Path

root_dir = str(Path('..').absolute().resolve())

sys.path.append(root_dir)

print(f"-> Appended root dir: `{root_dir}`")

from pack1 import m1  # now we can import pack1 stuff from root dir

m1.hello()
