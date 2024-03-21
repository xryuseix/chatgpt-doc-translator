import os
import time
from typing import List
from dotenv import load_dotenv, find_dotenv
from models.models import TranslateResult
_ = load_dotenv(find_dotenv()) # read local .env file
file_folder = os.environ['FILE_FOLDER'] if 'FILE_FOLDER' in os.environ else "translated_file"

async def save_as_txt(content_list: List[TranslateResult]):

    filename = f"{content_list[i].translated_content[:16]}_{int(time.time())}"
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)

    with open(f"{file_folder}/{filename}.txt", "w+") as f:
        for i in range(len(content_list)):
            f.write(content_list[i].translated_content)

    return filename