
with open('data.txt', 'r', encoding='utf-8') as f:
    data = f.read()

with open('dictionar.txt', 'r', encoding='utf-8') as f:
    dictionar = f.read()

tries = 0
word = ""
guess = ""
alphabet = "AĂEIRTOCNLSMNUPDGFVZBHȚȘÂJXÎKYWQ"

rows = data.strip().split("\n")
dictionar_words = [w.upper() for w in dictionar.strip().split("\n")]

for row in rows:
    index_alpha = 0
    number, masked_word, full_word = row.split(";")
    word = full_word
    guess = masked_word

    #select words with the same length as our word
    possible_words = [w for w in dictionar_words if len(w) == len(word)]


    # filter by matching the revealed letters
    possible_words = [w for w in possible_words if all(
        guess[i] == "*" or guess[i] == w[i] for i in range(len(guess))
    )]

    triesB=0
    while word != guess:
        print(f"Word: {guess}, letter: {alphabet[index_alpha]} ,tries: {triesB}")

        if len(possible_words) == 1:
            guess = possible_words[0]
            triesB += 1
            print(f"I guessed the word: {guess} in {triesB} tries!")
            break


        if alphabet[index_alpha] in guess:
            print(f"This letter is already in the word:  {alphabet[index_alpha]}")
            index_alpha += 1
            continue

        # update possible words based on the current guess
        possible_words = [w for w in possible_words if all(
            guess[i] == "*" or guess[i] == w[i] for i in range(len(guess))
        )]

        # check if the letter is in any possible word
        found = any(alphabet[index_alpha] in w for w in possible_words)

        if not found:
            triesB += 1
            print(f"{alphabet[index_alpha]} is not in the word ")
            index_alpha += 1
            continue

        # try to match letters based on the alphabet
        for i in range(len(word)):
            if guess[i] == "*":
                if word[i] == alphabet[index_alpha]:
                    triesB += 1
                    guess = guess[:i] + alphabet[index_alpha] + guess[i + 1:]
                    print(f"Letter: {alphabet[index_alpha]} has been added, tries for this word: {triesB}")

        # move to the next letter
        index_alpha += 1
    tries= tries + triesB
    print("____________________")

print(f"Total tries: {tries} . Game finished!")
