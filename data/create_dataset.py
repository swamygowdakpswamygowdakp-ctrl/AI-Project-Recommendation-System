import pandas as pd
from io import StringIO
from pathlib import Path


# ============================================================
# AI-BASED PERSONALIZED PROJECT RECOMMENDATION SYSTEM
# Dataset Creation
# ============================================================

data = """Project_ID|Project_Name|Domain|Description|Required_Skills|Difficulty|Project_Type|AI_Technique|Duration
1|House Price Prediction|Machine Learning|Predict house prices using property features such as area and number of bedrooms|Python, Pandas, NumPy, Scikit-learn, Regression, Data Analysis|Beginner|Prediction|Linear Regression|2-3 Weeks
2|Student Performance Prediction|Machine Learning|Predict student academic performance using attendance, study time and previous scores|Python, Pandas, NumPy, Scikit-learn, Classification, Data Analysis|Beginner|Prediction|Random Forest|2-3 Weeks
3|Customer Churn Prediction|Machine Learning|Predict whether a customer is likely to leave a service using customer behavior data|Python, Pandas, NumPy, Scikit-learn, Classification, Data Visualization|Intermediate|Prediction|Logistic Regression|3-4 Weeks
4|Customer Segmentation|Machine Learning|Group customers into meaningful segments based on purchasing behavior|Python, Pandas, NumPy, Scikit-learn, Clustering, Data Visualization|Intermediate|Clustering|K-Means|3 Weeks
5|Credit Card Fraud Detection|Machine Learning|Detect potentially fraudulent financial transactions using transaction patterns|Python, Pandas, NumPy, Scikit-learn, Classification, Data Analysis|Advanced|Detection|Random Forest|4-5 Weeks
6|Loan Approval Prediction|Machine Learning|Predict whether a loan application should be approved using applicant information|Python, Pandas, Scikit-learn, Classification, Data Preprocessing|Beginner|Prediction|Decision Tree|2-3 Weeks
7|Movie Recommendation System|Recommender Systems|Recommend movies based on descriptions, genres, keywords and user preferences|Python, Pandas, Scikit-learn, NLP, TF-IDF, Cosine Similarity|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
8|Book Recommendation System|Recommender Systems|Recommend books based on genres, descriptions, authors and user interests|Python, Pandas, NLP, TF-IDF, Cosine Similarity, Scikit-learn|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
9|Music Recommendation System|Recommender Systems|Recommend songs based on music characteristics, genres, artists and preferences|Python, Pandas, NumPy, Machine Learning, Recommendation Systems|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
10|Personalized Project Recommendation System|Recommender Systems|Recommend suitable academic projects based on student skills, interests and difficulty preference|Python, Pandas, Scikit-learn, NLP, TF-IDF, Cosine Similarity, Recommendation Systems|Advanced|Recommendation|Content-Based Filtering|4-5 Weeks
11|Email Spam Detection|Natural Language Processing|Classify emails as spam or legitimate messages using text processing|Python, NLP, Text Processing, Scikit-learn, Classification|Beginner|Classification|Naive Bayes|2-3 Weeks
12|Sentiment Analysis System|Natural Language Processing|Analyze text reviews and classify them as positive, negative or neutral|Python, NLP, Pandas, Scikit-learn, Text Processing|Beginner|Classification|TF-IDF and Logistic Regression|2-3 Weeks
13|Fake News Detection|Natural Language Processing|Classify news articles as potentially real or fake using text-based machine learning|Python, NLP, TF-IDF, Scikit-learn, Classification|Intermediate|Classification|Logistic Regression|3-4 Weeks
14|Resume Screening System|Natural Language Processing|Analyze resumes and identify relevant skills and job-related information|Python, NLP, Text Processing, TF-IDF, Scikit-learn|Intermediate|Information Extraction|NLP|3-4 Weeks
15|Text Summarization System|Natural Language Processing|Generate concise summaries from long text documents|Python, NLP, Text Processing, Machine Learning|Advanced|Text Generation|NLP|4-5 Weeks
16|College Enquiry Chatbot|Artificial Intelligence|Build a chatbot that answers common student questions about college facilities and courses|Python, NLP, Chatbots, Machine Learning|Intermediate|Conversational AI|NLP|3-4 Weeks
17|AI Career Guidance System|Artificial Intelligence|Recommend suitable career paths based on student skills, interests and education|Python, Machine Learning, NLP, Scikit-learn, Recommendation Systems|Advanced|Recommendation|Machine Learning|4-5 Weeks
18|Student Skill Gap Analyzer|Artificial Intelligence|Identify missing technical skills by comparing student profiles with career requirements|Python, NLP, Pandas, Machine Learning, Data Analysis|Intermediate|Analysis|NLP|3-4 Weeks
19|AI Interview Question Generator|Artificial Intelligence|Generate technical interview questions based on candidate skills and job role|Python, NLP, Machine Learning, Text Processing|Advanced|Generative AI|NLP|4-5 Weeks
20|Face Mask Detection|Computer Vision|Detect whether people in images or video streams are wearing face masks|Python, OpenCV, NumPy, Machine Learning, Computer Vision|Intermediate|Image Classification|CNN|3-4 Weeks
21|Cats and Dogs Classification|Computer Vision|Classify images into cats and dogs using image processing and machine learning|Python, TensorFlow, Computer Vision, CNN, NumPy|Intermediate|Image Classification|CNN|3-4 Weeks
22|Hand Gesture Recognition|Computer Vision|Recognize different hand gestures from images or camera input|Python, TensorFlow, OpenCV, CNN, Computer Vision|Intermediate|Image Classification|CNN|4 Weeks
23|Food Image Classification|Computer Vision|Classify food images into different categories using deep learning|Python, TensorFlow, CNN, Computer Vision, Image Processing|Advanced|Image Classification|CNN|4-6 Weeks
24|Plant Disease Detection|Computer Vision|Identify plant diseases from leaf images using image classification|Python, TensorFlow, CNN, OpenCV, Computer Vision|Advanced|Image Classification|CNN|4-6 Weeks
25|Traffic Sign Recognition|Computer Vision|Recognize different traffic signs from road images using deep learning|Python, TensorFlow, CNN, Computer Vision, Image Processing|Advanced|Image Classification|CNN|4-6 Weeks
26|Object Detection System|Computer Vision|Detect and identify multiple objects in images or video streams|Python, OpenCV, Deep Learning, Computer Vision, CNN|Advanced|Object Detection|Deep Learning|5-6 Weeks
27|Face Recognition Attendance System|Computer Vision|Automatically record student attendance by recognizing faces using a camera|Python, OpenCV, Computer Vision, Face Recognition, NumPy|Advanced|Recognition|Face Recognition|4-5 Weeks
28|Vehicle Detection System|Computer Vision|Detect vehicles in road images and video for traffic monitoring|Python, OpenCV, Computer Vision, Deep Learning|Advanced|Object Detection|Deep Learning|4-6 Weeks
29|Weather Prediction System|Data Science|Predict weather conditions using historical temperature, humidity and pressure data|Python, Pandas, NumPy, Machine Learning, Data Visualization|Intermediate|Prediction|Regression|3-4 Weeks
30|Stock Price Prediction|Data Science|Analyze historical stock data and predict future price trends|Python, Pandas, NumPy, Machine Learning, Data Visualization|Advanced|Prediction|Regression|4-5 Weeks
31|Sales Forecasting System|Data Science|Forecast future sales using historical sales records|Python, Pandas, NumPy, Time Series, Machine Learning|Intermediate|Forecasting|Regression|3-4 Weeks
32|Retail Sales Analysis|Data Science|Analyze retail sales data to identify trends and business insights|Python, Pandas, NumPy, Matplotlib, Seaborn, Data Analysis|Beginner|Data Analysis|Data Analytics|2-3 Weeks
33|COVID-19 Data Analysis|Data Science|Analyze pandemic data to understand trends in cases and recoveries|Python, Pandas, NumPy, Matplotlib, Seaborn, Data Visualization|Beginner|Data Analysis|Data Analytics|2-3 Weeks
34|Air Quality Prediction|Data Science|Predict air quality levels using environmental and weather-related data|Python, Pandas, NumPy, Scikit-learn, Regression|Intermediate|Prediction|Machine Learning|3-4 Weeks
35|Energy Consumption Prediction|Data Science|Predict electricity consumption using historical usage patterns|Python, Pandas, NumPy, Machine Learning, Time Series|Intermediate|Forecasting|Regression|3-4 Weeks
36|Customer Review Analyzer|Natural Language Processing|Analyze customer reviews and identify sentiment and frequently discussed topics|Python, NLP, Pandas, Text Processing, Machine Learning|Intermediate|Text Analysis|Sentiment Analysis|3-4 Weeks
37|News Recommendation System|Recommender Systems|Recommend relevant news articles based on user interests and article content|Python, NLP, TF-IDF, Scikit-learn, Cosine Similarity|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
38|Course Recommendation System|Recommender Systems|Recommend online courses based on student skills, interests and learning goals|Python, NLP, Pandas, TF-IDF, Cosine Similarity|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
39|Job Recommendation System|Recommender Systems|Recommend suitable job opportunities based on candidate skills and job descriptions|Python, NLP, TF-IDF, Scikit-learn, Recommendation Systems|Advanced|Recommendation|Content-Based Filtering|4-5 Weeks
40|Internship Recommendation System|Recommender Systems|Recommend suitable internships based on student skills and preferred technical domains|Python, NLP, Pandas, TF-IDF, Cosine Similarity|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
41|Skill-Based Team Formation|Artificial Intelligence|Create suitable project teams by matching students according to complementary skills|Python, Pandas, Machine Learning, Recommendation Systems|Advanced|Matching|Similarity Matching|4-5 Weeks
42|Hackathon Recommendation System|Recommender Systems|Recommend hackathons based on student skills, technologies and interests|Python, Pandas, NLP, TF-IDF, Recommendation Systems|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
43|Learning Path Recommendation System|Artificial Intelligence|Recommend a personalized sequence of technical topics based on current skills and career goals|Python, Machine Learning, NLP, Recommendation Systems|Advanced|Recommendation|Content-Based Filtering|4-5 Weeks
44|Personalized Study Material Recommendation|Recommender Systems|Recommend study resources based on subject preferences and difficulty level|Python, Pandas, NLP, TF-IDF, Scikit-learn|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
45|Disease Prediction System|Machine Learning|Predict possible diseases based on selected symptoms using classification|Python, Pandas, NumPy, Scikit-learn, Classification|Intermediate|Prediction|Decision Tree|3-4 Weeks
46|Diabetes Prediction System|Machine Learning|Predict diabetes risk using demographic and health-related features|Python, Pandas, NumPy, Scikit-learn, Classification|Beginner|Prediction|Logistic Regression|2-3 Weeks
47|Heart Disease Prediction|Machine Learning|Predict heart disease risk from structured health data|Python, Pandas, NumPy, Scikit-learn, Classification|Intermediate|Prediction|Random Forest|3-4 Weeks
48|Handwritten Digit Recognition|Computer Vision|Recognize handwritten numerical digits from image input|Python, NumPy, Scikit-learn, Computer Vision, Machine Learning|Beginner|Image Classification|Neural Network|2-3 Weeks
49|Object Tracking System|Computer Vision|Track selected objects across consecutive frames in a video|Python, OpenCV, Computer Vision, NumPy|Advanced|Object Tracking|Computer Vision|4-5 Weeks
50|OCR Document Scanner|Computer Vision|Extract text from scanned documents and images using optical character recognition|Python, OpenCV, OCR, Image Processing, NLP|Intermediate|Text Extraction|OCR|3-4 Weeks
51|AI Expense Tracker|Artificial Intelligence|Categorize personal expenses automatically and provide spending insights|Python, Pandas, Machine Learning, Classification, Data Analysis|Intermediate|Classification|Machine Learning|3-4 Weeks
52|Personal Finance Recommendation System|Artificial Intelligence|Provide personalized financial planning suggestions based on spending patterns|Python, Pandas, Machine Learning, Recommendation Systems, Data Analysis|Advanced|Recommendation|Machine Learning|4-5 Weeks
53|Smart Agriculture Recommendation System|Artificial Intelligence|Recommend suitable crops based on soil, climate and environmental conditions|Python, Pandas, NumPy, Scikit-learn, Machine Learning|Intermediate|Recommendation|Classification|3-4 Weeks
54|Crop Disease Classification|Computer Vision|Classify crop diseases from leaf images using deep learning|Python, TensorFlow, CNN, Computer Vision, Image Processing|Advanced|Image Classification|CNN|4-6 Weeks
55|Smart Parking Detection|Computer Vision|Detect available and occupied parking spaces from camera images|Python, OpenCV, Computer Vision, Image Processing|Advanced|Object Detection|Computer Vision|4-5 Weeks
56|Traffic Density Analysis|Computer Vision|Analyze traffic video and estimate vehicle density on roads|Python, OpenCV, Computer Vision, Deep Learning|Advanced|Video Analysis|Object Detection|5-6 Weeks
57|Project Difficulty Predictor|Machine Learning|Predict the difficulty level of an academic project using project characteristics|Python, Pandas, Scikit-learn, Classification, Data Analysis|Intermediate|Prediction|Classification|3-4 Weeks
58|AI Project Idea Generator|Artificial Intelligence|Generate project ideas based on technical interests and preferred technologies|Python, NLP, Machine Learning, Recommendation Systems|Advanced|Recommendation|NLP|4-5 Weeks
59|Cloud Project Recommendation System|Cloud Computing|Recommend cloud computing projects based on cloud, networking and programming skills|Python, AWS, Azure, Docker, Networking, Cloud Computing|Intermediate|Recommendation|Content-Based Filtering|3-4 Weeks
60|DevOps Project Recommendation System|Cloud Computing|Recommend DevOps projects based on Git, Docker, CI/CD, Linux and cloud skills|Git, Docker, Linux, CI/CD, AWS, Azure, Python|Advanced|Recommendation|Content-Based Filtering|4-5 Weeks
"""


# Convert the text data into a Pandas DataFrame
df = pd.read_csv(StringIO(data), sep="|")


# Get the project directory
project_root = Path(__file__).resolve().parent


# Save the dataset
output_file = project_root / "project_dataset.csv"
df.to_csv(output_file, index=False)


# ============================================================
# DISPLAY DATASET INFORMATION
# ============================================================

print("=" * 60)
print("PROJECT DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print(f"Total Projects: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print(f"Dataset Location: {output_file}")

print("\nColumns:")
for column in df.columns:
    print(f" - {column}")

print("\nDomain Distribution:")
print(df["Domain"].value_counts())

print("\nDifficulty Distribution:")
print(df["Difficulty"].value_counts())

print("\nFirst 5 Projects:")
print(df.head().to_string(index=False))

print("\nDataset Shape:")
print(df.shape)

print("\nDataset creation completed successfully!")