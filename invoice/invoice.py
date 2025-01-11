class Invoice:
    def __init__(self, invoice_number, date_issued, due_date):
        self.invoice_number = invoice_number
        self.date_issued = date_issued
        self.due_date = due_date

        self.seller = {
            "name": "",
            "address": "",
            "contact": "",
            "tax_registration_number": "",
        }

        self.buyer = {
            "name": "",
            "address": "",
            "contact": "",
        }

        self.items = []  # List to hold item dictionaries
        self.sub_total = 0
        self.tax_amount = 0
        self.grand_total = 0

        self.payment_details = {
            "method": "",
            "terms_and_conditions": "",
        }

    # Method to add items
    def add_item(self, description, quantity, unit_price):
        total = quantity * unit_price
        self.items.append({
            "description": description,
            "quantity": quantity,
            "unit_price": unit_price,
            "total": total,
        })
        self.calculate_totals()

    # Method to calculate totals
    def calculate_totals(self, tax_rate=0):
        self.sub_total = sum(item["total"] for item in self.items)
        self.tax_amount = (self.sub_total * tax_rate) / 100
        self.grand_total = self.sub_total + self.tax_amount


# Example usage
invoice = Invoice("INV-001", "2025-01-09", "2025-01-15")

invoice.seller = {
    "name": "ABC Corp",
    "address": "123 Main St, City",
    "contact": "123-456-7890",
    "tax_registration_number": "TAX-001",
}

invoice.buyer = {
    "name": "John Doe",
    "address": "456 Elm St, City",
    "contact": "987-654-3210",
}

invoice.add_item("Product A", 2, 50)  # Add an item
invoice.add_item("Service B", 1, 100)  # Add another item
invoice.calculate_totals(10)  # Apply a 10% tax rate

print(invoice.__dict__)
