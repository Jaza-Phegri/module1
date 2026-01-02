amount=int(input("Please enter amount"))
n1=amount//100
n2=(amount%100)//50
n3=((amount%100)%50)//10
print(f"100 rs note are {n1}")
print(f"50 rs note are {n2}")
print(f"10 rs note are {n3}")