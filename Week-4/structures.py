'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    first_and_last = [the_list[0], the_list[-1]]
    return [first_and_last]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 

# FIRST ATTEMPT
# def part_reverse(the_list, beginning, end):
#     slice_list = the_list[int(beginning],the_list[int(end)]
#     part_reverse = slice_list.reverse()
#     if part_reverse[0] < part_reverse[-1]:
#         print("ValueError")
#     else:
#         return part_reverse
        # hint this is incomplete
def part_reverse(the_list, beginning, end):
    first = int(beginning)
    last = int(end)
    slice_list = []
    slice_list = [the_list[first], the_list[last]]
    part_reverse = slice_list.reverse()
    if part_reverse[0] < part_reverse[-1]:
        print("ValueError")
    else:
        return part_reverse



# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
#note insert method.
# list1 = ['Google', 'Runoob', 'Taobao']
# list1.insert(1, 'Baidu')
# print('列表插入元素后为 : ', list1)
# output
# 列表插入元素后为:  ['Google', 'Baidu', 'Runoob', 'Taobao']


def repeat_at_index(the_list, index):
    locat_insert = int(index)
    for i in range(locat_insert):
        the_list.insert(locat_insert, locat_insert)
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards   eg. madam

#method 1
def palindrome_word(word):
    rev_word = word[::-1]
    if rev_word == word:
        return True
    else:
        return False
#method 2
# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1

# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True


   

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    return

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentenece1, sentence2): 
    spac_sentence1 = sentence1.strip()
    spac_sentence2 = sentence2.strip()
    spac_sentence1[0].upper() = spac_sentence1[0]
    concat_str = sentenece1 + " " + sentence2 + "."
    
    return concat_str


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    return

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    return

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    return
