import csv


with open("results.csv", "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        print(f"For users : {row['No. of Users']}")
        print()
        print("####################################")
        for header in headers:
            if header == "Min":
                print(f"(0, {row[header]})")
            elif header == "50%":
                print(f"(50, {row[header]})")

            elif header == "50%":
                print(f"(50, {row[header]})")
            elif header == "66%":
                print(f"(66, {row[header]})")
            elif header == "75%":
                print(f"(75, {row[header]})")
            elif header == "80%":
                print(f"(80, {row[header]})")
            elif header == "90%":
                print(f"(90, {row[header]})")
            elif header == "95%":
                print(f"(95, {row[header]})")
            elif header == "98%":
                print(f"(98, {row[header]})")
            elif header == "99%":
                print(f"(99, {row[header]})")
            elif header == "99.90%":
                print(f"(99.90, {row[header]})")
            elif header == "99.99%":
                print(f"(99.99, {row[header]})")
            elif header == "99.99%":
                print(f"(99.99, {row[header]})")

        print("####################################")
        print()
