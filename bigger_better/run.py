def me(word):
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
    import pdb; pdb.set_trace()
    end_indx = ending.find(letter)
    ret = [letter]
    ret.extend(list(ending))
    ret[end_indx + 1] = original_letter

    return ''.join(ret)