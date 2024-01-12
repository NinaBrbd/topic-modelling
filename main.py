from code import app
from fastapi import File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from code.model_functions import get_prediction

@app.get("/")
async def get_data():
    content = """
<body>
<h1> BERTopic to find candidates topics </h1>
<p> Fill the form to get a label prediction of a question/answer. You can either fill the three columns, or simply fill the "All in one" form. </p>
<p> "All in one" stands for the merge of the three forms. </p>
<p> Note that the "All in one" form takes precedence over the other forms.</p>
<form enctype="multipart/form-data" method="post">
<p> Question Title: <input name="question_title" type="str" multiple> </p>
<p> Question Content: <input name="question_content" type="str" multiple> </p>
<p> Best Answer: <input name="best_answer" type="str" multiple> </p>
<p> All in one: <input name="text" type="str" multiple> </p>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/")
async def predict(question_title: Annotated[str, Form()]="",question_content: Annotated[str, Form()]="",best_answer: Annotated[str, Form()]="",text: Annotated[str, Form()]=None):
    if text is None:
        text = ' '.join([question_content, question_title, best_answer])
    label = get_prediction(text)
    return {"label":label}
