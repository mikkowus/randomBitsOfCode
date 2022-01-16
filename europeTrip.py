##Math for a trip to europe



##this block of code helps you know when you have to start work and end work in NY vs Barcelona
startWorkTimeNY = 7 #Your start time in NY
quitWorkTimeNY = 6 #your quit time in NY

timeDiffBarecelona = 6
startWorkTimeBar = startWorkTimeNY+timeDiffBarecelona
getOffWorkTimeBar = quitWorkTimeNY+timeDiffBarecelona

#adujust start time to 12 hour clock from 24
if startWorkTimeBar > 12:
  startWorkTimeBar = startWorkTimeBar - 12

#adjust get off time to 12 hour clock from 24
if getOffWorkTimeBar > 12:
  getOffWorkTimeBar = getOffWorkTimeBar - 12

print(f"time to start work: " + str(startWorkTimeBar))
print(f"time to quit work: " + str(getOffWorkTimeBar))