from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine, Base

from backend.models.user import User
from backend.models.blog import Blog
from backend.models.interaction import Interaction
from backend.models.like import Like
from backend.models.save import Save

from backend.routes.auth import router as auth_router
from backend.routes.blog_routes import router as blog_router
from backend.routes.interaction_routes import router as interaction_router
from backend.routes.recommendation_routes import router as recommendation_router
from backend.routes.social_routes import router as social_router
from backend.routes.nlp_routes import router as nlp_router
from backend.routes.gemini_routes import router as gemini_router

import pandas as pd
import os

# =========================
# FASTAPI APP
# =========================

app = FastAPI()

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# DATABASE TABLES
# =========================

Base.metadata.create_all(bind=engine)

# =========================
# ROUTERS
# =========================

app.include_router(auth_router)
app.include_router(blog_router)
app.include_router(interaction_router)
app.include_router(recommendation_router)
app.include_router(social_router)
app.include_router(nlp_router)
app.include_router(gemini_router)

# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():
    return {
        "message": "Smart AI Feed Backend Running Successfully 🚀"
    }

# =========================
# LOAD CSV DATASET
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "..", "articles_dataset.csv")

df = pd.read_csv(csv_path)

# =========================
# ALL BLOGS API
# =========================

@app.get("/all-blogs")
def get_all_blogs():

    blogs = df.to_dict(orient="records")

    return blogs
# ==============================
# GET ALL CATEGORIES
# ==============================

@app.get("/categories")
def get_categories():

    categories = df["Category"].dropna().unique().tolist()

    return {
        "categories": categories
    }