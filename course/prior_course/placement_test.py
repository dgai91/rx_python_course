all_fib, word_dict = [], {}
text_file = open('../../data/sentiment.train.data', encoding='utf-8').read()

# Fib
a, b, n = 0, 1, 30
for _ in range(n):
    a, b = b, a + b
    all_fib.append(a)


# for word in text_file:
#     if word not in word_dict:
#         word_dict[word] = len(word_dict) + 1
#
# # get word which count in fibo
# for key in word_dict:
#     if word_dict[key] in all_fib:
#         # if word_dict[key] > 1:
#         print(key, word_dict[key])

for idx, word in enumerate(text_file):
    if idx in all_fib:
        print(word, idx)
