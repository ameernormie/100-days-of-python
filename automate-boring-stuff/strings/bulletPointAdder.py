#! python3
# bulletPointAdder.py - adds wikipedia bulletpoints to start
# of each line on text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    if lines[i]:
        lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
print(text)

pyperclip.copy(text)
