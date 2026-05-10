from fastapi import APIRouter,File,UploadFile,Form
from uuid import uuid4
from src.friend_image import fri_palm
from store.image_upload import upload_image_to_supabase
import os

router_fri=APIRouter()

@router_fri.post('/SoulPalm/friend')
async def show_fri_palm(friend1:str=Form(...), friend2:str=Form(...),f1z:str=Form(...),f2z:str=Form(...),f1:UploadFile=File(...),f2: UploadFile=File(...)):
    file_extension1 = f1.content_type.split('/')[-1]
    file_extension2=f1.content_type.split('/')[-1]
    file_name1,file_name2 = f"{uuid4()}.{file_extension1}",f"{uuid4()}.{file_extension2}"


    
    if file_extension1 not in ["jpeg", "jpg", "png"] and file_extension2 not in ["jpeg", "jpg", "png"]:
        return {"error": "Invalid file type"}
    content1, content2=await f1.read(),await f2.read()
    file_url1, file_url2=upload_image_to_supabase(image_name=file_name1,image_content=content1),upload_image_to_supabase(image_name=file_name2,image_content=content2)
    result=fri_palm(image1_url=file_url1,image2_url=file_url2,f1=friend1,f2=friend2,f1z=f1z,f2z=f2z)
    return{
        'SoloPalm':result
    }


        

