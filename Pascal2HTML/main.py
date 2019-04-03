import re

pascal_keywords = ['and', 'array', 'begin', 'case', 'const', 'div', 'do', 'else', 'end', 'for', 'function',
                   'if', 'implementation', 'interface', 'mod', 'not', 'of', 'procedure', 'program', 'record',
                   'repeat', 'shl', 'shr', 'string', 'then', 'to', 'type', 'unit', 'until', 'uses', 'var', 'with',
                   'while', 'or', 'class']
keyword_symbols = ['.', ';', ' ']

comment_pattern = "<span class=comment>{}</span>"
keyword_pattern = "<span class=keyword>{}</span>"
string_pattern = "<span class=string>{}</span>"
number_pattern = "<span class=number>{}</span>"


def output(string):
    style = '<STYLE> \
        span.string {color: fuchsia;} \
        span.number {color: darkblue;} \
        span.keyword {font-weight: bold; color: black;} \
        span.comment {font-style: italic; color: gray;} \
            </STYLE>'
    f = open('output.html', 'w')
    f.writelines(style + string)
    f.close()


def get_strings(input):
    collection = []
    flag_begin = 0
    count = 0
    for i in range(len(input)):
        if input[i] is '\'' and flag_begin == 0:
            flag_begin = i
            count += 1
        elif input[i] is '\'' and flag_begin != 0:
            collection.append(input[flag_begin:flag_begin + count + 1])
            flag_begin = 0
            count = 0
        elif flag_begin != 0:
            count += 1
    return collection


with open('data.pas', 'r') as file:
    data = file.read()
    old_line = ''
    for line in data.split('\n'):
        # replace comments
        if line.find('//') != -1:
            ls = line.partition('//')
            comment = ls[1] + ls[2]
            data = data.replace(comment, comment_pattern.format(comment) + '<br>')

        # replace strings
        if len(get_strings(line)) > 0:
            old_line = line
            for word in get_strings(line):
                line = line.replace(word, string_pattern.format(word))
            data = data.replace(old_line, line + '<br>')

        # replace numbers
        if len(re.findall(r'\d+',line)) > 0:
            old_line = line
            for number in re.findall(r'\d+', line):
                line = line.replace(number, number_pattern.format(number))
            data = data.replace(old_line, line + '<br>')

        # replace keywords
        for keyword in pascal_keywords:
            for symbol in keyword_symbols:
                # check '.', ';', ' ' symbols
                if line.find(keyword + symbol) != -1:
                    old_line = line
                    line = line.replace(keyword, keyword_pattern.format(keyword))
                    data = data.replace(old_line, line + '<br>')
                # check on end of string
                elif line.find(keyword) != -1 and line.find(keyword) + len(keyword) == len(line):
                    old_line = line
                    line = line.replace(keyword, keyword_pattern.format(keyword))
                    data = data.replace(old_line, line + '<br>')
                else:
                    continue
file.close()
output(data)

