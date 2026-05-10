from supabase import create_client, Client,StorageException,SupabaseException
import os
from dotenv import load_dotenv
import uuid

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_PROJECT_URL")
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def upload_image_to_supabase(image_name: str,image_content:str, bucket_name: str = "files") -> str:
    FOLDER_NAME='soulmate'
 

    try:
        file_path=f"{FOLDER_NAME}/{image_name}"
        supabase.storage.from_(bucket_name).upload(file_path, image_content)
        public_url = supabase.storage.from_(bucket_name).get_public_url(file_path)
        return public_url
    except (StorageException,SupabaseException) as e:
        raise e


