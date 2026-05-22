from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from backend.models.blog import Blog

def recommend_similar_blogs(blog_id, db):

    blogs = db.query(Blog).all()

    blog_contents = []

    for blog in blogs:

        text = f"{blog.title} {blog.content} {blog.category}"

        blog_contents.append(text)

    vectorizer = TfidfVectorizer(stop_words='english')

    tfidf_matrix = vectorizer.fit_transform(blog_contents)

    similarity = cosine_similarity(tfidf_matrix)

    target_index = None

    for index, blog in enumerate(blogs):

        if blog.id == blog_id:

            target_index = index
            break

    if target_index is None:
        return []

    similarity_scores = list(
        enumerate(similarity[target_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommended = []

    for i in similarity_scores[1:6]:

        recommended.append(blogs[i[0]])

    return recommended