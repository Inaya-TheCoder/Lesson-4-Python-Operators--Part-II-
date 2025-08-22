Amount = int (input("Enter the amount u need:"))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10
print ("No. of $100 notes is",note1)
print ("No. of $50 notes is",note2)
print ("No. of $10 notes is",note3)