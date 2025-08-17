import json
from openai import OpenAI

openai_client = OpenAI(
    base_url = 'https://api.subconscious.dev/v1',
    api_key = 'GET API KEY FROM https://subconscious.dev',
)

def agent(research_question):
    response = openai_client.chat.completions.create(
        model = 'tim-large',
        messages = [
            {
                'role': 'user',
                'content': research_question
            }
        ],
        max_completion_tokens = 10000,
        temperature = 0.7,
        stream = True,
        tools = [
            {
                'type': "web_search"
            },
            {
                'type': "webpage_understanding"
            }
        ]
    )
    
    ans_str = ''
    for chunk in response:
        ans_str += chunk.choices[0].delta.content

    return json.loads(ans_str)


def main():
    research_question = 'How can AI be leveraged to address climate change mitigation and adaptation in a way that minimizes unintended consequences?'
    ans_obj = agent(research_question)
    
    print('### Reasoning:')
    print(json.dumps(ans_obj, indent=2))

    print('### Answer:')
    print(ans_obj['answer'])


if __name__ == '__main__':
    main()