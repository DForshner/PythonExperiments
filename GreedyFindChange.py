print("A greedy algorithm is used to solve optimization problems that involve picking items from a set.")
print("At every stage it always takes the next best choice without looking ahead or into the past.")
print("While it can offer a simple and efficient solution it doesn't always give the correct answer.")

def find_change(amount):
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    change = []

    while amount > 0:
        if amount > quarter:
            change.append(quarter)
            amount -= quarter
        elif amount > dime:
            change.append(dime)
            amount -= dime
        elif amount > nickel:
            change.append(nickel)
            amount -= nickel
        else:
            change.append(penny)
            amount -= penny

    return change

print('Change for 0.90: ', find_change(.90))
print('Change for 2.15: ', find_change(2.15))
