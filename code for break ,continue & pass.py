for i in range(1, 10):
    if i == 3:
        pass       # Do nothing
    elif i == 5:
        continue   # Skip this iteration
    elif i == 7:
        break      # Stop the loop
    print("Current number:", i)

OUTPUT
Current number: 1
Current number: 2
Current number: 3
Current number: 4
Current number: 6

