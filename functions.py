import re


def check_for_sqrt(text):
    re_exp1 = re.compile(r'\d√\d+')
    re_exp2 = re.compile(r'√\d+')
    to_change = re_exp1.findall(text)
    ans2 = re_exp2.findall(text)
    for item in to_change:
        text = text.replace(item, f"{item[0]}*math.sqrt({item[2:]})")
    for item in ans2:
        text = text.replace(item, f"math.sqrt({item[1:]})")
    return text


def check_for_square(text):
    re_exp = re.compile(r'\d+²')
    to_change = re_exp.findall(text)
    for item in to_change:
        text = text.replace(item, f'math.pow({2},2)')
    print(text)
    return text


def check_output(text):
    match = re.fullmatch(r'\d+\.0', str(text))
    print(match[0])
    if match:
        return match[0][:-2]


def check_if_1_number(text):
    one_number = False
    match = re.fullmatch(r'\d', str(text))
    if match:
        one_number = True
    return one_number
