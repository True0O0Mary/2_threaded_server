import csv
message_list = []


def write_empty_row(filename="history.csv"):
    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow("")


def write_message(datetime_mes, who, message, filename="history.csv"):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow((datetime_mes, who, message))

if __name__ == "__main__":
    write_message("12/12/22 09:03:04", "Mary", "HOHsadasd")
    write_empty_row()
    write_message("12/12/22 09:03:04", "Mary", "HOHOHO")
    write_empty_row()
    write_message("12/12/22 09:03:04", "Mary", "HOHOHO")