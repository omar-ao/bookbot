def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    char_count = {}
    words = text.split()
    for word in words:
        for char in word:
            c = char.lower()
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
    return char_count


def sort_on(items):
    return items["num"]


def get_sorted_char_count(char_count):
    list_char = []
    for key in char_count:
        tmp = {}
        tmp["char"] = key
        tmp["num"] = char_count[key]
        list_char.append(tmp)

    list_char.sort(reverse=True, key=sort_on)
    return list_char
