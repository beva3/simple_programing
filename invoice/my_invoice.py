class Invoice:
    def __init__(self,id,d_issued,d_due):
        self._id        = id
        self._d_issued  = d_issued
        self._d_due     = d_due
    
        # seller :
        self.seller = {
            "name" : "",
            "contact" : "",
            "addres" : "",
            "taxRegistrationNumber" : ""
        }

        # buyer
        self.buyer = {
            "name" : "",
            "contact" : "",
            "addres" : "",
        }

        # (item) product : 
        self.items          = []
        self.sub_total      = 0
        self.tax_amount     = 0
        self.grand_total    = 0
    
    # add  item :
    def add_item(self,description,quatity,unit_price):
        total = quatity * unit_price
        self.items.append({
            "d":description,
            "qnt" : quatity,
            "up" : unit_price,
            "t" : total
        })
        self.calculate_total()
    def calculate_total(self,tax_rate = 0):
        self.sub_total = sum(item["t"] for item in self.items)
        self.tax_amount = (self.sub_total * tax_rate)/ 100
        self.grand_total = self.tax_amount + self.sub_total

    def display(self):
        print(f"id              = {self._id}")
        print(f"date issued     = {self._d_issued}")
        print(f"due date        = {self._d_due}")

        print("\n")

        # seller:
        print("seller")
        for key in self.seller :
            print(f"{key}   = {self.seller[key]}")
        print("\n")

        # buyer:
        print("buyer")
        for key in self.buyer :
            print(f"{key}   = {self.buyer[key]}")
        print("\n")

        # items
        if len(self.items) > 0 :
            for obj in self.items:
                print(obj)
        print(f"sub total = {self.sub_total}")
        print(f"tax amount = {self.tax_amount}")
        print(f"grand total = {self.grand_total}")


invoice = Invoice('12d','12-12-12','02-01-13')
invoice.seller = {
    "name"                  : "Raphel",
    "contact"               : "111-111-111",
    "addres"                : "LTE Tana",
    "taxRegistrationNumber" : "TAX-100"
}
invoice.buyer = {
    "name"                  : "Bienvenu",
    "contact"               : "111-111-222",
    "addres"                : "LTE Zama",
}

my_product = [
    {
        "description": "banana",
        "quantity" : 2,
        "unit_price" : 40      
    },
    {
        "description": "ananas",
        "quantity" : 2,
        "unit_price" : 20      
    }
]

# invoice.add_item("laptop",2,120)
# invoice.add_item('smart phone',1,200)
for obj in my_product :
    invoice.add_item(obj["description"],obj["quantity"],obj["unit_price"])
invoice.calculate_total(10)


invoice.display()
