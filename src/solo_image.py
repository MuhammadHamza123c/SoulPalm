from fastapi import HTTPException
from dotenv import load_dotenv
import os
from groq import (
    Groq,
    APIError,
    RateLimitError,
    APITimeoutError,
    APIConnectionError
)
from .prompt import solo_image_prompt
from schema.solo_schema import SoloPalmResponse
import json

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


def solo_palm(image_url: str,zodiac_sign:str):

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",

            messages=[
                {
                    "role": "system",
                    "content": f"Only Do if image is palm and clear otherwise just return every json None {solo_image_prompt}"
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Analyze this palm image and return full structured JSON Here is zodianc sign: {zodiac_sign}"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ],

            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "solo_palm",
                    "schema": SoloPalmResponse.model_json_schema()
                }
            },

            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )

        raw = response.choices[0].message.content

        data = json.loads(raw)
        result = SoloPalmResponse.model_validate(data)

        return result.model_dump()

  

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
