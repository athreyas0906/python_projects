from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="llama3.2",
    temperature=0
    
)
def in_context_learning(task_description,  input_text, target_tone_sentiment):
    prompt = PromptTemplate(
        input_variables=["task_description", "input_text", 'target_tone_sentiment'],
        template="""
        You analyse tone and sentiment of the messages you are given. Classified into a spectrum of positive to neutral to negative sentiment
        and an appropriate guess of the tone that the author of the message is able to convey.

        Return the reasoning for your judgements.

        Further more, based on the target tone and sentiment proposed by the user, return a modified version of the text.
        
        Task: {task_description}

        Now perform the task on the following input.

        Structure the output as such (You may rephrase these pointers in the output):
        1. Inferred tone, sentiment, and emotion from the text.
        2. Stand out lines in the text that suggest a certain emotion, tone or sentiment.
        3. Reason for the classification.
        4. Return the modified version that incorporates the target tone and sentiment or emotion.
        5. Return the reason as to why you made changes, and what changes were made.

        Input: {input_text}
        Target tone and sentiment : {target_tone_sentiment}
        Output:
        """
    )

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({
        "task_description": task_description,
        "input_text": input_text,
        'target_tone_sentiment': target_tone_sentiment
    })

task_desc = "Perform sentiment and tonal analysis on the following, and return a modified version if the target tone and sentiment are different than inferred tone and sentiment"
#text goes here - 
text_input = """ """
#target sentiment emotion and tone goes here
target=""" """


result = in_context_learning(task_desc, text_input, target)
print('Input - ')
print(text_input)
print()
print()
print(result)

