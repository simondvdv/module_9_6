def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(len(text)):
            if j + i > len(text):
                break
            yield text[j: j + i]


a = all_variants("abcd")
for i in a:
    print(i)
