class SalesReport:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, product_name, quantity, total_amount):
        self.sales_data.append({
            'product_name': product_name,
            'quantity': quantity,
            'total_amount': total_amount
        })

    def generate_sales_by_product_report(self):
        # Logic to generate sales by product report
        pass

    def generate_daily_sales_report(self):
        # Logic to generate daily sales report
        pass

    def generate_monthly_sales_summary(self):
        # Logic to generate monthly sales summary
        pass

    def display_sales_report(self):
        # Logic to display sales report
        pass
