from itertools import product

#Буквы для которых мы должны ныйти коды
lett = "ЕНЗР"
#Уже известные коды
codes = ["101","010","00"]
#Все возможные коды: 0 1 00 01 10 11...
all_codes = []
for code_len in range(1,len(lett)+len(codes)):
    all_codes+=list(map("".join, product("01", repeat=code_len)))

#Функция проверяет выполняется ли условие Фано
#c - код для которого мы проверяем условие
#codes - список кодов без c
def is_valid(c,codes):
    for i in codes:
        if c==i[:len(c)] or i==c[:len(i)]:
            return False
    return True

count = 0
for l in lett:
    is_found = False
    while not is_found:
        c = all_codes[count]
        
        #Если число выполняет условие Фано то
        if is_valid(c,codes):
            #Проверяем останутся ли свободные ветки после добавления кода
            for i in codes+[c]:
                #Инвертирует последнюю цифру кода
                #"0" (int)-> 0 (not)-> True (int)-> 1 (str)-> "1"
                branch = i[:-1]+str(int(not int(i[-1])))

                #Если нашлась хотя бы одна свободная ветка после
                #добавления кода, то он подходит
                if is_valid(branch,codes+[c]):
                    print(l,c)
                    codes.append(c)
                    is_found = True
                    break

        count+=1
