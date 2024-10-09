from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

information = """
    Sir Winston Leonard Spencer Churchill[a] KG OM CH TD DL FRS RA (30 November 1874 – 24 January 1965) 
    was a British statesman, military officer, and writer who was Prime Minister of the United Kingdom 
    from 1940 to 1945 (during the Second World War) and again from 1951 to 1955. 
    Apart from 1922 to 1924, he was a member of Parliament (MP) from 1900 to 1964 and represented 
    a total of five constituencies. 
    Ideologically an adherent to economic liberalism and imperialism, 
    he was for most of his career a member of the Conservative Party, which he led from 1940 to 1955. 
    He was a member of the Liberal Party from 1904 to 1924.
    """

if __name__ == "__main__":
    print("Hello LangChain")

    summary_template = """
        given the information {information} about a person from I want you to create: 
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    llm = ChatOllama(model = "llama3" )
    # llm = ChatOllama(model = "mistral")
    
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)