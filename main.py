import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent

def read_rows(filename, required):
    with open(ROOT / filename, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or not set(required).issubset(reader.fieldnames):
            raise ValueError(f"{filename} needs columns: {', '.join(required)}")
        return list(reader)

def main():
    try:
        requirements = read_rows("requirements.csv", ["material", "unit", "required_quantity"])
        purchases = read_rows("purchases.csv", ["date", "material", "quantity", "unit_price", "supplier"])
        required, units = {}, {}
        for r in requirements:
            key = r["material"].strip().lower()
            required[key] = float(r["required_quantity"])
            units[key] = r["unit"].strip()
        bought, spend, prices = defaultdict(float), defaultdict(float), defaultdict(list)
        for r in purchases:
            key = r["material"].strip().lower()
            qty, price = float(r["quantity"]), float(r["unit_price"])
            if qty <= 0 or price < 0:
                raise ValueError("Purchase quantities must be positive and prices non-negative.")
            bought[key] += qty
            spend[key] += qty * price
            prices[key].append((price, r["supplier"], r["date"]))
    except (OSError, ValueError) as e:
        print("Data error:", e)
        return

    print("\nCONSTRUCTION MATERIAL REQUIREMENT & PURCHASE TRACKER")
    print("=" * 70)
    print(f"Actual purchase entries: {len(purchases)}")
    print(f"{'Material':<18}{'Required':>12}{'Purchased':>12}{'Balance':>12}{'Unit':>10}")
    print("-" * 70)
    for key, qty in required.items():
        got = bought[key]
        balance = max(qty - got, 0)
        print(f"{key.title():<18}{qty:>12.2f}{got:>12.2f}{balance:>12.2f}{units[key]:>10}")
        if prices[key]:
            best = min(prices[key], key=lambda x: x[0])
            average = spend[key] / got
            print(f"  Lowest recorded price: Rs.{best[0]:,.2f} from {best[1]} ({best[2]})")
            print(f"  Average recorded unit price: Rs.{average:,.2f}")
    print("-" * 70)
    print(f"Recorded purchase expenditure: Rs. {sum(spend.values()):,.2f}")
    print("Balance = estimated requirement minus recorded purchases (minimum zero).")
    print("This does not measure physical stock or material consumed.")

if __name__ == "__main__":
    main()
