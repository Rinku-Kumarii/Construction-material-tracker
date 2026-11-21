# Construction Material Requirement & Purchase Tracker

A small Python CLI tool that compares estimated material requirements with recorded purchases. It reports purchased quantity, remaining requirement, recorded expenditure, and the lowest recorded unit price for each material.

## Requirements
Python 3.9+; no third-party packages.

## CSV files
`requirements.csv`: `material,unit,required_quantity`
`purchases.csv`: `date,material,quantity,unit_price,supplier`

Use consistent units for each material. Enter only actual records shared with permission. Anonymize confidential supplier, client and project details before publishing.

## Run
```bash
python main.py
```

## Limitations
- Purchase quantity may differ from quantity physically received or consumed.
- It does not track opening stock, consumption, wastage, returns or closing stock.
- Lowest price does not necessarily mean best value; quality, delivery, tax and transport are not modeled.
- It does not read engineering drawings or forecast future prices.
- Balance is a simple estimate-minus-purchases calculation.

Document actual data collection in `fieldwork.md`. Add two sources actually read in `research.md`. Write the required half-page reflection yourself in `reflection.md`.
