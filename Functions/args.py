# def year_of_birth(name,age):
#     year=2026-age
#     print(f"{name} was born in {year}")
# year_of_birth(name="Angella", age=21)
# year_of_birth(age=23, name="Alice")
# year_of_birth("Eunice",20)



# def infinite(**kwargs):
#     for key in kwargs.keys():
#         print(f"{key}")

# infinite(name="Anu", age=12, status="single",boyfriend="none")


# numbers=[1,23,3,4,5]
# sum = 0
# for number in numbers:
#     sum +=number
# print(sum)    


# sentence="What are you"
# reverse=sentence[::-1]
# print(reverse)

# list1=[1,23,3,4,5]
# list1.append(12)
# print(list1)



# def list_prediction(numbers):
#      is_positive=False
#      is_negative=False

#      for number in numbers:
#           if number>0:
#                is_positive=True
#           elif number<0:
#                is_negative=True

#      if is_negative and is_positive:
#           return "mixed"
#      elif is_negative:
#           return "negative"
#      elif is_positive:
#           return "positive"
#      else:
#           return "all zeros"
     
# print(list_prediction([0,0,0,0,0,0,0]))

# def int_list(array):
#     array.sort()
#     array.insert(5,700)
#     return array

# print(int_list([1,-25,7,-2,0,1]))


def num_list(array):
    for i in range(0,6):
        array[i]*=8
        return array
            break
    array[-2]+=5
    array[-1]+=5
        
    return array
        
print(num_list([1,2,3,4,5,6,7,8,9]))




