def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

filename = input("Введите имя текстового файла: ")
print("Количество строк:", count_lines(filename))
