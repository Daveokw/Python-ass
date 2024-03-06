
def set_calculator():
    print('''Set Calculator,
        1. Union,
        2. Intersection,
        3. Difference,
        4. Symmetric Difference
        ''')
    
    user = int(input("Enter choice (1/2/3/4): "))

    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())

    if user == 1:
        result = set1.union(set2)
        print("Union:", result)
    elif user == 2:
        result = set1.intersection(set2)
        print("Intersection:", result)
    elif user == 3:
        result = set1.difference(set2)
        print("Difference (set1 - set2):", result)
    elif user == 4:
        result = set1.symmetric_difference(set2)
        print("Symmetric Difference:", result)
    else:
        print("Invalid choice")

set_calculator ()
