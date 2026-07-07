import joblib
import numpy as np
import os

CAREER_DATA = {
    "AI Engineer": {
        "required_skills": ["python", "machine learning", "deep learning", "tensorflow", "keras", "neural networks", "data analysis"],
        "salary": "₹8 LPA – ₹25 LPA",
        "roadmap": ["Learn Python", "Master Statistics & Math", "Study ML Algorithms", "Learn Deep Learning", "Build Projects", "Deploy ML Models"],
        "resources": [{"title": "Deep Learning Specialization", "type": "Course", "url": "https://www.coursera.org/specializations/deep-learning", "provider": "Coursera"}, {"title": "Krish Naik", "type": "YouTube", "url": "https://www.youtube.com/@krishnaik06", "provider": "YouTube"}]
    },
    "Data Scientist": {
        "required_skills": ["python", "machine learning", "statistics", "data visualization", "pandas", "scikit-learn", "sql"],
        "salary": "₹6 LPA – ₹22 LPA",
        "roadmap": ["Learn Python & SQL", "Master Statistics", "Data Wrangling", "Machine Learning", "Data Visualization", "Kaggle Projects"],
        "resources": [{"title": "Kaggle Learn", "type": "Platform", "url": "https://www.kaggle.com/learn", "provider": "Kaggle"}, {"title": "Sentdex", "type": "YouTube", "url": "https://www.youtube.com/@sentdex", "provider": "YouTube"}]
    },
    "Full Stack Developer": {
        "required_skills": ["javascript", "react", "nodejs", "html", "css", "rest api", "mongodb", "sql"],
        "salary": "₹5 LPA – ₹20 LPA",
        "roadmap": ["HTML/CSS Basics", "JavaScript Mastery", "React Frontend", "Node.js Backend", "Databases", "Deploy"],
        "resources": [{"title": "The Odin Project", "type": "Course", "url": "https://www.theodinproject.com", "provider": "Free"}, {"title": "Traversy Media", "type": "YouTube", "url": "https://www.youtube.com/@TraversyMedia", "provider": "YouTube"}]
    },
    "Backend Developer": {
        "required_skills": ["python", "django", "flask", "rest api", "postgresql", "docker", "redis"],
        "salary": "₹5 LPA – ₹18 LPA",
        "roadmap": ["Learn Python/Java", "Framework (Django/Flask)", "Databases & SQL", "REST APIs", "Docker", "Microservices"],
        "resources": [{"title": "Django Documentation", "type": "Docs", "url": "https://docs.djangoproject.com", "provider": "Django"}, {"title": "Tech With Tim", "type": "YouTube", "url": "https://www.youtube.com/@TechWithTim", "provider": "YouTube"}]
    },
    "Frontend Developer": {
        "required_skills": ["react", "javascript", "html", "css", "typescript", "redux", "figma"],
        "salary": "₹4 LPA – ₹16 LPA",
        "roadmap": ["HTML & CSS", "JavaScript ES6+", "React.js", "TypeScript", "State Management", "Testing"],
        "resources": [{"title": "JavaScript.info", "type": "Docs", "url": "https://javascript.info", "provider": "Free"}, {"title": "Kevin Powell", "type": "YouTube", "url": "https://www.youtube.com/@KevinPowell", "provider": "YouTube"}]
    },
    "DevOps Engineer": {
        "required_skills": ["docker", "kubernetes", "aws", "linux", "ci/cd", "terraform", "ansible"],
        "salary": "₹7 LPA – ₹22 LPA",
        "roadmap": ["Linux Fundamentals", "Scripting", "Docker & Containers", "Kubernetes", "CI/CD Pipelines", "Cloud"],
        "resources": [{"title": "KodeKloud", "type": "Platform", "url": "https://kodekloud.com", "provider": "KodeKloud"}, {"title": "TechWorld with Nana", "type": "YouTube", "url": "https://www.youtube.com/@TechWorldwithNana", "provider": "YouTube"}]
    },
    "Data Analyst": {
        "required_skills": ["sql", "python", "excel", "tableau", "power bi", "statistics", "data visualization"],
        "salary": "₹4 LPA – ₹14 LPA",
        "roadmap": ["Excel & Statistics", "SQL Mastery", "Python for Analysis", "Tableau/Power BI", "Data Storytelling", "Portfolio"],
        "resources": [{"title": "Alex The Analyst", "type": "YouTube", "url": "https://www.youtube.com/@AlexTheAnalyst", "provider": "YouTube"}]
    },
    "NLP Engineer": {
        "required_skills": ["python", "nlp", "transformers", "bert", "text classification", "pytorch", "spacy"],
        "salary": "₹8 LPA – ₹24 LPA",
        "roadmap": ["Python & ML Basics", "NLP Fundamentals", "Transformers & BERT", "HuggingFace", "Build NLP Projects", "Fine-tune LLMs"],
        "resources": [{"title": "HuggingFace Course", "type": "Course", "url": "https://huggingface.co/learn/nlp-course", "provider": "HuggingFace"}]
    },
    "Computer Vision Engineer": {
        "required_skills": ["python", "opencv", "deep learning", "pytorch", "image processing", "tensorflow", "yolo"],
        "salary": "₹8 LPA – ₹24 LPA",
        "roadmap": ["Python & Math", "OpenCV Basics", "Deep Learning", "CNN Architectures", "Object Detection", "Deploy Vision Models"],
        "resources": [{"title": "PyImageSearch", "type": "Blog", "url": "https://pyimagesearch.com", "provider": "Free/Paid"}]
    },
    "Android Developer": {
        "required_skills": ["android", "java", "kotlin", "firebase", "rest api", "xml", "jetpack compose"],
        "salary": "₹4 LPA – ₹18 LPA",
        "roadmap": ["Java/Kotlin Basics", "Android Studio", "UI with XML/Jetpack", "Firebase", "REST APIs", "Play Store"],
        "resources": [{"title": "Android Developers Docs", "type": "Docs", "url": "https://developer.android.com", "provider": "Google"}, {"title": "Philipp Lackner", "type": "YouTube", "url": "https://www.youtube.com/@PhilippLackner", "provider": "YouTube"}]
    },
    "iOS Developer": {
        "required_skills": ["swift", "ios", "xcode", "swiftui", "objective-c", "firebase", "rest api"],
        "salary": "₹5 LPA – ₹20 LPA",
        "roadmap": ["Swift Basics", "UIKit/SwiftUI", "Xcode IDE", "Firebase & APIs", "App Store", "Advanced Swift"],
        "resources": [{"title": "Hacking with Swift", "type": "Course", "url": "https://www.hackingwithswift.com", "provider": "Free"}]
    },
    "Database Administrator": {
        "required_skills": ["sql", "postgresql", "mongodb", "data modeling", "etl", "data warehouse", "mysql"],
        "salary": "₹5 LPA – ₹16 LPA",
        "roadmap": ["SQL Mastery", "Database Design", "PostgreSQL/MySQL", "NoSQL (MongoDB)", "Performance Tuning", "Data Warehousing"],
        "resources": [{"title": "PostgreSQL Docs", "type": "Docs", "url": "https://www.postgresql.org/docs/", "provider": "Free"}]
    },
    "Cybersecurity Engineer": {
        "required_skills": ["cybersecurity", "networking", "linux", "penetration testing", "ethical hacking", "python", "firewall"],
        "salary": "₹6 LPA – ₹20 LPA",
        "roadmap": ["Networking Basics", "Linux OS", "Ethical Hacking", "Penetration Testing", "Kali Linux Tools", "Certifications (CEH, OSCP)"],
        "resources": [{"title": "TryHackMe", "type": "Platform", "url": "https://tryhackme.com", "provider": "TryHackMe"}, {"title": "NetworkChuck", "type": "YouTube", "url": "https://www.youtube.com/@NetworkChuck", "provider": "YouTube"}]
    },
    "Blockchain Developer": {
        "required_skills": ["blockchain", "solidity", "ethereum", "web3", "smart contracts", "javascript", "cryptography"],
        "salary": "₹7 LPA – ₹28 LPA",
        "roadmap": ["Blockchain Fundamentals", "Solidity Programming", "Ethereum & Smart Contracts", "Web3.js", "DApp Development", "Security"],
        "resources": [{"title": "CryptoZombies", "type": "Course", "url": "https://cryptozombies.io", "provider": "Free"}]
    },
    "AI Researcher": {
        "required_skills": ["python", "machine learning", "deep learning", "pytorch", "tensorflow", "research", "mathematics"],
        "salary": "₹10 LPA – ₹35 LPA",
        "roadmap": ["Strong Math Foundation", "Deep Learning Theory", "Research Papers", "PyTorch/TensorFlow", "Publish Research", "PhD/Masters"],
        "resources": [{"title": "Papers With Code", "type": "Platform", "url": "https://paperswithcode.com", "provider": "Free"}]
    },
    "Cloud Architect": {
        "required_skills": ["aws", "azure", "gcp", "cloud computing", "serverless", "terraform", "docker"],
        "salary": "₹10 LPA – ₹30 LPA",
        "roadmap": ["Cloud Basics", "AWS/Azure/GCP Certifications", "Infrastructure as Code", "Serverless", "Cost Optimization", "Security"],
        "resources": [{"title": "AWS Training", "type": "Course", "url": "https://aws.amazon.com/training", "provider": "AWS"}]
    },
    "Big Data Engineer": {
        "required_skills": ["apache spark", "hadoop", "kafka", "python", "scala", "data pipeline", "hive"],
        "salary": "₹8 LPA – ₹25 LPA",
        "roadmap": ["SQL & Python", "Hadoop Ecosystem", "Apache Spark", "Kafka Streaming", "Data Pipelines", "Cloud Big Data"],
        "resources": [{"title": "DataCamp", "type": "Platform", "url": "https://www.datacamp.com", "provider": "DataCamp"}]
    },
    "UI/UX Designer": {
        "required_skills": ["figma", "ui design", "ux research", "prototyping", "adobe xd", "wireframing", "user testing"],
        "salary": "₹4 LPA – ₹16 LPA",
        "roadmap": ["Design Principles", "Figma Mastery", "UX Research", "Prototyping", "User Testing", "Portfolio"],
        "resources": [{"title": "Google UX Design Certificate", "type": "Course", "url": "https://www.coursera.org/professional-certificates/google-ux-design", "provider": "Coursera"}]
    },
    "Product Analyst": {
        "required_skills": ["python", "statistics", "sql", "a/b testing", "data visualization", "product analytics"],
        "salary": "₹6 LPA – ₹18 LPA",
        "roadmap": ["SQL & Python", "Statistics & A/B Testing", "Product Metrics", "Data Visualization", "User Behavior Analysis", "Product Strategy"],
        "resources": [{"title": "Product Analytics Course", "type": "Course", "url": "https://www.coursera.org", "provider": "Coursera"}]
    },
    "Java Developer": {
        "required_skills": ["java", "spring boot", "microservices", "docker", "sql", "hibernate", "maven"],
        "salary": "₹5 LPA – ₹20 LPA",
        "roadmap": ["Core Java", "Spring Framework", "Spring Boot", "Microservices", "Docker & Kubernetes", "Cloud Deployment"],
        "resources": [{"title": "Java Brains", "type": "YouTube", "url": "https://www.youtube.com/@Java.Brains", "provider": "YouTube"}]
    },
    "Game Developer": {
        "required_skills": ["unity", "c sharp", "game development", "3d", "physics", "unreal", "blender"],
        "salary": "₹4 LPA – ₹18 LPA",
        "roadmap": ["C# / C++ Basics", "Unity/Unreal Engine", "Game Physics", "3D Modeling Basics", "Game Design Principles", "Publish on Steam/Play Store"],
        "resources": [{"title": "Unity Learn", "type": "Platform", "url": "https://learn.unity.com", "provider": "Unity"}, {"title": "Brackeys", "type": "YouTube", "url": "https://www.youtube.com/@Brackeys", "provider": "YouTube"}]
    },
    ".NET Developer": {
        "required_skills": ["c sharp", "dotnet", "asp net", "entity framework", "sql server", "azure", "rest api"],
        "salary": "₹5 LPA – ₹18 LPA",
        "roadmap": ["C# Fundamentals", "ASP.NET Core", "Entity Framework", "SQL Server", "Azure Deployment", "Microservices"],
        "resources": [{"title": "Microsoft Learn", "type": "Docs", "url": "https://learn.microsoft.com/dotnet", "provider": "Microsoft"}]
    },
    "Embedded Engineer": {
        "required_skills": ["embedded systems", "c", "microcontroller", "arduino", "rtos", "hardware", "firmware"],
        "salary": "₹5 LPA – ₹18 LPA",
        "roadmap": ["C Programming", "Microcontroller Basics (Arduino)", "RTOS", "Hardware Interfaces", "Embedded Linux", "IoT Projects"],
        "resources": [{"title": "Embedded Systems Course", "type": "Course", "url": "https://www.coursera.org", "provider": "Coursera"}]
    },
    "Robotics Engineer": {
        "required_skills": ["robotics", "ros", "python", "slam", "sensors", "kinematics", "c++"],
        "salary": "₹6 LPA – ₹22 LPA",
        "roadmap": ["Python & C++", "Robot Operating System (ROS)", "Kinematics & Dynamics", "Sensors & Actuators", "SLAM", "Robot Projects"],
        "resources": [{"title": "ROS Documentation", "type": "Docs", "url": "https://www.ros.org", "provider": "Open Source"}]
    },
    "AR/VR Developer": {
        "required_skills": ["ar vr", "unity", "unreal", "c sharp", "3d modeling", "spatial computing", "openxr"],
        "salary": "₹6 LPA – ₹22 LPA",
        "roadmap": ["Unity/Unreal Basics", "3D Modeling (Blender)", "AR/VR SDKs", "Spatial Computing", "Performance Optimization", "Deploy on Quest/HoloLens"],
        "resources": [{"title": "Unity XR Course", "type": "Course", "url": "https://learn.unity.com", "provider": "Unity"}]
    },
}

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'career_model.pkl')
_model = None

def load_model():
    global _model
    if _model is None and os.path.exists(MODEL_PATH):
        _model = joblib.load(MODEL_PATH)
    return _model

def get_career_data(career):
    return CAREER_DATA.get(career, {
        "required_skills": [],
        "salary": "₹5 LPA – ₹15 LPA",
        "roadmap": ["Build foundational skills", "Work on projects", "Get certified", "Apply for jobs"],
        "resources": []
    })

def predict_career(name, skills_input):
    skills_clean = skills_input.lower().strip()
    skills_list = [s.strip() for s in skills_clean.split(',')]
    model = load_model()

    if model:
        proba = model.predict_proba([skills_clean])[0]
        classes = model.classes_
        top_indices = np.argsort(proba)[::-1][:3]
        top_matches = [{"career": classes[i], "confidence": round(float(proba[i]) * 100, 1)} for i in top_indices]
        recommended = top_matches[0]["career"]
        confidence = top_matches[0]["confidence"]
    else:
        recommended, confidence, top_matches = rule_based_predict(skills_list)

    career_info = get_career_data(recommended)
    required = set(career_info.get("required_skills", []))
    user_skills = set(skills_list)
    missing = list(required - user_skills)
    readiness = round((len(required & user_skills) / max(len(required), 1)) * 100, 1)

    return {
        "name": name,
        "recommended_career": recommended,
        "confidence": f"{confidence}%",
        "top_matches": top_matches,
        "missing_skills": missing,
        "readiness_score": readiness,
        "roadmap": career_info.get("roadmap", []),
        "salary": career_info.get("salary", "₹5 LPA – ₹15 LPA"),
        "resources": career_info.get("resources", [])
    }

def rule_based_predict(skills):
    scores = {}
    for career, data in CAREER_DATA.items():
        required = set(data["required_skills"])
        user = set(skills)
        scores[career] = len(required & user)
    sorted_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_careers[:3]
    total = max(scores[sorted_careers[0][0]], 1)
    top_matches = [{"career": c, "confidence": round((s / total) * 100, 1)} for c, s in top3]
    return top3[0][0], top_matches[0]["confidence"], top_matches
