import uvicorn
from typing import List
from fastapi import FastAPI, UploadFile, File, Response
from pydantic_models.photo_model import PhotoModel

app = FastAPI()


@app.get("/status")
def check_status():
    return "Hello World"


# @app.get("/photos", response_model=List[PhotoModel])
# def get_photos():


@app.post("/add_photo")
def add_photo(file: UploadFile):

    uploaded_file_url = (
        f"https://github.com/CristyGuzman/ImageUpload/blob/main/images/{file.filename}"
    )

    print(f"File uploaded is {file.filename} with content {file.content_type}")
    return {"file": file.filename, "content": file.content_type}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
