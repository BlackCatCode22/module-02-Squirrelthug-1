def computepay(h, r):
    if hours > 40:
        overtimepay = 40 * rate + (hours - 40) * rate * 1.5
        return(f"OT Pay: {overtimepay}")
    else:
        reg = hours * rate
        return(f"Regular Pay: {reg}")

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

displaypay = computepay(hours, rate)

print(displaypay)
