# sentiment_analysis_app  
Sentiment Analysis Application using PyCaret, MLflow and Streamlit  

The aim of this project is to train a sentiment analysis model and provide a user-friendly interface for analyzing text sentiment in real-time.

---

## 🚀 **Features**

- **Model Training**: Automatically selects the best sentiment classification model using **PyCaret**.  
- **Interactive UI**: Real-time sentiment predictions with a simple and clean **Streamlit** interface.  
- **MLflow Integration**: Logs model experiments, parameters, and metrics for version control and analysis.  
- **User Input**: Users can input text to receive predictions (positive/negative sentiment).  

---

## 🛠️ **Technologies Used**

- **Python**: Core programming language.  
- **PyCaret**: Automated machine learning library for model training and selection.  
- **Streamlit**: Web interface for real-time sentiment predictions.  
- **MLflow**: Experiment tracking and model versioning.  
- **Pandas**: Data manipulation and processing.  

---

## 📋 **How It Works**

1. **Model Training**  
   - A Turkish sentiment analysis dataset is loaded and processed.  
   - PyCaret is used to compare models, finalize the best-performing one, and save it.  

2. **User Interface**  
   - Users enter text in the Streamlit app.  
   - The trained model predicts the sentiment and returns the result.  

3. **Model Logging**  
   - Experiment parameters, metrics, and the model are logged using MLflow.  
