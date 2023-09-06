from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import status, HTTPException
import time



#  get current time in utc and day of the week
def get_current_time_and_day():
  return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), time.strftime("%A", time.gmtime())

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def stage_one_task(slack_name="null", track="null"):

  try:
    if slack_name == "null":
      return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status":400,
              "message": "Please enter slack name"
              })
    
    if track == "null":
      return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
        "status": 400, 
        "message": "Please enter a track"
      })
    
    Time, day = get_current_time_and_day() 
    return {
      "slack_name": slack_name,
      "current_day": day,
      "utc_time": Time,
      "track": track,
      "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
      "github_repo_url": "https://github.com/blacdev/repo",
      "status": 200
  }
     
  except Exception as e:
    return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Oops!\n\n\nSomething went wrong"}
  

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True )

