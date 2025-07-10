pricesf = {
    "Codealpha": 180,
    "Codesf": 250,
    "Fredztech": 140,
    "Jonova": 130,
    "Princesoft": 310
}

print(" Simple Stock Tracker")
print(" options :",pricesf)
print("Type 'done' to finish.\n")

total = 0
summary = []
while True:
    stock = input("Stock name: ").title()
    if stock == "Done":
        break
    if stock not in pricesf:
        print("Not available. Try Codealpha,Codesf,Fredztech ,Jonova , princesoft.")
        continue

    try:
        qty = int(input("Quantity: "))
        total += qty * pricesf[stock]
    except:
        print("Enter a valid number.")

print(f"\n Total Investment: ${total}")
save = input("Save to a .txt file? (yes/no): ").lower()
if save == "yes":
    file_name = input("Enter file name (Example: portfolio.txt): ")
    with open(file_name, "w") as f:
        f.write("Your Stock Summary:\n")
        for line in summary:
            f.write(line + "\n")
        f.write(f"\nTotal Investment: ${total}\n")
    print(f"Saved to '{file_name}'")
else:
    print("All done. No file saved")
