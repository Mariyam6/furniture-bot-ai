import csv
import os
from groq import Groq

# 1. Connection settings (Paste your BRAND NEW key below)
API_KEY = "PASTE KEY"
client = Groq(api_key=API_KEY)

# 2. Explicit folder location setup for your project folder
csv_file = r"C:\Users\Lenovo\Desktop\DEVELOPMENT PROJECTS\local_leads.csv"


# Automatically create the file and add headers if it doesn't exist yet
if not os.path.exists(csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Platform", "Product Interest", "Budget", "Draft Reply"])

print("Initialized Successfully! (Type 'exit' to close)\n")

# 3. Execution loop
while True:
    print("-" * 50)
    messy_chat = input("Paste your raw customer chat/comment here: ")
    
    if messy_chat.strip().lower() == "exit":
        print(f"\nShutting down. Data saved in your folder as 'local_leads.csv'. Goodbye!")
        break
        
    if not messy_chat.strip():
        continue

    try:
        # 4. Prompt optimized to return comma-separated text for spreadsheets
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
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
        
        # 5. Split text line at commas and append row to file
        parsed_row = [item.strip() for item in raw_output.split(",", 4)]
        
        with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(parsed_row)
            
        print("Success! Row written permanently to 'local_leads.csv'\n")
        
    except Exception as e:
        print(f"\nError processing data: {e}\n")
