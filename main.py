
from agent import initialize_agent, ask_agent


agent = initialize_agent()

print("SQL AI Agent is ready!")
print("Type 'exit' to quit.\n")

while True:

    question = input("Ask your question: ")

    if question.lower() == "exit":
        break

    answer = ask_agent(agent, question)

    print("\nAI:", answer)
    print("-" * 50)
