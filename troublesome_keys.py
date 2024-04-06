keys = input()
displayed = input()

if len(keys) > len(displayed):
    silent = True
else:
    silent = False

for idx in range(len(displayed)):
    key = keys[idx]
    disp = displayed[idx]
    if not silent and key != disp:
        break
    elif key != disp:
        if keys[idx + 1] == disp:
            silent = key
            break
    elif idx == len(displayed) - 1 and idx < len(keys) - 1:
        silent = keys[-1]

if silent:
    keys = keys.replace(silent, '')
    for idx in range(len(displayed)):
        key = keys[idx]
        disp = displayed[idx]
        if key != disp:
            break

print(key, disp)
print('-' if not silent else silent)
