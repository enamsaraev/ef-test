from datetime import datetime

from prettytable import PrettyTable


def prompt(msg, default=None, type_cast=None):
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


def input_int(msg='Введите число', default=None):
	"""Запрашивает целое число от пользователя и возвращает ввод"""
	return prompt(msg, default, type_cast=int)



def input_float(msg='Введите число', default=None):
	"""Запрашивает дробное число от пользователя и возвращает ввод"""
	return prompt(msg, default, type_cast=float)


def input_date(msg='Введите дату', default=None, fmt='%Y-%m-%d'):
	"""Запрашивает дату от пользователя и возвращает ввод"""	
	return prompt(
        msg,
        default,
        type_cast=lambda value: datetime.strptime(value, fmt).date()
    )


def print_table(headers, iterable):
	table = PrettyTable()
	table.field_names = headers.values()

	for row in iterable:
		for idx in row:
			data = [value for value in row[idx].values()]
			data.insert(0, idx)

			table.add_row(data)

	print(table)

