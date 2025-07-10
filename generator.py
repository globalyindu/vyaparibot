from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_social_posts(business_info):
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)

    with open("prompts/post_prompt.txt", "r") as file:
        prompt_text = file.read()

    prompt_template = PromptTemplate.from_template(prompt_text)

    chain = LLMChain(llm=llm, prompt=prompt_template)

    response = chain.run(
        business_type=business_info['type'],
        city=business_info['city'],
        products=business_info['products'],
        tone=business_info['tone'],
        language=business_info['language'],
        audience_profile=business_info['audience'],
        offers=business_info['offers']
    )

    return response