#basic chat w/ model with context saved
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
llm=ChatOllama(
    model='llama3.2',
    temperature=0)
config = {"configurable": {"thread_id": "my-chat"}}
agent=create_agent(
    model=llm,
    checkpointer=InMemorySaver())
prev=''
a=1
while a:
    q=input('Ask more y/n : ')
    if q=='n':
        a=0
    else:
        qn=input('')
        response=agent.invoke({'messages':[HumanMessage(content=qn)]},config=config)
        print(response['messages'][-1].content)

