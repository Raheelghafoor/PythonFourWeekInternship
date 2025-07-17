# fuzzer_q11.py
import requests

test_inputs_q11 = [
    "", 
    "' OR '1'='1", 
    "<script>alert(1)</script>", 
    "../../../../etc/passwd", 
    "%00", 
    "正常输入", 
    "💣", 
    "DROP TABLE users;", 
    "😊" * 1000
]

for input_q11 in test_inputs_q11:
    response_q11 = requests.get("http://localhost:5001/search", params={"q": input_q11})
    print(f"Input: {repr(input_q11)} → Status: {response_q11.status_code} | Output: {response_q11.text}")