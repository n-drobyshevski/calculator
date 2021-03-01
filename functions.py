import re


def check_multiply_perenthesis(text):
    re_exp = re.compile(r'\d\(')
    to_change = re_exp.findall(text)
    for item in to_change:
        text = text.replace(item, f'{item[0]}*(')
    return text


def check_for_sqrt(text):
    print('entred in chech_for_sqrt')
    text = bracketed_expression_after('√', text)
    #re_exp1 = re.compile(r'\d+√\(\d+\)|\d+√\(\w+.\w+\(\d+,\d+\)\)')
    #re_exp2 = re.compile(r'√\(\d+\)|\(\w+.\w+\(\d+,\d+\)\)')
    re_exp1 = re.compile(r'\d+√\(.+\)')
    re_exp2 = re.compile(r'√\(.+\)')
    to_change = re_exp1.findall(text)
    ans2 = re_exp2.findall(text)
    print(to_change,'to_change')
    print(ans2,'ans2')
    if to_change:
        for item in to_change:
            print(item,' -- to_change item')
            text = text.replace(item, f"{item[0]}*math.sqrt({item[3:-1]})")
            print(text,' -- to_change text')
    elif ans2:
        for item in ans2:
            print(item,' -- ans2 item')
            text = text.replace(item, f"math.sqrt({item[1:]})")
            print(text,' -- to_change text')
    print(text, 'exit of check sqrt')
    return text


def check_for_square(text):
    print('entred in chech_for_square')
    text = bracketed_expression_before('²', text)
    print(text, ' -- text')
    re_exp = re.compile(r'\d+²')
    to_change = re_exp.findall(text)
    if to_change:
        for item in to_change:
            text = text.replace(item, f'math.pow({item[:-1]},2)')
    print(text)
    return text


def check_if_1_number(text):
    one_number = False
    match = re.fullmatch(r'\d', str(text))
    if match:
        print(match)
        one_number = True
    return one_number


def calculate_brackets(text):
    print(text,'text, entred in calculate brackets')
    text = analyse(text)
    print('---------------------------------')
    print(text, 'text after analysis')
    try:
        match = re.search(r'[^a-zA-Z\-+]\(.+\)',text)
        if match:
            print(match[0],'---match[0]')
            print(match[0][1:-1],'---match[0][1:-1]')
            text = match[0][1:-1]
            print(text, '---text')
            res = eval(str(text))
        else:
            res = text
    except BaseException as Ex:
        print(Ex, '-- excepted')
    res = '('+res+')'
    print(res, '---res')
    return res

def bracketed_expression_after(char, text):
    print('entred in bracket_after')
    re_exp = re.compile(char + r'\(.+\)')
    to_change = re_exp.findall(text)
    if to_change:
        print(f'{to_change}, to_change')
        for item in to_change:
            try:
                match = re.search(r'\(.+\)', item)
                print(item, "--item")
                print(match[0][1:-1], "--match[0][1:-1]")
                res = calculate_brackets(match[0][1:-1])
                print(res, "--res")
                text = text.replace(item, char + f'{res}')
            except BaseException as exc:
                print(exc, ' excepted')

    print(text, 'exit from bracket_after')
    return text


def bracketed_expression_before(char, text):
    print('entred in bracket_before')
    re_exp = re.compile(r'\(.+\)' + char)
    to_change = re_exp.findall(text)
    if to_change:
        print(f'{to_change}, to_change')
        for item in to_change:
            print(item, "--item")
            res = calculate_brackets(item)
            print(res, "--res")
            text = text.replace(item, f'{res}' + char)
    return text

def check_output(text):
    match = re.fullmatch(r'\d+\.0', str(text))
    if match:
        return match[0][:-2]
    else:
        return text




def analyse(text):
    print('===================================')
    print(text, '-- enter in analyse...')
    one_number = check_if_1_number(text)
    print(one_number, 'is one number')
    if not one_number:
        print(f'analysy`s if ')
        inter_text = check_multiply_perenthesis(text)
        inter_text = check_for_sqrt(inter_text)
        inter_text = check_for_square(inter_text)
        print(f'{inter_text} -- final func print')
        return inter_text
    else:
        return False
