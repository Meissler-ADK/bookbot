def word_counter(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def get_letters_in_text(text):
    text = text.lower()
    letter_dic = {}
    for letter in text:
        if letter in letter_dic:
            letter_dic[letter] +=1
        else:
            letter_dic[letter] = 1
    return letter_dic

def sorted_letter_count(unsorted_dic):
    sorted_list = []
    for char, count in unsorted_dic.items():
        if char.isalpha():
            temp_data = {"char":char, "count":count}
            sorted_list.append(temp_data)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def sort_on(dict):
    return dict["count"]