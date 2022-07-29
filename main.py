import csv
from function import *


if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    SaveFullName(contacts_list)
    FullNameColumbs(contacts_list)
    search_double(contacts_list)
    telnote(contacts_list)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
