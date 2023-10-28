import openai
import os


# Load your OpenAI API key from a .env file (recommended)
api_key = os.getenv("KEY")

# Initialize the OpenAI API client
openai.api_key = api_key
context =""
def generate_text(prompt, context):
    context += f"User: {prompt}\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{context}\nUser: {prompt}\nAI:",
        max_tokens=100,  # Adjust based on your requirements
        temperature=0.7,  # Adjust for randomness
    )
    context +=f"AI: {response.choices[0].text}\n"
    return response.choices[0].text

def summarize_documents(documents):
    text = "\n".join(documents)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following documents:\n{text}\nSummary:",
        max_tokens=150,  # Adjust based on your requirements
        temperature=0.7,  # Adjust for randomness
    )
    return response.choices[0].text

def analyze_sentiment(text):
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"you are a emotion recognition assistant analyze this text and give me one word reponse to this {text}",
        max_tokens=100,  # Adjust based on your requirements
        temperature=0.5,  # Adjust for randomness
    )
    return response.choices[0].text

# print(analyze_sentiment("I'm extremely grateful for all the support I've received."))
# Additional functions can be added for more advanced features as required.
print(generate_text("how are you", ""))