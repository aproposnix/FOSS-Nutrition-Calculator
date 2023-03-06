import csv

# Load CSV file and create a dictionary for each vegetable
vegetables = {}
with open('vegetables.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        vegetables[row['Vegetable']] = row

# Ask user to select a vegetable and enter the amount used
selected_vegetables = []
while True:
    print("Select a vegetable to add:")
    for i, vegetable in enumerate(vegetables.keys()):
        print(f"{i+1}. {vegetable}")
    print("0. Done adding vegetables.")
    choice = int(input("> "))
    if choice == 0:
        break
    vegetable_name = list(vegetables.keys())[choice-1]
    vegetable_amount = int(input(f"Enter the amount of {vegetable_name} used (in grams): "))
    selected_vegetables.append({'name': vegetable_name, 'amount': vegetable_amount})

# Calculate total nutritional value of selected vegetables
total_nutrients = {}
for vegetable in selected_vegetables:
    vegetable_nutrients = vegetables[vegetable['name']]
    nutrient_keys = [key for key in vegetable_nutrients.keys() if key not in ['Vegetable', 'Serving size', 'Amount Used']]
    for nutrient in nutrient_keys:
        nutrient_value = float(vegetable_nutrients[nutrient]) * vegetable['amount'] / 100
        if nutrient in total_nutrients:
            total_nutrients[nutrient] += nutrient_value
        else:
            total_nutrients[nutrient] = nutrient_value

# Print total nutritional value
print("\nTotal nutritional value:")
for nutrient, value in total_nutrients.items():
    print(f"{nutrient}: {value:.2f}g")

