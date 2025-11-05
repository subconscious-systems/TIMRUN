import json
from subconscious import Client
from typing import Tuple, List

subconscious_client = Client(
    base_url = 'https://api.subconscious.dev/v1',
    api_key='Get API KEY from https://subconscious.dev',
)

subconscious_client.build_toolkit(
    json.load(open('tools.json'))
)

research_question = 'How can AI be leveraged to address climate change mitigation and adaptation in a way that minimizes unintended consequences?'
messages = [
    {
        "role": "system",
        "content": "You are a research agent that uses tools to gather information and provide a comprehensive answer to complex research questions. Use the search tools to find the urls for relevant articles, then use the reader tool to read and extract key information. Finally, synthesize the information to provide a well-rounded answer."
    },
    {
        "role": "user",
        "content": f"Research Question: {research_question}"
    }
]

def flex_deep_research():

    response = subconscious_client.agent.run(messages)
    ans_obj = json.loads(response.content)

    print('### Reasoning:')
    print(json.dumps(ans_obj, indent=2))

    print('### Answer:')
    print(ans_obj['answer'])


def controlled_deep_research():
    search_task = subconscious_client.create_task(
        task_name='search',
        tools=('SearchTool',)
    )
    
    read_task = subconscious_client.create_task(
        task_name='web_reading',
        tools=('ReaderTool',)
    )
    
    summary_task = subconscious_client.create_task(
        task_name='summarization',
        thought='Analyze the web reading result and find out if there is any information needs further search to expand.',
    )
    
    rs_task = subconscious_client.create_task(
        task_name='research_synthesis',
        subtasks=Tuple[read_task, summary_task]
    )
    
    search_attempt = subconscious_client.create_task(
        task_name='search_attempt',
        tools=('SearchTool',),
        subtasks=List[rs_task]
    )
    
    thread = subconscious_client.create_thread(
        reasoning_model=List[search_attempt],
        answer_model=str
    )
    
    response = subconscious_client.agent.run(messages)
    ans_obj = json.loads(response.content)

    print('### Reasoning:')
    print(json.dumps(ans_obj, indent=2))

    print('### Answer:')
    print(ans_obj['answer'])


if __name__ == '__main__':
    flex_deep_research()
    # controlled_deep_research()