import os
import uuid
import json

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from detector import detect_defects
from agent import root_agent

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="AI Quality Inspection")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

sessions = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name="quality_inspection",
    session_service=sessions
)

@app.post("/inspect")
async def inspect_product(file: UploadFile = File(...)):

    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(400, "Only JPG, PNG and WEBP images are supported")

    content = await file.read()

    if not content or len(content) > 10 * 1024 * 1024:
        raise HTTPException(400, "Invalid image or file exceeds 10 MB")

    filename = f"{uuid.uuid4().hex}.jpg"
    image_path = os.path.join("uploads", filename)

    with open(image_path, "wb") as f:
        f.write(content)

    result = detect_defects(image_path)

    session_id = str(uuid.uuid4())

    await sessions.create_session(
        app_name="quality_inspection",
        user_id="inspector",
        session_id=session_id
    )

    message = types.Content(
        role="user",
        parts=[
            types.Part(
                text="Generate a quality inspection report using these "
                     "YOLO results. Do not change the detection values: "
                     + json.dumps(result)
            )
        ]
    )

    report = ""

    async for event in runner.run_async(
        user_id="inspector",
        session_id=session_id,
        new_message=message
    ):
        if event.is_final_response() and event.content:
            report = "".join(
                part.text or "" for part in event.content.parts
            )

    return {
        **result,
        "filename": file.filename,
        "ai_report": report
    }