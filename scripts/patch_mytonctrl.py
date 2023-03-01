# # patch /usr/src/mytonctrl/mytonctrl.py
# with open('/usr/src/mytonctrl/mytonctrl.py', 'r') as f:
#     code = f.read()

# lines = code.split('\n')

# new_lines = []
# for idx, line in enumerate(lines):
#     new_line = line
#     # if idx >= 321 and idx <= 331:
#     #     new_line = '#' + line
#     new_lines.append(new_line)

# new_code = '\n'.join(new_lines)
# with open('/usr/src/mytonctrl/mytonctrl.py', 'w') as f:
#     f.write(new_code)

# # patch /usr/src/mytonctrl/mypylib/mypylib.py
# with open('/usr/src/mytonctrl/mypylib/mypylib.py', 'r') as f:
#     code = f.read()

# lines = code.split('\n')

# new_lines = []
# skipping = False
# for idx, line in enumerate(lines):
#     new_line = line
#     if line.startswith('def GetInternetInterfaceName():'):
#         new_lines.append(line)
#         new_lines.append('\treturn "eth0"')
#         skipping = True

#     if line.startswith('#end define'):
#         skipping = False
#     if not skipping:
#         new_lines.append(new_line)

# new_code = '\n'.join(new_lines)
# with open('/usr/src/mytonctrl/mypylib/mypylib.py', 'w') as f:
#     f.write(new_code)
