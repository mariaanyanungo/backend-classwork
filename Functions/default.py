def greet_student(name="Student"):
    print(f"Hello {name}, welcome to the python class")


def delivery_fee(location="Karen"):
    if location=="Karen":
        print(500)
    elif location=="Kilimani":
        print(800)
    else:
        print(1000)

delivery_fee()
delivery_fee("Karen")
delivery_fee("Kilimani")
delivery_fee("Kiambu")