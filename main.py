import whisper


def returntranscription():
    model = whisper.load_model("base")
    result = model.transcribe(r"C:\Users\anton\PycharmProjects\pythonProject\res\American_English.mp3")
    return result["text"]
