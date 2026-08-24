total_sales = 0
for i in range(1, 6):
    sales = float(input(f"Enter sales for employee {i}:"))

    #Tax rate check
    if sales < 50000:
        tax_rate = 0.05
    elif 50000 <= sales <= 100000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    tax_amount = sales * tax_rate
    total_sales += sales
    print(f"Sale Amount: Rs.{sales:.2f}")
    print(f"Tax Amount: Rs.{tax_amount:.2f}")
    print()
avg_sales = total_sales / 5
print(f"Total sales: Rs.{total_sales:.2f}")
print(f"Average sales: Rs.{avg_sales:.2f}")