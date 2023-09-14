import openai

openai.api_key = "API_KEY"

# model="gpt-3.5-turbo"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    # text = f"""
    # You should express what you want a model to do by \ 
    # providing instructions that are as clear and \ 
    # specific as you can possibly make them. \ 
    # This will guide the model towards the desired output, \ 
    # and reduce the chances of receiving irrelevant \ 
    # or incorrect responses. Don't confuse writing a \ 
    # clear prompt with writing a short prompt. \ 
    # In many cases, longer prompts provide more clarity \ 
    # and context for the model, which can lead to \ 
    # more detailed and relevant outputs.
    # """

    text = f"""
    Thank you very much Indigo for sending my baggage to Hyderabad and flying me to Bangalore at the same time. Brilliant service!!!\
    """
    prompt = f"""
    Your task is to find out the sentiment of the review which is delimitted by backticks?
    This is a review of an airline. In airlines, people usually complain about their baggage being lost or sent to different place.
    Check if the reviewer was being sarcastic, angry, delighted, happy, sad, or neutral.
    Format your response as a JSON object with the following keys: sentiment, confidence, and feeling
    Review Text : '''{text}'''
    """
    # print(prompt)
    print(get_completion(prompt))