"""
Practical Project Roadmaps
==========================

Project-specific practical roadmaps for the
AI-Based Personalized Project Recommendation System.

Each roadmap follows:

What to build
→ Requirements
→ Dataset
→ Folder structure
→ Setup
→ Implementation
→ Testing
→ Common errors
→ Final checklist
"""

PROJECT_ROADMAPS = {

    # ============================================================
    # 1. HOUSE PRICE PREDICTION
    # ============================================================

    "House Price Prediction": {
        "overview": """
Build a machine learning web application that predicts the approximate
price of a house from features such as area, bedrooms, bathrooms and
other property information.
""",
        "difficulty": "Beginner",
        "estimated_time": "4–6 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git",
            "Web browser"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "matplotlib",
            "streamlit",
            "joblib"
        ],

        "dataset": {
            "required": True,
            "name": "House Prices Dataset",
            "source": "Kaggle – House Prices",
            "file": "train.csv",
            "placement": "data/train.csv"
        },

        "folder_structure": """
house-price-prediction/
│
├── data/
│   └── train.csv
│
├── model/
│   └── house_price_model.pkl
│
├── outputs/
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create the project folder",
                "actions": [
                    "Create a folder named house-price-prediction.",
                    "Open it in VS Code.",
                    "Create data, model and outputs folders."
                ]
            },
            {
                "step": 2,
                "title": "Create virtual environment",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate"
                ],
                "expected": "The terminal should show (venv)."
            },
            {
                "step": 3,
                "title": "Install libraries",
                "commands": [
                    "pip install pandas numpy scikit-learn matplotlib streamlit joblib"
                ]
            },
            {
                "step": 4,
                "title": "Add dataset",
                "actions": [
                    "Download the House Prices dataset.",
                    "Extract train.csv.",
                    "Place it inside data/."
                ]
            },
            {
                "step": 5,
                "title": "Prepare the data",
                "actions": [
                    "Load train.csv using pandas.",
                    "Select useful features.",
                    "Handle missing values.",
                    "Separate features and target.",
                    "Split the dataset into training and testing data."
                ]
            },
            {
                "step": 6,
                "title": "Train the model",
                "actions": [
                    "Create train_model.py.",
                    "Train a regression model.",
                    "Calculate MAE and R².",
                    "Save the trained model using joblib."
                ],
                "command": "python train_model.py"
            },
            {
                "step": 7,
                "title": "Create Streamlit application",
                "actions": [
                    "Create app.py.",
                    "Load the saved model.",
                    "Create input fields.",
                    "Accept house details.",
                    "Generate the prediction.",
                    "Display the predicted price."
                ]
            },
            {
                "step": 8,
                "title": "Run application",
                "command": "streamlit run app.py",
                "expected": "The House Price Prediction application opens in the browser."
            },
            {
                "step": 9,
                "title": "Test application",
                "actions": [
                    "Enter valid house information.",
                    "Click Predict.",
                    "Verify that a predicted price is displayed.",
                    "Try different input values."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "ModuleNotFoundError",
                "fix": "Install the missing package inside the active venv."
            },
            {
                "error": "FileNotFoundError: train.csv",
                "fix": "Make sure train.csv is inside data/."
            },
            {
                "error": "Model file not found",
                "fix": "Run train_model.py before starting app.py."
            }
        ],

        "final_checklist": [
            "Dataset downloaded",
            "Dataset placed correctly",
            "Libraries installed",
            "Model trained",
            "Model saved",
            "Streamlit application running",
            "Prediction working",
            "Project tested",
            "README created",
            "Project uploaded to GitHub"
        ]
    },


    # ============================================================
    # 2. STUDENT PERFORMANCE PREDICTION
    # ============================================================

    "Student Performance Prediction": {
        "overview": """
Build a machine learning application that predicts student academic
performance using information such as study time, attendance,
previous scores and other available student attributes.
""",
        "difficulty": "Beginner",
        "estimated_time": "4–6 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git",
            "Web browser"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "matplotlib",
            "streamlit",
            "joblib"
        ],

        "dataset": {
            "required": True,
            "name": "Student Performance Dataset",
            "source": "Public student performance dataset",
            "file": "student_data.csv",
            "placement": "data/student_data.csv"
        },

        "folder_structure": """
student-performance-prediction/
│
├── data/
│   └── student_data.csv
│
├── model/
│   └── student_model.pkl
│
├── outputs/
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create the project",
                "actions": [
                    "Create student-performance-prediction.",
                    "Open it in VS Code.",
                    "Create data, model and outputs folders."
                ]
            },
            {
                "step": 2,
                "title": "Create virtual environment",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate"
                ]
            },
            {
                "step": 3,
                "title": "Install libraries",
                "commands": [
                    "pip install pandas numpy scikit-learn matplotlib streamlit joblib"
                ]
            },
            {
                "step": 4,
                "title": "Add dataset",
                "actions": [
                    "Download the selected student performance dataset.",
                    "Place it inside data/.",
                    "Verify the CSV opens correctly."
                ]
            },
            {
                "step": 5,
                "title": "Prepare data",
                "actions": [
                    "Load the CSV.",
                    "Inspect columns.",
                    "Handle missing values.",
                    "Separate input features and target.",
                    "Split training and testing data."
                ]
            },
            {
                "step": 6,
                "title": "Train model",
                "actions": [
                    "Create train_model.py.",
                    "Train a regression model.",
                    "Calculate MAE and R².",
                    "Save the model."
                ],
                "command": "python train_model.py"
            },
            {
                "step": 7,
                "title": "Build Streamlit application",
                "actions": [
                    "Create input fields.",
                    "Load the saved model.",
                    "Generate the prediction.",
                    "Display the predicted performance."
                ]
            },
            {
                "step": 8,
                "title": "Run application",
                "command": "streamlit run app.py"
            },
            {
                "step": 9,
                "title": "Test",
                "actions": [
                    "Enter sample student information.",
                    "Generate a prediction.",
                    "Try different values.",
                    "Confirm that the application works."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "CSV file not found",
                "fix": "Check that the file is inside data/."
            },
            {
                "error": "Column not found",
                "fix": "Print df.columns and use the exact column names."
            },
            {
                "error": "Model file not found",
                "fix": "Run train_model.py first."
            }
        ],

        "final_checklist": [
            "Dataset added",
            "Data preprocessing completed",
            "Model trained",
            "Model evaluated",
            "Model saved",
            "Streamlit UI created",
            "Prediction tested",
            "README created",
            "GitHub repository created"
        ]
    },


    # ============================================================
    # 3. CUSTOMER CHURN PREDICTION
    # ============================================================

    "Customer Churn Prediction": {
        "overview": """
Build a machine learning system that predicts whether a customer is
likely to leave a service based on customer and service information.
""",
        "difficulty": "Intermediate",
        "estimated_time": "5–7 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "matplotlib",
            "seaborn",
            "streamlit",
            "joblib"
        ],

        "dataset": {
            "required": True,
            "name": "Telco Customer Churn Dataset",
            "source": "IBM Telco Customer Churn dataset",
            "file": "WA_Fn-UseC_-Telco-Customer-Churn.csv",
            "placement": "data/customer_churn.csv"
        },

        "folder_structure": """
customer-churn-prediction/
│
├── data/
│   └── customer_churn.csv
│
├── model/
│   └── churn_model.pkl
│
├── outputs/
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create project folders",
                "actions": [
                    "Create customer-churn-prediction.",
                    "Create data, model and outputs."
                ]
            },
            {
                "step": 2,
                "title": "Create virtual environment",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate"
                ]
            },
            {
                "step": 3,
                "title": "Install libraries",
                "commands": [
                    "pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib"
                ]
            },
            {
                "step": 4,
                "title": "Add dataset",
                "actions": [
                    "Download the Telco Customer Churn CSV.",
                    "Place it inside data/.",
                    "Rename it customer_churn.csv."
                ]
            },
            {
                "step": 5,
                "title": "Clean data",
                "actions": [
                    "Load the CSV.",
                    "Convert TotalCharges to numeric.",
                    "Handle missing values.",
                    "Encode categorical variables."
                ]
            },
            {
                "step": 6,
                "title": "Train classification model",
                "actions": [
                    "Separate X and y.",
                    "Split the dataset.",
                    "Train a classification model.",
                    "Calculate accuracy, precision and recall.",
                    "Save the model."
                ]
            },
            {
                "step": 7,
                "title": "Build application",
                "actions": [
                    "Create customer input fields.",
                    "Load the model.",
                    "Predict churn.",
                    "Display churn probability."
                ]
            },
            {
                "step": 8,
                "title": "Run",
                "command": "streamlit run app.py"
            },
            {
                "step": 9,
                "title": "Test",
                "actions": [
                    "Enter customer details.",
                    "Click Predict.",
                    "Verify the prediction.",
                    "Test multiple customer profiles."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "Could not convert TotalCharges",
                "fix": "Use pd.to_numeric(..., errors='coerce')."
            },
            {
                "error": "Unknown categorical value",
                "fix": "Use the same preprocessing pipeline during training and prediction."
            },
            {
                "error": "Model not found",
                "fix": "Train the model before starting Streamlit."
            }
        ],

        "final_checklist": [
            "Dataset added",
            "Data cleaned",
            "Categorical values encoded",
            "Model trained",
            "Evaluation completed",
            "Prediction UI created",
            "Churn prediction tested",
            "README created",
            "GitHub repository created"
        ]
    },


    # ============================================================
    # 4. CUSTOMER SEGMENTATION
    # ============================================================

    "Customer Segmentation": {
        "overview": """
Build an unsupervised machine learning application that groups
customers into different segments based on purchasing behavior.
""",
        "difficulty": "Intermediate",
        "estimated_time": "5–7 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "matplotlib",
            "seaborn",
            "streamlit",
            "joblib"
        ],

        "dataset": {
            "required": True,
            "name": "Mall Customers Dataset",
            "source": "Kaggle – Mall Customer Segmentation",
            "file": "Mall_Customers.csv",
            "placement": "data/Mall_Customers.csv"
        },

        "folder_structure": """
customer-segmentation/
│
├── data/
│   └── Mall_Customers.csv
│
├── outputs/
│   ├── customer_clusters.png
│   └── cluster_data.csv
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create project",
                "actions": [
                    "Create customer-segmentation.",
                    "Create data and outputs folders."
                ]
            },
            {
                "step": 2,
                "title": "Create virtual environment",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate"
                ]
            },
            {
                "step": 3,
                "title": "Install libraries",
                "commands": [
                    "pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib"
                ]
            },
            {
                "step": 4,
                "title": "Add dataset",
                "actions": [
                    "Download Mall_Customers.csv.",
                    "Place it inside data/."
                ]
            },
            {
                "step": 5,
                "title": "Prepare features",
                "actions": [
                    "Load the dataset.",
                    "Select Annual Income and Spending Score.",
                    "Scale the features if required."
                ]
            },
            {
                "step": 6,
                "title": "Create clusters",
                "actions": [
                    "Use K-Means clustering.",
                    "Try different K values.",
                    "Select a suitable number of clusters.",
                    "Save cluster assignments."
                ],
                "command": "python train_model.py"
            },
            {
                "step": 7,
                "title": "Create visualization",
                "actions": [
                    "Plot the customer clusters.",
                    "Save the plot inside outputs."
                ]
            },
            {
                "step": 8,
                "title": "Build Streamlit UI",
                "actions": [
                    "Allow the user to enter income and spending score.",
                    "Predict the customer's cluster.",
                    "Display the segment."
                ]
            },
            {
                "step": 9,
                "title": "Run",
                "command": "streamlit run app.py"
            }
        ],

        "common_errors": [
            {
                "error": "Wrong number of clusters",
                "fix": "Compare different K values using the elbow method."
            },
            {
                "error": "Column not found",
                "fix": "Check df.columns and use the exact dataset column names."
            }
        ],

        "final_checklist": [
            "Mall Customers dataset added",
            "Features selected",
            "K-Means model trained",
            "Clusters generated",
            "Visualization created",
            "Streamlit application created",
            "Cluster prediction tested",
            "README created",
            "GitHub repository created"
        ]
    },


    # ============================================================
    # 5. CREDIT CARD FRAUD DETECTION
    # ============================================================

    "Credit Card Fraud Detection": {
        "overview": """
Build a machine learning classification system that identifies
transactions that may be fraudulent.
""",
        "difficulty": "Advanced",
        "estimated_time": "6–8 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "matplotlib",
            "seaborn",
            "streamlit",
            "joblib"
        ],

        "dataset": {
            "required": True,
            "name": "Credit Card Fraud Detection Dataset",
            "source": "Kaggle Credit Card Fraud Detection",
            "file": "creditcard.csv",
            "placement": "data/creditcard.csv"
        },

        "folder_structure": """
credit-card-fraud-detection/
│
├── data/
│   └── creditcard.csv
│
├── model/
│   └── fraud_model.pkl
│
├── outputs/
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create project structure",
                "actions": [
                    "Create the project folder.",
                    "Create data, model and outputs folders."
                ]
            },
            {
                "step": 2,
                "title": "Set up Python",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate",
                    "pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib"
                ]
            },
            {
                "step": 3,
                "title": "Add dataset",
                "actions": [
                    "Download creditcard.csv.",
                    "Place it inside data/."
                ]
            },
            {
                "step": 4,
                "title": "Inspect dataset",
                "actions": [
                    "Check the number of rows.",
                    "Check fraud/non-fraud distribution.",
                    "Identify Class as the target."
                ]
            },
            {
                "step": 5,
                "title": "Prepare data",
                "actions": [
                    "Separate features and target.",
                    "Scale required numerical values.",
                    "Use a stratified train/test split."
                ]
            },
            {
                "step": 6,
                "title": "Train model",
                "actions": [
                    "Train a classification model.",
                    "Evaluate precision, recall and F1-score.",
                    "Save the trained model."
                ]
            },
            {
                "step": 7,
                "title": "Build Streamlit application",
                "actions": [
                    "Create transaction input fields.",
                    "Load the model.",
                    "Display fraud or legitimate prediction.",
                    "Display prediction probability."
                ]
            },
            {
                "step": 8,
                "title": "Run",
                "command": "streamlit run app.py"
            },
            {
                "step": 9,
                "title": "Test",
                "actions": [
                    "Test valid transaction values.",
                    "Verify that a prediction is generated.",
                    "Check that invalid input is handled safely."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "Model predicts almost everything as legitimate",
                "fix": "Check class imbalance and evaluate precision/recall."
            },
            {
                "error": "Application is slow",
                "fix": "Use a smaller development sample and optimize the final model."
            }
        ],

        "final_checklist": [
            "Dataset downloaded",
            "Class imbalance inspected",
            "Data preprocessing completed",
            "Model trained",
            "Precision and recall evaluated",
            "Model saved",
            "Streamlit UI created",
            "Prediction tested",
            "README created",
            "GitHub repository created"
        ]
    },


    # ============================================================
    # 6. LOAN APPROVAL PREDICTION
    # ============================================================

    "Loan Approval Prediction": {
        "overview": """
Build a machine learning application that predicts whether a loan
application is likely to be approved based on applicant information.
""",
        "difficulty": "Beginner",
        "estimated_time": "4–6 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "streamlit",
            "joblib"
        ],

        "dataset": {
            "required": True,
            "name": "Loan Approval Dataset",
            "source": "Public/Kaggle loan approval dataset",
            "file": "loan_data.csv",
            "placement": "data/loan_data.csv"
        },

        "folder_structure": """
loan-approval-prediction/
│
├── data/
│   └── loan_data.csv
│
├── model/
│   └── loan_model.pkl
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create folders",
                "actions": [
                    "Create the project directory.",
                    "Create data and model folders."
                ]
            },
            {
                "step": 2,
                "title": "Install libraries",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate",
                    "pip install pandas numpy scikit-learn streamlit joblib"
                ]
            },
            {
                "step": 3,
                "title": "Add dataset",
                "actions": [
                    "Download a loan approval dataset.",
                    "Place the CSV inside data/."
                ]
            },
            {
                "step": 4,
                "title": "Prepare data",
                "actions": [
                    "Load the dataset.",
                    "Handle missing values.",
                    "Encode categorical columns.",
                    "Separate target and input features."
                ]
            },
            {
                "step": 5,
                "title": "Train model",
                "actions": [
                    "Split the dataset.",
                    "Train a classification model.",
                    "Evaluate classification metrics.",
                    "Save the model."
                ]
            },
            {
                "step": 6,
                "title": "Create Streamlit app",
                "actions": [
                    "Create applicant input fields.",
                    "Load the saved model.",
                    "Display loan approval prediction."
                ]
            },
            {
                "step": 7,
                "title": "Run",
                "command": "streamlit run app.py"
            },
            {
                "step": 8,
                "title": "Test",
                "actions": [
                    "Enter applicant details.",
                    "Click Predict.",
                    "Verify the result."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "Categorical values cannot be converted",
                "fix": "Encode categorical features before training."
            },
            {
                "error": "Input shape mismatch",
                "fix": "Use exactly the same feature order during training and prediction."
            }
        ],

        "final_checklist": [
            "Dataset added",
            "Data cleaned",
            "Categorical values encoded",
            "Model trained",
            "Model evaluated",
            "Streamlit app created",
            "Prediction tested",
            "README created"
        ]
    },


    # ============================================================
    # 7. MOVIE RECOMMENDATION SYSTEM
    # ============================================================

    "Movie Recommendation System": {
        "overview": """
Build a content-based movie recommendation application that recommends
movies similar to a movie selected by the user.
""",
        "difficulty": "Intermediate",
        "estimated_time": "5–7 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "streamlit"
        ],

        "dataset": {
            "required": True,
            "name": "TMDB 5000 Movie Dataset",
            "source": "Kaggle / TMDB 5000 Movie Dataset",
            "files": [
                "tmdb_5000_movies.csv",
                "tmdb_5000_credits.csv"
            ],
            "placement": "data/"
        },

        "folder_structure": """
movie-recommendation-system/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── model/
│
├── train_model.py
├── recommender.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create project",
                "actions": [
                    "Create movie-recommendation-system.",
                    "Create data and model folders."
                ]
            },
            {
                "step": 2,
                "title": "Install libraries",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate",
                    "pip install pandas numpy scikit-learn streamlit"
                ]
            },
            {
                "step": 3,
                "title": "Download dataset",
                "actions": [
                    "Download TMDB 5000 Movie Dataset.",
                    "Place both CSV files inside data/."
                ]
            },
            {
                "step": 4,
                "title": "Create movie features",
                "actions": [
                    "Combine genres, keywords, cast and overview.",
                    "Clean the text.",
                    "Create a combined feature column."
                ]
            },
            {
                "step": 5,
                "title": "Create TF-IDF representation",
                "actions": [
                    "Use TfidfVectorizer.",
                    "Transform movie descriptions into vectors.",
                    "Calculate cosine similarity."
                ]
            },
            {
                "step": 6,
                "title": "Create recommendation function",
                "actions": [
                    "Accept a movie name.",
                    "Find its index.",
                    "Calculate similarity scores.",
                    "Sort scores.",
                    "Return top recommendations."
                ]
            },
            {
                "step": 7,
                "title": "Create Streamlit UI",
                "actions": [
                    "Create a movie selection box.",
                    "Add a Recommend button.",
                    "Display recommended movies."
                ]
            },
            {
                "step": 8,
                "title": "Run",
                "command": "streamlit run app.py"
            },
            {
                "step": 9,
                "title": "Test",
                "actions": [
                    "Select a movie.",
                    "Click Recommend.",
                    "Verify similar movies are displayed."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "Movie not found",
                "fix": "Use an exact title from the dataset."
            },
            {
                "error": "Similarity matrix takes too long",
                "fix": "Start with a smaller dataset or optimize vectorization."
            }
        ],

        "final_checklist": [
            "Movie dataset added",
            "Features created",
            "TF-IDF completed",
            "Cosine similarity implemented",
            "Recommendation function working",
            "Streamlit UI working",
            "Recommendations tested",
            "README created",
            "GitHub repository created"
        ]
    },


    # ============================================================
    # 8. BOOK RECOMMENDATION SYSTEM
    # ============================================================

    "Book Recommendation System": {
        "overview": """
Build a content-based book recommendation system that recommends
books similar to a book selected by the user.
""",
        "difficulty": "Intermediate",
        "estimated_time": "5–7 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "streamlit"
        ],

        "dataset": {
            "required": True,
            "name": "Books Dataset",
            "source": "Kaggle public books dataset",
            "file": "books.csv",
            "placement": "data/books.csv"
        },

        "folder_structure": """
book-recommendation-system/
│
├── data/
│   └── books.csv
│
├── model/
│
├── train_model.py
├── recommender.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create project",
                "actions": [
                    "Create book-recommendation-system.",
                    "Create data and model."
                ]
            },
            {
                "step": 2,
                "title": "Install libraries",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate",
                    "pip install pandas numpy scikit-learn streamlit"
                ]
            },
            {
                "step": 3,
                "title": "Add books dataset",
                "actions": [
                    "Download the selected books dataset.",
                    "Place books.csv inside data/."
                ]
            },
            {
                "step": 4,
                "title": "Prepare book features",
                "actions": [
                    "Load title, author, category and description where available.",
                    "Combine useful text fields.",
                    "Clean the combined text."
                ]
            },
            {
                "step": 5,
                "title": "Create recommendation model",
                "actions": [
                    "Convert book features using TF-IDF.",
                    "Calculate cosine similarity.",
                    "Create a recommendation function."
                ]
            },
            {
                "step": 6,
                "title": "Create Streamlit application",
                "actions": [
                    "Allow the user to select a book.",
                    "Display similar books."
                ]
            },
            {
                "step": 7,
                "title": "Run",
                "command": "streamlit run app.py"
            },
            {
                "step": 8,
                "title": "Test",
                "actions": [
                    "Select a known book.",
                    "Generate recommendations.",
                    "Verify recommendations are displayed."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "KeyError for a column",
                "fix": "Run print(df.columns) and use the actual column name."
            },
            {
                "error": "Book not found",
                "fix": "Select a title from the dataset."
            }
        ],

        "final_checklist": [
            "Dataset added",
            "Features prepared",
            "TF-IDF implemented",
            "Cosine similarity implemented",
            "Recommendations working",
            "Streamlit UI working",
            "Testing completed",
            "README created"
        ]
    },


    # ============================================================
    # 9. MUSIC RECOMMENDATION SYSTEM
    # ============================================================

    "Music Recommendation System": {
        "overview": """
Build a music recommendation application that recommends songs
similar to a selected song using audio or descriptive features.
""",
        "difficulty": "Intermediate",
        "estimated_time": "5–7 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "streamlit"
        ],

        "dataset": {
            "required": True,
            "name": "Spotify Songs Dataset",
            "source": "Kaggle public Spotify dataset",
            "file": "spotify_songs.csv",
            "placement": "data/spotify_songs.csv"
        },

        "folder_structure": """
music-recommendation-system/
│
├── data/
│   └── spotify_songs.csv
│
├── model/
│
├── train_model.py
├── recommender.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create project",
                "actions": [
                    "Create music-recommendation-system.",
                    "Create data and model folders."
                ]
            },
            {
                "step": 2,
                "title": "Install libraries",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate",
                    "pip install pandas numpy scikit-learn streamlit"
                ]
            },
            {
                "step": 3,
                "title": "Add Spotify dataset",
                "actions": [
                    "Download the Spotify songs dataset.",
                    "Place spotify_songs.csv inside data/."
                ]
            },
            {
                "step": 4,
                "title": "Select song features",
                "actions": [
                    "Use available numerical audio features.",
                    "Remove unnecessary columns.",
                    "Handle missing values."
                ]
            },
            {
                "step": 5,
                "title": "Create similarity model",
                "actions": [
                    "Scale numerical features.",
                    "Calculate cosine similarity.",
                    "Create a recommendation function."
                ]
            },
            {
                "step": 6,
                "title": "Build Streamlit UI",
                "actions": [
                    "Add song selection.",
                    "Add recommendation button.",
                    "Display recommended songs and artists."
                ]
            },
            {
                "step": 7,
                "title": "Run",
                "command": "streamlit run app.py"
            },
            {
                "step": 8,
                "title": "Test",
                "actions": [
                    "Select a song.",
                    "Generate recommendations.",
                    "Check that multiple recommendations appear."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "Missing feature columns",
                "fix": "Check the actual columns in spotify_songs.csv."
            },
            {
                "error": "NaN values",
                "fix": "Fill or remove missing numerical values before similarity calculation."
            }
        ],

        "final_checklist": [
            "Dataset added",
            "Features selected",
            "Features scaled",
            "Similarity calculated",
            "Recommendations generated",
            "Streamlit UI working",
            "Testing completed",
            "README created"
        ]
    },


    # ============================================================
    # 10. PERSONALIZED PROJECT RECOMMENDATION SYSTEM
    # ============================================================

    "Personalized Project Recommendation System": {
        "overview": """
Build a system that recommends academic or portfolio projects to a
student based on skills, interests, preferred domain, difficulty and
project type.
""",
        "difficulty": "Intermediate",
        "estimated_time": "6–8 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git",
            "Web browser"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "streamlit",
            "plotly"
        ],

        "dataset": {
            "required": True,
            "name": "Project Recommendation Dataset",
            "source": "Project dataset included with this academic project",
            "file": "project_dataset.csv",
            "placement": "data/project_dataset.csv"
        },

        "folder_structure": """
project-recommendation-system/
│
├── data/
│   └── project_dataset.csv
│
├── models/
├── outputs/
│
├── src/
│   ├── preprocessing.py
│   ├── recommender.py
│   └── evaluation.py
│
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create project structure",
                "actions": [
                    "Create data, models, outputs and src folders.",
                    "Create app.py."
                ]
            },
            {
                "step": 2,
                "title": "Create virtual environment",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate"
                ]
            },
            {
                "step": 3,
                "title": "Install libraries",
                "commands": [
                    "pip install pandas numpy scikit-learn streamlit plotly"
                ]
            },
            {
                "step": 4,
                "title": "Add project dataset",
                "actions": [
                    "Place project_dataset.csv inside data/.",
                    "Verify that pandas can read the CSV."
                ]
            },
            {
                "step": 5,
                "title": "Prepare project text",
                "actions": [
                    "Combine project name, domain, description, skills, project type and AI technique.",
                    "Clean the text.",
                    "Create TF-IDF vectors."
                ]
            },
            {
                "step": 6,
                "title": "Create recommendation engine",
                "actions": [
                    "Create a student profile.",
                    "Transform the profile using the fitted TF-IDF vectorizer.",
                    "Calculate cosine similarity.",
                    "Rank projects by similarity."
                ]
            },
            {
                "step": 7,
                "title": "Generate explanations",
                "actions": [
                    "Compare student skills with project skills.",
                    "Display matching skills.",
                    "Display match percentage."
                ]
            },
            {
                "step": 8,
                "title": "Build Streamlit UI",
                "actions": [
                    "Add student profile inputs.",
                    "Add recommendation button.",
                    "Display top projects.",
                    "Display match scores.",
                    "Display explanations."
                ]
            },
            {
                "step": 9,
                "title": "Add project roadmap",
                "actions": [
                    "Add a Start Project Roadmap button.",
                    "Show the practical project-building guide.",
                    "Display setup, dataset, folder structure, implementation and testing steps."
                ]
            },
            {
                "step": 10,
                "title": "Run",
                "command": "streamlit run app.py"
            },
            {
                "step": 11,
                "title": "Test",
                "actions": [
                    "Enter student skills.",
                    "Select interests.",
                    "Generate recommendations.",
                    "Check the top 5 results.",
                    "Open a project roadmap.",
                    "Verify that the roadmap is displayed correctly."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "TF-IDF matrix shape mismatch",
                "fix": "Use the same fitted vectorizer when transforming the student profile."
            },
            {
                "error": "No recommendations displayed",
                "fix": "Check the dataset path and recommendation function."
            },
            {
                "error": "Streamlit import error",
                "fix": "Activate venv and install streamlit."
            }
        ],

        "final_checklist": [
            "Dataset loaded",
            "Text preprocessing completed",
            "TF-IDF implemented",
            "Cosine similarity implemented",
            "Recommendations generated",
            "Match scores displayed",
            "Explanation generated",
            "Roadmap feature added",
            "Streamlit application tested",
            "Evaluation completed",
            "README created",
            "GitHub repository created"
        ]
    }
}


# ================================================================
# PROJECT-SPECIFIC ROADMAP INFORMATION
# ================================================================
#
# The following projects use a practical roadmap generator.
# This keeps the file maintainable while still giving every
# recommended project its own build instructions.
# ================================================================

PROJECT_CONFIGS = {

    # ------------------------------------------------------------
    # MACHINE LEARNING
    # ------------------------------------------------------------

    "Credit Card Fraud Detection": {
        "domain": "Machine Learning",
        "goal": "Classify transactions as legitimate or potentially fraudulent.",
        "dataset": "creditcard.csv",
        "dataset_location": "data/creditcard.csv",
        "model": "Random Forest / Logistic Regression",
        "target": "Class",
        "output": "Fraud or legitimate transaction prediction"
    },

    "Loan Approval Prediction": {
        "domain": "Machine Learning",
        "goal": "Predict whether a loan application is likely to be approved.",
        "dataset": "loan_data.csv",
        "dataset_location": "data/loan_data.csv",
        "model": "Logistic Regression / Random Forest",
        "target": "Loan approval status",
        "output": "Approved or rejected prediction"
    },

    "Disease Prediction System": {
        "domain": "Machine Learning",
        "goal": "Predict a possible disease category from structured health-related features.",
        "dataset": "disease_prediction.csv",
        "dataset_location": "data/disease_prediction.csv",
        "model": "Random Forest",
        "target": "Disease",
        "output": "Predicted disease category"
    },

    "Diabetes Prediction System": {
        "domain": "Machine Learning",
        "goal": "Build a classification model that predicts diabetes risk from dataset features.",
        "dataset": "diabetes.csv",
        "dataset_location": "data/diabetes.csv",
        "model": "Logistic Regression / Random Forest",
        "target": "Outcome",
        "output": "Prediction result"
    },

    "Heart Disease Prediction": {
        "domain": "Machine Learning",
        "goal": "Predict the presence of heart disease using structured features.",
        "dataset": "heart.csv",
        "dataset_location": "data/heart.csv",
        "model": "Logistic Regression / Random Forest",
        "target": "Target",
        "output": "Prediction result"
    },

    "Project Difficulty Predictor": {
        "domain": "Machine Learning",
        "goal": "Predict whether a project is beginner, intermediate or advanced.",
        "dataset": "project_dataset.csv",
        "dataset_location": "data/project_dataset.csv",
        "model": "Decision Tree / Random Forest",
        "target": "Difficulty",
        "output": "Predicted project difficulty"
    },


    # ------------------------------------------------------------
    # RECOMMENDER SYSTEMS
    # ------------------------------------------------------------

    "News Recommendation System": {
        "domain": "Recommender Systems",
        "goal": "Recommend news articles based on article content.",
        "dataset": "news.csv",
        "dataset_location": "data/news.csv",
        "model": "TF-IDF + Cosine Similarity",
        "target": "Article similarity",
        "output": "Top recommended news articles"
    },

    "Course Recommendation System": {
        "domain": "Recommender Systems",
        "goal": "Recommend courses based on student skills and interests.",
        "dataset": "courses.csv",
        "dataset_location": "data/courses.csv",
        "model": "TF-IDF + Cosine Similarity",
        "target": "Course similarity",
        "output": "Recommended courses"
    },

    "Job Recommendation System": {
        "domain": "Recommender Systems",
        "goal": "Recommend jobs based on skills and interests.",
        "dataset": "jobs.csv",
        "dataset_location": "data/jobs.csv",
        "model": "TF-IDF + Cosine Similarity",
        "target": "Job similarity",
        "output": "Recommended jobs"
    },

    "Internship Recommendation System": {
        "domain": "Recommender Systems",
        "goal": "Recommend internships based on student skills and preferred domain.",
        "dataset": "internships.csv",
        "dataset_location": "data/internships.csv",
        "model": "TF-IDF + Cosine Similarity",
        "target": "Internship similarity",
        "output": "Recommended internships"
    },

    "Hackathon Recommendation System": {
        "domain": "Recommender Systems",
        "goal": "Recommend hackathons based on skills and project interests.",
        "dataset": "hackathons.csv",
        "dataset_location": "data/hackathons.csv",
        "model": "TF-IDF + Cosine Similarity",
        "target": "Hackathon similarity",
        "output": "Recommended hackathons"
    },

    "Personalized Study Material Recommendation": {
        "domain": "Recommender Systems",
        "goal": "Recommend study resources based on topic and student interests.",
        "dataset": "study_material.csv",
        "dataset_location": "data/study_material.csv",
        "model": "TF-IDF + Cosine Similarity",
        "target": "Material similarity",
        "output": "Recommended study resources"
    },


    # ------------------------------------------------------------
    # NLP
    # ------------------------------------------------------------

    "Email Spam Detection": {
        "domain": "Natural Language Processing",
        "goal": "Classify messages as spam or legitimate.",
        "dataset": "spam.csv",
        "dataset_location": "data/spam.csv",
        "model": "TF-IDF + Logistic Regression",
        "target": "Spam label",
        "output": "Spam / Not Spam"
    },

    "Sentiment Analysis System": {
        "domain": "Natural Language Processing",
        "goal": "Classify text into positive, negative or neutral sentiment.",
        "dataset": "sentiment.csv",
        "dataset_location": "data/sentiment.csv",
        "model": "TF-IDF + Logistic Regression",
        "target": "Sentiment",
        "output": "Sentiment prediction"
    },

    "Fake News Detection": {
        "domain": "Natural Language Processing",
        "goal": "Classify news articles as real or potentially fake.",
        "dataset": "news.csv",
        "dataset_location": "data/news.csv",
        "model": "TF-IDF + Logistic Regression",
        "target": "Label",
        "output": "Real / Fake prediction"
    },

    "Resume Screening System": {
        "domain": "Natural Language Processing",
        "goal": "Match resumes with job descriptions.",
        "dataset": "resumes.csv",
        "dataset_location": "data/resumes.csv",
        "model": "TF-IDF + Cosine Similarity",
        "target": "Resume-job similarity",
        "output": "Candidate match score"
    },

    "Text Summarization System": {
        "domain": "Natural Language Processing",
        "goal": "Create a system that produces a shorter version of input text.",
        "dataset": "articles.csv",
        "dataset_location": "data/articles.csv",
        "model": "Extractive text summarization",
        "target": "Summary",
        "output": "Generated summary"
    },

    "Customer Review Analyzer": {
        "domain": "Natural Language Processing",
        "goal": "Analyze customer reviews and identify sentiment.",
        "dataset": "reviews.csv",
        "dataset_location": "data/reviews.csv",
        "model": "TF-IDF + Logistic Regression",
        "target": "Sentiment",
        "output": "Review sentiment"
    },


    # ------------------------------------------------------------
    # ARTIFICIAL INTELLIGENCE
    # ------------------------------------------------------------

    "College Enquiry Chatbot": {
        "domain": "Artificial Intelligence",
        "goal": "Build a chatbot that answers common college-related questions.",
        "dataset": "college_faq.json",
        "dataset_location": "data/college_faq.json",
        "model": "Intent matching / TF-IDF",
        "target": "FAQ response",
        "output": "Chatbot response"
    },

    "AI Career Guidance System": {
        "domain": "Artificial Intelligence",
        "goal": "Recommend career directions based on skills and interests.",
        "dataset": "career_data.csv",
        "dataset_location": "data/career_data.csv",
        "model": "Content-based recommendation",
        "target": "Career match",
        "output": "Career recommendations"
    },

    "Student Skill Gap Analyzer": {
        "domain": "Artificial Intelligence",
        "goal": "Compare current student skills with required skills for a target role.",
        "dataset": "skills.csv",
        "dataset_location": "data/skills.csv",
        "model": "Skill matching",
        "target": "Skill gap",
        "output": "Missing skill list"
    },

    "AI Interview Question Generator": {
        "domain": "Artificial Intelligence",
        "goal": "Generate interview questions based on selected skills and role.",
        "dataset": "interview_questions.csv",
        "dataset_location": "data/interview_questions.csv",
        "model": "Template-based generation",
        "target": "Questions",
        "output": "Interview question list"
    },

    "Skill-Based Team Formation": {
        "domain": "Artificial Intelligence",
        "goal": "Create balanced teams based on participant skills.",
        "dataset": "participants.csv",
        "dataset_location": "data/participants.csv",
        "model": "Clustering / matching",
        "target": "Team assignment",
        "output": "Generated teams"
    },

    "Learning Path Recommendation System": {
        "domain": "Artificial Intelligence",
        "goal": "Recommend a practical learning sequence based on the student's current skills.",
        "dataset": "learning_paths.csv",
        "dataset_location": "data/learning_paths.csv",
        "model": "Content-based recommendation",
        "target": "Learning path",
        "output": "Recommended project path"
    },

    "AI Expense Tracker": {
        "domain": "Artificial Intelligence",
        "goal": "Create an expense tracking application that categorizes spending.",
        "dataset": "expenses.csv",
        "dataset_location": "data/expenses.csv",
        "model": "Rule-based categorization / classification",
        "target": "Expense category",
        "output": "Expense category and summary"
    },

    "Personal Finance Recommendation System": {
        "domain": "Artificial Intelligence",
        "goal": "Recommend simple financial actions from categorized expense data.",
        "dataset": "expenses.csv",
        "dataset_location": "data/expenses.csv",
        "model": "Rule-based recommendation",
        "target": "Recommendation",
        "output": "Personalized suggestions"
    },

    "Smart Agriculture Recommendation System": {
        "domain": "Artificial Intelligence",
        "goal": "Recommend suitable crops or farming actions from agricultural features.",
        "dataset": "crop_data.csv",
        "dataset_location": "data/crop_data.csv",
        "model": "Random Forest",
        "target": "Crop",
        "output": "Crop recommendation"
    },

    "AI Project Idea Generator": {
        "domain": "Artificial Intelligence",
        "goal": "Generate project ideas based on domain, skills and difficulty.",
        "dataset": "project_dataset.csv",
        "dataset_location": "data/project_dataset.csv",
        "model": "Content-based recommendation",
        "target": "Project idea",
        "output": "Generated project ideas"
    },


    # ------------------------------------------------------------
    # DATA SCIENCE
    # ------------------------------------------------------------

    "Weather Prediction System": {
        "domain": "Data Science",
        "goal": "Predict a weather-related value using historical weather data.",
        "dataset": "weather.csv",
        "dataset_location": "data/weather.csv",
        "model": "Random Forest / Linear Regression",
        "target": "Weather variable",
        "output": "Weather prediction"
    },

    "Stock Price Prediction": {
        "domain": "Data Science",
        "goal": "Build a model that estimates future stock-related values from historical data.",
        "dataset": "stock_data.csv",
        "dataset_location": "data/stock_data.csv",
        "model": "Regression",
        "target": "Closing price",
        "output": "Estimated price"
    },

    "Sales Forecasting System": {
        "domain": "Data Science",
        "goal": "Forecast future sales using historical sales records.",
        "dataset": "sales.csv",
        "dataset_location": "data/sales.csv",
        "model": "Time-series regression",
        "target": "Sales",
        "output": "Sales forecast"
    },

    "Retail Sales Analysis": {
        "domain": "Data Science",
        "goal": "Analyze retail sales and identify important sales patterns.",
        "dataset": "retail_sales.csv",
        "dataset_location": "data/retail_sales.csv",
        "model": "Data analysis",
        "target": "Sales metrics",
        "output": "Charts and business insights"
    },

    "COVID-19 Data Analysis": {
        "domain": "Data Science",
        "goal": "Analyze historical COVID-19 data and visualize trends.",
        "dataset": "covid_data.csv",
        "dataset_location": "data/covid_data.csv",
        "model": "Data analysis",
        "target": "Cases/deaths/recovery",
        "output": "Trend dashboard"
    },

    "Air Quality Prediction": {
        "domain": "Data Science",
        "goal": "Predict air quality from environmental measurements.",
        "dataset": "air_quality.csv",
        "dataset_location": "data/air_quality.csv",
        "model": "Random Forest Regression",
        "target": "Air quality value",
        "output": "Air quality prediction"
    },

    "Energy Consumption Prediction": {
        "domain": "Data Science",
        "goal": "Predict energy consumption from historical measurements.",
        "dataset": "energy.csv",
        "dataset_location": "data/energy.csv",
        "model": "Random Forest Regression",
        "target": "Energy consumption",
        "output": "Energy prediction"
    },


    # ------------------------------------------------------------
    # COMPUTER VISION
    # ------------------------------------------------------------

    "Face Mask Detection": {
        "domain": "Computer Vision",
        "goal": "Classify images as mask or no-mask.",
        "dataset": "face_mask_dataset/",
        "dataset_location": "data/face_mask_dataset/",
        "model": "CNN / Transfer Learning",
        "target": "Mask class",
        "output": "Mask detection"
    },

    "Cats and Dogs Classification": {
        "domain": "Computer Vision",
        "goal": "Classify an image as a cat or dog.",
        "dataset": "cats_vs_dogs/",
        "dataset_location": "data/cats_vs_dogs/",
        "model": "CNN / SVM",
        "target": "Animal class",
        "output": "Cat or dog"
    },

    "Hand Gesture Recognition": {
        "domain": "Computer Vision",
        "goal": "Recognize predefined hand gestures from images.",
        "dataset": "gesture_dataset/",
        "dataset_location": "data/gesture_dataset/",
        "model": "CNN",
        "target": "Gesture",
        "output": "Detected gesture"
    },

    "Food Image Classification": {
        "domain": "Computer Vision",
        "goal": "Classify food images into food categories.",
        "dataset": "Food-101",
        "dataset_location": "data/food101/",
        "model": "CNN / Transfer Learning",
        "target": "Food class",
        "output": "Food category"
    },

    "Plant Disease Detection": {
        "domain": "Computer Vision",
        "goal": "Identify plant diseases from leaf images.",
        "dataset": "PlantVillage",
        "dataset_location": "data/plantvillage/",
        "model": "CNN / Transfer Learning",
        "target": "Disease class",
        "output": "Plant disease"
    },

    "Traffic Sign Recognition": {
        "domain": "Computer Vision",
        "goal": "Recognize traffic signs from images.",
        "dataset": "GTSRB",
        "dataset_location": "data/gtsrb/",
        "model": "CNN",
        "target": "Traffic sign",
        "output": "Recognized sign"
    },

    "Object Detection System": {
        "domain": "Computer Vision",
        "goal": "Detect objects in images.",
        "dataset": "COCO or a custom object dataset",
        "dataset_location": "data/object_dataset/",
        "model": "YOLO",
        "target": "Object classes",
        "output": "Detected objects with bounding boxes"
    },

    "Face Recognition Attendance System": {
        "domain": "Computer Vision",
        "goal": "Recognize registered faces and record attendance.",
        "dataset": "Custom face images",
        "dataset_location": "data/faces/",
        "model": "Face embeddings",
        "target": "Person identity",
        "output": "Attendance record"
    },

    "Vehicle Detection System": {
        "domain": "Computer Vision",
        "goal": "Detect vehicles in images or video.",
        "dataset": "Vehicle detection dataset",
        "dataset_location": "data/vehicles/",
        "model": "YOLO",
        "target": "Vehicle class",
        "output": "Detected vehicles"
    },

    "Handwritten Digit Recognition": {
        "domain": "Computer Vision",
        "goal": "Recognize handwritten digits from images.",
        "dataset": "MNIST",
        "dataset_location": "data/mnist/",
        "model": "CNN",
        "target": "Digit",
        "output": "Predicted digit"
    },

    "Object Tracking System": {
        "domain": "Computer Vision",
        "goal": "Track an object across video frames.",
        "dataset": "Sample video",
        "dataset_location": "data/videos/",
        "model": "OpenCV tracking",
        "target": "Object position",
        "output": "Tracked object"
    },

    "OCR Document Scanner": {
        "domain": "Computer Vision",
        "goal": "Extract text from document images.",
        "dataset": "Sample document images",
        "dataset_location": "data/documents/",
        "model": "OCR",
        "target": "Extracted text",
        "output": "Digital text"
    },

    "Crop Disease Classification": {
        "domain": "Computer Vision",
        "goal": "Classify crop disease from leaf images.",
        "dataset": "Plant disease image dataset",
        "dataset_location": "data/crop_disease/",
        "model": "CNN / Transfer Learning",
        "target": "Disease class",
        "output": "Disease prediction"
    },

    "Smart Parking Detection": {
        "domain": "Computer Vision",
        "goal": "Detect available and occupied parking spaces.",
        "dataset": "Parking lot images",
        "dataset_location": "data/parking/",
        "model": "OpenCV / YOLO",
        "target": "Parking status",
        "output": "Available parking spaces"
    },

    "Traffic Density Analysis": {
        "domain": "Computer Vision",
        "goal": "Estimate traffic density from road images or video.",
        "dataset": "Traffic video/images",
        "dataset_location": "data/traffic/",
        "model": "YOLO + OpenCV",
        "target": "Vehicle count",
        "output": "Traffic density"
    }
}


# ================================================================
# ROADMAP GENERATOR
# ================================================================

def create_generated_roadmap(project_name):
    """
    Create a practical roadmap for projects that do not yet have
    a manually written roadmap.
    """

    config = PROJECT_CONFIGS.get(project_name)

    if config is None:
        return {
            "overview": f"""
Build the project:

{project_name}

The project should be implemented as a practical working application.
Follow each step in order and test the result before moving forward.
""",

            "difficulty": "Intermediate",
            "estimated_time": "5–8 hours",

            "requirements": [
                "Python 3.12",
                "VS Code",
                "Git",
                "Web browser"
            ],

            "libraries": [
                "pandas",
                "numpy",
                "scikit-learn",
                "streamlit",
                "joblib"
            ],

            "dataset": {
                "required": True,
                "name": "Project-specific dataset",
                "source": "Use the dataset appropriate for this project.",
                "file": "project_data.csv",
                "placement": "data/project_data.csv"
            },

            "folder_structure": f"""
{project_name.lower().replace(" ", "-")}/
│
├── data/
├── model/
├── outputs/
├── src/
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

            "steps": [
                {
                    "step": 1,
                    "title": "Create project folder",
                    "actions": [
                        f"Create a folder named {project_name.lower().replace(' ', '-')}.",
                        "Open the folder in VS Code.",
                        "Create data, model, outputs and src folders."
                    ]
                },
                {
                    "step": 2,
                    "title": "Create Python environment",
                    "commands": [
                        "python -m venv venv",
                        "venv\\Scripts\\activate"
                    ],
                    "expected": "The terminal shows (venv)."
                },
                {
                    "step": 3,
                    "title": "Install libraries",
                    "commands": [
                        "pip install pandas numpy scikit-learn streamlit joblib"
                    ]
                },
                {
                    "step": 4,
                    "title": "Download and place dataset",
                    "actions": [
                        "Download the dataset required for the project.",
                        "Place the dataset inside data/.",
                        "Verify that Python can read the dataset."
                    ]
                },
                {
                    "step": 5,
                    "title": "Prepare the dataset",
                    "actions": [
                        "Load the dataset.",
                        "Inspect columns.",
                        "Handle missing values.",
                        "Select the required features.",
                        "Prepare the target when applicable."
                    ]
                },
                {
                    "step": 6,
                    "title": "Implement the main project logic",
                    "actions": [
                        f"Implement the main functionality required for {project_name}.",
                        f"Use {config['model'] if config else 'an appropriate model or algorithm'}.",
                        "Save the trained model or generated output."
                    ],
                    "command": "python train_model.py"
                },
                {
                    "step": 7,
                    "title": "Create the Streamlit application",
                    "actions": [
                        "Create app.py.",
                        "Add input controls.",
                        "Load the model or project logic.",
                        "Display the result clearly."
                    ]
                },
                {
                    "step": 8,
                    "title": "Run the application",
                    "command": "streamlit run app.py",
                    "expected": f"The {project_name} application opens in the browser."
                },
                {
                    "step": 9,
                    "title": "Test the project",
                    "actions": [
                        "Test normal inputs.",
                        "Test multiple examples.",
                        "Test invalid or empty inputs.",
                        "Fix errors before continuing."
                    ]
                },
                {
                    "step": 10,
                    "title": "Complete the project",
                    "actions": [
                        "Create requirements.txt.",
                        "Create README.md.",
                        "Add screenshots.",
                        "Test the final application.",
                        "Upload the project to GitHub."
                    ]
                }
            ],

            "common_errors": [
                {
                    "error": "ModuleNotFoundError",
                    "fix": "Activate venv and install the missing package."
                },
                {
                    "error": "FileNotFoundError",
                    "fix": "Check the dataset location and folder structure."
                },
                {
                    "error": "Column not found",
                    "fix": "Print df.columns and use the exact dataset column name."
                },
                {
                    "error": "Application does not start",
                    "fix": "Read the first error shown in the terminal and fix that error first."
                }
            ],

            "final_checklist": [
                "Project folder created",
                "Virtual environment created",
                "Libraries installed",
                "Dataset added",
                "Dataset preprocessing completed",
                "Main functionality implemented",
                "Application created",
                "Application tested",
                "README created",
                "GitHub repository created"
            ]
        }

    return {
        "overview": f"""
{config["goal"]}

Build the project as a complete working application rather than
stopping after model training. Follow every step in order.
""",

        "difficulty": "Intermediate",
        "estimated_time": "5–8 hours",

        "requirements": [
            "Python 3.12",
            "VS Code",
            "Git",
            "Web browser"
        ],

        "libraries": [
            "pandas",
            "numpy",
            "scikit-learn",
            "streamlit",
            "joblib"
        ],

        "dataset": {
            "required": True,
            "name": config["dataset"],
            "source": "Use the public dataset specified for this project.",
            "file": config["dataset"],
            "placement": config["dataset_location"]
        },

        "folder_structure": f"""
{project_name.lower().replace(" ", "-")}/
│
├── data/
│   └── {config["dataset"]}
│
├── model/
│
├── outputs/
│
├── src/
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
""",

        "steps": [
            {
                "step": 1,
                "title": "Create the project folder",
                "actions": [
                    f"Create a folder named {project_name.lower().replace(' ', '-')}.",
                    "Open the folder in VS Code.",
                    "Create data, model, outputs and src folders."
                ]
            },

            {
                "step": 2,
                "title": "Create virtual environment",
                "commands": [
                    "python -m venv venv",
                    "venv\\Scripts\\activate"
                ],
                "expected": "The terminal should show (venv)."
            },

            {
                "step": 3,
                "title": "Install required libraries",
                "commands": [
                    "pip install pandas numpy scikit-learn streamlit joblib"
                ]
            },

            {
                "step": 4,
                "title": "Download the dataset",
                "actions": [
                    f"Download the dataset required for {project_name}.",
                    f"Place it at {config['dataset_location']}.",
                    "Open the CSV or dataset and verify that it contains the required information."
                ],
                "expected": f"The dataset is available at {config['dataset_location']}."
            },

            {
                "step": 5,
                "title": "Prepare the data",
                "actions": [
                    "Create train_model.py.",
                    "Load the dataset using pandas.",
                    "Inspect the columns.",
                    "Handle missing values.",
                    "Select the required features.",
                    f"Use {config['target']} as the main target/output where applicable."
                ]
            },

            {
                "step": 6,
                "title": "Implement the main model or algorithm",
                "actions": [
                    f"Implement {config['model']}.",
                    "Split the data when supervised learning is required.",
                    "Train the model or calculate the required similarity.",
                    "Evaluate the result.",
                    "Save the model when required."
                ],
                "command": "python train_model.py"
            },

            {
                "step": 7,
                "title": "Create the Streamlit application",
                "actions": [
                    "Create app.py.",
                    "Create user input controls.",
                    "Load the trained model or project logic.",
                    "Connect the input to the project.",
                    f"Display the final {config['output']}."
                ]
            },

            {
                "step": 8,
                "title": "Run the application",
                "command": "streamlit run app.py",
                "expected": f"The {project_name} application opens in the browser."
            },

            {
                "step": 9,
                "title": "Test the application",
                "actions": [
                    "Enter valid sample input.",
                    "Generate the result.",
                    "Try multiple inputs.",
                    "Test empty or invalid input.",
                    "Confirm that the application does not crash."
                ]
            },

            {
                "step": 10,
                "title": "Complete the project",
                "actions": [
                    "Create requirements.txt.",
                    "Create README.md.",
                    "Add screenshots.",
                    "Document how to run the project.",
                    "Upload the project to GitHub."
                ]
            }
        ],

        "common_errors": [
            {
                "error": "ModuleNotFoundError",
                "fix": "Activate venv and install the missing library."
            },
            {
                "error": "FileNotFoundError",
                "fix": f"Check that the dataset exists at {config['dataset_location']}."
            },
            {
                "error": "Column not found",
                "fix": "Run print(df.columns) and use the exact column names."
            },
            {
                "error": "Input shape mismatch",
                "fix": "Use the exact same features and order during training and prediction."
            },
            {
                "error": "Streamlit application does not start",
                "fix": "Check the first error shown in the terminal and fix that error before continuing."
            }
        ],

        "final_checklist": [
            "Project folder created",
            "Virtual environment created",
            "Libraries installed",
            "Dataset downloaded",
            "Dataset placed correctly",
            "Data preprocessing completed",
            "Main model or algorithm implemented",
            "Model/output tested",
            "Streamlit application created",
            "Application tested",
            "README created",
            "requirements.txt created",
            "GitHub repository created"
        ]
    }


# ================================================================
# GET ROADMAP
# ================================================================

def get_roadmap(project_name):
    """
    Return the manually written roadmap if available.
    Otherwise generate a project-specific practical roadmap.
    """

    if project_name in PROJECT_ROADMAPS:
        return PROJECT_ROADMAPS[project_name]

    return create_generated_roadmap(project_name)


# ================================================================
# TEST
# ================================================================

if __name__ == "__main__":

    print("=" * 60)
    print("PROJECT ROADMAP SYSTEM")
    print("=" * 60)

    print("Detailed roadmaps:", len(PROJECT_ROADMAPS))
    print("Project configurations:", len(PROJECT_CONFIGS))

    test_projects = [
        "House Price Prediction",
        "Customer Churn Prediction",
        "Email Spam Detection",
        "Face Mask Detection",
        "Weather Prediction System",
        "Job Recommendation System"
    ]

    print("\nTesting roadmaps...\n")

    for project in test_projects:

        roadmap = get_roadmap(project)

        print(f"✓ {project}")
        print(f"  Difficulty: {roadmap['difficulty']}")
        print(f"  Steps: {len(roadmap['steps'])}")

    print("\nRoadmap system test completed successfully.")