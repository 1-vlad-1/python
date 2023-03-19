from functools import reduce

lines = ["first STRING","Second string"]

concatenated_string  = reduce(lambda string1, string2: string1.lower() + " " + string2.lower(), lines)

print(concatenated_string)

#фильтр четных чисел, которые больше или равны 10

def even_greater_10(number):
    if (number % 2 == 0 and number >=10):
        return True

sorting_numbers = filter(even_greater_10,(1,10,15,5,16,24,31))

print(list(sorting_numbers))

#удаление первой буквы из строки

list_of_strings = ['string','hello','ben']

def delete_first_letter(string):
    new_string = string[1:]
    return new_string

new_list = map(delete_first_letter,list_of_strings)

print(list(new_list))