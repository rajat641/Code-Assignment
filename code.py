def is_pyramind_word(input_string):
    char_count = dict()
    for x in range(len(input_string)):
        char_count[input_string[x]] += 1
    import pdb;
    pdb.set_trace()
    print(char_count)