hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

def computepay():
    if hours > 40:
        overtimepay = 40 * rate + (hours - 40) * rate * 1.5
        print(f"OT Pay: {overtimepay}")
    else:
        reg = hours * rate
        print(f"Regular Pay: {reg}")

computepay()
