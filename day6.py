def text_analyzer(text):
    total_characters = len(text)
    total_words = len(text.split())
    total_lines = len(text.splitlines())
    return total_characters, total_words, total_lines

print("=== Text Analyzer Suite ===")
print("Enter your text (type 'END' to stop):")

analyzer_lines = [] 
while True:
    user_line = input().strip()
    if user_line.lower() == "end":
        break
    analyzer_lines.append(user_line)

full_text_block = "\n".join(analyzer_lines)

num_characters, num_words, num_lines = text_analyzer(full_text_block)

print("\n=== Analysis Result ===")
print("Total Characters:", num_characters)
print("Total Words:", num_words)
print("Total Lines:", num_lines)

#QUESTION 2
def to_title_case(text):
    return text.title()

def to_camel_case(text):
    words_list = text.split()
    first_word = words_list[0].lower()
    rest_words = []
    for word in words_list[1:]:
        rest_words.append(word.capitalize())
    return first_word + ''.join(rest_words)

def to_snake_case(text):
    words_list = text.split()
    lowercase_list = []
    for word in words_list:
        lowercase_list.append(word.lower())
    return "_".join(lowercase_list)

print("=== String Manipulation Toolkit ===")
string_input = input("Enter a string: ")

print("\nTitle Case:   ", to_title_case(string_input))
print("Camel Case:   ", to_camel_case(string_input))
print("Snake Case:   ", to_snake_case(string_input))

#QUESTION 3
import re
print("=== Pattern Matching Engine ===")
regex_pattern_input = input("Enter your regex pattern: ")
regex_search_text = input("Enter the text to search in: ")
regex_matches = re.finditer(regex_pattern_input, regex_search_text)
found_any = False
for match in regex_matches:
    # Print the matched text and its position
    print("Match found:", match.group())
    print("Position: from", match.start(), "to", match.end())
    found_any = True
if found_any == False:
    print("No matches found.")

#QUESTION 4
print("=== Text Statistics Calculator ===")
text_input = input("Enter your text: ")
words_list = text_input.split()
sentence_list = text_input.split(".")
cleaned_sentences = []
for sentence in sentence_list:
    if sentence.strip() != "":
        cleaned_sentences.append(sentence)
total_word_length = 0
for word in words_list:
    total_word_length += len(word)
if len(words_list) > 0:
    avg_word_length = total_word_length / len(words_list)
else:
    avg_word_length = 0
if len(cleaned_sentences) > 0:
    avg_sentence_length = len(words_list) / len(cleaned_sentences)
else:
    avg_sentence_length = 0
unique_words_set = []
for word in words_list:
    lower_word = word.lower()
    if lower_word not in unique_words_set:
        unique_words_set.append(lower_word)
if len(words_list) > 0:
    lexical_density = len(unique_words_set) / len(words_list)
else:
    lexical_density = 0
print("\n=== Statistics Result ===")
print("Total Words:", len(words_list))
print("Total Sentences:", len(cleaned_sentences))
print("Average Word Length:", round(avg_word_length, 2))
print("Average Sentence Length:", round(avg_sentence_length, 2), "words per sentence")
print("Lexical Density:", round(lexical_density, 2))

#QUESTION 5
from collections import Counter
print("=== Word Frequency Analyzer ===")
paragraph_text = input("Enter a paragraph: ")
words = paragraph_text.split()
lowercase_words=[]
for word in words:
    lowercase_words.append(word.lower())
word_counts = Counter(lowercase_words)
for word, count in word_counts.items():
    print(f"'{word}': {count}")

#QUESTION 6
print("=== Sentence Structure Parser ===")
paragraph = input("Enter a paragraph: ")
import re
sentence_parts = re.findall(r'[^.!?]+[.!?]', paragraph)
print("\n=== Sentence Types ===")
for sentence in sentence_parts:
    sentence = sentence.strip()
    if sentence.endswith("."):
        print(f"Declarative: {sentence}")
    elif sentence.endswith("?"):
        print(f"Interrogative: {sentence}")
    elif sentence.endswith("!"):
        print(f"Exclamatory: {sentence}")
    else:
        print(f"Unknown Type: {sentence}")

#QUESTION 7
print("=== Caesar Cipher Encoder/Decoder ===")
text = input("Enter your message: ")
while True:
    mode = input("Do you want to encode or decode? ").strip().lower()
    if mode in ["encode", "decode"]:
        break
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")
while True:
    shift_input = input("Enter shift value (a number like 3): ").strip()
    if shift_input.isdigit():
        shift = int(shift_input)
        break
    else:
        print("Please enter a valid number for the shift.")

def caesar_cipher(message, shift_amount):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift_amount) % 26
            result += chr(base + shifted)
        else:
            result += char  
    return result
if mode == "encode":
    output = caesar_cipher(text, shift)
    print("\n Encoded Message:", output)
elif mode == "decode":
    output = caesar_cipher(text, -shift)
    print("\n Decoded Message:", output)

#QUESTION 8
print("=== Language Detection Tool ===")
english_keywords = ["the", "and", "is", "you", "hello"]
spanish_keywords = ["el", "y", "es", "usted", "hola"]
french_keywords  = ["le", "et", "est", "vous", "bonjour"]

text_input = input("Enter a sentence: ").lower()
words = text_input.split()

english_count = 0
spanish_count = 0
french_count = 0

for word in words:
    if word in english_keywords:
        english_count += 1
    if word in spanish_keywords:
        spanish_count += 1
    if word in french_keywords:
        french_count += 1

print("\n=== Detection Result ===")
if english_count > spanish_count and english_count > french_count:
    print("Language detected: English 🇬🇧")
elif spanish_count > english_count and spanish_count > french_count:
    print("Language detected: Spanish 🇪🇸")
elif french_count > english_count and french_count > spanish_count:
    print("Language detected: French 🇫🇷")
elif english_count == spanish_count == french_count == 0:
    print("Could not detect language.")
else:
    print("Could not determine clearly — possible mix or unclear.")

#QUESTION 9
print("=== Text Summarizer ===")
paragraph = input("Enter a paragraph:\n")
import re
sentences = re.split(r'[.!?]', paragraph)
sentences = [s.strip() for s in sentences if s.strip() != ""]
from collections import Counter
words = re.findall(r'\b\w+\b', paragraph.lower())
word_counts = Counter(words)
sentence_scores = []
for sentence in sentences:
    sentence_words = re.findall(r'\b\w+\b', sentence.lower())
    score = 0
    for word in sentence_words:
        score += word_counts[word]
    sentence_scores.append((score, sentence))
sentence_scores.sort(reverse=True)
top_sentences = sentence_scores[:3]
print("\n=== Summary ===")
for score, sentence in top_sentences:
    print("-", sentence)

#QUESTION 10
print("=== Keyword Extractor ===")
text = input("Enter your text:\n").lower()
stopwords = ["the", "is", "and", "a", "an", "to", "in", "of", "on", "it", "that", "this", "for", "with", "as", "by", "are", "was", "at", "be"]
for symbol in [".", ",", "!", "?", ":", ";", "-", "(", ")", "[", "]", '"', "'"]:
    text = text.replace(symbol, "")
words = text.split()
word_counts = {}
for word in words:
    if word not in stopwords:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
sorted_keywords = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
top_5 = sorted_keywords[:5]
print("\n=== Top 5 Keywords ===")
for word, count in top_5:
    print(f"{word}: {count}")

#QUESTION 11
print("=== Text Formatter ===")
text = input("Enter your text: ")
while True:
    width_input = input("Enter total width (e.g. 30): ")
    if width_input.isdigit():
        width = int(width_input)
        break
    else:
        print("Please enter a valid number.")
while True:
    alignment = input("Choose alignment (left, right, center): ").strip().lower()
    if alignment in ["left", "right", "center"]:
        break
    else:
        print("Invalid option. Choose 'left', 'right', or 'center'.")
def format_text(text, width, alignment_type):
    if alignment_type == "left":
        return text.ljust(width)
    elif alignment_type == "right":
        return text.rjust(width)
    elif alignment_type == "center":
        return text.center(width)
formatted = format_text(text, width, alignment)
print("\n=== Formatted Text ===")
print(formatted)

#QUESTION 12
print("=== Character Encoding Converter ===")
text = input("Enter your text: ")
print("\nChoose the encoding format:")
print("1. UTF-8")
print("2. ASCII")
print("3. Unicode escape")
choice = input("Enter your choice (1/2/3): ")
if choice == "1":
     encoded = text.encode("utf-8")
     print("\nUTF-8 Encoded Bytes:", encoded)
     print("Decoded Back:", encoded.decode("utf-8"))
elif choice == "2":
    try:
        encoded = text.encode("ascii")
        print("\nASCII Encoded Bytes:", encoded)
        print("Decoded Back:", encoded.decode("ascii"))
    except UnicodeEncodeError:
        print("\nError: Your text contains characters that can't be encoded in ASCII.")
elif choice == "3":
    encoded = text.encode("unicode_escape")
    print("\nUnicode Escape:", encoded)
    print("As Text:", encoded.decode("unicode_escape"))
else:
    print("Invalid choice.")

#QUESTION 13
print("=== Text Comparison Tool ===")
text1 = input("Enter the first text: ").lower()
text2 = input("Enter the second text: ").lower()
words1 = set(text1.split())
words2 = set(text2.split())
common_words = words1 & words2           
added_words = words2 - words1            
removed_words = words1 - words2 
print("\n=== Comparison Result ===")
print("Common Words:", common_words if common_words else "None")
print("Added Words:", added_words if added_words else "None")
print("Removed Words:", removed_words if removed_words else "None")

#QUESTION 14
print("=== Spell Checker Basics ===")
import difflib
dictionary_words = [
    "hello", "world", "python", "programming", "language", "spell", "checker", "text"
]
text = input("Enter a sentence: ").lower()
words_in_text = text.split()
for word in words_in_text:
    if word in dictionary_words:
        print(f" Correct: {word}")
    else:
        print(f" Misspelled: {word}")
        suggestions = difflib.get_close_matches(word, dictionary_words)
        if suggestions:
            print("   Suggestions:", ", ".join(suggestions))
        else:
            print("   No suggestions found.")

#QUESTION 15
print("=== Grammar Analyzer ===")
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
repeated=[]
for i in range(1,len(words)):
    if words[i]==words[i-1]:
        repeated.append(words[i])
passive_keywords = ["was", "were", "is", "are", "been", "being"]
passive_detected = False
for word in passive_keywords:
    if word in words and "by" in words:
        passive_detected=True
        break
print("\n=== Analysis Result ===")
if repeated:
    print("Repeated Words Found:", ", ".join(repeated))
else:
    print("No repeated words.")

if passive_detected:
    print("Passive voice might be present.")
else:
    print("No passive voice detected.")

#QUESTION 16
print("=== Text Template Engine ===")
template_text = input("Enter your template (example: Hello {name}, welcome to {city}): ")
name_value = input("Enter the name: ")
city_value = input("Enter the city: ")
data = {
    "name": name_value,
    "city": city_value
}
filled_text = template_text.format(**data)
print("\n=== Final Result ===")
print(filled_text)

#QUESTION 17
print("=== Simple Markdown Processor ===")
text = input("Enter markdown text: ")
if text.startswith("# "):
    result = "<h1>" + text[2:] + "</h1>"
elif "**" in text:
    start = text.find("**")
    end = text.find("**", start + 2)
    if end != -1:
        bold_word = text[start+2:end]
        result = text[:start] + "<strong>" + bold_word + "</strong>" + text[end+2:]
    else:
        result = text
elif "*" in text:
    start = text.find("*")
    end = text.find("*", start + 1)
    if end != -1:
        italic_word = text[start+1:end]
        result = text[:start] + "<em>" + italic_word + "</em>" + text[end+1:]
    else:
        result = text
else:
    result = text
print("\n=== HTML Output ===")
print(result)

#QUESTION 18
print("=== Easy CSV Parser ===")
print("Enter CSV data (first line should be headers like: name,age,city)")
print("Type 'END' to stop entering:")
liness=[]
while True:
    lined=input()
    if lined.strip().upper()=="END":
        break
    liness.append

header_line = lined[0]
headers = header_line.split(",")
data_lines = lined[1:]
result = []
for data_line in data_lines:
    values = data_line.split(",")
    row = {}
    for i in range(len(headers)):
        row[headers[i].strip()] = values[i].strip()
    result.append(row)
print("\n=== Parsed Data ===")
for row in result:
    print(row)

#QUESTION 19
print("=== Log File Analyzer ===")
log_data = input("Enter log entry (example: [2025-06-27 10:30:00] ERROR: Server not responding): ")
start_time = log_data.find("[") + 1
end_time = log_data.find("]")
timestamp = log_data[start_time:end_time]
after_bracket = log_data[end_time + 1:].strip()
log_parts = after_bracket.split(":")
level = log_parts[0].strip()
message = log_parts[1].strip() if len(log_parts) > 1 else "No message"
print("\n=== Log Analysis Result ===")
print("Timestamp:", timestamp)
print("Level:    ", level)
print("Message:  ", message)

#QUESTION 20
print("=== Configuration File Parser ===")
print("Enter your configuration (key=value). Type 'END' to finish:")
config_lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    config_lines.append(line.strip())

config_dict = {}
for line in config_lines:
    if "=" in line:
        key, value = line.split("=", 1)  
        config_dict[key.strip()] = value.strip()

print("\n=== Parsed Configuration ===")
for key, value in config_dict.items():
    print(f"{key} = {value}")























     

