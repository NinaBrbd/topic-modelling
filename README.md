# topic-modelling

## Subject of this project

🎯 **Objective:**

Help our team to automate one of their time-consuming manual tasks.
They spend a lot of time classifying open-ended answers (cannot be “yes” or “no”, require
the respondent to elaborate) among candidate topics. They come to ask you if you could
help them to automatically find out the candidate topics.

**Business context:**
Text classification relies on two manual steps:
1. Determine candidate topics
2. Classify open-ended answers among these candidate topics

The goal of the project is to automate the first step only.
The current process to determine candidate topics is to read the first 25% of the
open-ended answers, then manually choose multiple topics that the
member has found relevant and frequent.

We would like to automate this process so that we can use 100% of the open-ended
answers for this first step and save a significant amount of time, in addition to standardizing
the process.

**Dataset:**
The dataset of the test is an extract from Yahoo answers and is composed of the question
title, the question content and the best answer. For simplicity of the test, you can predict
one topic per row.

**Steps:**
1. Find a relevant model for Topic Modelling that suits the given dataset;
2. Train the model to predict human-readable topic;
3. Build a simple REST API that we can run locally to predict topics. 
4. Briefly identify next steps to improve the model and the inference.

Time estimation and evaluation:
~2-3 hours, not more than 3 hours.

## Libraries

The model selected is BERTopic. The training has been done on Google Collab with T4 GPU. 
Here is the Wiki of the library: `https://maartengr.github.io/BERTopic/index.html`

## Getting Started

Clone the repo.

`git clone
cd topic-modelling`

Create a virtual environment.

On macOS/Linux:

 `python3 -m venv .env
 source .env/bin/activate`

Install required dependencies. 

`pip install -r requirements.txt`

Run the FastAPI.

`uvicorn main:app`

You can only make a single prediction at the time by filling the forms. 

## API Endpoints 

The FastAPI app provides the following endpoints: 

- `/` : Accept a Form (text string) and predicts the label using the trained BERTopic model (GET and POST)

## Model

BERTopic is used with basically all default parameters. 
We fixed a random state for the UMAP algorithm, reduced the minimum size of a cluster in HDSCAN algorithm. More details are available on the notebook. 

After the training, we use update_topic function with a transformer ('google/flan-t5-base') in order to get better human-readable labels (a single 2-grams rather than the 4 first keywords).

## Improvements
1. **API**: we can only predict new instances one by one. We would prefer to upload a csv file.
2. **Topic modelling**: we could get better results by a better fine-tuning, some topics are still overlaping.
3. **Prompt engineering**: we could work on the prompt of the transformer. Only two prompts have been compared.
4. **Evaluation**: we could implement a metric to evaluate the coherence between the topic and the documents assigned to it. 




