# 1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? 

# upper() method 


# Ask Python for help on what you can do with strings!
# Built-in help function on strings:

# print(help(str))



# 2. Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

# def print_upper_words(words):
#     """Print each word in a list of words on a separate line uppercased.

#             >>> print_upper_words(["hello", "world", "how", "are", "you"])
#             HELLO
#             WORLD 
#             HOW
#             ARE 
#             YOU?
#     """

#     for word in words:
#         print(word.upper())

# print_upper_words(["hello", "world", "how", "are", "you?"])



# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

# def print_upper_words_start_letter_e(words):
#     """Print each word from a list of words on separate line, uppercased, if start with E or e

#             >>> print_upper_words_start_letter_e(["elephant", "egret", "apple", "Edith", "zebra", "eraser"])
#             ELEPHANT
#             EGRET
#             EDITH
#             ERASER
#     """

#     for word in words:
#         if word.startswith("e") or word.startswith("E"):
#             print(word.upper())

# print_upper_words_start_letter_e(["elephant", "egret", "apple", "Edith", "zebra", "eraser"])



# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
# For example:
# # this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})

def print_upper_words_spec_letters(words, must_start_with):
    """Print each word from list of words, only if it starts with one of given letters that is specified in a set of letters passed in as arg
    
            >>> print_upper_words_spec_letters(["hello", "hey", "goodbye", "yo", "yes"], 
            must_start_with={"h", "y"})
            HELLO
            HEY
            YO
            YES
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words_spec_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

                               



