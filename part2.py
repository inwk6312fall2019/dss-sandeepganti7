with open('2600-0.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}


def find_rot_pairs():
    final_list = []
    for word in word_dict:
        for i in range(1, 26):
            if rotate.rotate_word(word, i) in word_dict:
                final_list.append((word, i, rotate.rotate_word(word, i)))
    final_list.sort()
    for pair in final_list:
        print pair

find_rot_pairs()
