from image_processing import show_blue_channel
from marker_tracking import track_marker

def main():
    print("Выберите задание:")
    print("1. Вывод синего канала изображения")
    print("2. Отслеживание метки")
    print("3. Отслеживание метки с проверкой области")
    choice = input("Введите номер задания: ")

    if choice == "1":
        show_blue_channel('images/variant-4.jpeg')
    elif choice == "2":
        track_marker(check_region=False)
    elif choice == "3":
        track_marker(check_region=True)
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()