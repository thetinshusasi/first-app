# Introduction to Natural Language Processing (NLP)

A comprehensive collection of Jupyter notebooks and Python scripts for learning Natural Language Processing concepts and techniques.

## 📚 Course Overview

This repository contains educational materials for an Introduction to NLP course, covering fundamental concepts including:

- **Text Preprocessing**: Lowercasing, stopword removal, regular expressions, tokenization, stemming, lemmatization
- **N-grams**: Understanding word sequences and context
- **Part-of-Speech (POS) Tagging**: Identifying grammatical components
- **Named Entity Recognition (NER)**: Extracting entities from text
- **Sentiment Analysis**: Rule-based and transformer-based approaches
- **Feature Extraction**: Bag of Words, TF-IDF
- **Topic Modeling**: LDA (Latent Dirichlet Allocation), LSA (Latent Semantic Analysis)
- **Custom Classifiers**: Building and training NLP models

## 🚀 Quick Start

### Prerequisites

- Python 3.9 - 3.12
- Poetry (recommended) or pip

### Installation

#### Option 1: Using Poetry (Recommended)

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd intro-to-ai
   ```

2. **Install dependencies using Poetry**

   ```bash
   poetry install
   ```

3. **Activate the virtual environment**

   ```bash
   poetry shell
   ```

4. **Download spaCy language model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

#### Option 2: Using pip

1. **Create a virtual environment**

   ```bash
   python -m venv nlp_env
   source nlp_env/bin/activate  # On Windows: nlp_env\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install jupyter pandas numpy matplotlib seaborn scikit-learn spacy
   pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0.tar.gz
   ```

## 📖 How to Run

### Jupyter Notebooks

1. **Start Jupyter Lab**

   ```bash
   jupyter lab
   ```

   Or for Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. **Navigate to the course files**
   - Open the `course files/` directory
   - Start with `2.2 Lowercase.ipynb` for the beginning of the course
   - Follow the numerical sequence for a structured learning path

### Python Scripts

1. **Run the main analysis script**

   ```bash
   python src/main.py
   ```

2. **Run POS tagging example**
   ```bash
   python "src/POS tagging.py"
   ```

## 📁 Project Structure

```
intro-to-ai/
├── course files/                 # Jupyter notebooks for the course
│   ├── 2.2 Lowercase.ipynb      # Text preprocessing
│   ├── 2.3 Stopwords.ipynb      # Stopword removal
│   ├── 2.4 Regular Expressions.ipynb
│   ├── 2.5 Tokenizing Text.ipynb
│   ├── 2.6 Stemming.ipynb
│   ├── 2.7 Lemmatization.ipynb
│   ├── 2.8 N-grams.ipynb
│   ├── 2.9 Practical.ipynb
│   ├── 3.2 POS tagging.ipynb    # Part-of-speech tagging
│   ├── 3.3 NER.ipynb            # Named Entity Recognition
│   ├── 3.4 Practical.ipynb
│   ├── 4.2 Rule Based Sentiment.ipynb
│   ├── 4.3 Pre-trained transormer models.ipynb
│   ├── 4.4 Practical Task.ipynb
│   ├── 5.2 Bag of Words.ipynb
│   ├── 5.3 TF-IDF in python.ipynb
│   ├── 6.4 LDA.ipynb            # Topic modeling
│   ├── 6.6 LSA.ipynb
│   ├── 7.2-4 Custom classifier (combined).ipynb
│   ├── 8 Practical.ipynb
│   └── txt_files/               # Sample text files for exercises
├── src/                         # Python scripts
│   ├── main.py                  # Main analysis script
│   └── POS tagging.py           # POS tagging example
├── pyproject.toml               # Poetry configuration
├── poetry.lock                  # Locked dependencies
└── Notes.txt                    # Course notes and concepts
```

## 🛠️ Dependencies

The project uses the following key libraries:

- **jupyter**: Interactive notebook environment
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning library
- **spacy**: Advanced NLP library
- **en_core_web_sm**: English language model for spaCy

## 📚 Learning Path

1. **Text Preprocessing** (2.2 - 2.9): Start here to learn basic text cleaning
2. **POS Tagging & NER** (3.2 - 3.4): Understand grammatical analysis
3. **Sentiment Analysis** (4.2 - 4.4): Learn emotion detection
4. **Feature Extraction** (5.2 - 5.3): Convert text to numerical features
5. **Topic Modeling** (6.4 - 6.6): Discover hidden topics in text
6. **Custom Classifiers** (7.2-4): Build your own NLP models
7. **Practical Applications** (8): Apply everything you've learned

## 💡 Usage Examples

### Basic Text Analysis

```python
import spacy
import pandas as pd

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Process text
text = "Natural Language Processing is fascinating!"
doc = nlp(text)

# Extract tokens and POS tags
for token in doc:
    print(f"{token.text}: {token.pos_}")
```

### Running Notebooks

Each notebook is self-contained and includes:

- Theoretical explanations
- Code examples
- Practical exercises
- Sample datasets

## 🤝 Contributing

This is an educational repository. Feel free to:

- Report issues or bugs
- Suggest improvements
- Add new examples or exercises

## 📄 License

This project is for educational purposes. Please respect the original course materials and licensing terms.

## 🔗 Related Resources

- [365 Data Science NLP Course](https://learn.365datascience.com/courses/nlp)
- [Udemy Introduction to NLP](https://www.udemy.com/course/intro-to-natural-language-processing-in-python-for-ai/)
- [spaCy Documentation](https://spacy.io/)
- [NLTK Documentation](https://www.nltk.org/)

## 📞 Support

If you encounter any issues:

1. Check the course files README for additional setup instructions
2. Ensure all dependencies are properly installed
3. Verify that the spaCy English model is downloaded
4. Check that your Python version is compatible (3.9-3.12)

---

Happy learning! 🎓
