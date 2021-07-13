import requests

response = requests.get("http://www-personal.umich.edu/~jlawler/wordlist")
words = response.text.split()

assert words


def get_conjugate(word):

    word = word.lower()

    sub_words = []
    for word_ in words:
        if word_ in word:
            sub_words.append(word_)

    log = []

    def branch(index=0):
        char = word[index]

        possibilities = sorted(
            [word_ for word_ in sub_words if word_.startswith(char) and len(word_) > 2 and word_ != word],
            key=len,
        )

        if possibilities:

            for possibility in possibilities:
                if possibility == word[index:]:
                    log.insert(0, possibility.title())
                    return possibility

                else:
                    try:
                        result = possibility + branch(word.index(possibility, index) + len(possibility))
                    except:
                        continue

                    if result == word[index:]:
                        log.insert(0, possibility.title())
                        return result

                    else:
                        continue

        return result

    branch()  # tracked by log
    return log
