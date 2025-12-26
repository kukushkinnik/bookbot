def words_counter(text):
    splitted_text = text.split()
    num_words = len(splitted_text)
    return num_words


def count_chars(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]

def sorted_output(dict):
    list = []
    for record in dict:
        list.append({"char":record, "num": dict[record]})

    list.sort(reverse=True, key=sort_on)
    
    for record in list:
        if record["char"].isalpha():
            print(f'{record["char"]}: {record["num"]}')

        