import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resumes(job_desc, resume_texts):
    corpus = [job_desc] + [r['text'] for r in resume_texts]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    for i, score in enumerate(scores):
        resume_texts[i]['match'] = round(score * 100, 2)
    return sorted(resume_texts, key=lambda x: x['match'], reverse=True)