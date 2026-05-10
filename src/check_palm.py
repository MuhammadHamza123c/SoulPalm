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



load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


def check_point(image1_url: str):

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",

            messages=[
                {
                    "role": "system",
                    "content": 'You will get a image just simply tell if its Hand Palm or not. If its Plam reply with "Yes" else "No"'
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Is this hand Palm?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": image1_url}
                        },
                       
                    ]
                }
            ],

           

            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )

        raw = response.choices[0].message.content
        return raw

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

 

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )
    


print(check_point('https://znuiuhxyhpgqmdftansc.supabase.co/storage/v1/object/public/files/snap_20260320_221012.png'))
