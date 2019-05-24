
def run_me(word):
    sorted_words = sorted(word, key=lambda letter: -1 * ord(letter))
    if list(word) == sorted_words:
        return "no answer"

    letter_index = None
    for index, letter in enumerate(word):
        if letter != sorted_words[index]:
            letter_index = index
            break

    letter = word[letter_index]
    beginning = word[:index]
    ending = comupte_ending(word[index:], letter)
    return beginning + ending


def comupte_ending(ending, original_letter):
    sorted_ending = sorted(ending)
    letter_value = ord(original_letter)
    letter = None
    for l in sorted_ending:
        if ord(l) > letter_value:
            letter = l
            break
    end_indx = ending.find(letter)
    ret = ending[:end_indx] + original_letter

    if not end_indx:
        ret += end_indx[end_indx - 1:]

    return ret


def parse_query(number):
    for _ in number:
        print run_me(raw_input().strip())

if __name__ == '__main__':
    n = range(int(raw_input()))
    run_me(parse_query(n))
