morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def morse_code(sentence):
    converted_word =""

    if "   " in sentence:
        my_splitted_sentence= sentence.split("   ")
        for my_word in my_splitted_sentence:
            my_word=my_word.split(" ")
            for my_letter in my_word:
                if my_letter in morse_code_dict.values():
                    for k, v in morse_code_dict.items():
                        if my_letter==v:
                            converted_word += k
            converted_word+=" "

    elif " " in sentence:
        my_splitted_sentence=sentence.split(" ")
        for my_letter in my_splitted_sentence:
            if my_letter in morse_code_dict.values():
                for k, v in morse_code_dict.items():
                    if v==my_letter:
                        converted_word+=k
    else:
        my_letter=sentence
        if my_letter in morse_code_dict.values():
            for k, v in morse_code_dict.items():
                if v == my_letter:
                    converted_word += k

    print(converted_word)
morse_code(".... . -.--   .--- ..- -.. .") # two or more words, with a single gap between every word.
morse_code(".... . -.--") # single word
morse_code('....') #single letter
