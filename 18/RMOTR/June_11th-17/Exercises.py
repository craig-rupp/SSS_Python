def tuple_count(a_tuple):
    tup_dict = {}
    for ind_tup in a_tuple:
        if ind_tup in tup_dict.keys():
            tup_dict[ind_tup] += 1 
        else:
            tup_dict[ind_tup] = 1 
    return tup_dict
print(tuple_count(('a', 'b', 'c', 'c')))

# Write a function that takes a large string, cleans it up and breaks it into individual words, 
# counts how many times each word is used, and then returns a list of words that are repeated.
def count_words(a_string):
    str_l = a_string.split(" ")
    str_dict = {}
    for word in str_l:
        if word in str_dict.keys():
            str_dict[word] += 1 
        else:
            str_dict[word] = 1
    return str_dict


def get_list_of_duplicates(word_count_dict):
    new_list = []
    print(word_count_dict)
    for key, value in word_count_dict.items():
        if value >= 2 and key not in new_list:
            new_list.append(key)
    print(new_list)
    return sorted(new_list)

print(get_list_of_duplicates(count_words("Happy Python Programming Programming Programming Happy Me")))
#print(get_list_of_duplicates(str_dict))

# Write a function sum_of_dict_values that receives 3 dictionaries as parameters: d1, d2, and d3. 
# Get the sum of the values for each matching key 3 dictionaries, and return a new dictionary showing 
# the results of each. If there is a non-integer as a value, set the value to None for that key.
def sum_of_dict_values(d1, d2, d3):
    letters = ['a', 'b', 'c']
    combined = [d1, d2, d3]
    second = [[], [], []]
    result = {'a': 0, 'b': 0, 'c': 0}
    #why can't result be empty?
    for item in combined:
        for key, value in item.items():
            second[letters.index(key)].append(value)
    for i in range(len(letters)):
        for l in range(len(second[i])):
            if type(second[i][l]) == int or type(second[i][l]) == float:
                result[letters[i]] += second[i][l]
            else:
                result[letters[i]] = None
                break
    return result
            
    
d1 = {
    'a': 10,
    'b': 30,
    'c': 5
}
d2 = {
    'a': 7,
    'b': 22,
    'c': 90
}
d3 = {
    'a': 5,
    'b': 1,
    'c': 'hello'
}
print(sum_of_dict_values(d1, d2, d3))


d4 = {
    'a': 30,
    'b': 10,
    'c': 5
}

d5 = {
    'a': 7,
    'b': 'hi',
    'c': 90
}

d6 = {
    'a': 'aloha',
    'b': 'howdy',
    'c': 'hello'
}
# Write a function get_largest_numbers that receives 3 dictionaries as parameters: d1, d2, and d3. 
# Get the highest integer value for each dictionary, and return a new dictionary showing the results of each. 
# If there is a non-integer as a value, ignore it. If none of the values are integers, set that result value 
# to None. Your keys in your result dictionary will be the name of each dictionary 
# parameter (hardcoded to "d1", "d2", and "d3").
def get_largest_numbers(d1, d2, d3):
    key_maxes = [d1, d2, d3]
    max_values = [[], [], []]
    result = {}
    for i in range(len(key_maxes)):
        for key, value in key_maxes[i].items():
            if type(value) == int or type(value) == float:
                max_values[i].append(value)
    for i in range(len(max_values)):
        if len(max_values[i]) >= 1:
            result['d{}'.format(i + 1)] = max(max_values[i])
        else:
            result['d{}'.format(i + 1)] = None 
    return result
print(get_largest_numbers(d4, d5, d6))


# The government wants you to "update" some books (in our case, dictionaries) and remove the words 
# with descriptions including certain words. Write a function censor_dictionary that receives an 
# dictionary named unclean_dictionary and a string flagged_word. If the flagged_word is in the 
# description (value) of a word (key), remove the word (key-value pair) from the dictionary.
# Hint:
# You can use pop or del to remove key-value pairs.
expressions = {
    "pumped": "I'm so darn excited!",
    "happy": "Yeehaw",
    "agreeable": "darn tootin!"
}
print(expressions)
print('should be different below')
def censor_dictionary(unclean_dictionary, flagged_word):
    potential_finds = []
    for key, value in unclean_dictionary.items():
        if flagged_word in value:
            potential_finds.append(key)
    for item in potential_finds:
        del unclean_dictionary[item]
    return unclean_dictionary
print(censor_dictionary(expressions, "darn"))