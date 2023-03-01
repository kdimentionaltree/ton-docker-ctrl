# patch /etc/systemd/system/validator.service
with open('/etc/systemd/system/validator.service', 'r') as f:
    code = f.read()

lines = code.split('\n')

new_lines = []
for idx, line in enumerate(lines):
    new_line = line
    
    if line.startswith('User ='):
        new_line = 'User = root'
    if line.startswith('Group ='):
        new_line = 'Group = root'

    new_lines.append(new_line)

new_code = '\n'.join(new_lines)
with open('/etc/systemd/system/validator.service', 'w') as f:
    f.write(new_code)
