from fastapi import FastAPI
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Define the embedding model
model_embedding = "all-MiniLM-L6-v2"

sentence_model = SentenceTransformer(model_embedding)

# load the model from the safetensors format
topic_model = BERTopic.load("model", embedding_model=model_embedding)
