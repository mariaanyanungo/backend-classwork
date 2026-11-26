stop=int (input("Enter where to stop:"))
counter=1
while counter<=stop:
    if counter%2==0:
        counter+=1
        continue
    print(counter)
    counter+=1