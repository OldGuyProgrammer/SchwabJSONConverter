#
# Schwab JSON Loader
#
# Program to read financial transaction data downloaded from schwab.com
#
# The JSON data is converted to spreadsheet data for analysis
#
# The Old Guy Programmer, 2026
# Jim Olivi
#
import datetime
import json
import locale

import pandas

locale.setlocale(locale.LC_ALL, '')
import pandas as pd

def init_Schwab_JSON():

    file = 'Schwab.json'
    print('Get: ' + file)  # Press Ctrl+F8 to toggle the breakpoint.

    try:
        schwab_json = json.load(open(file))

    except FileNotFoundError:
        print(file + ' not found')
        return False

    from_date = datetime.datetime.strptime(schwab_json['FromDate'],'%m/%d/%Y')
    print(from_date)

    to_date = datetime.datetime.strptime(schwab_json['ToDate'],'%m/%d/%Y')
    print(to_date)

    total_amount = float(schwab_json['TotalTransactionsAmount'].replace("$", "").replace(",", ""))
    print(total_amount)

    transactions_df = pandas.DataFrame(schwab_json['BrokerageTransactions'])
    transactions_df['Date'] = pandas.to_datetime(transactions_df['Date'], errors='coerce')
    transactions_df['Amount'] = transactions_df['Amount'].str.replace("$", "").replace(",", "")
    transactions_df.to_csv("schwab_transactions.csv")

    print('Schwab JSON read into pandas complete')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Start Schwab JSON extractor')
    init_Schwab_JSON()

    print('End Schwab JSON extractor')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
