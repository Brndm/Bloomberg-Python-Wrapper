from title import *
import sys
import os

# Global variables
bucket = {}
storage_folder = 'C:/Users/Fake_path/'


# Main menu
def main_menu():
    print("Welcome,")
    print("Please choose the menu you want to start:")
    print("1. Fetch Bloomberg data")
    print("0. Quit")
    choice = input(">> ")
    exec_menu(choice)
    return


def exec_menu(choice):
    os.system('cls')
    ch = choice.lower()

    if ch == '':
        print("Invalid selection, please insert a key.")
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.")
            menu_actions['main_menu']()
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def end_program():
    sys.exit()


# Store dict to excel
def store_to_excel(data):
    global storage_folder

    with pd.ExcelWriter(storage_folder + 'bloom_output.xlsx') as writer:
        for key in data:
            data[key].get_data().to_excel(writer, sheet_name=key)


def import_bloom_data():
    # Get inputs
    tickers = input("Enter titles: ('/' as sep)").split("/")
    fields = input("Enter fields:").split(" ")
    dates = input("Enter desired dates (yyyy-mm-dd):").split(" ")

    # If nothing is specified launch the example
    if len(tickers) == 1 or len(fields) == 1 or len(dates) == 1:
        print("Invalid entries. Example will be displayed ")
        bucket['SPX Index'] = Title(['SPX Index', ['open', 'high', 'low', 'last_price'], '2020-01-01', '2020-01-31'])
        bucket['SPX Index'].display_candle()
    else:
        # Fill dictionnary
        if len(dates) > 2:
            print("Incorrect number of arguments for field dates")
        else:
            for i in range(len(tickers)):
                # Check if ref or histo
                if len(dates) < 2:
                    bucket[tickers[i]] = Title([tickers[i], fields])
                elif len(dates) == 2:
                    bucket[tickers[i]] = Title([tickers[i], fields, dates[0], dates[1]])
                    # bucket[tickers[i]].display_candle()

    # Save to excel
    store_to_excel(bucket)
    return


# =======================
#      MAIN PROGRAM
# =======================

menu_actions = {'main_menu': main_menu, '1': import_bloom_data, '9': back, '0': end_program}
main_menu()
