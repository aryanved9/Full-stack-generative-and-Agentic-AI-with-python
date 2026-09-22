# spliting complex task. write a function generate_report() that calls fetch_sales(), filter_valid_orders(),summarize_data().

def fetch_sales():
    print(f"fetching sales data")

def filter_valid_orders():
    print(f"filtering valid orders")

def summarize_data():
    print(f"summarzing data")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print(f"Report is ready")
    
generate_report()