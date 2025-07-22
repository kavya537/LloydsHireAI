def match_candidates(job_description, candidates):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np

    # Extracting skills and experience from job description
    job_desc_vector = [job_description]

    # Extracting candidate data
    candidate_texts = [f"{candidate['skills']} {candidate['experience']}" for candidate in candidates]

    # Combine job description and candidate texts for vectorization
    all_texts = job_desc_vector + candidate_texts

    # Vectorizing the texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Calculating cosine similarity
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Creating a list of matched candidates with their match percentages
    matched_candidates = []
    for idx, candidate in enumerate(candidates):
        match_percentage = cosine_similarities[idx] * 100  # Convert to percentage
        matched_candidates.append({
            'name': candidate['name'],
            'email': candidate['email'],
            'skills': candidate['skills'],
            'experience': candidate['experience'],
            'match': round(match_percentage, 2)  # Round to 2 decimal places
        })

    # Sort candidates by match percentage in descending order
    matched_candidates.sort(key=lambda x: x['match'], reverse=True)

    return matched_candidates