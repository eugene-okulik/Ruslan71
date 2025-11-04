text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
words = text.split()

result = []

for word in words:
    if word[-1] in [',', '.', '!', '?']:
        punctuation = word[-1]
        word = word[:-1] + 'ing' + punctuation
    else:
        word = word + 'ing'
    result.append(word)

new_text = ' '.join(result)

print(new_text)
