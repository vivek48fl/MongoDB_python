from fastapi import BackgroundTasks,FastAPI
from starlette.requests import Request
from starlette.responses import Response,JSONResponse
app=FastAPI()
def demo_fun():
    for i in range(0,11):
        print(i)

def write_notification(email: str, message):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)
        #demo_fun()
        

        
@app.post("/send-notification")
async def send_notification(background_tasks: BackgroundTasks,request:Request)-> JSONResponse:
    
    data = await request.json()
    print(data)
    background_tasks.add_task(write_notification, data["email"], message="some notification")
    background_tasks.add_task(demo_fun)
    
    return JSONResponse({"message": "Notification sent in the background"})