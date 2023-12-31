from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse
from datetime import datetime



#  get current time in utc and day of the week
def get_current_time_and_day():
  return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), datetime.utcnow().strftime("%A")


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api")
async def stage_one_task(slack_name="null", track="null"):

  try:
    if slack_name == "null":
      return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"status_code":400,
              "message": "Please enter slack name"
              })
    
    if track == "null":
      return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
        "status_code": 400, 
        "message": "Please enter a track"
      })
    
    Time, day = get_current_time_and_day() 
    print({
      "slack_name": slack_name,
      "current_day": day,
      "utc_time": Time,
      "track": track,
      "github_file_url": "https://github.com/blacdev/repo/blob/main/staging/main.py",
      "github_repo_url": "https://github.com/blacdev/HNGx-repo",
      "status_code": 200
  })
    return JSONResponse(status_code=status.HTTP_200_OK, content={
      "slack_name": slack_name,
      "current_day": day,
      "utc_time": Time,
      "track": track,
      "github_file_url": "https://github.com/blacdev/repo/blob/main/staging/main.py",
      "github_repo_url": "https://github.com/blacdev/HNGx-repo",
      "status_code": 200
  })
     
  except Exception as e:
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Oops!\n\n\nSomething went wrong"})
  

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True )

