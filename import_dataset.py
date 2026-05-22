import pandas as pd

from backend.database import SessionLocal
from backend.models.blog import Blog

# Load CSV file
df = pd.read_csv("articles_dataset.csv")

# Database session
db = SessionLocal()

# Loop through dataset
for index, row in df.iterrows():

    blog = Blog(
        title=row["Title"],
        content=row["Content"],
        category=row["Category"]
    )

    db.add(blog)

# Save all blogs
db.commit()

print("Dataset imported successfully!")