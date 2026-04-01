## 📊 Retail Demand Forecasting & Shelf Monitoring System
This project was developed during my internship at BISAG-N, focusing on improving retail inventory management by combining machine learning-based demand forecasting with computer vision-driven shelf monitoring.
## 🚀 Overview
The system integrates two core components:
Demand Forecasting Model – Predicts future product demand using historical sales data.
Out-of-Stock Detection System – Uses YOLO-based object detection to identify missing products on retail shelves in real time.
Together, these components enable proactive inventory management, reduce stockouts, and improve operational efficiency.
## 🔧 Key Features
### 📈 Demand Forecasting
Built using models like XGBoost, Random Forest, and Neural Networks
Uses historical sales data, timestamps, and external factors (e.g., holidays, weather)
Evaluated using metrics like RMSE and MAPE
### 👁️ Shelf Monitoring (Computer Vision)
YOLO-based object detection for identifying products and stockouts
Annotated retail shelf images using tools like LabelImg/VOTT
Evaluated using precision, recall, and F1-score
### 🔄 Real-Time Integration
Combined both models into a unified system
Processes sales data and shelf images simultaneously
Enables real-time inventory monitoring and alerts
### ⚙️ Methodology
Collected and preprocessed structured sales data and unstructured image data
Performed feature engineering and data cleaning for forecasting models
Trained and optimized ML models using cross-validation
Annotated and augmented image datasets for robust YOLO training
Integrated both systems into a deployable pipeline for real-world use
## 📊 Impact
Improved demand forecasting accuracy and inventory planning
Achieved high accuracy in detecting out-of-stock items
Reduced manual monitoring effort through automation
Enabled data-driven decision-making for retail operations
## 🛠️ Tech Stack
Languages & Libraries: Python, Pandas, NumPy, Scikit-learn
ML Models: XGBoost, Random Forest, Neural Networks
Computer Vision: YOLO
Tools: LabelImg / VOTT, Streamlit (for visualization)
## 📌 Future Improvements
Enhance model performance with advanced time-series models
Deploy on cloud infrastructure for scalability
Integrate predictive alerts for supply chain optimization
