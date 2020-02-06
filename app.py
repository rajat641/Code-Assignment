from flask import Flask
from flask import request

app = Flask(__name__)
"""
PROBLEM STATEMENT: Please write a web service that takes in a string and returns a boolean to indicate 
whether a word is a pyramid word. A word is a ‘pyramid’ word if you can arrange the letters in increasing 
frequency, starting with 1 and continuing without gaps and without duplicates.
Examples:
banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's.
bandana is not a pyramid word because you have 1 'b' and 1 'd'.
You can use any language. When completed, please upload to a public repository, such as GitHub, 
and provide us with the link.

"""


# Method to check if the character count map is increasing or not.
def check_increasing(char_count_arr):
    len_arr = len(char_count_arr)
    for ind in range(len_arr):
        if char_count_arr[ind] == 0:
            return False
    return True


def is_pyramid_word(input_string):
    if len(input_string) < 2:  # If a word has length less that or equal to 2, its a pyramid word
        return True
    char_count = dict()  # map to store the frequency of each character.
    max_count = 0
    for x in range(len(input_string)):
        if input_string[x] in char_count:
            char_count[input_string[x]] = char_count[input_string[x]] + 1
            max_count = max(max_count, char_count[input_string[x]])
        else:
            char_count[input_string[x]] = 1
            max_count = 1
    char_count_arr = [0] * max_count    # Another map created to check if the char frequency is strictly increasing
    for value in char_count.values():
        char_count_arr[value - 1] = char_count_arr[value - 1] + 1
        if char_count_arr[value - 1] > 1:
            return False
    return check_increasing(char_count_arr)


@app.route("/", methods=['GET'])
def home():
    if 'query' in request.args:
        query_word = request.args['query']
        if is_pyramid_word(query_word):
            return "Success: The input word is a Pyramid word"
        else:
            return "Fail:The input word is not a Pyramid word"
    else:
        return "Error: No input field provided. Please specify an input."


app.run()
