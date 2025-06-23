import statistics
from typing import List, Dict


def parse_aggregate(argument: str) -> tuple[str, str]:
    if '=' not in argument:
        raise ValueError("Параметр --aggregate должен быть в формате column=value")
    column, operation = argument.split('=')
    return column.strip(), operation.strip()


def aggregate(rows: List[Dict[str, str]], column: str, operation: str) -> float:
    try:
        values = [float(row[column]) for row in rows]
    except ValueError:
        raise ValueError(f"Невозможно агрегировать по полю '{column}' — значения не числовые")
    if not values:
        raise ValueError("Нет значений для агрегации")
    match operation:
        case 'avg':
            return statistics.mean(values)
        case 'min':
            return min(values)
        case 'max':
            return max(values)
        case _:
            raise ValueError("Операция должна быть одной из: avg, min, max")
