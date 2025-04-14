
def word_count (text):
    words = text.split()
    return len(words)
    
def count_char(text):
    char_num_dict = {}

    for char in text.lower():
        if char in char_num_dict:
            char_num_dict[char] += 1
        else:
            char_num_dict[char] = 1

    return char_num_dict

def sort(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse = True)
