#Question 1
def intro_q1(name_q1, age_q1, city_q1):
    print("My name is", name_q1)
    print("I am", age_q1, "years old")
    print("I live in", city_q1)

intro_q1("Ali", 18, "Karachi")

#Question 2
def get_info_q2():
    name_q2="Ali"
    age_q2=18
    city_q2="Lahore"
    return name_q2, age_q2, city_q2
name_q2, age_q2, city_q2 = get_info_q2()
print("Name:", name_q2)
print("Age:", age_q2)
print("City:", city_q2)

#Question 3
def greet_q3(name_q3, greeting_q3="Hello"):
    print(greeting_q3, name_q3)
greet_q3("Ali")
greet_q3("Sara", "Hi")

#Question 4
def show_info_q4(name_q4, age_q4, city_q4):
    print("Name:", name_q4)
    print("Age:", age_q4)
    print("City:", city_q4)
show_info_q4(name_q4="Ali", age_q4=18, city_q4="Karachi")

#Question 5
def sum_numbers_q5(*numbers_q5):
    total_q5 = 0
    for num_q5 in numbers_q5:
        total_q5 += num_q5
    return total_q5
print("Sum:", sum_numbers_q5(1, 2, 3, 4, 5))

#Question 6
def handle_q6(*args_q6):
    if len(args_q6) == 1:
        return args_q6[0] 
    elif len(args_q6) == 2:
        val1_q6, val2_q6 = args_q6
        if isinstance(val1_q6, (int, float)) and isinstance(val2_q6, (int, float)):
            return val1_q6 + val2_q6
        elif isinstance(val1_q6, str) and isinstance(val2_q6, str):
            return val1_q6 + " " + val2_q6
    return args_q6 
print(handle_q6(7))
print(handle_q6(3, 4))
print(handle_q6("Good", "Morning"))
print(handle_q6(1, 2, 3))

#Question 7
def double_q7(x_q7):
    return x_q7 * 2

def increment_q7(x_q7):
    return x_q7 + 1

def compose_q7(x_q7):
    return increment_q7(double_q7(x_q7))
print("Result:", compose_q7(5)) 

#Question 8
def applyq8(listq8,functq8):
    newlistq8=[]
    for itemq8 in listq8:
        newlistq8.append(functq8(itemq8))
    return newlistq8
def squareq8(numq8):
    return numq8 * numq8
print("mapped:", applyq8([1, 2, 3, 4], squareq8))

#Question 9
def fq9(aq9):
    def gq9(bq9):
        def hq9(cq9):
            return aq9 * bq9 * cq9
        return hq9
    return gq9
print("result:", fq9(2)(3)(4))

#Question 10
import functools as ftq10
def multiplyq10(aq10, bq10):
    return aq10 * bq10
multiplybytenq10 = ftq10.partial(multiplyq10, 10)
print("result:", multiplybytenq10(7))

#Question 11
def fibq11(nq11,cacheq11={}):
    if nq11 in cacheq11:
        return cacheq11[nq11]
    if nq11 <= 1:
        resultq11 = nq11
    else:
        resultq11 = fibq11(nq11 - 1) + fibq11(nq11 - 2)
    cacheq11[nq11] = resultq11
    return resultq11
print("fib(10):", fibq11(10))

#question 12
from functools import lru_cache
@lru_cache(maxsize=None)
def heavycalcq12(nq12):
    if nq12 <= 1:
        return nq12
    return heavycalcq12(nq12 - 1) + heavycalcq12(nq12 - 2)
print("result:", heavycalcq12(30))

#question 13
import time
def timerq13(funcq13):
    def wrapperq13(*argsq13, **kwargsq13):
        startq13 = time.time()
        resultq13 = funcq13(*argsq13, **kwargsq13)
        endq13 = time.time()
        print("time taken:", endq13 - startq13, "seconds")
        return resultq13
    return wrapperq13
@timerq13 
def exampletaskq13():
    totalq13 = 0
    for numq13 in range(1000000):
        totalq13 += numq13
    return totalq13

print("result:", exampletaskq13())

#Question 14
def docprinterq14(funcq14):
    def wrapperq14(*argsq14, **kwargsq14):
        print("docstring:", funcq14.__doc__)
        return funcq14(*argsq14, **kwargsq14)
    return wrapperq14
@docprinterq14
def greetq14(nameq14):
    """This function greets the person by name."""
    print("hello", nameq14)
greetq14("ali")

#Question 15
def testfunctionq15(funcq15, testcasesq15):
    for indexq15, caseq15 in enumerate(testcasesq15):
         inputq15, expectedq15 = caseq15
         outputq15 = funcq15(*inputq15)
         if outputq15 == expectedq15:
            print("test", indexq15, "passed")
         else:
            print("test", indexq15, "failed → expected:", expectedq15, "got:", outputq15)

def addq15(aq15, bq15):
    return aq15 + bq15
casesq15 = [
    ((2, 3), 5),
    ((0, 0), 0),
    ((-1, 1), 0),
    ((10, 5), 15)
]
testfunctionq15(addq15, casesq15)

#Question 16
def validateq16(funcq16):
    def wrapperq16(*argsq16, **kwargsq16):
        for valueq16 in argsq16:
            if not (isinstance(valueq16, int) and valueq16 > 0):
                print("error: only positive integers allowed")
                return None
        return funcq16(*argsq16, **kwargsq16)
    return wrapperq16
def multiplyq16(aq16, bq16):
    return aq16 * bq16

print("result 1:", multiplyq16(5, 3))    
print("result 2:", multiplyq16(-2, 4))   
print("result 3:", multiplyq16(2, 0))    
print("result 4:", multiplyq16(7, 1))

#question 17
import dill

def greetq17(nameq17):
    print("hello", nameq17)
with open("greetq17.pkl", "wb") as fileq17:
    dill.dump(greetq17, fileq17)
with open("greetq17.pkl", "rb") as fileq17:
    loadedgreetq17 = dill.load(fileq17)
loadedgreetq17("ali")

#question 18
registryq18 = {}

def registerq18(funcq18):
    registryq18[funcq18.__name__] = funcq18
    return funcq18 

@registerq18
def greetq18(nameq18):
    print("hello", nameq18)

@registerq18
def addq18(aq18, bq18):
    return aq18 + bq18

@registerq18
def squareq18(nq18):
    return nq18 * nq18

print("registry:", registryq18)  
print("square of 5:", registryq18 )

#Question 19

def middlewareq19(funcq19):
    def wrapperq19(*argsq19, **kwargsq19):
        print("input →", argsq19, kwargsq19)
        resultq19 = funcq19(*argsq19, **kwargsq19)
        print("output →", resultq19)
        return resultq19
    return wrapperq19
@middlewareq19
def addq19(aq19, bq19):
    return aq19 + bq19
@middlewareq19
def greetq19(nameq19):
    return "hello " + nameq19
addq19(5, 3)
greetq19("ali")

#question 20
def buildpipelineq20(*funcsq20):
    """returns a new function that applies all funcs in order"""
    def pipelineq20(valueq20):
        resultq20 = valueq20
        for stepq20 in funcsq20:
            resultq20 = stepq20(resultq20)   
        return resultq20
    return pipelineq20

def doubleq20(xq20):
    return xq20 * 2

def incrementq20(xq20):
    return xq20 + 1

def squareq20(xq20):
    return xq20 * xq20
mypipelineq20 = buildpipelineq20(doubleq20, incrementq20, squareq20)
print("pipeline result:", mypipelineq20(3)) 


#question 21
def addq21(aq21, bq21):
    return aq21 + bq21
def subtractq21(aq21, bq21):
    return aq21 - bq21
def multiplyq21(aq21, bq21):
    return aq21 * bq21
def divideq21(aq21, bq21):
    if bq21 == 0:
        return "error: division by zero"
    return aq21 / bq21
def powerq21(aq21, bq21):
    return aq21 ** bq21
def modulusq21(aq21, bq21):
    return aq21 % bq21
print("add:", addq21(3, 2))
print("subtract:", subtractq21(10, 4))
print("multiply:", multiplyq21(6, 3))
print("divide:", divideq21(8, 2))
print("power:", powerq21(2, 5))
print("modulus:", modulusq21(10, 3))


#question 22
import string
def cleanreversecapq22(textq22):
    cleanedq22 = ""
    for charq22 in textq22:
        if charq22 not in string.punctuation:
            cleanedq22 += charq22
    reversedq22 = cleanedq22[::-1]
    capitalizedq22 = reversedq22.upper()
    return capitalizedq22

print(cleanreversecapq22("Hello, world!"))

#question 23
def processdataq23(dataq23, keyq23, thresholdq23=0):
    validq23 = []
    for itemq23 in dataq23:
        if keyq23 in itemq23:
            valq23 = itemq23[keyq23]
            if isinstance(valq23, (int, float)) and valq23 >= thresholdq23:
                validq23.append(valq23)
    if not validq23:
        return None
    return sum(validq23) / len(validq23)
sampleq23 = [
    {"value": 10, "name": "a"},
    {"value": -3, "name": "b"},
    {"value": 7.5, "name": "c"},
    {"name": "d"},
    {"value": 2, "name": "e"}
]
print(processdataq23(sampleq23, "value", 0))


#question 24
def isprimeq24(nq24):
    if nq24 < 2:
        return False
    for xq24 in range(2, int(nq24 ** 0.5) + 1):
        if nq24 % xq24 == 0:
            return False
    return True
def factorialq24(nq24):
    if nq24 < 0:
        return None
    resultq24 = 1
    for xq24 in range(2, nq24 + 1):
        resultq24 *= xq24
    return resultq24

def isevenq24(nq24):
    return nq24 % 2 == 0
print("prime:", isprimeq24(13))
print("factorial:", factorialq24(5))
print("even:", isevenq24(6))

#Question 25
def runonceq25(funcq25):
    hasrunq25 = {"done": False}
    def wrapperq25(*argsq25, **kwargsq25):
        if not hasrunq25["done"]:
            hasrunq25["done"] = True
            return funcq25(*argsq25, **kwargsq25)
        else:
            print("skipped: already run once")
    return wrapperq25

@runonceq25
def setupq25():
    print("setup function executed")

setupq25()
setupq25()
setupq25()

#✅ Title: Advanced Function Concepts
#🎯 Focus: Master advanced Python function concepts including *args, **kwargs, lambdas, closures, generators, async, decorators, and design patterns.
#question 1
def showargskwargsq27(*argsq27, **kwargsq27):
    print("positional args:", argsq27)
    print("keyword args:", kwargsq27)

showargskwargsq27(1, 2, 3, nameq27="ali", ageq27=18, cityq27="lahore")

#question 2
squareq28 = lambda xq28: xq28 * xq28
cubeq28 = lambda xq28: xq28 * xq28 * xq28
absq28 = lambda xq28: xq28 if xq28 >= 0 else -xq28

print("square:", squareq28(4))
print("cube:", cubeq28(3))
print("absolute:", absq28(-7))

#question 3
def makecounterq29():
    countq29 = 0
    def counterq29():
        nonlocal countq29
        countq29 += 1
        return countq29
    return counterq29
counterinstanceq29 = makecounterq29()
print("call 1:", counterinstanceq29())
print("call 2:", counterinstanceq29())
print("call 3:", counterinstanceq29())

#question 4
import time
import random
def timingq30(funcq30):
    def wrapperq30(*argsq30, **kwargsq30):
        startq30 = time.time()
        resultq30 = funcq30(*argsq30, **kwargsq30)
        endq30 = time.time()
        print("time taken:", endq30 - startq30, "seconds")
        return resultq30
    return wrapperq30

def retryq30(maxtriesq30=3, delayq30=1):
    def decoratorq30(funcq30):
        def wrapperq30(*argsq30, **kwargsq30):
            attemptq30 = 0
            while True:
                try:
                    return funcq30(*argsq30, **kwargsq30)
                except Exception as errorq30:
                    attemptq30 += 1
                    print("attempt", attemptq30, "failed:", errorq30)
                    if attemptq30 >= maxtriesq30:
                        raise
                    else:
                        time.sleep(delayq30)
        return wrapperq30
    return decoratorq30
@timingq30
@retryq30(maxtriesq30=5, delayq30=0.5)
def flakyq30():
    numberq30 = random.random()
    if numberq30 < 0.7:
        raise ValueError("random failure")
    else:
        print("success:", numberq30)

flakyq30()

#Question 5
def mathfactoryq31(operationq31):
    if operationq31 == "add":
        def addq31(aq31, bq31):
            return aq31 + bq31
        return addq31
    elif operationq31 == "subtract":
        def subtractq31(aq31, bq31):
            return aq31 - bq31
        return subtractq31
    elif operationq31 == "multiply":
        def multiplyq31(aq31, bq31):
            return aq31 * bq31
    elif operationq31 == "divide":
        def divideq31(aq31, bq31):
            if bq31 == 0:
                return "error: division by zero"
            else:
                return aq31 / bq31
        return divideq31
    else:
        return None

addfuncq31 = mathfactoryq31("add")
multiplyfuncq31 = mathfactoryq31("multiply")
dividefuncq31 = mathfactoryq31("divide")
print("add result:", addfuncq31(5, 3))
print("multiply result:", multiplyfuncq31(4, 2))
print("divide result:", dividefuncq31(10, 0))

#Question 6
eventmanagerq32 = {
    "registry": {}
}
def registercallbackq32(eventnameq32, callbackq32):
    """attach a callback to an event name"""
    if eventnameq32 in eventmanagerq32["registry"]:
        eventmanagerq32["registry"][eventnameq32].append(callbackq32)
    else:
        eventmanagerq32["registry"][eventnameq32] = [callbackq32]
def triggereventq32(eventnameq32, payloadq32=None):
    """run all callbacks linked to an event"""
    if eventnameq32 in eventmanagerq32["registry"]:
        for cbq32 in eventmanagerq32["registry"][eventnameq32]:
            cbq32(payloadq32)
    else:
        print("no callbacks for event:", eventnameq32)
def emailnotifyq32(dataq32):
    print("email sent with data:", dataq32)

def smsnotifyq32(dataq32):
    print("sms sent with data:", dataq32)

def lognotifyq32(dataq32):
    print("log entry:", dataq32)

registercallbackq32("order_placed", emailnotifyq32)
registercallbackq32("order_placed", smsnotifyq32)
registercallbackq32("order_placed", lognotifyq32)
triggereventq32("order_placed", {"orderid": 101, "amount": 2500})
triggereventq32("payment_failed", {"orderid": 102})

#Question 7
class eventhandlerq33:
    def __init__(self):
        self.listenersq33 = {}
    def addlistenerq33(self, eventnameq33, callbackq33):
        if eventnameq33 in self.listenersq33:
            self.listenersq33[eventnameq33].append(callbackq33)
        else:
            self.listenersq33[eventnameq33] = [callbackq33]
    def removeallq33(self, eventnameq33):
        if eventnameq33 in self.listenersq33:
            del self.listenersq33[eventnameq33]
    def dispatchq33(self, eventnameq33, dataq33=None):
        if eventnameq33 in self.listenersq33:
            for callbackq33 in self.listenersq33[eventnameq33]:
                callbackq33(dataq33)
        else:
            print("no listeners for:", eventnameq33)
def handleroneq33(dataq33):
    print("handler one:", dataq33)
def handlertwoq33(dataq33):
    print("handler two:", dataq33)
def handlerthreeq33(dataq33):
    print("handler three:", dataq33)
eventsysq33 = eventhandlerq33()
eventsysq33.addlistenerq33("click", handleroneq33)
eventsysq33.addlistenerq33("click", handlertwoq33)
eventsysq33.addlistenerq33("submit", handlerthreeq33)
eventsysq33.dispatchq33("click", {"target": "button1"})
eventsysq33.dispatchq33("submit", {"form": "login"})
eventsysq33.dispatchq33("hover", {"area": "nav"})

#question 8
def composeq34(fq34, gq34):
    def composedq34(xq34):
        return fq34(gq34(xq34))
    return composedq34
def doubleq34(xq34):
    return xq34 * 2
def squareq34(xq34):
    return xq34 * xq34
combinedq34 = composeq34(squareq34, doubleq34)
print("result:", combinedq34(3))

#Question 9
class functionchainq35:
    def __init__(self, valueq35):
        self.valueq35 = valueq35
        self.stepsq35 = []
    def addstepq35(self, funcq35):
        self.stepsq35.append(funcq35)
        return self
    def runq35(self):
        resultq35 = self.valueq35
        for funcq35 in self.stepsq35:
            resultq35 = funcq35(resultq35)
        return resultq35
def doubleq35(xq35):
    return xq35 * 2
def incrementq35(xq35):
    return xq35 + 1

def squareq35(xq35):
    return xq35 * xq35
chainq35 = functionchainq35(3).addstepq35(doubleq35).addstepq35(incrementq35).addstepq35(squareq35)
print("final result:", chainq35.runq35())

#question 10
import asyncio

async def fetchdataq36():
    print("starting fetch...")
    await asyncio.sleep(2)
    print("data received!")
    return {"user": "ali", "id": 101}

async def mainq36():
    resultq36 = await fetchdataq36()
    print("result:", resultq36)

asyncio.run(mainq36())

#question 11
def evennumsq37(nq37):
    currentq37 = 0
    while currentq37 <= nq37:
        yield currentq37
        currentq37 += 2

for numq37 in evennumsq37(20):
    print(numq37)

#question 12
def flattenq38(listq38):
    resultq38 = []
    for itemq38 in listq38:
        if isinstance(itemq38, list):
            resultq38.extend(flattenq38(itemq38))
        else:
            resultq38.append(itemq38)
    return resultq38

nestedlistq38 = [1, [2, [3, 4], 5], [6, 7], 8]
print("flattened:", flattenq38(nestedlistq38))

#question 13

def sumtailq39(numbersq39):
    def helperq39(indexq39, accumq39):
        if indexq39 == len(numbersq39):
            return accumq39
        else:
            return helperq39(indexq39 + 1, accumq39 + numbersq39[indexq39])
    return helperq39(0, 0)

print(sumtailq39([1, 2, 3, 4, 5]))

#question 14
def makecounterq40():
    countq40 = 0
    def counterq40():
        nonlocal countq40
        countq40 += 1
        return countq40
    return counterq40
countera40 = makecounterq40()
print(countera40())  
print(countera40())  
print(countera40())   
counterb40 = makecounterq40()
print(counterb40())

#question 15
def safeexecuteq41(funcq41, *argsq41, **kwargsq41):
    try:
        return funcq41(*argsq41, **kwargsq41)
    except Exception as errorq41:
        print("error occurred:", errorq41)
        return None

def divideq41(aq41, bq41):
    return aq41 / bq41
print(safeexecuteq41(divideq41, 10, 2))  
print(safeexecuteq41(divideq41, 10, 0))

#question 16
calllogq42 = {}

def logcallsq42(funcq42):
    def wrapperq42(*argsq42, **kwargsq42):
        print("call:", funcq42.__name__, "args:", argsq42, "kwargs:", kwargsq42)
        resultq42 = funcq42(*argsq42, **kwargsq42)
        print("return:", resultq42)
        calllogq42[funcq42.__name__] = calllogq42.get(funcq42.__name__, []) + [(argsq42, kwargsq42, resultq42)]
        return resultq42
    return wrapperq42

@logcallsq42
def addq42(aq42, bq42):
    return aq42 + bq42

@logcallsq42
def greetq42(nameq42):
    return "hello " + nameq42

addq42(3, 4)
greetq42("ali")
print("history:", calllogq42)

#question 17
import time

statsq43 = {}
def monitorq43(funcq43):
    def wrapperq43(*argsq43, **kwargsq43):
        startq43 = time.time()
        resultq43 = funcq43(*argsq43, **kwargsq43)
        endq43 = time.time()
        durationq43 = endq43 - startq43

        nameq43 = funcq43.__name__
        if nameq43 not in statsq43:
            statsq43[nameq43] = {"count": 0, "total_time": 0.0}

        statsq43[nameq43]["count"] += 1
        statsq43[nameq43]["total_time"] += durationq43

        return resultq43
    return wrapperq43

@monitorq43
def slowtaskq43():
    time.sleep(0.3)
    return "done"

slowtaskq43()
slowtaskq43()
slowtaskq43()

countq43 = statsq43["slowtaskq43"]["count"]
averageq43 = statsq43["slowtaskq43"]["total_time"] / countq43
print("calls:", countq43)
print("average time:", round(averageq43, 3), "seconds")

#question 18
def optimizedfibq44(nq44, cacheq44={}):
    if nq44 in cacheq44:
        return cacheq44[nq44]
    if nq44 <= 1:
        cacheq44[nq44] = nq44
    else:
        cacheq44[nq44] = optimizedfibq44(nq44 - 1) + optimizedfibq44(nq44 - 2)
    return cacheq44[nq44]

print("fib(10):", optimizedfibq44(10))
print("fib(30):", optimizedfibq44(30))
print("fib(50):", optimizedfibq44(50))

#question 19
def executeq45(strategyq45, aq45, bq45):
    return strategyq45(aq45, bq45)

def addq45(aq45, bq45):
    return aq45 + bq45

def subtractq45(aq45, bq45):
    return aq45 - bq45

def multiplyq45(aq45, bq45):
    return aq45 * bq45

print("add:", executeq45(addq45, 10, 5))
print("subtract:", executeq45(subtractq45, 10, 5))
print("multiply:", executeq45(multiplyq45, 10, 5))

#question 20

def calculate_averageq46(numbersq46):
    """Returns the average of a list of numbers if valid, otherwise None."""
    if not numbersq46:
        return None

    totalq46 = 0
    for valueq46 in numbersq46:
        if not isinstance(valueq46, (int, float)):
            return None
        totalq46 += valueq46

    return totalq46 / len(numbersq46)


print("average 1:", calculate_averageq46([10, 20, 30]))      
print("average 2:", calculate_averageq46([]))                 
print("average 3:", calculate_averageq46([5, 'a', 15]))



















