sentence = input(&quot;Enter a sentence: &quot;)

vowels = 0
consonants = 0
for letter in sentence:
letter = letter.lower()
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter:
vowels = vowels+1