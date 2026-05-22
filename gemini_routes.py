from google import genai
from fastapi import APIRouter

router = APIRouter()

client = genai.Client(
    api_key="AIzaSyCaifBzM-KVXbAET4nXfYEnliMtXZRwyN4"
)

@router.get("/generate-blog/{topic}")
def generate_blog(topic: str):

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Write a blog on {topic}"
        )

        return {
            "blog": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }