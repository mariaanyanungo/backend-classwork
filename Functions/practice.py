def calculate_discount(price,category):
    def get_discount(category):
        if category=="student":
            return 20
        elif category=="senior":
            return 40
        else:
            return 0
    
    def final_price(price,discount_percentage):
        return price - (price * discount_percentage / 100)
    
    discount_percentage = get_discount(category)
    return final_price(price, discount_percentage)

print(calculate_discount(1000,"student"))


def reverse_string(text):
    result = ""
    
    for char in text:
        result = char + result
    
    return result
print(reverse_string("hello"))



def word_frequency(text):
  
    text = text.lower()
    
  
    for char in ".,!?":
        text = text.replace(char, "")
    
    words = text.split(" ")
    
    freq = {}
    
    for word in words:
      
            freq[word] = freq.get(word,0)+1
      
    return freq

print(word_frequency("hello! baby boo hello, hello? I"))

def student_report(students):
# students = [
#     {"name": "Alice", "scores": [80, 90, 100]},
#     {"name": "Bob", "scores": [40, 50, 60]},
#     {"name": "Charlie", "scores": [100, 100, 100]}
# ]

    for student in students:
    # print(student["name"])
       point1,point2,point3=(student["scores"])
       print(point1)
    # print(point2)
    # print(point3)
       average=0
       for point in point1:
           average+=point
           max=average/3

       for point in point2:
          average+=point
          max=average/3

       for point in point3:
          average+=point
          max=average/3

    

def report(students):
   result={}
   for student in students:
      name=student["name"]
      scores=student["scores"]
      avg=sum(scores)/len(scores)

      result[name]=(avg)
      highest=max(result.items(),key=lambda item:item[1])

   print(highest)
      
   
    

report(students = [
     {"name": "Alice", "scores": [80, 90, 100]},
     {"name": "Bob", "scores": [40, 50, 60]},
     {"name": "Charlie", "scores": [100, 100, 100]}
 ])
         
         
employees = [
    {"name": "Alice", "department": "Engineering", "salary": 90000},
    {"name": "Bob", "department": "Sales", "salary": 70000},
    {"name": "Charlie", "department": "Engineering", "salary": 110000},
    {"name": "Diana", "department": "Sales", "salary": 80000},
    {"name": "Eve", "department": "HR", "salary": 60000}
]
result={}
for employee in employees:
    department=employee["department"]
    salary=employee["salary"]

    result[department]=(salary)
print(result)








if student==max_mark:
    print([student])
print(max_mark)

def highest_students(students):
    highest={}

    for student in students:
        name=student["name"]
        grade=student["grade"]

        highest[name]=(grade)
    max_mark=max(highest.items(), key=lambda item:item[1])
    return max_mark

   

print(highest_students(students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 92}
]))


def high_students(students):
    result={}
    names_list=[]
    for student in students:

       name=student["name"]
       grade=student["grade"]
       result[name]=(grade)
    
       max_value=max(result, key=result.get)
       for k,v in result.items(): #if v==max_value:
           names_list.append(name)
           return(max_value,names_list)
        

print(high_students(students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 92}
]))


def login():
   users = {
    "alice": "1234",
    "bob": "pass99",
    "charlie": "qwerty"}
   username=(input("enter your username"))
   password=input("enter password")
   if username not in users:
       return "user not found"
    
   elif username in users and password in users:
        return "successful"
    
print(login())