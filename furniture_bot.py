import csv
import os
from groq import Groq

API_KEY = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")
client = Groq(api_key=API_KEY)

csv_file = "local_leads.csv"

if not os.path.exists(csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Name", "Platform", "Product Interest", "Budget", "Draft Reply"])

print("Initialized Successfully! (Type 'exit' to close)\n")

while True:
    print("-" * 50)
    messy_chat = input("Paste your raw customer chat/comment here: ")
    
    if messy_chat.strip().lower() == "exit":
        print(f"\nShutting down. Data saved in your folder as 'local_leads.csv'. Goodbye!")
        break
        
    if not messy_chat.strip():
        continue

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a backend spreadsheet parser. Extract values from the text and return ONLY a single comma-separated line containing exactly these 5 items in order: Name, Platform, Product Interest, Budget, and a short polite draft reply. Do not copy example text. Write a completely custom draft reply based on what the customer is asking. Do not write introductory words, markdown bolding, lists, numbers, or internal quotation marks."

                },
                {"role": "user", "content": messy_chat}
            ]
        )
        
        raw_output = completion.choices[0].message.content.strip()
        print(f"\nParsed Payload Output: {raw_output}")
        
        parsed_row = [item.strip() for item in raw_output.split(",", 4)]
        
        with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(parsed_row)
            
        print("Success! Row written permanently to 'local_leads.csv'\n")
        
    except Exception as e:
        print(f"\nError processing data: {e}\n")
