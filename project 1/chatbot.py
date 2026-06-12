
def start_chatbot():
    print("========================================================")
    print("  DECODELABS AI CHATBOT CORE LAYER v1.0 ONLINE         ")
    print("  Processing Blueprint: IPO (Input-Process-Output)      ")
    print("  Instructions: Type your query. Type 'exit' to close.  ")
    print("========================================================\n")
    

    while True:
        
        user_raw = input("You: ")
       
        user_input = user_raw.lower().strip()
       
        if user_input == "exit" or user_input == "quit":
            print("Bot: Terminating continuous loop. Safe shutdown complete. Goodbye!")
            break 

        elif user_input == "hello" or user_input == "hi" or user_input == "hey":
            print("Bot: Hello! I am your deterministic AI companion. How can I help you progress today?")
            
        elif user_input == "how are you" or user_input == "status":
            print("Bot: My logic gates are functional and operating at full efficiency. Thank you!")
            
        elif user_input == "what is your purpose" or user_input == "who are you":
            print("Bot: I am a rule-based AI chatbot built to act as a strict guardrail control layer.")
            
        elif user_input == "who created you" or user_input == "creator":
            print("Bot: I was developed by an AI Engineer Intern under the DecodeLabs 2026 Batch.")
            
        elif user_input == "help" or user_input == "commands":
            print("Bot: Predefined intents I recognize: 'hi', 'status', 'purpose', 'creator', 'project info'.")
            
        elif user_input == "project info" or user_input == "tell me about project 1":
            print("Bot: Project 1 tests input normalization, conditional structures, and infinite runtime control.")
            
        else:
            print("Bot: I cannot match that input stream. Please try a predefined keyword or command.")
            
        print() 

if __name__ == "__main__":
    start_chatbot()# Updated
