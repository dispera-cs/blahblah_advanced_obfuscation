import base64
import zlib
import os
import random
import string
import marshal

print("Welcome to Blah Blah advanced python code obfuscation!\n\n")

script_directory = input("Enter the directory path of the Python script: ")

script_code = ""
with open(script_directory, 'r') as file:
    script_code = file.read()

encoded_code = base64.b64encode(script_code.encode()).decode()

compressed_code = zlib.compress(encoded_code.encode())

variable_name = ''.join(random.choices(string.ascii_letters, k=10))

control_flow_code = []
for c in compressed_code:
    control_flow_code.append(str(ord(chr(c))))

encrypted_code = ''.join(chr((int(c) + 5) % 256) for c in control_flow_code)
encrypted_code = base64.b64encode(encrypted_code.encode()).decode()

dynamic_code = f'''
import zlib, base64, marshal, random, string
{variable_name} = base64.b64decode('{encrypted_code}').decode()
exec(zlib.decompress(bytes({variable_name}, 'utf-8')).decode())
'''

obfuscated_code = marshal.dumps(compile(dynamic_code, '', 'exec'))

obfuscated_variable = ''.join(random.choices(string.ascii_letters, k=10))

final_code = f'''
import marshal, zlib, base64, random, string
{obfuscated_variable} = {obfuscated_code}
exec(marshal.loads({obfuscated_variable}))
'''

with open('obfuscated.py', 'w') as file:
    file.write(final_code)
