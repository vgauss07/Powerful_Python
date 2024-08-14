# remove trailing whitelines
trimmed_lines = []
for line in open('file.txt'):
    line = line.strip()
    if line != "":
        trimmed_lines.append(line)

print(f'Got {len(trimmed_lines)} lines')



# Convert flattened list to flattened dictionary
prices_flat_list = [
    "orange", 0.70,
    "banana", 0.86,
    "cataloupe", 0.63,
    "bok choy", 1.56,
    "coconuts", 1.06
]

def list2dict(flattened):
    assert len(flattened) % 2 == 0
    "Input must be list of key-value pairs"
    unflattened = dict()
    for i in range(0, len(flattened), 2):
        key, value = flattened[i], flattened[i+1]
        unflattened[key] = value
    return unflattened