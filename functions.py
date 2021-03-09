'''
expression enter in analyse ===> check if it's one number ==Yes==> return this number
     /\                                              \/
   /_|_\             activate divide_in_parts func<==no
    ||               \/                               \/
    ||      more then one part                       one part ===> check for sqrt and square function
    ||               \/                                                          \/
    \\===send each part to analyse                                           return expression
'''

'''
(?<=\().*?(?=\)) - re_exp will find all expressions in brackets
[-+]√?[^-+()\n]+²? - re_exp will find all expressions that consist of sign (sqrt, and square included) and digits (+5²)

'''

import re


def get_bracketed_exp(text):
    print('----- get_bracketed_exp -----')
    counter = 0
    first_ind = 0
    second_ind = 0
    char_list = ("+", '-', '*', '/','(', ')')
    re_text = text
    try:
        for i in range(len(text)):
            print(i,text[i])

            if text[i] == '(':
                if counter == 0:
                    first_ind = i
                    print(first_ind, ' -- first_ind')
                    counter += 1
                    print(f'{counter} -- counter')
            if text[i] == ')':
                counter -= 1
                print(f'{counter} -- counter')
                print('second< if')
                if counter == 0:
                    print('second< if 1')
                    second_ind = i
                    print(second_ind, ' -- second_ind')
                else:
                    print('second< if 2')
                    counter -= 1
                    print(f'{counter} -- counter')
    except BaseException as exc:
        print(exc)
    item = text[first_ind:second_ind+1]
    print(item, ' -- item')
    n = 1
    if text[first_ind-n] == '*':
        while type(text[first_ind-n])) int:

    print(item)
    return item


def check_if_1_number(text):
    one_number = False
    match = re.fullmatch(r'\d', str(text))
    if match:
        one_number = True
    return one_number


# check if there is multiplication of digit for bracket, or bracket for bracket
# [ digit*(expression) or (expression)*(expression)  ]
def check_multiply_brackets(text):
    re_exp = re.compile(r'\d\(')
    to_change = re_exp.findall(text)
    for item in to_change:
        text = text.replace(item, f'{item[0]}*(')
    re_exp = re.compile(r'\)\(')
    to_change = re_exp.findall(text)
    for item in to_change:
        text = text.replace(item, f')*(')
    return text


# if there is minus before expression, change all sign ('+' => '-')
def multiply_for_minus_1(text):
    try:
        re_exp_sign = re.compile(r'[-][√]?\d+|[+][√]?\d+')
        re_exp_begining_sign = re.compile(r'-\([√]?\d+\)?[²]?|\([√]?\d+\)?[²]?')
        to_change_sign = re_exp_sign.findall(text)
        to_change_begining_sign = re_exp_begining_sign.findall(text)
        print(to_change_sign, to_change_begining_sign)
        for item in to_change_sign:
            print(item)
            if item[0] == '-':
                text = text.replace(item[0], '+')
            else:
                text = text.replace(item[0], '-')
            print(text, ' -- ')
        for item in to_change_begining_sign:
            print(item)
            text = text.replace(item, '(-' + item[1])
            print(text, ' -- ')
        print(text, ' -- text exited from multiply_for_minus_1')
    except BaseException as Exc:
        print(Exc)
'''
    try:
        re_exp_sign = re.compile(r'[-][√]?\d+\)?[²]?]|[+][√]?\d+\)?[²]?]')
        re_exp_begining_sign = re.compile(r'-\([√]?\d+\)?[²]?|\([√]?\d+\)?[²]?')
        to_change_sign = re_exp_sign.findall(text)
        to_change_begining_sign = re_exp_begining_sign.findall(text)
        print(to_change_sign, to_change_begining_sign)
        for item in to_change_sign:
            print(item)
            if item[0] == '-':
                text = text.replace(item[0], '+')
            else:
                text = text.replace(item[0], '-')
            print(text, ' -- ')
        for item in to_change_begining_sign:
            print(item)
            text = text.replace(item, '(-' + item[1])
            print(text, ' -- ')
        print(text, ' -- text exited from multiply_for_minus_1')
    except BaseException as Exc:
        print(Exc)
'''

# works if there is 2 or more difficult items like 2√4+2² => 2 items 2² and 2√4
# will calculate all items...
def divide_in_parts(text):
    print('----- divide_in_parts -----')
    re_exp = re.compile(r'[-+]√?[^-+()\n]+²?')
    to_change = re_exp.findall(text)
    print(to_change, ' -- to_change')
    to_change = to_change + get_bracketed_exp(text)
    print(get_bracketed_exp(text))
    print(to_change, ' -- divide_in_parts\'s to_change ')
    if len(to_change) > 1:
        print(to_change, ' -- divide_in_parts\'s to_change ')
        for item in to_change:
            #if item[0] == '-' and item[-1] != '²' and item[1] != '√':
            #    item = multiply_for_minus_1(item)
            ext_text = analyse(item[:-1])
            text = text.replace(item, ext_text)
    return text


def open_bracket(text):
    print('----- entred in open_braccket -----')
    match = re.search(r'[-]?\(\)|\(\)',text)
    if match[0][0] != '-':
        ext_text = match[0][1:-1]
    else:
        ext_text = multiply_for_minus_1(match[0])
    return ext_text


def check_for_sqrt(text):
    numbs = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    print('----- entred in check_for_sqrt -----')             #                               item
    re_exp1 = re.compile(r'[-]?[\d+]?√\d+|[-]?[\d+]?√\(.+\)')#  1          negative /                  \positive
    to_change = re_exp1.findall(text)                         # 2multiplyed/        \not        multiplyed/       \not
    if to_change:                                             #3bracket/\no | bracket/ \no | bracket/ \no | bracket/ \no
        print(f'{to_change} -- check_for_sqrt\'s to_change')
        for item in to_change:
            print(f'{item} -- item')
            if item[0] == '-':                                              # 1 if item is negative
                #print('|| item is negative ||')
                if item[1] in numbs:                                       # 2 if sqrt is multiplicated for digit
                    #print('|| item is multiplicated for digit ||')
                    if item[3] == '(':                                           # 3 if there is brackets after
                        #print('|| sqrt from brackets ||')
                        bracket = brackets_after('√', item[3:])
                        text = text.replace(item, f'-{item[1]}*math.sqrt({bracket})')
                    else:                                                        # 3 if there is NOT brackets after
                        #print('|| sqrt from digit ||')
                        text = text.replace(item, f'-{item[1]}*math.sqrt({item[3:]})')
                else:                                                       # 2 if sqrt is NOT multiplicated for digit
                    #print('|| item is not multiplicated for digit ||')
                    if item[2] == '(':                                           # 3 if there is brackets after
                        #print('|| sqrt from brackets ||')
                        bracket = brackets_after('√', item[2:])
                        text = text.replace(item, f'-math.sqrt({bracket})')
                    else:                                                        # 3 if there is NOT brackets after
                        #print('|| sqrt from digit ||')
                        text = text.replace(item, f'-math.sqrt({item[2:]})')

            else:                                                            # 1 if item is positive
                #print('|| item is positive ||')
                if item[0] in numbs:                                       # 2 if sqrt is multiplicated for digit
                    #print(f'|| item is multiplicated for digit ||')
                    if item[2] == '(':                                           # 3 if there is brackets after
                        #print('|| sqrt from brackets ||')
                        bracket = brackets_after('√', item[2:])
                        text = text.replace(item, f'{item[0]}*math.sqrt({bracket})')
                    else:                                                        # 3 if there is NOT brackets after
                        #print('|| sqrt from digit ||')
                        text = text.replace(item, f'{item[0]}*math.sqrt({item[2:]})')
                else:                                                        # 2 if sqrt is NOT multiplicated for digit
                    #print(f'|| item is not multiplicated for digit [{item[0]}]||')
                    if item[1] == '(':                                           # 3 if there is brackets after
                        #print('|| sqrt from brackets ||')
                        bracket = brackets_after('√', item[1:])
                        text = text.replace(item, f'math.sqrt({bracket})')
                    else:                                                        # 3 if there is NOT brackets after
                        #print('|| sqrt from digit ||')
                        text = text.replace(item, f'math.sqrt({item[1:]})')
    return text


def check_for_square(text):
    print('----- entred in chech_for_square -----')
    text = brackets_before('²', text)
    # print(text, ' -- text')
    re_exp = re.compile(r'\d+²|\(.+\)²')
    to_change = re_exp.findall(text)
    if to_change:
        print(f'{to_change} -- check_for_square\'s to_change ')
        for item in to_change:
            if item[0] == '+' or item[0] == '-':
                item = item[1:]
            text = text.replace(item, f'math.pow({item[:-1]},2)')
        print(text, ' -- exit from check_for_square')
    return text


def calculate_brackets(text):
    print('----- entred in calculate brackets -----')
    text_match = re.search(r'\(.+\)', text)
    text = analyse(text_match[0][1:-1])

    print('---------------------------------')
    print(text, ' -- text after analysis')
    print('---------------------------------\n')

    res = 'predefined'
    try:
        match = re.search(r'[^a-zA-Z\-+]\(.+\)', text)
        if match:
            print(match[0], ' -- match[0]')
            print(match[0][1:-1], ' -- match[0][1:-1]')
            text = match[0][1:-1]
            print(text, ' -- text')
            res = eval(str(text))
        else:
            res = text
    except BaseException as Ex:
        print(Ex, '-- excepted in calculate_brackets')
    res = '(' + res + ')'
    print(res, ' -- result exited from calculate_brackets')
    return res


def brackets_after(char, text):
    print('----- entred in bracket_after -----')
    re_exp = re.compile(char + r'\(.+\)')
    to_change = re_exp.findall(text)

    if to_change:
        print(f'{to_change}, -- brackets_after\'s to_change')
        for item in to_change:
            try:
                match = re.search(r'\(.+\)', item)
                print(item, " -- item")
                print(match[0][1:-1], " -- match[0][1:-1]")
                res = calculate_brackets(match[0])
                print(res, " -- res")
                text = text.replace(item, char + f'{res}')
            except BaseException as exc:
                print(exc, ' -- excepted in brackets_after')

        print(text, ' -- exit from bracket_after')
    return text


def brackets_before(char, text):
    print('----- entred in bracket_before -----')
    re_exp = re.compile(r'\(.+\)' + char)
    to_change = re_exp.findall(text)
    if to_change:
        print(f'{to_change}, -- brackets_before\'s to_change')
        for item in to_change:
            print(item, " -- item")
            match = re.search(r'\(.+\)', item)
            res = calculate_brackets(match[0])
            print(res, " -- result of brackets_before")
            text = text.replace(item, f'{res}' + char)
    return text


def check_output(text):
    match = re.fullmatch(r'\d+\.0', str(text))
    if match:
        return match[0][:-2]
    else:
        return text


def analyse(text):
    print('\n=================Analyse==================')
    print(text, ' -- entered in analyse...')
    one_number = check_if_1_number(text)
    print(one_number, ' -- is one number ?')
    if not one_number:
        # match = re.search()
        print(f'----- analysy`s if ----- ')
        inter_text = check_multiply_brackets(text)
        inter_text = divide_in_parts(inter_text)
        inter_text = check_for_sqrt(inter_text)
        inter_text = check_for_square(inter_text)
        print(f'{inter_text} -- exited from analyse')
        return inter_text
    else:
        return text
