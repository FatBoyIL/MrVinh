import json
from difflib import get_close_matches
#từ module difflib (dùng để tìm kiếm kết quả đúng nhất)

def load_brain(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        return data
def save_brain(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_close_matches(user_question: str, question:list[str]) -> str |None:
    close_matches:list = get_close_matches(user_question,question,n=1, cutoff=0.6)
    return close_matches[0] if close_matches else None

def get_answer(question:str, brain_knowlege:dict)-> str | None:
    for key in brain_knowlege["questions"]:
        if key["question"] == question:
            return key["answer"]

def chatbot():
    brain_knowlege:dict = load_brain("Botbrain.json")
    while True:
        user_question:str = input("You: ")
        if user_question.lower() == "exit":
            break
        close_matches:str | None = find_close_matches(user_question,
                            [key["question"] for key in brain_knowlege["questions"]])
        if close_matches:
            answer:str = get_answer(close_matches, brain_knowlege)
            print(f"Bot: {answer}")
        else:
            print("Bot: Your question out of my knowledge, please teach me: ")
            new_answer:str = input('Type your answer or "concac" to skip: ')

            if new_answer.lower() != "concac":
                brain_knowlege["questions"].append({"question":user_question, "answer":new_answer})
                save_brain("Botbrain.json", brain_knowlege)
                print(f"Bot: Love you")

if __name__ == "__main__":
    chatbot()
