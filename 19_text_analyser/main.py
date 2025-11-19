from collections import Counter
import re


# 1. Function to analyse text files
def analyse(filename: str) -> None:
    with open(filename, 'r') as f:
        text: str = f.read()

    words: list[str] = re.findall(r'\b\w+\b', text.lower())
    word_count: int = len(words)
    comma_count: int = text.count(',')
    char_count_incl_ws: int = len(text)
    whitespace_count: int = sum(c.isspace() for c in text)
    top_words: list[tuple[str, int]] = Counter(words).most_common(3)

    print('-' * 30)
    print(f'Word count: {word_count}')
    print(f'Commas used: {comma_count}')
    print(f'Character count (incl. whitespaces): {char_count_incl_ws}')
    print(f'Whitespace characters: {whitespace_count}')
    print('')
    print('Top 3 most used words:')

    for word, count in top_words:
        print(f' > {word}: {count}')
    print('-' * 30)


def main() -> None:
    analyse('sample.txt')


if __name__ == '__main__':
    main()


# Homework:
# 1. Count punctuation marks (`.`, `!`, `?`, `:`, `;`).
# 2. Calculate the average word length.
