import csv
import enum

import click as click
import xlrd as xlrd
import xlsxwriter as xlsxwriter


class Month(enum.Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Columns(enum.Enum):
    CURRENCY = 0
    TRADE_DATE = 1
    SETTLEMENT_DATE = 2
    TRADE_NUMBER = 3
    ACTION = 4
    QUANTITY = 5
    SYMBOL = 6
    DESCRIPTION = 7
    TB = 8
    EX = 9
    PRICE = 10
    GROSS_AMOUNT = 11
    COMMISION = 12
    SEC_FEES = 13
    INTEREST_AMOUNT = 14
    NET_AMOUNT = 15
    NET_AMOUNT_ACCOUNT_CURRENCY = 16


def extract_and_populate():
    input_file = "input.csv"


    with open(input_file) as csv_file, xlsxwriter.Workbook('hello.xlsx') as excel_book:
        sheet = excel_book.add_worksheet()
        csv_reader = csv.reader(csv_file, delimiter=',')

        for count, row in enumerate(csv_reader):
            rows_to_write = get_row_to_write(row)
            # Print relevant indexes to the Excel Sheet
            sheet.write_row(row=count, col=0, data=rows_to_write)


def get_row_to_write(row):
    relevant_column_indexes = [
        Columns.TRADE_DATE.value,
        Columns.ACTION.value,
        Columns.QUANTITY.value,
        Columns.SYMBOL.value,
        Columns.DESCRIPTION.value,
        Columns.GROSS_AMOUNT.value,
        Columns.COMMISION.value,
        Columns.SEC_FEES.value,
    ]
    row_to_write = []

    for col_index in relevant_column_indexes:
        # First row check
        if "-" not in row[Columns.TRADE_DATE.value]:
            row_to_write.append(row[col_index])
        else:
            if col_index == Columns.TRADE_DATE.value:
                row_to_write.append(get_formatted_date(row[col_index]))
            elif col_index == Columns.SYMBOL.value and not row[col_index]:
                row_to_write.append(get_symbol_from_description(row[Columns.DESCRIPTION.value]))
            elif col_index == 5:
                row_to_write.append(int(row[col_index]))
            elif col_index > 10:
                value = get_valid_number(row[col_index])
                row_to_write.append(value)
            else:
                row_to_write.append(row[col_index])

    return row_to_write


def get_valid_number(number: str) -> float:
    number = number.replace(",", "")

    if "(" in number:
        number = number.replace("(", "")
        number = number.replace(")", "")
        return float(f"-{number}")
    return float(number)


def get_symbol_from_description(description: str) -> str:
    return description.split()[1]


def get_formatted_date(date: str) -> str:
    # "11-11-20" DAY-MONTH-YEAR
    day, month, year = date.split("-")
    month_name = get_month_from_date(int(month))

    return f"{month_name} {day}, 20{year}"


def get_month_from_date(month_number: int) -> str:
    months = [
        "January",
        "Feburary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return months[month_number - 1]


if __name__ == "__main__":
    extract_and_populate()