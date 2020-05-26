'''
x Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    if len(word) < 2:
        return 0
    else:
        if word[0:2] == "th":
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])

    # Way more complicated approach:
    # word_length = len(word)
    # th_counter = 0
    # storage = []
    # current_letter = 0

    # if word_length == 0:
    #     return th_counter
    
    # # turn string into list, each letter an index
    # listed_word = list(word)
    # # add 1 letter to storage
    # storage.append(listed_word[current_letter])
    # #pop current_letter from listed word
    # listed_word.pop(current_letter)
    # # add 1 letter to storage
    # storage.append(listed_word[current_letter])
    # # increment current and next letter once used

    # if storage[0] == "t" and storage[1] == "h":
    #     th_counter += 1
    #     storage.pop(0) # can this be brough out of this scope? since it need to happen after every comparison

    # else:
    #     #get rid of first letter in storage, so we can check next pair
    #     storage.pop(0)
    #     #pop current_letter from listed word, its already in storage
    #     listed_word.pop(current_letter)
