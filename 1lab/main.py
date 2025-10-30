# Двизов Иван Алексеевич ПИ25-2
    text = input("Введите текст: ").lower()

for ch in ",.!?;:-()\"'":
    text = text.replace(ch, "")

words = text.split()

word_count = {}
for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

letter_count = {}
for ch in text:
    if ch.isalpha():
        if ch in letter_count:
            letter_count[ch] += 1
        else:
            letter_count[ch] = 1

top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
top_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nТоп 5 слов:")
for word, count in top_words:
    print(f"{word}: {count}")

print("\nТоп 5 букв:")
for letter, count in top_letters:
    print(f"{letter}: {count}")
