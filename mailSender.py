import os
from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv('.env')
print(os.getenv('MAIL_USERNAME'))
print(os.getenv('MAIL_PASSWORD'))
print(os.getenv('MAIL_FROM'))
print(os.getenv('MAIL_PORT'))
print(os.getenv('MAIL_SERVER'))

app = FastAPI()
class EmailSchema(BaseModel):
   email: List[EmailStr]

@app.post("/send_mail")
async def send_mail(email:EmailSchema):
    template="""<html>
	<body>
		<p>Hi !!! <br />Thanks for using fastapi mail, keep using it..!!!</p>
	</body>
    </html>"""

   
    conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_PORT=os.getenv('MAIL_PORT'),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    #TEMPLATE_FOLDER='./templates/email'
    )
    message = MessageSchema(
    subject="Fastapi-Mail module trial 2",
    recipients=email.dict().get("email"),  # List of recipients, as many as you can pass  
    body=template,
    subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    print(message)
    return JSONResponse(status_code=200,content={"message":"Email sent successfully"})

    