####################
#This math will help you see how many miles need to be driven to pay off a new part in
#your car. It is math
####################

partCost = 100 #y
higherMPG = 21 #b higher mpg mpg1
lowerMPG = 19 #a lower mpg mpg2
gasPrice = 2.5 #z

#costToDrive1 = (8000/mpg1*gasPrice)
#costToDrive2 = (8000/mpg2*gasPrice)

#print("CostToDrive1: ", costToDrive1)
#print("CostToDrive2: ", costToDrive2)
##################################################################

#partCostX = (8000/19*gasPrice) - (8000/21*gasPrice)

#print("PartCostX: ", partCostX)
##################################################################

#(a*b*y)/(-a*z+b*z)
partCost = float(input("Cost of upgrade: "))
higherMPG = float(input("new higher average mpg: "))
lowerMPG = float(input("old lower average mpg: "))
gasPrice = float(input("enter gas price: "))

milageNeededToPayForPart = (lowerMPG*higherMPG*partCost)/(-lowerMPG*gasPrice+higherMPG*gasPrice)

print("milage needed to pay for part: ", milageNeededToPayForPart)