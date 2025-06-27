grid = [
[1, 1, 1],
[1, 0, 1],
[1, 1, 1]
]
sumfromright=0
sumfromdown=0
sumfromrightdown=0
sumfromdownright=0
for i in range(0,2):
    for j in range(0,2):
        if i==0:
            sumfromright+=grid[i][j]
            if j==0:
                sumfromdownright+=grid[i][j]
                sumfromrightdown+=grid[i][j]
            if j==1:
                sumfromrightdown+=grid[i][j]
        if i==1:
            if j==0:
                sumfromdownright+=grid[i][j]
        if j==1:
            if i==2:
                sumfromdownright+=grid[i][j]
            if i==1:
                sumfromdownright+=grid[i][j]
                sumfromrightdown+=grid[i][j]
        if j==2:
            sumfromright+=grid[i][j]
            if i==1:
                sumfromrightdown+=grid[i][j]
            if j==2:
                 sumfromrightdown+=grid[i][j]
                 sumfromdownright+=grid[i][j]
        if j==0:
            sumfromdown+=grid[i][j]
        if i==2:
            sumfromdown+=grid[i][j]

print("Sum starting from right: ",sumfromright)
print("Sum starting from down: ",sumfromdown)
print("sum starting from right then down:",sumfromrightdown)
print("sum starting from down then right ",sumfromdownright)

#Question 2
print("Enter the list of prices in this: ")
print("to stop adding press 1")
num=input("Enter the number of prices ")
prices=[]
sum=0
while True:
 t=input("Enter price: ")
 if t<=1:
      break
 prices.append(t)
 sum+=t
avg=sum/num
max=0
min=1000000
for i in prices:
  if prices[i+1]>prices[i]:
      max=prices[i+1]
  if prices[i+1]<prices[i]:
      min=prices[i+1]

print("Minimum= ",min)
print("Maximum= ",max)
print("Avg= ", avg)

#QUESTION 4
def check_positive(x):
    if x>0:
        return(x*x)
    else:
        return ("Invalid! ")

numb=input("Enter a number! ")
print(check_positive(numb))









     











    





        
       


