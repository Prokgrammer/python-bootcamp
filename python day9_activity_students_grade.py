import csv

input_file = "grades.csv"
output_file = "results.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["Average", "Status"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        math = int(row["Math"])
        science = int(row["Science"])
        english = int(row["English"])

        average = round((math + science + english) / 3, 2)
        status = "Pass" if average >= 60 else "Fail"

        row["Average"] = average
        row["Status"] = status

        writer.writerow(row)

print("✅ Student results saved to results.csv")

with open("results.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)