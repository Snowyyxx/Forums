import os
import openai
openai.api_key='sk-proj-djmLws19v8kWNcHxg92mT3BlbkFJ8aGFpjB0vX85WI6nTxnl'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(model=model,messages=messages,temperature=0)
    return response.choices[0].message["content"]

previous_titles = []
    
def random_thought():
    excluded = ', '.join(previous_titles)
    title_prompt = f'Give me a title for a instresting shower thought. Keep it short and Crisp. Exclude these topics: {excluded}'
    title_response = get_completion(title_prompt)
    previous_titles.append(title_response)
    thought_prompt = f'write a thought on {title_response} few lines'
    thought_response = get_completion(thought_prompt)
    context = {'title':title_response,'thought':thought_response}
    return context

