from fastapi import HTTPException
from dotenv import load_dotenv
import os
from groq import (
    Groq,
    RateLimitError,
    APITimeoutError,
    APIConnectionError,
    APIError
)
from .prompt import friend_image_prompt
from schema.friend_schema import FriendPalmResponse
import json

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


def fri_palm(image1_url: str, image2_url: str, f1: str, f2: str,f1z:str,f2z:str):

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",

            messages=[
                {
                    "role": "system",
                    "content": friend_image_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Friend one: {f1} and zodiac sign: {f1z}, Friend two: {f2} and zodiac sign: {f2z}. Return full structured JSON."
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": image1_url}
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": image2_url}
                        }
                    ]
                }
            ],

            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "friend_palm",
                    "schema": FriendPalmResponse.model_json_schema()
                }
            },

            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )

        raw = response.choices[0].message.content

        data = json.loads(raw)
        result = FriendPalmResponse.model_validate(data)

        return result.model_dump()

    # ---------------- ERROR HANDLING ----------------

    except RateLimitError:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    except APITimeoutError:
        raise HTTPException(
            status_code=504,
            detail="Request timed out"
        )

    except APIConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Connection error"
        )

    except APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Groq API error: {str(e)}"
        )

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Invalid JSON returned by model"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )