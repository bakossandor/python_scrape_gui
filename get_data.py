from bs4 import BeautifulSoup
import requests


def get_data_from(url):
    r = requests.get(f"http://{url}")
    soup = BeautifulSoup(r.text, "html.parser")
    return count_words(beauti_data(soup))


def beauti_data(soup):
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


def count_words(text):
    word_tree = {}
    print("count")
    for word in text.split():
        if hasattr(word_tree, word):
            word_tree[word] += 1
        else:
            word_tree[word] = 1
    return word_tree

