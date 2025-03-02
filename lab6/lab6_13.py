def delete_file(filename):
    try:
        f = open(filename, 'r')  # Файл бар ма, жоқ па тексеру
        f.close()
        open(filename, 'w').close()  # Файлды босату
        print("Файл жойылды")
    except FileNotFoundError:
        print("Файл жоқ")
filename=input()
delete_file(filename)
