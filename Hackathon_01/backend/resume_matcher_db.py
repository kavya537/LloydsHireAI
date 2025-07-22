from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resumes(requirement_text, resumes):
    documents = [requirement_text] + [res['text'] for res in resumes]
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(documents)

    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    
    for i, score in enumerate(scores):
        resumes[i]['match'] = round(score * 100, 2)

    return sorted(resumes, key=lambda x: x['match'], reverse=True)

def extract_resume_data(text):
    import re
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Extract email and phone
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\+?\d[\d\s\-]{8,}\d', text)

    # Try better logic for name: use first few lines
    lines = text.strip().split('\n')[:10]  # First 10 lines
    name = 'NA'
    for line in lines:
        if len(line.strip()) > 2 and not any(keyword in line.lower() for keyword in ['resume', 'email', 'phone', '@']):
            name = line.strip()
            break

    # Extract predefined skills
    predefined_skills = [
        'python', 'java', 'c++', 'aws', 'azure', 'docker', 'flask', 'django', 'mongodb',
        'mysql', 'nlp', 'pandas', 'numpy', 'machine learning', 'data science', 'javascript',
        'html', 'css', 'react', 'angular', 'node', 'sql', 'git', 'github', 'rest', 'api',
        'kubernetes'
    ]
    found_skills = [skill for skill in predefined_skills if skill.lower() in text.lower()]

    return {
        'name': name,
        'email': email[0] if email else 'NA',
        'phone': phone[0] if phone else 'NA',
        'skills': list(set(found_skills)),
        'text': text
    }


