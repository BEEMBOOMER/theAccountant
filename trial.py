from datetime import datetime

date_text = "12/08/2026"  # example from your CSV
date_value = datetime.strptime(date_text, "%d/%m/%Y").date()
print(date_value)