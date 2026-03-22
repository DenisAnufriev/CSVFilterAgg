import argparse
import csv

from tabulate import tabulate

from src.aggregation import parse_aggregate, aggregate
from src.filters import parse_where, apply_where


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Путь к CSV-файлу')
    parser.add_argument('--where', help='Условие фильтрации, например price>500')
    parser.add_argument('--aggregate', help='Агрегация, например price=avg')
    args = parser.parse_args()

    with open(args.file, newline='', encoding='utf-8') as f:
        data = list(csv.DictReader(f))

    if args.where:
        column, op, value = parse_where(args.where)
        data = apply_where(data, column, op, value)

    if args.aggregate:
        column, operation = parse_aggregate(args.aggregate)
        result = aggregate(data, column, operation)
        print(tabulate([[result]], headers=[operation], tablefmt="grid"))
    else:
        if not data:
            print("Нет данных для отображения.")
            return
        headers = data[0].keys()
        rows = [list(row.values()) for row in data]
        print(tabulate(rows, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
