# Furniture Sales AI Helper

This is a Python tool that uses AI to read messy customer messages from social media and automatically save the important details into a clean spreadsheet. 

## Why I Built This (The Problem)
My family runs a busy furniture shop. Customers send questions from all over the place—TikTok, WhatsApp, and Facebook. Because the messages are scattered and unorganized, it was easy to lose track of who wanted to buy what, leading to missed sales and a lot of messy paperwork.

## How It Works (The Solution)
Instead of copying details by hand, we paste the messy customer chat directly into this tool. 
1. The tool connects to an online AI brain (**Meta's Llama 3.1** model using the **Groq API**).
2. The AI reads the message and instantly separates the important details (Customer Name, Platform, Product, and Budget).
3. The tool automatically writes a polite reply draft for the customer.
4. Finally, it saves all this information into a spreadsheet file (`local_leads.csv`) on the computer so nothing gets lost.

* **Situation (The Mess):** My family's furniture business gets a lot of customer inquiries across TikTok, WhatsApp, and Facebook. The chats were messy and unorganized, which made sorting them slow and caused us to miss out on sales.
* **Task (The Goal):** I wanted to build a simple computer tool that could read a messy message and automatically sort out the important business details.
* **Action (What I Did):** I wrote a Python script that stays open and waits for chat text. I hooked it up to Meta's Llama 3.1 AI model. I told the AI to only output the specific facts we need, and I used Python code to save those facts directly into a local spreadsheet file.
* **Result (The Impact):** We no longer have to sort through messy messages by hand. The tool turns chat text into organized spreadsheet rows instantly and automatically writes a follow-up reply draft to save time.

## 🛠️ Built With
* **Python** (To handle the files and setup)
* **Groq SDK & Llama 3.1** (The AI brain that reads the messages)
* **CSV file** (The spreadsheet where data is saved)
