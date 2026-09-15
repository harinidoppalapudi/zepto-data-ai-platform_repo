# Zepto Data & AI Platform

An end-to-end Artificial Intelligence and Machine Learning capstone project covering **data engineering, exploratory data analysis, predictive modeling, and a grounded Generative AI support assistant**.

The project is organized as one connected repository containing three major capabilities:

1. **Data Pipeline** — Scrape, clean, transform, store, and query catalog data.
2. **Analytics Pipeline** — Perform EDA, statistical analysis, predictive modeling, model evaluation, tuning, and regression.
3. **GenAI Support Assistant** — Build a document-grounded RAG assistant using embeddings, ChromaDB, LangGraph, Pydantic, and FastAPI.

---

## 📌 Project Overview

The objective of this project is to demonstrate a complete AI/ML engineering workflow:

```text
                ┌─────────────────────────┐
                │     Raw External Data   │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │    Data Engineering     │
                │ Scrape → Clean → Store  │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │     SQLite Database     │
                │   SQL + Pandas Queries  │
                └─────────────────────────┘


                ┌─────────────────────────┐
                │     Titanic Dataset     │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ EDA & Data Preparation  │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Predictive Modeling     │
                │ LR / DT / Random Forest │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Model Evaluation &      │
                │ Hyperparameter Tuning   │
                └─────────────────────────┘


                ┌─────────────────────────┐
                │   Zepto Policy Docs     │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Chunking & Embeddings   │
                │ Sentence Transformers   │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │       ChromaDB          │
                │   Vector Database       │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │      LangGraph          │
                │ Intent → Retrieval →    │
                │ Answer                  │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │       FastAPI           │
                │       POST /ask         │
                └─────────────────────────┘
```

---

# 📂 Repository Structure

```text
zepto-data-ai-platform/
│
├── README.md
├── .gitignore
│
├── data_pipeline/
│   ├── scraper.py
│   ├── database.py
│   ├── queries.py
│   ├── main.py
│   ├── requirements.txt
│   ├── zepto_catalog.db
│   ├── outputs/
│   │   ├── scraped_data.csv
│   │   └── query_results/
│   └── README.md
│
├── analytics/
│   ├── 01_eda.ipynb
│   ├── 02_modeling.ipynb
│   ├── titanic.csv
│   ├── requirements.txt
│   ├── outputs/
│   │   ├── charts/
│   │   ├── model_results/
│   │   └── residuals/
│   ├── models/
│   │   └── best_pipeline.joblib
│   └── README.md
│
└── support_assistant/
    ├── main.py
    ├── graph.py
    ├── rag.py
    ├── schemas.py
    ├── prompts.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docs/
    │   ├── doc_01.txt
    │   ├── doc_02.txt
    │   ├── doc_03.txt
    │   ├── doc_04.txt
    │   ├── doc_05.txt
    │   ├── doc_06.txt
    │   ├── doc_07.txt
    │   └── doc_08.txt
    └── README.md
```

> The exact filenames may differ depending on the implementation. The important requirement is that all three modules remain inside this **single repository**.

---

# 🛠️ Technologies Used

## Data Engineering

* Python
* Requests
* BeautifulSoup
* Pandas
* SQLite
* SQL
* `sqlite3`

## Data Analytics & Machine Learning

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn
* SMOTE
* GridSearchCV
* Joblib
* Jupyter Notebook

## Generative AI / RAG

* Python
* Sentence Transformers
* `all-MiniLM-L6-v2`
* ChromaDB
* LangGraph
* Pydantic
* FastAPI
* Uvicorn
* Docker

---

# 📦 Installation

Each module contains its own `requirements.txt`.

Therefore, dependencies are installed separately for each module.

---

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd zepto-data-ai-platform
```

---

# 🔹 Module 1 — Data Pipeline

## Objective

Build an end-to-end data engineering pipeline that:

```text
Website
   ↓
Web Scraping
   ↓
Data Cleaning
   ↓
Currency Conversion
   ↓
SQLite Database
   ↓
SQL Queries
   ↓
Pandas Analysis
```

The data source is **Books to Scrape**, a public website designed for scraping practice.

The pipeline collects book information from at least three categories and produces at least 60 records.

---

## Data Collected

The following fields are collected:

| Field          | Description       |
| -------------- | ----------------- |
| `title`        | Book title        |
| `price`        | Original price    |
| `star_rating`  | Rating as text    |
| `availability` | Availability text |
| `category`     | Book category     |

These fields are then transformed into:

| Field       | Type    |
| ----------- | ------- |
| `price_gbp` | Float   |
| `rating`    | Integer |
| `in_stock`  | Boolean |
| `price_inr` | Float   |

---

## Currency Conversion

The project uses the required fixed conversion rate:

```text
1 GBP = 105.50 INR
```

This is a project-defined fixed baseline and does not require an external currency API.

The conversion is:

```python
price_inr = price_gbp * 105.50
```

---

## Database Design

The database uses a normalized relational structure.

### Categories

```text
categories
--------------------------------
category_id       PRIMARY KEY
category_name     UNIQUE
```

### Books

```text
books
--------------------------------
book_id           PRIMARY KEY
title
price_gbp
price_inr
rating
in_stock
category_id       FOREIGN KEY
```

Relationship:

```text
categories
     │
     │ 1
     │
     │ N
     ▼
   books
```

---

## Running Module 1

Navigate to the module:

```bash
cd data_pipeline
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python main.py
```

The pipeline will:

1. Scrape the required categories.
2. Clean the raw data.
3. Convert prices from GBP to INR.
4. Create the SQLite database.
5. Populate the normalized tables.
6. Execute the required SQL queries.
7. Save/query results using pandas.

---

## SQL Analysis

The project includes SQL queries demonstrating:

* `SELECT`
* `WHERE`
* `ORDER BY`
* `LIMIT`
* `DISTINCT`
* `IN` or `BETWEEN`
* `JOIN`

Example:

```sql
SELECT
    b.title,
    b.price_gbp,
    b.rating,
    c.category_name
FROM books b
JOIN categories c
    ON b.category_id = c.category_id
ORDER BY b.rating DESC
LIMIT 10;
```

The project also demonstrates reading SQL results into pandas using:

```python
pd.read_sql(...)
```

and reproducing the join using:

```python
pd.merge(...)
```

---

# 🔹 Module 2 — Analytics Pipeline

## Objective

The analytics module demonstrates a complete data science workflow using the Titanic dataset:

```text
Load Dataset
     ↓
Data Profiling
     ↓
Missing Value Analysis
     ↓
Data Cleaning
     ↓
EDA
     ↓
Feature Analysis
     ↓
Train/Test Split
     ↓
Preprocessing
     ↓
Classification Models
     ↓
Model Evaluation
     ↓
Imbalance Analysis
     ↓
Hyperparameter Tuning
     ↓
Regression
     ↓
Final Model
     ↓
Save Pipeline
```

---

# Dataset

The Titanic dataset is initially loaded using:

```python
sns.load_dataset("titanic")
```

The loaded dataset is immediately saved as:

```text
analytics/titanic.csv
```

This CSV acts as the offline fallback so that the project can be executed without downloading the dataset again.

The modeling notebook uses this same saved dataset rather than independently loading the Titanic dataset again.

---

# Exploratory Data Analysis

The EDA includes:

### Dataset Profiling

```python
df.info()
df.describe()
df.shape
```

Missing-value percentages are calculated for columns containing missing values.

---

## Missing Value Strategy

The project follows the required threshold:

| Missing Percentage | Strategy                                                        |
| -----------------: | --------------------------------------------------------------- |
|               < 5% | Drop rows                                                       |
|           5% – 30% | Impute                                                          |
|              > 30% | Drop column or encode missing as a category, with justification |

The exact missing-value percentages and selected strategies are documented in the EDA notebook.

---

# Univariate Analysis

The following variables are analyzed:

* `age`
* `fare`

For each variable, the project includes:

* Histogram
* Box plot
* IQR-based outlier analysis

For `fare`, the following are calculated:

```text
Mean
Median
Mode
```

The distribution is classified as:

```text
Right-skewed / Left-skewed / Approximately symmetric
```

based on the relationship between mean, median, and mode.

---

# Bivariate Analysis

Survival rates are analyzed by:

1. Sex
2. Passenger class
3. Sex + passenger class

Boolean masking using `&` and `|` is used where appropriate.

---

# Correlation Analysis

The correlation matrix contains exactly these six columns:

```text
survived
pclass
age
sibsp
parch
fare
```

The following derived boolean columns are intentionally excluded:

```text
adult_male
alone
```

A Seaborn heatmap is used to visualize the matrix.

The two strongest correlations are identified using:

```text
absolute value of off-diagonal correlation
```

and are interpreted in the notebook.

---

# Multivariate Data Story

At least four charts are produced to explain the relationship between passenger characteristics and survival.

Examples include:

* Survival by gender
* Survival by passenger class
* Survival by gender and class
* Age/fare relationship
* Class/fare relationship
* Correlation heatmap

Every chart has a written interpretation explaining the observed pattern.

---

# Standardization Check

`age` and `fare` are standardized using the z-score:

```text
z = (x - mean) / standard deviation
```

The before/after statistics demonstrate that the standardized variables have approximately:

```text
Mean = 0
Standard deviation = 1
```

This is an exploratory EDA check only.

The modeling pipeline performs its own training-data-only preprocessing.

---

# Predictive Modeling

The target variable is:

```text
survived
```

A stratified train/test split is performed before preprocessing.

Stratification ensures that the relative proportion of survived/not-survived passengers is maintained between the training and test sets.

---

# Preprocessing

The modeling pipeline uses:

* Missing-value imputation
* Categorical encoding
* Numerical scaling
* `StandardScaler`
* `ColumnTransformer`
* Scikit-learn `Pipeline`

The preprocessing steps are fitted only on the training data.

```text
Training Data
     ↓
Fit Imputer
     ↓
Fit Encoder
     ↓
Fit Scaler
     ↓
Train Model
```

The test data is only transformed:

```text
Test Data
     ↓
Transform using fitted preprocessing
     ↓
Model Prediction
```

This prevents data leakage.

---

# Classification Models

Three classifiers are trained using the same train/test split:

### 1. Logistic Regression

A linear classification model used as a strong baseline.

### 2. Decision Tree

A tree-based classifier.

The trained tree is visualized using:

```python
plot_tree()
```

with feature names and class names.

### 3. Random Forest

An ensemble of decision trees used to improve predictive performance and reduce overfitting compared with a single decision tree.

---

# Model Evaluation

Every classifier is evaluated using:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* ROC Curve
* AUC

Final results are presented in a comparison table.

### Classification Results

| Model               | Accuracy | Precision | Recall |  F1 | AUC |
| ------------------- | -------: | --------: | -----: | --: | --: |
| Logistic Regression |      TBD |       TBD |    TBD | TBD | TBD |
| Decision Tree       |      TBD |       TBD |    TBD | TBD | TBD |
| Random Forest       |      TBD |       TBD |    TBD | TBD | TBD |

> Replace `TBD` with the actual values generated by the notebook.

---

# Class Imbalance Analysis

The project compares three approaches:

### Baseline

No imbalance handling.

### Class Weight

```python
class_weight="balanced"
```

### SMOTE

Synthetic Minority Oversampling Technique applied only to the training data.

The three approaches are compared using:

* Precision
* Recall
* F1 Score

The final notebook contains a written conclusion explaining which approach performed best.

---

# Hyperparameter Tuning

Random Forest is tuned using:

```python
GridSearchCV
```

The search covers:

```text
n_estimators
max_depth
max_features
```

The final tuned model is created with:

```python
oob_score=True
```

The following are reported:

* Best parameter combination
* Best cross-validation result
* Out-of-bag score

### Best Random Forest Parameters

```text
n_estimators: TBD
max_depth: TBD
max_features: TBD
OOB Score: TBD
```

---

# Regression Side Task

A multivariate linear regression model is used to predict:

```text
fare
```

from the other available features.

The following metrics are reported:

* MAE
* RMSE
* R²
* Adjusted R²

### Regression Results

| Metric      | Result |
| ----------- | -----: |
| MAE         |    TBD |
| RMSE        |    TBD |
| R²          |    TBD |
| Adjusted R² |    TBD |

A residual plot is also generated and analyzed for evidence of heteroscedasticity.

---

# Final Model Recommendation

The final classifier recommendation is based on the actual evaluation metrics rather than accuracy alone.

The selected model should be justified using metrics such as:

* Precision
* Recall
* F1
* AUC
* Overall predictive performance

### Final Recommendation

> **Replace this section with the actual 3–5 sentence recommendation from the completed modeling notebook.**

Example structure:

```text
Based on the evaluation results, the recommended classifier is ______.
It achieved an F1 score of ______ and an AUC of ______.
Compared with the other models, it provides the best balance between precision and recall.
Therefore, it would be the preferred model for deployment for this classification task.
```

---

# Saved Machine Learning Pipeline

The complete fitted pipeline is saved using:

```python
joblib.dump(full_pipeline, "models/best_pipeline.joblib")
```

The saved object contains both:

```text
Preprocessing
      +
Final Estimator
```

Therefore, new raw data can be passed directly into the pipeline without manually repeating preprocessing.

The artifact is reloaded using:

```python
joblib.load(...)
```

and tested to confirm that it can make predictions on raw input.

---

# 🔹 Module 3 — GenAI Support Assistant

## Objective

The support assistant is a document-grounded Retrieval-Augmented Generation (RAG) application.

The system answers questions using Zepto's policy documents.

The complete architecture is:

```text
User Query
     ↓
Intent Classification
     ↓
 ┌───────────────┐
 │               │
 ▼               ▼
Policy       General
Question     Question
 │               │
 ▼               ▼
Retrieve       Direct
Top-3 Chunks   Answer
 │               │
 └───────┬───────┘
         ▼
Structured Response
         ↓
      FastAPI
         ↓
     POST /ask
```

---

# RAG Architecture

The RAG pipeline follows four major stages:

```text
INGESTION
    ↓
EMBEDDING
    ↓
RETRIEVAL
    ↓
GENERATION
```

---

## 1. Ingestion

Eight Zepto policy documents are stored inside:

```text
support_assistant/docs/
```

The documents cover:

1. Delivery Policy
2. Returns & Refunds
3. Membership Tiers
4. Order Tracking
5. Order Cancellation
6. Damaged or Missing Items
7. Gift Cards
8. Customer Support Hours

Each document is loaded and divided into chunks.

---

# 2. Embedding

Each document chunk is converted into a vector embedding using:

```text
all-MiniLM-L6-v2
```

from the `sentence-transformers` library.

The embeddings are generated locally and do not require an API key.

---

# 3. Vector Storage

The embeddings and corresponding document/chunk information are stored in:

```text
ChromaDB
```

The vector database allows incoming user queries to be compared against the stored policy chunks.

---

# 4. Retrieval

When the user asks a policy-related question, the query is embedded using the same embedding model.

ChromaDB performs similarity search using cosine similarity.

The top three most relevant chunks are retrieved.

The LangGraph node responsible for this process is:

```text
retrieve_and_answer
```

---

# Intent Classification

The LangGraph contains three main nodes:

```text
classify_intent
retrieve_and_answer
direct_answer
```

The first node classifies the query as:

```text
policy_question
```

or:

```text
general_question
```

---

## Mock Mode

The required graded configuration is:

```text
MOCK_LLM
```

unset or:

```bash
MOCK_LLM=1
```

In mock mode, no external LLM API is called.

The intent classifier uses a deterministic keyword-based approach.

The following keywords identify policy questions:

```text
delivery
return
refund
membership
tracking
cancel
gift card
support hours
```

---

# Conditional LangGraph Routing

The graph uses a conditional edge:

```text
                 classify_intent
                       │
            ┌──────────┴──────────┐
            │                     │
            ▼                     ▼
   policy_question        general_question
            │                     │
            ▼                     ▼
 retrieve_and_answer        direct_answer
            │                     │
            └──────────┬──────────┘
                       ▼
                Final Response
```

This makes the routing logic deterministic and easy to test.

---

# Structured Output

The final API response follows a Pydantic schema:

```json
{
    "answer": "string",
    "sources": [],
    "confidence": 1.0
}
```

### Fields

| Field        | Description                       |
| ------------ | --------------------------------- |
| `answer`     | Final answer returned to the user |
| `sources`    | IDs of documents/chunks used      |
| `confidence` | Confidence score between 0 and 1  |

For general questions:

```text
sources = []
```

In mock mode, the response is deterministic.

---

# Prompt Design

The optional real-LLM path uses a structured prompt following:

```text
Role
Context
Task
Format
Length
```

The prompt also includes:

* An explicit negative constraint
* A few-shot example
* Instructions to answer only from retrieved context

Example negative constraint:

```text
Do not answer using information that is not present
in the provided context.
```

---

# FastAPI Application

The LangGraph workflow is exposed through FastAPI.

Endpoint:

```text
POST /ask
```

Request:

```json
{
    "query": "What is the delivery fee for orders below INR 149?"
}
```

Example response structure:

```json
{
    "answer": "Based on the retrieved context: ...",
    "sources": [
        "doc_01"
    ],
    "confidence": 1.0
}
```

---

# Running Module 3

Navigate to:

```bash
cd support_assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Start FastAPI

Keep the default mock mode enabled:

```bash
MOCK_LLM=1
```

Then run:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Example API Calls

## Policy Question

Request:

```json
{
    "query": "What is the delivery fee for an order below INR 149?"
}
```

Expected routing:

```text
classify_intent
       ↓
policy_question
       ↓
retrieve_and_answer
       ↓
ChromaDB retrieval
       ↓
structured response
```

Actual output:

```json
{
    "answer": "Based on the retrieved context: ...",
    "sources": ["doc_01"],
    "confidence": 1.0
}
```

> Replace the placeholder answer with the actual response generated by your implementation.

---

## General Question

Request:

```json
{
    "query": "What is the capital of France?"
}
```

Expected routing:

```text
classify_intent
       ↓
general_question
       ↓
direct_answer
```

Example mock response:

```json
{
    "answer": "I can only answer questions about Zepto policies right now.",
    "sources": [],
    "confidence": 1.0
}
```

---

# 🐳 Docker

The support assistant includes a Dockerfile for local containerization.

Build the image:

```bash
docker build -t zepto-support-assistant .
```

Run the container:

```bash
docker run -p 7860:7860 zepto-support-assistant
```

The FastAPI service will then be available at:

```text
http://localhost:7860
```

The required Docker implementation is local and does not require deployment to a cloud service.

---

# 🔐 Mock LLM vs Real LLM

The project is designed so that the graded implementation works without an external LLM.

## Default

```bash
MOCK_LLM=1
```

or leave it unset.

Advantages:

* No API key
* No external LLM dependency
* Deterministic behavior
* Fully offline LLM logic
* Suitable for grading

---

## Optional Real LLM

The optional path can be enabled using:

```bash
MOCK_LLM=0
```

The real-LLM implementation should:

1. Classify the query using an LLM.
2. Retrieve relevant policy documents.
3. Generate a grounded answer.
4. Validate the response against the Pydantic schema.
5. Retry up to two additional times if structured output validation fails.

API keys must never be hardcoded or committed to GitHub.

---

# 🧪 Testing Strategy

The project validates each module independently.

## Data Pipeline Tests

The pipeline verifies:

* At least 60 scraped books
* At least 3 categories
* Correct data types
* Correct currency conversion
* Valid SQLite schema
* Primary/foreign key relationship
* Required SQL clauses
* SQL JOIN
* Pandas `read_sql`
* Pandas `merge`

---

## Analytics Tests

The analytics module verifies:

* Dataset profiling
* Missing-value analysis
* IQR outliers
* Survival-rate analysis
* Six-column correlation matrix
* Four or more interpreted charts
* Standardization
* Stratified splitting
* Leakage-free preprocessing
* Three classifiers
* Full evaluation metrics
* Imbalance comparison
* GridSearchCV
* OOB score
* Regression metrics
* Residual analysis
* Saved complete pipeline
* Reloadable predictions

---

## Support Assistant Tests

The support assistant verifies:

* Eight policy documents
* Embedding generation
* ChromaDB storage
* LangGraph StateGraph
* TypedDict state
* Three required nodes
* Conditional routing
* Policy retrieval
* Mock-mode generation
* Pydantic validation
* FastAPI endpoint
* Docker build/run

---

# 📊 Overall Project Deliverables

| Module            | Main Deliverables                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Data Pipeline     | Scraper, cleaning pipeline, SQLite DB/schema, SQL queries, pandas analysis               |
| Analytics         | EDA notebook, modeling notebook, `titanic.csv`, charts, model evaluation, saved pipeline |
| Support Assistant | Policy documents, embeddings, ChromaDB, LangGraph, FastAPI, Pydantic schema, Dockerfile  |

---

# ⚙️ Design Decisions

## Data Pipeline

A normalized SQLite database was selected because the catalog data naturally separates into book-level and category-level information. The category foreign key avoids unnecessary repetition of category names across book records.

The fixed conversion rate of **1 GBP = 105.50 INR** is used exactly as specified by the project rather than depending on an external currency API.

---

## Analytics Pipeline

The EDA and modeling stages use the same cleaned dataset so that the project represents one continuous analytical workflow rather than independent analyses.

A scikit-learn `Pipeline` and `ColumnTransformer` are used to ensure preprocessing is fitted only on training data and to prevent data leakage.

Multiple classification algorithms are compared rather than selecting a model based on a single metric.

---

## Support Assistant

A RAG architecture is used so that policy answers are grounded in Zepto's supplied documents.

ChromaDB provides vector similarity search, while LangGraph manages intent routing and workflow orchestration.

The `MOCK_LLM` design provides a deterministic, offline baseline while still allowing an optional real-LLM implementation.

---

# 🔄 End-to-End Project Flow

The three modules collectively demonstrate:

```text
                 ZEpto AI/ML PLATFORM
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 DATA ENGINEERING    ANALYTICS         GENAI/RAG
        │                │                │
        ▼                ▼                ▼
    Scraping            EDA          Documents
        │                │                │
        ▼                ▼                ▼
    Cleaning         Modeling       Embeddings
        │                │                │
        ▼                ▼                ▼
   SQLite DB       Evaluation       ChromaDB
        │                │                │
        ▼                ▼                ▼
 SQL + Pandas       Tuning          LangGraph
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                AI/ML ENGINEERING
                  WORKFLOW DEMO
```

---

# 🚀 How to Run the Complete Project

## Step 1 — Clone

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd zepto-data-ai-platform
```

## Step 2 — Run Data Pipeline

```bash
cd data_pipeline
pip install -r requirements.txt
python main.py
```

## Step 3 — Run Analytics

```bash
cd ../analytics
pip install -r requirements.txt
jupyter notebook
```

Run:

```text
01_eda.ipynb
```

followed by:

```text
02_modeling.ipynb
```

The first notebook creates/updates:

```text
titanic.csv
```

The second notebook reads the same CSV and performs the modeling workflow.

## Step 4 — Run Support Assistant

```bash
cd ../support_assistant
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

---

# 📋 Requirements Summary

### Python

Recommended:

```text
Python 3.10+
```

### Data Pipeline

```text
requests
beautifulsoup4
pandas
```

### Analytics

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
joblib
jupyter
```

### Support Assistant

```text
sentence-transformers
chromadb
langgraph
langchain
pydantic
fastapi
uvicorn
```

The exact package versions are maintained in each module's `requirements.txt`.

---

# 🔀 Git Workflow

The repository follows a feature-branch workflow.

Example:

```bash
git checkout -b feature/data-pipeline

git add .
git commit -m "Add data scraping pipeline"

git add .
git commit -m "Add SQLite database and SQL analysis"

git checkout main
git merge feature/data-pipeline
```

The repository history should demonstrate:

```text
main
 │
 ├── feature branch
 │      ├── commit 1
 │      └── commit 2
 │
 └── merge commit
```

This satisfies the project requirement for a feature branch with at least two commits merged back into `main`.

---

# 🛡️ Security

The repository must not contain:

* API keys
* Passwords
* Tokens
* Private credentials
* `.env` files containing secrets

If the optional real-LLM path is used, credentials should be stored as environment variables.

Example:

```bash
export GROQ_API_KEY="your-key"
```

Never commit the actual key to GitHub.

---

# 📌 Important Notes

* The project is submitted as **one public GitHub repository**.
* All three modules must remain inside the same repository.
* The root repository contains this `README.md`.
* Each module can additionally contain its own README.
* The Data Pipeline uses the fixed **1 GBP = 105.50 INR** conversion rate.
* The Analytics module uses the committed `titanic.csv` as its offline fallback.
* The Support Assistant is fully functional in default `MOCK_LLM` mode without requiring an LLM API.
* Docker is required for the Support Assistant locally.
* Optional real-LLM and cloud deployment features are not required for the graded baseline.

---

# ✅ Final Submission Checklist

Before submitting the GitHub repository, verify:

### Repository

* [ ] One public GitHub repository
* [ ] Root `README.md`
* [ ] `/data_pipeline`
* [ ] `/analytics`
* [ ] `/support_assistant`
* [ ] Git feature branch created
* [ ] At least two commits on feature branch
* [ ] Feature branch merged into `main`

### Data Pipeline

* [ ] At least 60 books
* [ ] At least 3 categories
* [ ] Scraping runs end-to-end
* [ ] `price_gbp` is float
* [ ] `rating` is integer
* [ ] `in_stock` is boolean
* [ ] `price_inr` uses 105.50 conversion
* [ ] Two-table normalized SQLite schema
* [ ] PK/FK relationship
* [ ] At least 5 SQL queries
* [ ] Required SQL clauses included
* [ ] JOIN included
* [ ] `pd.read_sql()` demonstrated
* [ ] `pd.merge()` demonstrated
* [ ] Outputs recorded

### Analytics

* [ ] `titanic.csv` committed
* [ ] Dataset loaded once
* [ ] `df.info()`
* [ ] `df.describe()`
* [ ] `df.shape`
* [ ] Missing percentages
* [ ] Threshold-based missing handling
* [ ] Age histogram
* [ ] Age box plot
* [ ] Fare histogram
* [ ] Fare box plot
* [ ] IQR outlier counts
* [ ] Fare mean/median/mode
* [ ] Fare skewness interpretation
* [ ] Survival by sex
* [ ] Survival by pclass
* [ ] Survival by sex + pclass
* [ ] Exact six-column correlation matrix
* [ ] Correlation heatmap
* [ ] Two strongest correlations interpreted
* [ ] At least four interpreted charts
* [ ] Standardization check
* [ ] Stratified train/test split
* [ ] Training-only preprocessing
* [ ] Logistic Regression
* [ ] Decision Tree
* [ ] Random Forest
* [ ] Decision Tree visualization
* [ ] Confusion matrices
* [ ] Accuracy
* [ ] Precision
* [ ] Recall
* [ ] F1
* [ ] ROC/AUC
* [ ] Imbalance comparison
* [ ] Baseline
* [ ] `class_weight="balanced"`
* [ ] SMOTE on training data only
* [ ] GridSearchCV
* [ ] OOB score
* [ ] Regression
* [ ] MAE
* [ ] RMSE
* [ ] R²
* [ ] Adjusted R²
* [ ] Residual plot
* [ ] Heteroscedasticity conclusion
* [ ] Final model recommendation
* [ ] Complete `joblib` pipeline
* [ ] Pipeline reload test

### Support Assistant

* [ ] Eight policy documents
* [ ] Documents stored in `/docs`
* [ ] Chunking implemented
* [ ] `all-MiniLM-L6-v2`
* [ ] ChromaDB collection
* [ ] Structured prompt
* [ ] Role
* [ ] Context
* [ ] Task
* [ ] Format
* [ ] Length
* [ ] Negative constraint
* [ ] Few-shot example
* [ ] LangGraph `StateGraph`
* [ ] TypedDict state
* [ ] `classify_intent`
* [ ] `retrieve_and_answer`
* [ ] `direct_answer`
* [ ] Conditional edge
* [ ] `MOCK_LLM` branching
* [ ] Top-3 retrieval
* [ ] Pydantic response schema
* [ ] `answer`
* [ ] `sources`
* [ ] `confidence`
* [ ] FastAPI `POST /ask`
* [ ] Two example API calls
* [ ] JSON outputs recorded
* [ ] Dockerfile
* [ ] Docker build tested
* [ ] Docker run tested
* [ ] RAG architecture documented

---

# 🎯 Conclusion

This capstone demonstrates a complete AI/ML engineering workflow by combining:

```text
Data Engineering
       +
Data Analytics
       +
Machine Learning
       +
Generative AI
       +
RAG
       +
API Development
       +
Containerization
```

The resulting platform demonstrates the ability to move from **raw data collection and database design**, through **exploratory analysis and predictive modeling**, to a **document-grounded GenAI application exposed through an API**.

---

## Author

**Harini Doppalapudi**

AI/ML Engineering Capstone Project

---

## License

This project was created for educational and academic purposes.
