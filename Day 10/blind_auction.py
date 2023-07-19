#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program.\n")
bids = {}
others = True
while others:

  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  bids[name] = int(bid)
  if others == 'no':
    others = False

current = ""
max = 0
for names in bids:
  if bids[names] > max:
    max = bids[names]
    current = names

print(f"The winner is {current} with a bid of ${max}")
