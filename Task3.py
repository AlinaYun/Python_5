# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def rle_encode(string_to_encode):
    result = ''
    previous_char = ''
    counter = 0
    for char in string_to_encode:
        if char != previous_char:
            if previous_char:
                result += str(counter) + previous_char
            counter = 1
            previous_char = char
        else:
            counter += 1
    else:
        result += str(counter) + previous_char
    return result
    

with open('data_to_encode.txt', 'r') as data:
    my_text = data.read()
print(rle_encode(my_text))



def rle_decoding(string_to_decode):
    counter = ''
    result = ''
    for char in string_to_decode:
        if char.isdigit():
            counter += char 
        else:
            result += char * int(counter)
            counter = ''
    return result

with open('data_to_decode.txt', 'r') as data:
    my_text2 = data.read()
print(rle_decoding(my_text2))

