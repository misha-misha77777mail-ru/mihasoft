def center_window(roots, x_width, height):
    """
    Функция для размещения окон в центре экрана
    """

    x_window_height = height
    x_window_width = x_width

    # Получение ширины и высоты экрана монитора
    screen_width = roots.winfo_screenwidth()
    screen_height = roots.winfo_screenheight()

    # Расчёт координаты верхнего левого угла окна
    x_coordinate = int((screen_width / 2) - (x_window_width / 2))
    y_coordinate = int((screen_height / 2) - (x_window_height / 2))

    roots.geometry('{}x{}+{}+{}'.format(x_window_width, x_window_height, x_coordinate, y_coordinate))
