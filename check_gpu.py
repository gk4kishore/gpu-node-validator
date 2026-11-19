import csv
import sys


MAX_TEMP_C  = 85


def load_gpus(path):
    with open(path) as f:
       reader = csv.DictReader(f, skipinitialspace=True)
       return [row for row in reader if row.get("index", "").strip()]

def check_temperature(gpu):
    temp = int(gpu["temperature.gpu"])
    if temp < MAX_TEMP_C:
        return "PASS", f"GPU {gpu['index']} temp {temp}C"
    return "FAIL", f"GPU {gpu['index']} temp {temp}C (limit {MAX_TEMP_C}C)"

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "samples/healthy.csv"
    gpus = load_gpus(path)
    for gpu in gpus:
        status, message = check_temperature(gpu)
        print(f"[{status}] {message}")
