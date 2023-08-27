from datetime import datetime

from prettytable import PrettyTable


def prompt(msg, default: str = None, type_cast=None) -> str:
	"""Saves user input"""
	while True:

		value = input(f'{msg}: ' )

		if not value:
			return default

		if type_cast is None:
			return value

		try:
			return type_cast(value)
		except ValueError as err:
			print(err)


def print_table(headers: dict, iterable: list) -> None:
	"""Printing data table"""
	table = PrettyTable()
	table.field_names = headers.values()

	for row in iterable:
		for idx in row:
			data = [value for value in row[idx].values()]
			data.insert(0, idx)

			table.add_row(data)

	print(table)

