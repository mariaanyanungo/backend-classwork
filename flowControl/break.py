stop=int (input("Enter where to stop:"))
end=7
counter=1
while counter<=stop:
    print(counter)
    if counter==end:
        print("Ending the loop")
        break
    counter+=1