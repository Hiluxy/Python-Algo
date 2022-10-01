from contextlib import nullcontext
import re
new_id='abcd'
S = re.sub(r'[^a-z]', '', new_id)
N = re.sub(r'[^0-9]', '', new_id)
if N=='':
    N='0'
print(N)