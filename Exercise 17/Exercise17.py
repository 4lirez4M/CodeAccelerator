import csv

fieldnames = ['product title', 'initial price', 'inventory', 'discount',
              'seller', 'Date of Registration']

rows = [
    {
        'product title': 'clothing',
        'initial price': 300,
        'inventory': 12,
        'discount': 10,
        'seller': 'seller 1',
        'Date of Registration': "2023/10/20"
    },
    {
            'product title': 'shoes',
            'initial price': 400,
            'inventory': 20,
            'discount': 5,
            'seller': 'seller 2',
            'Date of Registration': "2023/10/20"
        }
]
filename = input("Enter file name:")
with open(f'{filename}.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
