import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_anthropic import ChatAnthropic

from app.models import get_character_info
from app.vector_store import search_similar_memory

load_dotenv()

# LangSmith tracing ON
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Claude 프롬프트 템플릿
template = """
이전 기억: {memories}

사용자 말: "{user_input}"

고인의 말투로 이 기억을 바탕으로 따뜻하게 대답해줘:
"""
prompt = PromptTemplate.from_template(template)


def build_system_prompt(char_info: dict) -> str:
    return f"""
너는 '{char_info['name']}'라는 {char_info['age']}세 {char_info['gender']}이고, 사용자의 {char_info['relationship']}야.
사용자를 '{char_info['calling']}'라고 부르지만, 매 문장마다 앞에 넣지 말고 자연스럽게 대화 속에서 적절히 사용해.
말투는 {char_info['tone']}고 성격은 {char_info['personality']}야.
{char_info['dialect']} 방언을 사용하고, 종교는 {char_info['belief']}야.
자주 하던 말은 {char_info['habit_phrases']}였고, 취미는 {char_info['hobbies']}였어.
"""



def generate_reply(user_id: int, user_input: str) -> str:
    char_info = get_character_info(user_id)
    system_prompt = build_system_prompt(char_info)

    similar_memory = search_similar_memory(user_input, user_id)

    llm = ChatAnthropic(
        model="claude-3-opus-20240229",
        temperature=0.7,
        system=system_prompt,
        max_tokens=700
    )

    chain: RunnableSequence = prompt | llm
    result = chain.invoke({
        "memories": similar_memory,
        "user_input": user_input
    })

    return result.content
