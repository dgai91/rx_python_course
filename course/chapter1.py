all_fib, word_dict = [], {}
text_file = open('../data/sentiment.train.data', encoding='utf-8').read().split('\n')

# Fib
a, b, n = 0, 1, 30
for _ in range(n):
    a, b = b, a + b
    all_fib.append(a)

for line in text_file:
    for w in line:
        if w not in word_dict:
            word_dict[w] = 1
        else:
            word_dict[w] += 1
# get word which count in fibo
for key in word_dict:
    if word_dict[key] in all_fib:
        if word_dict[key] > 1:
            print(key, word_dict[key])
