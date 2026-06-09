# Machine Learning Bootcamp

A comprehensive Machine Learning bootcamp program organized by TechIstanbul, instructed by Deniz ALKAN, implemented using the Positron IDE.

## Overview

This repository contains Python lessons and hands-on exercises covering fundamental machine learning concepts, data analysis, and practical implementations. The bootcamp is designed to provide participants with a solid foundation in Python programming and machine learning techniques.

## Curriculum

### Module 1: Python Fundamentals
- **Basic Syntax & Data Types**: Variables, integers, floats, strings, booleans, and operators
- **Control Flow**: Conditional statements (if/else), loops (for/while)
- **Data Structures**: Lists, tuples, sets, and dictionaries
- **Functions**: Function definitions, parameters, and return values
- **Object-Oriented Programming**: Classes, inheritance, encapsulation, polymorphism, and abstraction

### Module 2: Data Analysis & Manipulation
- **NumPy**: Array operations, matrix manipulation, statistical functions
- **Pandas**: DataFrame operations, data cleaning, merging, and joining datasets
- **Data I/O**: Reading/writing CSV and Excel files, SQL database connections

### Module 3: Data Visualization
- **Matplotlib**: Scatter plots, histograms, bar plots, line plots
- **Seaborn**: Statistical data visualizations and heatmaps
- **Plotly**: Interactive visualizations and graph objects

### Module 4: Web Scraping & APIs
- **HTTP Requests**: GET and POST requests using the requests library
- **BeautifulSoup**: Web scraping techniques and pagination handling
- **API Integration**: Working with RESTful APIs and JSON data

### Module 5: Machine Learning Algorithms
- **Linear Regression**: Predictive modeling for continuous variables
- **Logistic Regression**: Classification algorithms for binary outcomes
- **Decision Trees**: Tree-based classification models
- **K-Means Clustering**: Unsupervised learning for data clustering

### Module 6: Reinforcement Learning
- **Q-Learning**: Agent training using the FrozenLake environment with gymnasium

## Project Structure

```
Machine_Learning_Bootcamp/
├── Lesson - 2025.12.04.py     # Python fundamentals
├── Lesson - 2025.12.06.py     # OOP concepts
├── Lesson - 2025.12.09.py     # NumPy & Pandas
├── Lesson - 2025.12.11.py     # Data I/O & SQL
├── Lesson - 2025.12.13.py     # Web scraping & APIs
├── Lesson - 2025.12.16.py     # Data visualization
├── Lesson - 2025.12.23.py     # Linear regression
├── Lesson - 2025.12.25a.py    # Logistic regression
├── Lesson - 2025.12.25b.py    # Decision trees
├── Lesson - 2025.12.25c.py    # K-means clustering
├── Lesson - 2025.12.27.py     # Q-learning
├── data.csv                  # Spotify dataset for clustering
├── diabetes.csv              # Pima Indians diabetes dataset
├── titanic.csv               # Titanic dataset
├── customer.csv            # Telco customer churn dataset
├── insurance.csv           # Medical cost dataset
├── filtered_data.xlsx        # Processed Excel data
├── raw_data.xlsx             # Raw Excel data
├── normalized_df.xlsx        # Normalized API data
└── response_df.xlsx          # API response data
```

## Technologies

- **Language**: Python (>= 3.14.5)
- **IDE**: Positron
- **Core Libraries**:
  - NumPy - Numerical computing
  - Pandas - Data manipulation
  - Matplotlib & Seaborn - Visualization
  - Plotly - Interactive charts
  - scikit-learn - Machine learning
  - gymnasium - Reinforcement learning environments
  - requests & BeautifulSoup - Web scraping

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Machine_Learning_Bootcamp.git
cd Machine_Learning_Bootcamp

# Install dependencies
pip install numpy pandas matplotlib seaborn plotly scikit-learn gymnasium beautifulsoup4 requests sqlalchemy
```

## Usage

Each lesson file is self-contained and can be run in the Positron IDE or any Python environment. The files are organized by date and cover progressive learning topics.

```bash
# Example: Run a specific lesson
python "Lesson - 2025.12.25a.py"
```

## Datasets

The bootcamp uses publicly available datasets from Kaggle:
- Spotify Dataset (1921-2020, 160k+ Tracks)
- Pima Indians Diabetes Database
- Telco Customer Churn
- Medical Cost Personal Datasets
- Titanic Dataset

## Instructor

**Deniz ALKAN** - Machine Learning Bootcamp Instructor

## Organization

**TechIstanbul** - Technology education initiative

## License

See [LICENSE](LICENSE) file for details.