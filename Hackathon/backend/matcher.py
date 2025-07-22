from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resumes(requirement_text, resumes):
    docs = [requirement_text] + [res['text'] for res in resumes]
    tfidf = TfidfVectorizer().fit_transform(docs)
    cosine_sim = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    ranked = sorted(
        zip(resumes, cosine_sim),
        key=lambda x: x[1],
        reverse=True
    )
    return [{"name": r['name'], "email": r['email'], "phone": r['phone'],
             "skills": r['skills'], "score": round(score*100, 2), "resume_link": r['resume_link']}
            for r, score in ranked]
