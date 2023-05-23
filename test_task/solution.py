import csv


def get_max_positive_sequence(obj_iter):
    count = 0
    count_max = 0
    for elem in obj_iter:
        if int(elem[0]) > 0:
            count += 1
            if count > count_max:
                count_max = count
        else:
            count = 0
    return count_max


def main():
    file_name = input('Введите название файла: ')
    with open('numbers.csv') as f_read:
        rows = csv.reader(f_read)
        next(rows)  # Пропускаем заголовок
        print(get_max_positive_sequence(rows))


if __name__ == '__main__':
    main()