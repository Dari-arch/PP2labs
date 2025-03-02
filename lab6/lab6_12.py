def copy_and_show(src, dst):
    f1 = open(src, 'r', encoding='utf-8') if open(src, 'r', encoding='utf-8') else None

    if f1:
        data = f1.read()
        f1.close()

        f2 = open(dst, 'w', encoding='utf-8')
        f2.write(data)
        f2.close()

        f3 = open(dst, 'r', encoding='utf-8')
        print(f3.read())
        f3.close()
    else:
        print("Файл жоқ")


first=input()
second=input()
copy_and_show(first,second)



