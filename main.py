import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

produscts_per_supplier = {}

print(product_list.max_row)

for product_row in range(2, product_list.max_row + 1):
    supplier_name = product_list.cell(product_row, 4).value

    if supplier_name in produscts_per_supplier:
        current_num_products = produscts_per_supplier.get(supplier_name)
        produscts_per_supplier[supplier_name] = current_num_products + 1
    else:
        produscts_per_supplier[supplier_name] = 1

print(produscts_per_supplier)