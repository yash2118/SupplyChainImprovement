# AI-Powered Retail Inventory Optimization System
## 1. Problem Solved
Retail businesses face two major challenges:
- Stockouts → lost sales and poor customer experience
- Overstocking → increased storage and operational costs
- Manual shelf monitoring → inefficient and not scalable
- The core problem is the lack of a system that combines:
  - Future demand prediction
  - Real-time shelf visibility
This project solves both by integrating machine learning (forecasting) and computer vision (detection) into a single system.
## 2.  Why I Chose This Project
I worked on this project to solve a real-world supply chain problem. I chose this because:
- Retail generates both structured (sales) and unstructured (images) data
- It has direct business impact (revenue + operations)
## 3. Approach
I designed a two-module system:
### Demand Forecasting (Predict Future)
- Cleaned and preprocessed sales data
- Engineered time-based features (month, seasonality)
- Performed exploratory data analysis (EDA)
- Trained models:
  - Random Forest
  - XGBoost (best performer)
- Evaluated using RMSE and MAPE
### Shelf Monitoring (Detect Present)
- Used Grocery dataset (annotated via Roboflow)
- Applied data augmentation (flip, rotation, shear, exposure)
- Trained YOLOv8 model for object detection
- Built Streamlit app for real-time inference
### Integration Idea
- Forecast what should be in stock
- Detect what is actually on shelf
- Enables proactive inventory decisions
## 4.  Features (X) and Target (Y)
### Demand Forecasting
- X (Input Features): Product category, Shipping location (state), Time features (month, seasonality) (Why: Demand depends heavily on location, product type, and seasonality)
- Y (Target): Qty → number of units sold (Why: Direct representation of customer demand)
### Shelf Detection
- X: Shelf images
- Y: Bounding boxes + object labels (products) (Why: Needed for detecting product presence and stock availability)
## 5. EDA, Modeling, Accuracy & Visualization
### EDA
- Analyzed demand trends over time
- Identified seasonality and patterns
- Checked feature relationships
### Modeling
- Demand Forecasting:
  - Random Forest
  - XGBoost (best performance)
  - Neural Network (experimental)
- Shelf Detection:
  - YOLOv8 object detection model
### Accuracy Metrics
- Forecasting:
  - RMSE → prediction error magnitude
  - MAPE → percentage error
- Detection: Precision, Recall, mAP
### Visualization
- Demand trends (time-series plots)
- Actual vs Predicted graphs
- Feature importance (key demand drivers)
- YOLO bounding box outputs on images
## 6.Impact & Use Cases
- For Businesses / Stakeholders this system enables:
   - Better inventory planning
   - Reduced overstocking costs
   - Increased sales (fewer stockouts)
   - Automated shelf monitoring
- Use Cases
 - Retail Managers: Predict future demand and plan inventory
 - Store Operations Teams: Monitor shelves without manual checks
 - Supply Chain Teams: Optimize procurement and logistics
## 7.How Normal Users Can Use It
- Even non-technical users can:
  - Upload sales data → get demand forecasts
  - Upload shelf images → detect missing products
  - View insights via dashboard
- Can be integrated into:
  - Retail dashboards
  - Inventory systems
  - Smart store applications
- Final Takeaway
  - This project demonstrates how combining machine learning + computer vision can create a complete retail intelligence system that:
    - Predicts future demand
    - Monitors real-time inventory
    - Enables smarter, data-driven decisions
