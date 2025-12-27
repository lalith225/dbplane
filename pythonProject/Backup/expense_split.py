# Trip Expense Splitter - Final Version
# Author: ChatGPT
# Description: Handles multiple payments, multiple people, and detailed settlements.

print("💰 Trip Expense Splitter\n")

# Step 1: Get total number of people
num_people = int(input("Enter total number of people in the trip: "))

# Step 2: Get names of all people
people = []
for i in range(num_people):
    name = input(f"Enter name of person {i+1}: ").strip()
    people.append(name)

# Step 3: Collect expenses
print("\nNow start entering expenses. Type 'done' when finished.\n")

expenses = {person: 0.0 for person in people}

while True:
    payer = input("Who paid? (or type 'done' to finish): ").strip()
    if payer.lower() in ("done", "exit"):
        break

    if payer not in people:
        print("⚠️  Name not found. Please enter one of the registered people.")
        continue

    try:
        amount = float(input(f"How much did {payer} pay? (₹): ").strip())
    except ValueError:
        print("⚠️  Invalid amount. Try again.")
        continue

    purpose = input(f"What was it for? (e.g., breakfast, lunch, etc.): ").strip()

    expenses[payer] += amount
    print(f"✅ Recorded: {payer} paid ₹{amount:.2f} for {purpose}\n")

# Step 4: Summary of total and share
total_spent = sum(expenses.values())
share_per_person = total_spent / num_people

print("\n📊 --- Trip Expense Summary ---")
print(f"Total spent: ₹{total_spent:.2f}")
print(f"Equal share per person: ₹{share_per_person:.2f}\n")

# Step 5: Show what each person paid
print("🧾 Total Paid by Each Person:")
for person, amount in expenses.items():
    print(f"{person}: ₹{amount:.2f}")
print()

# Step 6: Balances (positive = receive, negative = pay)
balances = {p: round(expenses[p] - share_per_person, 2) for p in people}

print("📉 Balances:")
for person, balance in balances.items():
    if balance > 0:
        print(f"{person} should RECEIVE ₹{balance:.2f}")
    elif balance < 0:
        print(f"{person} should PAY ₹{-balance:.2f}")
    else:
        print(f"{person} is settled up")
print()

# Step 7: Settlement Matching (who pays whom)
payers = [(p, -b) for p, b in balances.items() if b < 0]
receivers = [(p, b) for p, b in balances.items() if b > 0]

settlements = []
i, j = 0, 0

while i < len(payers) and j < len(receivers):
    payer, pay_amount = payers[i]
    receiver, recv_amount = receivers[j]
    settle_amount = round(min(pay_amount, recv_amount), 2)
    settlements.append((payer, receiver, settle_amount))

    payers[i] = (payer, round(pay_amount - settle_amount, 2))
    receivers[j] = (receiver, round(recv_amount - settle_amount, 2))

    if payers[i][1] == 0:
        i += 1
    if receivers[j][1] == 0:
        j += 1

# Step 8: Show detailed settlement
print("💸 --- Who Pays Whom ---")
if settlements:
    for payer, receiver, amount in settlements:
        print(f"{payer} ➜ {receiver}: ₹{amount:.2f}")
else:
    print("All accounts are already settled!")

print("\n✅ All settlements complete! Everyone pays their fair share.")