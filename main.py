import argparse
import csv
import statistics


def parse_filter(filter_str):
    for op in ['>=', '<=', '==', '>', '<']:
        if op in filter_str:
            field, value = filter_str.split(op)
            return field.strip(), op, float(value.strip())
    raise ValueError("Фильтр должен содержать один из операторов: >, <, ==, >=, <=")


def apply_filter(rows, field, op, value):
    filtered = []
    for row in rows:
        try:
            cell = float(row[field])
            if eval(f"{cell} {op} {value}"):
                filtered.append(row)
        except (ValueError, KeyError):
            continue
    return filtered


def aggregate(rows, field, operation):
    try:
        values = [float(row[field]) for row in rows]
    except ValueError:
        raise ValueError(f"Не удалось преобразовать значения в числовой формат по полю {field}")
    if not values:
        return None
    if operation == 'avg':
        return statistics.mean(values)
    elif operation == 'min':
        return min(values)
    elif operation == 'max':
        return max(values)
    else:
        raise ValueError("Операция должна быть одной из: avg, min, max")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Путь к CSV-файлу')
    parser.add_argument('--where', help='Условие фильтрации, например price=>500 или brand==xiaomi')
    parser.add_argument('--aggregate', help='Агрегация, например price=avg')

    args = parser.parse_args()

    with open(args.file, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))

    if args.where:
        field, op, value = parse_filter(args.filter)
        reader = apply_filter(reader, field, op, value)

    if args.aggregate and args.operation:
        result = aggregate(reader, args.aggregate, args.operation)
        print(f"{args.operation} по полю '{args.aggregate}': {result}")
    else:
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
