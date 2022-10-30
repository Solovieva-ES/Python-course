def get_count_char(str_):
    list = str_.split()
    #list.sort(reverse=True)
    list = "".join(list)
    list= list.lower()
    list_dict = {}
    for sym in list :
        if sym.isalpha() :
            if sym in list_dict:
                list_dict[sym] += 1
            else :
                list_dict[sym] = 1
    else : pass


    return list_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова.
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
