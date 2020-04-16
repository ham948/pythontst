#!/usr/bin/python3
#path test file pwd etc.
import os
from pathlib import Path

print(Path.cwd())
print(Path.home())
i=input()
os.makedirs(f'./test{i}/test{i}/teest{i}')
