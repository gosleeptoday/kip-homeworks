import config as cfg

while True:
    try:
        b = int(input("Введите номер месяца "))
        print(cfg.a[b])
    except:
        print("Ошибка номера месяца")