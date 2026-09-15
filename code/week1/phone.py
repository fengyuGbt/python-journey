# Phone number masking - L1 Day 4
phone = input("Enter your phone number: ")
while len(phone) != 11 or not phone.isdigit():
    print("Invalid phone number. Please enter an 11-digit number.")
    phone = input("Enter your phone number: ")
print(phone[:3] + "****" + phone[7:])
