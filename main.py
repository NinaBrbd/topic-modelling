from code import app
from fastapi import File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from code.model_functions import get_prediction

@app.get("/")
async def get_data():
    """
    Get data from the 4 forms:
        - question_title
        - question_content
        - best_answer
        - all-in-one: represents the concat of the three precedent forms

    Note that if some values are submitted in the all-in-one form, only this data will be predicted.
    """
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
    """
    Get data from the 4 forms:
        - question_title
        - question_content
        - best_answer
        - all-in-one: represents the concat of the three precedent forms

    Note that if some values are submitted in the all-in-one form, only this data will be predicted.
    
    Returns the label name according to the trained model as JSON format.
    """
    if text is None:
        text = ' '.join([question_content, question_title, best_answer])
    label = get_prediction(text)
    return {"label":label}
