def show_menu() -> str:
    """
    Отображение меню пользователя
    :return:
    """
    print("*"*20)
    print("МЕНЮ:")
    print("\t(n)ew - Ввод новой заметки:")
    print("\t(r)ead   - Чтение заметки")
    print("\t(u)pdate  - Изменение заметки")
    print("\t(d)elete - Удаление заметки")
    #print("\t(i)mport - Импорт из файла")
    #print("\t(e)xport - Экспорт в файл")
    print("\t(l)ist   - Вывод на экран всех заметок")
    print("\t(q)uit   - Выход из заметок")

    return input("Выберите нужный пункт ")
