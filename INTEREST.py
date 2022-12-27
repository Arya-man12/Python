def interest(principal,time=2,rate=0.100):
             return principal*rate*time

#main
prin=float(input("enter principal amount:"))
print("simple interest with default ROI and time values is:")
si1=interest(prin)
print("Rs",si1)
roi=float(input("enter rate of interest(ROI):"))
time=int(input("Enter time in years:"))
print("simple interest with your provided roi is")
si2=interest(prin,time,roi/100)
print("Rs",si2)
