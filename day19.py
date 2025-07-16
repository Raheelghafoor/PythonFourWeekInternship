#Question 1
import functools
import time
def timerDecoratorQ1(funcQ1):
    @functools.wraps(funcQ1)
    def wrapperQ1(*argsQ1, **kwargsQ1):
        startTimeQ1 = time.perf_counter()
        resultQ1 = funcQ1(*argsQ1, **kwargsQ1)
        endTimeQ1 = time.perf_counter()
        durationQ1 = endTimeQ1 - startTimeQ1
        print(f"{funcQ1.__name__} executed in {durationQ1:.4f} seconds")
        return resultQ1
    return wrapperQ1
def intArgsOnlyDecoratorQ1(funcQ1):
    @functools.wraps(funcQ1)
    def wrapperQ1(*argsQ1, **kwargsQ1):
        for argQ1 in argsQ1:
            if not isinstance(argQ1, int):
                raise TypeError("All arguments must be integers")
        return funcQ1(*argsQ1, **kwargsQ1)
    return wrapperQ1
def callCounterDecoratorQ1(funcQ1):
    @functools.wraps(funcQ1)
    def wrapperQ1(*argsQ1, **kwargsQ1):
        wrapperQ1.callCountQ1 += 1
        print(f"{funcQ1.__name__} has been called {wrapperQ1.callCountQ1} times")
        return funcQ1(*argsQ1, **kwargsQ1)
    wrapperQ1.callCountQ1 = 0
    return wrapperQ1

if __name__ == '__main__':
    @timerDecoratorQ1
    @intArgsOnlyDecoratorQ1
    @callCounterDecoratorQ1
    def addNumbersQ1(aQ1, bQ1):
        time.sleep(1)
        return aQ1 + bQ1

    print("Result:", addNumbersQ1(10, 20))
    print("Result:", addNumbersQ1(5, 7))

#Question 2
import time
import functools

def timingDecoratorQ2(funcQ2):
    @functools.wraps(funcQ2)
    def wrapperQ2(*argsQ2, **kwargsQ2):
        startTimeQ2 = time.perf_counter()
        resultQ2 = funcQ2(*argsQ2, **kwargsQ2)
        endTimeQ2 = time.perf_counter()
        print(f"{funcQ2.__name__} took {endTimeQ2 - startTimeQ2:.4f} seconds to run")
        return resultQ2
    return wrapperQ2
if __name__ == '__main__':
    @timingDecoratorQ2
    def slowFunctionQ2():
        time.sleep(2)
        return "Finished slow function"

    print(slowFunctionQ2())

#Question 3

import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
def loggingDecoratorQ3(funcQ3):
    @functools.wraps(funcQ3)
    def wrapperQ3(*argsQ3, **kwargsQ3):
        logging.info(f"Calling {funcQ3.__name__} with args={argsQ3}, kwargs={kwargsQ3}")
        resultQ3 = funcQ3(*argsQ3, **kwargsQ3)
        logging.info(f"{funcQ3.__name__} returned {resultQ3}")
        return resultQ3
    return wrapperQ3

if __name__ == '__main__':
    @loggingDecoratorQ3
    def multiplyNumbersQ3(xQ3, yQ3):
        return xQ3 * yQ3

    print(multiplyNumbersQ3(3, 4))

#Question 4

import functools

def cachingDecoratorQ4(funcQ4):
    cacheQ4 = {}
    @functools.wraps(funcQ4)
    def wrapperQ4(*argsQ4, **kwargsQ4):
       
        keyQ4 = (argsQ4, tuple(sorted(kwargsQ4.items())))
        if keyQ4 in cacheQ4:
            return cacheQ4[keyQ4]
        else:
            resultQ4 = funcQ4(*argsQ4, **kwargsQ4)
            cacheQ4[keyQ4] = resultQ4
            return resultQ4
    return wrapperQ4
if __name__ == '__main__':
    @cachingDecoratorQ4
    def fibonacciQ4(nQ4):
        if nQ4 <= 1:
            return nQ4
        else:
            return fibonacciQ4(nQ4 - 1) + fibonacciQ4(nQ4 - 2)

    for indexQ4 in range(10):
        print(f"fibonacciQ4({indexQ4}) =", fibonacciQ4(indexQ4))

#Question 5

import functools
def validatePositiveIntegersQ5(funcQ5):
    @functools.wraps(funcQ5)
    def wrapperQ5(*argsQ5, **kwargsQ5):
        for valueQ5 in argsQ5:
            if not isinstance(valueQ5, int):
                raise TypeError("All arguments must be integers")
            if valueQ5 <= 0:
                raise ValueError("All arguments must be positive integers")
        return funcQ5(*argsQ5, **kwargsQ5)
    return wrapperQ5
if __name__ == '__main__':
    @validatePositiveIntegersQ5
    def calculateFactorialQ5(nQ5):
        resultQ5 = 1
        for iQ5 in range(1, nQ5 + 1):
            resultQ5 *= iQ5
        return resultQ5

    print(calculateFactorialQ5(5))


#Question 6

import functools

def adminRequiredDecoratorQ6(funcQ6):
    @functools.wraps(funcQ6)
    def wrapperQ6(userQ6, *argsQ6, **kwargsQ6):
        if not isinstance(userQ6, dict):
            raise TypeError("First argument must be a user dictionary")
        if 'isAdminQ6' not in userQ6:
            raise KeyError("User dictionary must contain 'isAdminQ6' key")
        if userQ6['isAdminQ6'] is True:
            return funcQ6(userQ6, *argsQ6, **kwargsQ6)
        else:
            raise PermissionError("Admin privileges required")
    return wrapperQ6
if __name__ == '__main__':
    userAdminQ6 = {'usernameQ6': 'Ahmed', 'isAdminQ6': True}
    userGuestQ6 = {'usernameQ6': 'Sara', 'isAdminQ6': False}

    @adminRequiredDecoratorQ6
    def viewSensitiveDataQ6(userQ6):
        return "🗄️ Top Secret Data"

    print(viewSensitiveDataQ6(userAdminQ6))
    print(viewSensitiveDataQ6(userGuestQ6))

#Question 7

import functools
import time

def retryDecoratorQ7(funcQ7):
    @functools.wraps(funcQ7)
    def wrapperQ7(*argsQ7, **kwargsQ7):
        attemptsQ7 = 3
        for attemptQ7 in range(1, attemptsQ7 + 1):
            try:
                return funcQ7(*argsQ7, **kwargsQ7)
            except Exception as errorQ7:
                print(f"Attempt {attemptQ7} failed: {errorQ7}")
                time.sleep(1)
        raise RuntimeError(f"{funcQ7.__name__} failed after {attemptsQ7} attempts")
    return wrapperQ7

if __name__ == '__main__':
    counterQ7 = {'failuresQ7': 2}

    @retryDecoratorQ7
    def unstableFunctionQ7():
        if counterQ7['failuresQ7'] > 0:
            counterQ7['failuresQ7'] -= 1
            raise ValueError("Simulated failure")
        return "✅ Success after retries"

    print(unstableFunctionQ7())

#Question 8

import functools
import time

def rateLimitDecoratorQ8(maxCallsQ8, perSecondsQ8):
    callTimesQ8 = []

    def decoratorQ8(funcQ8):
        @functools.wraps(funcQ8)
        def wrapperQ8(*argsQ8, **kwargsQ8):
            currentTimeQ8 = time.time()
            callTimesQ8[:] = [tQ8 for tQ8 in callTimesQ8 if currentTimeQ8 - tQ8 < perSecondsQ8]
            if len(callTimesQ8) >= maxCallsQ8:
                raise RuntimeError("Rate limit exceeded. Try again later.")
            callTimesQ8.append(currentTimeQ8)
            return funcQ8(*argsQ8, **kwargsQ8)
        return wrapperQ8
    return decoratorQ8

if __name__ == '__main__':
    @rateLimitDecoratorQ8(maxCallsQ8=3, perSecondsQ8=60)
    def fetchDataQ8():
        return "📡 Data fetched successfully"

    for iQ8 in range(5):
        try:
            print(fetchDataQ8())
        except RuntimeError as errorQ8:
            print(errorQ8)

#Question 9

import functools
import time
def performanceMonitorDecoratorQ9(funcQ9):
    callDataQ9 = {'countQ9': 0, 'totalTimeQ9': 0.0}

    @functools.wraps(funcQ9)
    def wrapperQ9(*argsQ9, **kwargsQ9):
        startQ9 = time.perf_counter()
        resultQ9 = funcQ9(*argsQ9, **kwargsQ9)
        endQ9 = time.perf_counter()

        callDataQ9['countQ9'] += 1
        callDataQ9['totalTimeQ9'] += (endQ9 - startQ9)
        averageQ9 = callDataQ9['totalTimeQ9'] / callDataQ9['countQ9']

        print(f"{funcQ9.__name__} called {callDataQ9['countQ9']} times, average time: {averageQ9:.4f} seconds")
        return resultQ9

    return wrapperQ9

if __name__ == '__main__':
    @performanceMonitorDecoratorQ9
    def processTaskQ9():
        time.sleep(0.5)
        return "🔄 Task done"

    for iQ9 in range(3):
        print(processTaskQ9())

#Question 10

import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def errorHandlerDecoratorQ10(funcQ10):
    @functools.wraps(funcQ10)
    def wrapperQ10(*argsQ10, **kwargsQ10):
        try:
            return funcQ10(*argsQ10, **kwargsQ10)
        except Exception as errorQ10:
            logging.info(f"Error in {funcQ10.__name__}: {errorQ10}")
            return None
    return wrapperQ10

if __name__ == '__main__':
    @errorHandlerDecoratorQ10
    def divideNumbersQ10(aQ10, bQ10):
        return aQ10 / bQ10

    print(divideNumbersQ10(10, 2))
    print(divideNumbersQ10(5, 0))

#Question 11

import functools
import inspect

def typeCheckDecoratorQ11(funcQ11):
    signatureQ11 = inspect.signature(funcQ11)
    annotationsQ11 = funcQ11.__annotations__

    @functools.wraps(funcQ11)
    def wrapperQ11(*argsQ11, **kwargsQ11):
        boundQ11 = signatureQ11.bind_partial(*argsQ11, **kwargsQ11)
        for paramNameQ11, valueQ11 in boundQ11.arguments.items():
            if paramNameQ11 in annotationsQ11:
                expectedTypeQ11 = annotationsQ11[paramNameQ11]
                if not isinstance(valueQ11, expectedTypeQ11):
                    raise TypeError(f"{paramNameQ11} must be {expectedTypeQ11.__name__}, got {type(valueQ11).__name__}")
        resultQ11 = funcQ11(*argsQ11, **kwargsQ11)
        if 'return' in annotationsQ11:
            expectedReturnQ11 = annotationsQ11['return']
            if not isinstance(resultQ11, expectedReturnQ11):
                raise TypeError(f"Return value must be {expectedReturnQ11.__name__}, got {type(resultQ11).__name__}")
        return resultQ11
    return wrapperQ11

if __name__ == '__main__':
    @typeCheckDecoratorQ11
    def concatenateQ11(textAQ11: str, textBQ11: str) -> str:
        return textAQ11 + textBQ11

    print(concatenateQ11("Hello ", "World"))

#Question 12

import functools
import sys
import linecache

def debugDecoratorQ12(funcQ12):
    @functools.wraps(funcQ12)
    def wrapperQ12(*argsQ12, **kwargsQ12):
        def tracerQ12(frameQ12, eventQ12, argQ12):
            if eventQ12 == 'line' and frameQ12.f_code == funcQ12.__code__:
                lineNumberQ12 = frameQ12.f_lineno
                fileNameQ12 = frameQ12.f_code.co_filename
                codeLineQ12 = linecache.getline(fileNameQ12, lineNumberQ12).rstrip()
                print(f"[{funcQ12.__name__}] {fileNameQ12}:{lineNumberQ12}: {codeLineQ12}")
            return tracerQ12
        sys.settrace(tracerQ12)
        try:
            resultQ12 = funcQ12(*argsQ12, **kwargsQ12)
            return resultQ12
        finally:
            sys.settrace(None)
    return wrapperQ12

if __name__ == '__main__':
    @debugDecoratorQ12
    def sampleFunctionQ12(xQ12):
        totalQ12 = 0
        for indexQ12 in range(xQ12):
            totalQ12 += indexQ12
        return totalQ12

    print(sampleFunctionQ12(3))

#Question 13

import functools
import time
import tracemalloc

def profileDecoratorQ13(funcQ13):
    @functools.wraps(funcQ13)
    def wrapperQ13(*argsQ13, **kwargsQ13):
        tracemalloc.start()
        startTimeQ13 = time.perf_counter()
        resultQ13 = funcQ13(*argsQ13, **kwargsQ13)
        endTimeQ13 = time.perf_counter()
        currentQ13, peakQ13 = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"{funcQ13.__name__} CPU time: {endTimeQ13 - startTimeQ13:.4f} sec")
        print(f"{funcQ13.__name__} Memory: Current = {currentQ13 / 1024:.2f} KB, Peak = {peakQ13 / 1024:.2f} KB")

        return resultQ13
    return wrapperQ13

if __name__ == '__main__':
    @profileDecoratorQ13
    def computeSquaresQ13(nQ13):
        return [iQ13 * iQ13 for iQ13 in range(nQ13)]

    print(computeSquaresQ13(10000))

#Question 14

import functools

def memoizationDecoratorQ14(funcQ14):
    cacheQ14 = {}
    @functools.wraps(funcQ14)
    def wrapperQ14(*argsQ14, **kwargsQ14):
        keyQ14 = (argsQ14, tuple(sorted(kwargsQ14.items())))
        if keyQ14 in cacheQ14:
            return cacheQ14[keyQ14]
        valueQ14 = funcQ14(*argsQ14, **kwargsQ14)
        cacheQ14[keyQ14] = valueQ14
        return valueQ14
    return wrapperQ14

if __name__ == '__main__':
    @memoizationDecoratorQ14
    def fibonacciQ14(nQ14):
        if nQ14 <= 1:
            return nQ14
        return fibonacciQ14(nQ14 - 1) + fibonacciQ14(nQ14 - 2)

    for indexQ14 in range(10):
        print(f"fibonacciQ14({indexQ14}) =", fibonacciQ14(indexQ14))


#Question 15

import functools

def composeDecoratorsQ15(*decoratorsQ15):
    def composerQ15(funcQ15):
        for oneDecoratorQ15 in reversed(decoratorsQ15):
            funcQ15 = oneDecoratorQ15(funcQ15)
        return funcQ15
    return composerQ15

if __name__ == '__main__':
    @composeDecoratorsQ15(errorHandlerDecoratorQ10, typeCheckDecoratorQ11)
    def divideAndConcatQ15(aQ15: int, bQ15: int) -> str:
        return str(aQ15 / bQ15)

    print(divideAndConcatQ15(10, 2))  
    print(divideAndConcatQ15(10, 0))   
    print(divideAndConcatQ15("five", 2))

#✅ Title: Exception Handling Mastery
#🎯 Focus: Master robust exception handling in Python with structured try/except, custom exceptions, and real-world error recovery systems.
#Question 1

def exceptionShowcaseQ1():
    try:
        print("Opening file...")
        with open("nonexistent_file_q1.txt", "r") as fileQ1:
            contentQ1 = fileQ1.read()
    except FileNotFoundError as eQ1:
        print(f"FileNotFoundError: {eQ1}")

    try:
        print("Dividing by zero...")
        resultQ1 = 10 / 0
    except ZeroDivisionError as eQ1:
        print(f"ZeroDivisionError: {eQ1}")

    try:
        print("Accessing list index...")
        listQ1 = [1, 2, 3]
        print(listQ1[5])
    except IndexError as eQ1:
        print(f"IndexError: {eQ1}")

    try:
        print("Converting string to int...")
        valueQ1 = int("abc")
    except ValueError as eQ1:
        print(f"ValueError: {eQ1}")

#Question 2

class ValidationErrorQ2(Exception):
    pass

class PermissionErrorQ2(Exception):
    pass

class RateLimitErrorQ2(Exception):
    pass

#Question 3

class BankErrorQ3(Exception):
    pass

class InsufficientFundsErrorQ3(BankErrorQ3):
    pass

class InvalidAccountErrorQ3(BankErrorQ3):
    pass

class UnauthorizedAccessErrorQ3(BankErrorQ3):
    pass

class TransactionLimitExceededErrorQ3(BankErrorQ3):
    pass


#Question 4

import logging
import traceback
from datetime import datetime

def logUnhandledExceptionsQ4(funcQ4):
    def wrapperQ4(*argsQ4, **kwargsQ4):
        try:
            return funcQ4(*argsQ4, **kwargsQ4)
        except Exception as errorQ4:
            with open("error_log_q4.txt", "a") as logFileQ4:
                timestampQ4 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logFileQ4.write(f"[{timestampQ4}] Unhandled Exception in {funcQ4.__name__}:\n")
                traceback.print_exc(file=logFileQ4)
                logFileQ4.write("\n")
            return None
    return wrapperQ4

#Question 5

def parseIntQ5(valueQ5):
    try:
        return int(valueQ5)
    except ValueError as errParseQ5:
        raise ValueError(f"Cannot convert {valueQ5!r} to int") from errParseQ5
def divideSafeQ5(aQ5, bQ5):
    try:
        aIntQ5 = parseIntQ5(aQ5)
        bIntQ5 = parseIntQ5(bQ5)
        return aIntQ5 / bIntQ5
    except ZeroDivisionError as errZeroQ5:
        raise ArithmeticError("Division by zero in divideSafeQ5") from errZeroQ5
    except ValueError as errValueQ5:
        raise TypeError("Invalid numeric input for divideSafeQ5") from errValueQ5

#Question 6

class SuppressAndLogQ6:
    def __init__(self, logToFileQ6=True):
        self.logToFileQ6 = logToFileQ6

    def __enter__(self):
        return self

    def __exit__(self, excTypeQ6, excValueQ6, tracebackQ6):
        if excTypeQ6 is not None:
            messageQ6 = f"Suppressed Exception: {excTypeQ6.__name__} - {excValueQ6}"
            if self.logToFileQ6:
                with open("exception_log_q6.txt", "a") as logFileQ6:
                    logFileQ6.write(messageQ6 + "\n")
            else:
                print(messageQ6)
            return True  
        return False 
#Question 7

def fileCleanupExampleQ7():
    fileQ7 = None
    try:
        fileQ7 = open("sample_file_q7.txt", "w")
        fileQ7.write("This is a sample line for cleanup test.\n")
        print("File written successfully.")
    finally:
        if fileQ7:
            fileQ7.close()
            print("File closed properly in finally block.")

#Question 8

class TransactionManagerQ8:
    def __init__(self, dataStoreQ8):
        self.dataStoreQ8 = dataStoreQ8
        self._backupQ8 = None

    def __enter__(self):
        self._backupQ8 = self.dataStoreQ8.copy()  
        return self.dataStoreQ8

    def __exit__(self, excTypeQ8, excValueQ8, tracebackQ8):
        if excTypeQ8 is not None:
            self.dataStoreQ8[:] = self._backupQ8  
            print(f"Transaction rolled back due to {excTypeQ8.__name__}: {excValueQ8}")
            return True  
        print("Transaction committed successfully.")
        return False

#Question 9

def safeFetchQ9(primaryFuncQ9, fallbackFuncQ9, *argsQ9, **kwargsQ9):
    try:
        return primaryFuncQ9(*argsQ9, **kwargsQ9)
    except Exception as errorQ9:
        print(f"Primary function failed: {errorQ9}. Using fallback...")
        return fallbackFuncQ9(*argsQ9, **kwargsQ9)
    
#Question 10

import json
import traceback

def serializeExceptionQ10(exceptionQ10):
    return json.dumps({
        "type": type(exceptionQ10).__name__,
        "message": str(exceptionQ10),
        "traceback": traceback.format_exc()
    }, indent=2)

#Question 11

import smtplib
from email.message import EmailMessage
import traceback

def sendCriticalAlertQ11(exceptionQ11, recipientEmailQ11):
    messageQ11 = EmailMessage()
    messageQ11["Subject"] = f"⚠️ Critical Exception: {type(exceptionQ11).__name__}"
    messageQ11["From"] = "noreply@example.com"
    messageQ11["To"] = recipientEmailQ11
    messageQ11.set_content(f"""
A critical error occurred:

Type: {type(exceptionQ11).__name__}
Message: {exceptionQ11}
Traceback:
{traceback.format_exc()}
""")
    try:
        with smtplib.SMTP("localhost") as serverQ11:
            serverQ11.send_message(messageQ11)
        print("Alert email sent successfully.")
    except Exception as mailErrorQ11:
        print(f"Failed to send alert email: {mailErrorQ11}")

#Question 12

import json
from collections import defaultdict

def analyzeExceptionLogsQ12(logFilePathQ12):
    typeCountQ12 = defaultdict(int)

    with open(logFilePathQ12, "r") as fileQ12:
        for lineQ12 in fileQ12:
            if "Unhandled Exception in" in lineQ12:
                continue
            if "Exception" in lineQ12 or "Error" in lineQ12:
                for wordQ12 in lineQ12.strip().split():
                    if wordQ12.endswith("Error") or wordQ12.endswith("Exception"):
                        typeCountQ12[wordQ12] += 1

    print("Exception Frequency Report:")
    for exceptionTypeQ12, countQ12 in typeCountQ12.items():
        print(f"{exceptionTypeQ12}: {countQ12}")

#Question 13

import json
import requests

def sendSlackAlertQ13(exceptionQ13, webhookUrlQ13):
    payloadQ13 = {
        "text": f":warning: *Critical Exception*: {type(exceptionQ13).__name__}\n>{exceptionQ13}"
    }
    try:
        responseQ13 = requests.post(
            webhookUrlQ13,
            data=json.dumps(payloadQ13),
            headers={"Content-Type": "application/json"}
        )
        return responseQ13.status_code == 200
    except Exception as notifyErrorQ13:
        print(f"Slack notification failed: {notifyErrorQ13}")
        return False

#Question 14

import traceback

def printDetailedTracebackQ14(exceptionQ14):
    print("Detailed Stack Trace:")
    traceback.print_exception(type(exceptionQ14), exceptionQ14, exceptionQ14.__traceback__)

#Question 15

def badPracticeQ15():
    try:
        xQ15 = int("abc")  
    except:
        print("Something went wrong.") 

def goodPracticeQ15():
    try:
        xQ15 = int("abc")
    except ValueError as valueErrQ15:
        print(f"ValueError: Invalid input - {valueErrQ15}")
    except Exception as genericErrQ15:
        print(f"Unexpected error: {type(genericErrQ15).__name__} - {genericErrQ15}")

#Question 16

import unittest

def divideQ16(aQ16, bQ16):
    if bQ16 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return aQ16 / bQ16

class TestDivideFunctionQ16(unittest.TestCase):
    def test_zero_division_q16(self):
        with self.assertRaises(ZeroDivisionError):
            divideQ16(10, 0)

    def test_valid_division_q16(self):
        self.assertEqual(divideQ16(10, 2), 5)

if __name__ == '__main__':
    unittest.main() 

#Question 17

import random

class RandomErrorSimulatorQ17:
    def __init__(self):
        self.errorTypesQ17 = [ValueError("Random value error"),
                              TypeError("Random type error"),
                              RuntimeError("Random runtime error")]

    def runQ17(self):
        if random.choice([True, False]):
            raise random.choice(self.errorTypesQ17)
        return "✅ Operation completed without error"

if __name__ == '__main__':
    simulatorQ17 = RandomErrorSimulatorQ17()
    try:
        resultQ17 = simulatorQ17.runQ17()
        print(resultQ17)
    except Exception as errorQ17:
        print(f"Simulated Error: {type(errorQ17).__name__} - {errorQ17}")


#Question 18

def fetchItemQ18(indexQ18, itemsQ18):
    """
    Fetch an item by index from a list.

    Args:
        indexQ18 (int): The index to fetch.
        itemsQ18 (list): The list of items.

    Returns:
        object: The item at the given index.

    Raises:
        IndexError: If the index is out of range.
        TypeError: If indexQ18 is not an integer.
    """
    if not isinstance(indexQ18, int):
        raise TypeError("indexQ18 must be an integer")
    return itemsQ18[indexQ18]

#Question 19

class ErrorCategorizerQ19:
    def __init__(self):
        self.categoryMapQ19 = {
            "ConnectionError": "network",
            "TimeoutError": "network",
            "PermissionError": "auth",
            "FileNotFoundError": "io",
            "OSError": "io",
            "ValueError": "validation",
        }

    def addCategoryQ19(self, exceptionTypeQ19, categoryNameQ19):
        self.categoryMapQ19[exceptionTypeQ19.__name__] = categoryNameQ19

    def categorizeQ19(self, exceptionInstanceQ19):
        return self.categoryMapQ19.get(
            type(exceptionInstanceQ19).__name__, "unknown"
        )

#Question 20

import functools
from collections import defaultdict

exceptionStatsQ20 = defaultdict(int)

def exceptionTrackerDecoratorQ20(funcQ20):
    @functools.wraps(funcQ20)
    def wrapperQ20(*argsQ20, **kwargsQ20):
        try:
            return funcQ20(*argsQ20, **kwargsQ20)
        except Exception as errorQ20:
            exceptionTypeQ20 = type(errorQ20).__name__
            exceptionStatsQ20[exceptionTypeQ20] += 1
            raise
    return wrapperQ20
if __name__ == '__main__':
    @exceptionTrackerDecoratorQ20
    def riskyOperationQ20(xQ20):
        if xQ20 < 0:
            raise ValueError("Negative value not allowed")
        elif xQ20 == 0:
            raise ZeroDivisionError("Zero is not allowed")
        return xQ20 * 2

    for testQ20 in [-1, 0, 1, -5, 0]:
        try:
            riskyOperationQ20(testQ20)
        except:
            pass

    print("Exception frequency stats:")
    for excTypeQ20, countQ20 in exceptionStatsQ20.items():
        print(f"{excTypeQ20}: {countQ20}")

#Question 21

def fetchDataOnlineQ21():
    raise ConnectionError("Failed to connect to server.")

def fetchDataOfflineQ21():
    return {"data": "Offline fallback data used."}

def getDataGracefullyQ21():
    try:
        return fetchDataOnlineQ21()
    except ConnectionError as errorQ21:
        print(f"Online fetch failed: {errorQ21}. Switching to offline mode...")
        return fetchDataOfflineQ21()

if __name__ == '__main__':
    resultQ21 = getDataGracefullyQ21()
    print(resultQ21)

#Question 22

def errorBoundaryWrapperQ22(funcQ22):
    def wrapperQ22(*argsQ22, **kwargsQ22):
        try:
            return funcQ22(*argsQ22, **kwargsQ22)
        except Exception as errorQ22:
            print(f"Oops! Something went wrong: {errorQ22}")
            return None
    return wrapperQ22

if __name__ == '__main__':
    @errorBoundaryWrapperQ22
    def simulateCrashQ22():
        return 10 / 0

    resultQ22 = simulateCrashQ22()
    print("Recovered:", resultQ22)

#Question 23

import functools
import logging
import traceback
from datetime import datetime

def exceptionMiddlewareQ23(funcQ23):
    @functools.wraps(funcQ23)
    def wrapperQ23(*argsQ23, **kwargsQ23):
        try:
            return funcQ23(*argsQ23, **kwargsQ23)
        except Exception as errorQ23:
            timestampQ23 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.error(f"[{timestampQ23}] {type(errorQ23).__name__}: {errorQ23}")
            with open("middleware_errors_q23.txt", "a") as logFileQ23:
                logFileQ23.write(f"[{timestampQ23}] {funcQ23.__name__} - {errorQ23}\n")
                traceback.print_exc(file=logFileQ23)
                logFileQ23.write("\n")
            return None
    return wrapperQ23

if __name__ == '__main__':
    @exceptionMiddlewareQ23
    def divideNumbersQ23(aQ23, bQ23):
        return aQ23 / bQ23

    print(divideNumbersQ23(10, 2))
    print(divideNumbersQ23(5, 0))

#Question 24


def failFastQ24(valueQ24):
    if not isinstance(valueQ24, int):
        raise TypeError("Only integers allowed (fail-fast)")
    return valueQ24 * 2


def failSafeQ24(valueQ24):
    try:
        return int(valueQ24) * 2
    except (ValueError, TypeError):
        return 0  


def retryOnceQ24(funcQ24, *argsQ24, **kwargsQ24):
    try:
        return funcQ24(*argsQ24, **kwargsQ24)
    except Exception:
        print("First attempt failed. Retrying once...")
        try:
            return funcQ24(*argsQ24, **kwargsQ24)
        except Exception as eQ24:
            print(f"Retry failed: {eQ24}")
            return None

if __name__ == '__main__':
    print("Fail-Fast:", failFastQ24(5))                      
    print("Fail-Safe:", failSafeQ24("oops"))    

    def riskyFuncQ24():
        raise RuntimeError("Temporary glitch")
    
    print("Retry-Once:", retryOnceQ24(riskyFuncQ24))

#Question 25

import functools
import logging
import traceback
import json
from datetime import datetime

logging.basicConfig(filename="error_framework_log_q25.txt", level=logging.ERROR, format="%(asctime)s %(message)s")

class ErrorFrameworkQ25:
    def __init__(self, notify=False, jsonLogPath="errors_q25.json"):
        self.notify = notify
        self.jsonLogPath = jsonLogPath
        self.errorHistory = []

    def handleException(self, errorQ25, funcNameQ25):
        errorRecordQ25 = {
            "timestamp": datetime.now().isoformat(),
            "function": funcNameQ25,
            "type": type(errorQ25).__name__,
            "message": str(errorQ25),
            "traceback": traceback.format_exc()
        }
        self.errorHistory.append(errorRecordQ25)
        logging.error(f"{funcNameQ25}: {type(errorQ25).__name__} - {errorQ25}")
        if self.notify:
            print(f"🚨 Notification: {funcNameQ25} failed with {type(errorQ25).__name__}")
        self.saveToJson()

    def saveToJson(self):
        with open(self.jsonLogPath, "w") as f:
            json.dump(self.errorHistory, f, indent=2)

    def exceptionHandler(self, funcQ25):
        @functools.wraps(funcQ25)
        def wrapperQ25(*argsQ25, **kwargsQ25):
            try:
                return funcQ25(*argsQ25, **kwargsQ25)
            except Exception as eQ25:
                self.handleException(eQ25, funcQ25.__name__)
                return None  
        return wrapperQ25


if __name__ == '__main__':
    frameworkQ25 = ErrorFrameworkQ25(notify=True)

    @frameworkQ25.exceptionHandler
    def divideQ25(aQ25, bQ25):
        return aQ25 / bQ25

    print(divideQ25(10, 2))  
    print(divideQ25(5, 0))