from fastapi import APIRouter,File,UploadFile,Form
from uuid import uuid4
from src.solo_image import solo_palm
from store.image_upload import upload_image_to_supabase
import os

router_sol=APIRouter()

@router_sol.post('/SoulPalm/solo')
async def show_solo_palm(zodiac_sign:str=Form(...),f1:UploadFile=File(...)):
    file_extension = f1.content_type.split('/')[-1]
    file_name = f"{uuid4()}.{file_extension}"


    
    if file_extension not in ["jpeg", "jpg", "png"]:
        return {"error": "Invalid file type"}
    content=await f1.read()
    file_url=upload_image_to_supabase(image_name=file_name,image_content=content)
    result=solo_palm(image_url=file_url,zodiac_sign=zodiac_sign)
    return{
        'SoloPalm':result
    }


        

