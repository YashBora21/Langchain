import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def main():

    print("Hello from genai!") 
    information="""AI. Musk has been the wealthiest person in the world since 2025; as of February 2026, Forbes estimates his net worth to be around US$852 billion. Wikipedia
Born: 28 June 1971 (age 54 years), Pretoria, South Africa
Children: Vivian Jenna Wilson, Nevada Alexander Musk, Saxon Musk, Kai Musk, Damian Musk, Griffin Musk, Romulus Musk
Spouse: Talulah Riley (m. 2013–2016), Talulah Riley (m. 2010–2012), Justine Musk (m. 2000–2008)
Organizations founded: Tesla · See more
Education: University of Pennsylvania School of Arts and Sciences (1997) · See more
Books: Elon Musk
Parents: Errol Musk, Maye Musk"""
    summary_template="""
    Give the information {information}about a personI want ot create:
     1. A short Summary 
     2. the two intresting prompt about them  
    """
    summary_prompt=PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        temperature=0
    )    
    chain=summary_prompt | llm
    response=chain.invoke(input={"information": information})
    print(response)







if __name__ == "__main__":
    main()
