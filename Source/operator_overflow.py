import re#, project


def operator_overflow(address):
    result = ''
    fp1 = open(address, 'r', encoding='gb18030', errors='ignore')
    text1 = fp1.read()
    fp1.close()
    text1_processed = re.sub(r'((?<=\n)|^)[ \t]*\/\*.*?\*\/\n?|\/\*.*?\*\/|((?<=\n)|^)[ \t]*\/\/[^\n]*\n|\/\/[^\n]*','', text1)
    # print(text1_processed)
    result = text1_processed + '\n'
    flag = 0
    '''
    while flag != 1:
        flag = 0
        for line in text1_processed.splitlines():
            for word in line.split(' '):
                if word == 'typedef':
                    temp = line.split(' ')[1]
                    temp_change = line.split(' ')[2][:-1]
                    delete = word + ' ' + temp + ' ' + temp_change + ';\n'
                    text1_processed = text1_processed.replace(delete, '')
                    text1_processed = project.change(text1_processed, temp_change, temp)
                elif re.match("#include", word):
                    text1_processed = text1_processed.replace(line + '\n', '')
                elif re.match("#define", word):
                    text1_processed = text1_processed.replace(line + '\n', '')
                else:
                    flag = 1
                break
    '''
    func_name_list1 = func_name_collect(text1_processed)
    print(func_name_list1)
    result = find_operator_overflow(text1_processed, func_name_list1, result)
    return result


def func_name_collect(text):  # 搜索所有的函数名称
    namelist = []
    namelist_temp = []
    for line in text.splitlines():
        if line.find('(') == -1:
            continue
        i = 0
        while i < len(line):
            i = line.find('(', i)
            if i == -1:
                break
            pos1 = line.rfind('(', 0, i)
            pos2 = line.rfind(' ', 0, i)
            if pos2 == i - 1:
                pos2 = -1  # 对于if、while等系统函数，函数名和小括号之间有空格
            pos3 = line.rfind('\t', 0, i)
            pos4 = line.rfind('=', 0, i)
            pos5 = line.rfind('+', 0, i)
            pos6 = line.rfind('-', 0, i)
            pos7 = line.rfind('*', 0, i)
            pos8 = line.rfind('/', 0, i)
            pos = max(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8)
            if re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[pos + 1:i]) is not None:
                namelist.append(line[pos + 1:i])
            i += 1
    for name in namelist:
        namelist_temp.append(name.strip())
    namelist = namelist_temp.copy()
    return list(set(namelist))


def find_operator_overflow(text, name, result):
    '''
    类型转换
    '''
    for word in name:
        i = 0
        while 1:
            i = text.find(word, i)
            if i == -1:
                break
            pos1 = text.find('{', i)
            pos2 = text.find(';', i)
            if (pos1 < pos2) & (pos1 != -1):
                brace = 1
                braceright = pos1 + 1
                while brace != 0:
                    if text[braceright] == '{':
                        brace += 1
                    elif text[braceright] == '}':
                        brace -= 1
                    braceright += 1
                pos2 = braceright
                name_space = scan(text[i:pos2])
                print(name_space)
                result = find_signed2unsigned(text[pos1:pos2], name_space, result)
            i += 1
    return result


def scan(text):
    name_space = {}
    for line in text.splitlines():
        i = 0
        if line.find('int') != -1:
            i = line.find('int') + len('len')
            while 1:
                temp = re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[i:])  # temp是局部变量名称
                if temp is None:
                    break
                temp = temp.group()
                name_space[temp] = 'int'
                temp_index = line.find(temp)
                i = i + len(temp) + temp_index
        elif line.find('unsigned short') != -1:
            i = line.find('unsigned short') + len('unsigned short')
            while 1:
                temp = re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[i:])  # temp是局部变量名称
                if temp is None:
                    break
                temp = temp.group()
                name_space[temp] = 'unsigned short'
                temp_index = line.find(temp)
                i = i + len(temp) + temp_index
        elif line.find('short') != -1:
            i = line.find('short') + len('short')
            while 1:
                temp = re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[i:])  # temp是局部变量名称
                if temp is None:
                    break
                temp = temp.group()
                name_space[temp] = 'short'
                temp_index = line.find(temp)
                i = i + len(temp) + temp_index
        elif line.find('long long') != -1:
            i = line.find('long long') + len('long long')
            while 1:
                temp = re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[i:])  # temp是局部变量名称
                if temp is None:
                    break
                temp = temp.group()
                name_space[temp] = 'long long'
                temp_index = line.find(temp)
                i = i + len(temp) + temp_index
        elif line.find('long') != -1:
            i = line.find('long') + len('long')
            while 1:
                temp = re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[i:])  # temp是局部变量名称
                if temp is None:
                    break
                temp = temp.group()
                name_space[temp] = 'long'
                temp_index = line.find(temp)
                i = i + len(temp) + temp_index
        elif line.find('unsigned') != -1:
            i = line.find('unsigned') + len('unsigned')
            while 1:
                temp = re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[i:])  # temp是局部变量名称
                if temp is None:
                    break
                temp = temp.group()
                name_space[temp] = 'unsigned'
                temp_index = line.find(temp)
                i = i + len(temp) + temp_index
    return name_space


def find_signed2unsigned(text, name_space, result):
    pos1 = 0
    pos3 = 0
    pos4 = 0
    while 1:
        pos1 = text.find('strncat', pos1)
        pos3 = text.find('memcpy', pos3)
        pos4 = text.find('=', pos4)
        if pos1 != -1:
            result = judge_danger(pos1, 'strncat', name_space, text, result)
            pos1 += 1
        if pos3 != -1:
            result = judge_danger(pos3, 'memcpy', name_space, text, result)
            pos3 += 1
        if pos4 != -1:
            result = judge_danger(pos4, '=', name_space, text, result)
            pos4 += 1
        if (pos1 == -1) & (pos3 == -1) & (pos4 == -1):
            break
    return result


def judge_danger(pos1, func, name_space, text, result):
    pos2 = text.find('\n', pos1)
    print(func)
    if func != '=':
        start = text.find('(', pos1, pos2)
        end = text.rfind(")", pos1, pos2)
        str_list = text[start + 1:end].split(',')  # 将函数内的参数切割开
        str_list_temp = []
        for para in str_list:
            str_list_temp.append(para.strip(' '))
        str_list = str_list_temp.copy()
        if func == 'strncat':
            if name_space.get(str_list[2]) is not None:
                if (name_space.get(str_list[2]) == 'int') | (name_space.get(str_list[2]) == 'long'):
                    print("存在溢出的风险：", text[pos1:pos2])
                    result = result + "存在溢出的风险：" + text[pos1:pos2] + '\n'
        elif func == 'memcpy':
            if name_space.get(str_list[2]) is not None:
                if (name_space.get(str_list[2]) == 'int') | (name_space.get(str_list[2]) == 'long'):
                    # print("存在溢出的风险：", text[pos1:pos2])
                    result = result + "存在溢出的风险：" + text[pos1:pos2] + '\n'
    else:
        pos = text.rfind('\n', text[:pos1])
        temp1 = re.search('[a-zA-Z_][a-zA-Z_0-9]*', text[pos:pos1])
        temp1 = temp1.group()
        temp2 = re.search('[a-zA-Z_][a-zA-Z_0-9]*', text[pos1:pos2])  # temp是等号右侧的局部变量名称
        if temp2 is None:
            pass
        else:
            temp2 = temp2.group()
            if (name_space[temp1] == 'unsigned short') & (name_space[temp2] == 'short'):
                # print("有溢出的风险：", text[pos + 1:pos2], '\n')
                result = result + "存在溢出的风险：" + text[pos1 + 1:pos2] + '\n'
            if (name_space[temp1] == 'unsigned') & (name_space[temp2] == 'int'):
                print("有溢出的风险：", text[pos + 1:pos2], '\n')
                result = result + "存在溢出的风险：" + text[pos1 + 1:pos2] + '\n'
    return result
add="intsigntest.c"
result=operator_overflow(add)
print(result)