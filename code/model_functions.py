from code import sentence_model, topic_model

def get_prediction(text):
    embeddings_text = sentence_model.encode([text], show_progress_bar=True)
    topic, prob = topic_model.transform([text], embeddings=embeddings_text )
    label = topic_model.get_topic_info(topic[0])["Name"][0].split('_')[1]
    return label