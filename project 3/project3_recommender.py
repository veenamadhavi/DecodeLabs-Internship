import math

job_roles = {
    "Data Scientist": ["python", "machine learning", "data analysis", "statistics"],
    "AI Engineer": ["python", "machine learning", "deep learning", "tensorflow"],
    "Web Developer": ["html", "css", "javascript", "react"],
    "Backend Developer": ["python", "sql", "api", "django"],
    "DevOps Engineer": ["aws", "docker", "kubernetes", "linux"]
}

print("===== Tech Stack Recommender =====")

skills = input("Enter 3 skills separated by commas: ").lower()
user_skills = [skill.strip() for skill in skills.split(",")]

scores = {}

# --- UPGRADED PROCESS LAYER (Cosine Similarity) ---
for role, role_skills in job_roles.items():
    # 1. Create a unique vocabulary list for this specific comparison
    vocab = list(set(user_skills + role_skills))
    
    # 2. Convert user choices and role skills into 1s and 0s vectors
    user_vector = [1 if skill in user_skills else 0 for skill in vocab]
    role_vector = [1 if skill in role_skills else 0 for skill in vocab]
    
    # 3. Apply the Cosine Similarity math formulas
    dot_product = sum(u * r for u, r in zip(user_vector, role_vector))
    magnitude_user = math.sqrt(sum(u * u for u in user_vector))
    magnitude_role = math.sqrt(sum(r * r for r in role_vector))
    
    # 4. Calculate the alignment score percentage
    if magnitude_user == 0 or magnitude_role == 0:
        cosine_similarity = 0.0
    else:
        cosine_similarity = dot_product / (magnitude_user * magnitude_role)
        
    scores[role] = cosine_similarity

# --- SORTING AND FILTERING ---
sorted_roles = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Recommendations:\n")

for role, score in sorted_roles[:3]:
    # Displaying it beautifully as a percentage match
    print(f"{role:<20} --> Match Score: {score * 100:.1f}%")