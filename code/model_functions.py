from code import sentence_model, topic_model

def get_prediction(text:str):
    """
    Returns the topic prediction from the text input.
    """
    # Encoding the embeddings
    embeddings_text = sentence_model.encode([text], show_progress_bar=True)
    # Make the prediction = topic number
    topic, prob = topic_model.transform([text], embeddings=embeddings_text )
    # Get topic name
    label = topic_model.get_topic_info(topic[0])["Name"][0].split('_')[1]
    return label