def fake_news_predictor(article, model):
    return_result = model.predict([article])
    if return_result[0] > 0.6:
        return "Real news"
    else:
        return "Fake news"
