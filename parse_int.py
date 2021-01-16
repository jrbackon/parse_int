def parse_int(string):
    word_conv = {'zero':0, 'one':1, 'two':2,'three':3, 'four':4, 'five':5, 'six':6,
    'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13,
    'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19,
    'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80,
    'ninety':90}

    first = 0
    hundreds = 0
    thousands = 0
    million = 0
    count = 0
    string = string.replace('-',' ')
    for part in string.split():
        if part == 'and':
            continue
        elif part == 'hundred':
            hundreds = first * 100
            first = 0
            count += 1
            continue
        elif part == 'thousand':
            if count == 1:
                thousands = (hundreds * 1000) + (first * 1000)
                hundreds = 0
                count = 0
                first = 0
            else:
                thousands = first * 1000
                first = 0
            continue
        elif part == 'million':
            million = first * 1000000
            first = 0
            continue
        first = first + word_conv.get(part)

    final = first + hundreds + thousands + million

    return final

