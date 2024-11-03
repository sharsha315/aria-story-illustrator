from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import base64
import os
from dotenv import load_dotenv

load_dotenv()

class AriaHelper:
    def __init__(self):
        self.chat = ChatOpenAI(
            model="aria",
            api_key=os.getenv('ARIA_API_KEY'),
            base_url="https://api.rhymes.ai/v1",
            streaming=False,
        )
    
    def analyze_story(self, story_text):
        response = self.chat.invoke([
            SystemMessage(content="You are a creative AI assistant that analyzes stories and suggests visual scenes to illustrate them."),
            HumanMessage(content=f"Analyze this story and suggest key scenes to illustrate: {story_text}")
        ])
        return response.content

    def process_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
