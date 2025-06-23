from typing import Union


def parse_where(condition: str) -> tuple[str, str, Union[str, float]]:
    for op in ['>=', '<=', '==', '>', '<']:
        if op in condition:
            column, value = condition.split(op)
            column = column.strip()
            value = value.strip()
            try:
                value = float(value)
            except ValueError:
                value = value.lower()
            return column, op, value
    raise ValueError("Параметр --where должен содержать один из операторов: >, <, ==, >=, <=")


def apply_where(rows, column, op, value):
    result = []

    for row in rows:
        cell = row.get(column, '').strip()
        try:
            cell_val = float(cell)
            is_numeric = True
        except ValueError:
            cell_val = cell.lower()
            is_numeric = False

        if is_numeric and isinstance(value, (int, float)):
            match op:
                case '>':
                    if cell_val > value:
                        result.append(row)
                case '<':
                    if cell_val < value:
                        result.append(row)
                case '>=':
                    if cell_val >= value:
                        result.append(row)
                case '<=':
                    if cell_val <= value:
                        result.append(row)
                case '==':
                    if cell_val == value:
                        result.append(row)
        # Строковое сравнение (только ==
        elif not is_numeric and op == '==' and cell_val == value:
            result.append(row)

    return result
