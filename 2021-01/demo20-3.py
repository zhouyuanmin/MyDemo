import random
import hashlib

m = hashlib.md5()
bb = [
    b"['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']\n",
    b'3\n']
cc = [
    b"['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']\n",
    b'4\n']
m.update(b''.join(cc))
d = m.hexdigest()
print(type(d))
print(d)
'202cb962ac59075b964b07152d234b70'
