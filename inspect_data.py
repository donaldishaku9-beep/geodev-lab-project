import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw in ("", "NA", "N/A", "-"):
            continue
        values.append(float(raw.replace(",", "")))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }


sum_result = inspect_column("mydata.csv", "pop_sum")
mean_result = inspect_column("mydata.csv", "pop_mean")

print("pop_sum:", sum_result)
print("pop_mean:", mean_result)