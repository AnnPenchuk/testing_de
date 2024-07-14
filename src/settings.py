from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv
'''
class Settings(BaseSettings):
     load_dotenv()
     user = os.getenv('USER')
     password= os.getenv('PASSWORD')
     host= os.getenv('HOST')
     port= os.getenv('PORT')
     name_database= os.getenv('DB')
     url= os.getenv('URL')


#a=Settings.user
#print(a)
settings = Settings()
'''