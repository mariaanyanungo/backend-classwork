# day = "Monday"
# match day:
#     case"Monday":
#         print("Start the week")
#     case "Friday":
#         print("End of week")
#     case _:
#         print("Regular day")



day= input("Enter today's day")
if day=="Monday":
    print("Start of the week")
elif day=="Friday":
    print("Wicked weekend")    
else:
    print("Regular day")