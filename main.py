import requests


def get_text(url):
    response = requests.get(url)
    return response.text


def count_word_frequencies(site_words, words_to_count):
    site_words = [word.lower() for word in site_words]
    count_words = {}
    for word in site_words:
        if word in words_to_count:
            count_words[word] = count_words.get(word, 0) + 1

    return count_words


def word_frequencies(url):
    text = get_text(url)
    words = text.split()
    return words


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    site_words = word_frequencies(url)

    words_to_count = []
    with open(words_file, 'r') as file:
        words_to_count = [line.strip().lower()
                          for line in file if line.strip()]

    words_to_count = set(words_to_count)

    frequencies = count_word_frequencies(site_words, words_to_count)

    print(frequencies)


if __name__ == "__main__":
    main()
