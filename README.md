# Blinkit Dataset Analysis and Modeling using Power BI and ML

## Introduction
This project aims to analyze the Blinkit dataset, clean and preprocess the data, and build a machine learning model to predict product sales performance based on various features. Additionally, it includes the creation of a Power BI dashboard to visualize and interact with the data, offering valuable insights into sales patterns and trends.

## Dataset Overview
The Blinkit dataset includes the following fields:
- **Item_Identifier**: Unique ID for each product.
- **Item_Weight**: Product weight.
- **Item_Fat_Content**: Indicates if the product is low fat or not.
- **Item_Visibility**: Percentage of display area allocated to the product.
- **Item_Type**: Product category or type.
- **Item_MRP**: Maximum retail price of the product.
- **Outlet_Identifier**: Unique ID for each store.
- **Outlet_Establishment_Year**: Year the store was established.
- **Outlet_Size**: Store size.
- **Outlet_Location_Type**: Type of city or region where the store is located.
- **Outlet_Type**: Indicates if the store is a grocery store or a supermarket.
- **Item_Outlet_Sales**: Sales of the product in the particular store (target variable).

## Data Cleaning and Preprocessing
### Handling Missing Values
- Missing values in **Item_Weight** were filled using the mean weight of the corresponding item category.
- Missing values in **Outlet_Size** were filled with the mode (most frequent value) of the dataset.
- Rows with any remaining missing values were removed.

### Standardizing and Encoding Data
- The **Item_Fat_Content** field was standardized by replacing inconsistent labels such as 'LF' and 'low fat' with 'Low Fat' and 'reg' with 'Regular'.
- Categorical features were encoded using **LabelEncoder** for binary variables and **OneHotEncoder** for multi-class variables.

### Feature Engineering
- A new feature, **Outlet_Age**, was created by subtracting the **Outlet_Establishment_Year** from the current year. This feature helps in analyzing the impact of store age on sales performance.

## Exploratory Data Analysis (EDA)
### Distribution of Item MRP by Item Type
- The dataset was analyzed to understand the distribution of **Item_MRP** across different item types. Visualizations such as histograms and violin plots revealed how the retail price varies within categories.

### Relationship Between Item Visibility and Sales
- A scatter plot was used to analyze the relationship between **Item_Visibility** and **Item_Outlet_Sales** across different outlet types. The results highlighted the influence of product visibility on sales.

### Sales Distribution by Outlet Location Type
- The sales performance was examined across various **Outlet_Location_Types** to identify any location-based trends or patterns.

### Item Sales vs. MRP by Fat Content
- The impact of **Item_Fat_Content** on the relationship between **Item_MRP** and **Item_Outlet_Sales** was visualized, offering insights into customer preferences for low-fat or regular products.

## Machine Learning Model Development
### Model Selection
- A **RandomForestClassifier** was chosen for predicting the **Item_Fat_Content** based on features related to the items and outlets.

### Model Training and Evaluation
- The dataset was split into training and testing sets, and the model was trained using the training set.
- The model achieved an accuracy of **0.6976** on the test set.
- The performance metrics, including precision, recall, and F1-score, were calculated. The model performed well in identifying low-fat products but had lower precision in predicting regular-fat items.
- A confusion matrix was generated to evaluate the classification performance across both classes.

### ROC Curve Analysis
- The Receiver Operating Characteristic (ROC) curve was plotted to visualize the model's ability to distinguish between the two classes. The area under the ROC curve (AUC) was updated to **0.73**, indicating moderate accuracy of the model.

### Model Saving
- The trained model and the list of features were saved using **pickle** for future deployment in a Streamlit application.

## Power BI Dashboard Analysis
The Power BI dashboard was created to visualize and interact with the Blinkit dataset, providing insights into sales patterns across various dimensions.

### Data Cleaning and Preparation
The dataset underwent a data cleaning process to ensure accuracy and consistency in the analysis:
- **Standardization of 'Item_Fat_Content'**: The dataset initially contained inconsistent labels for fat content, such as "LF," "low fat," and "reg." These were standardized to "Low Fat" and "Regular" to maintain uniformity in analysis.
- **Handling Missing Values**: Null values in the "Outlet_Size" field were replaced with the mode, which represents the most frequently occurring record. This imputation method was selected to minimize distortion in data distribution.

### Dashboard Features and Insights
The dashboard is designed to provide an interactive experience, allowing users to filter data based on specific criteria using slicers:
- **Slicers**: 
  - Outlet Location: Allows users to filter data based on the location type of outlets.
  - Outlet Size: Enables filtering based on the size of the outlet.
  - Item Type: Allows selection of product categories for a focused analysis.
- **Calculated Measures**:
  - Total Sales: This measure aggregates the total sales across all products and outlets.
  - Average Sales: This measure provides the average sales value per item across all outlets.
  - Total Number of Items: This measure counts the total number of items available across the dataset.

### Visuals and Insights
- **Total Sales by Outlet Year**: The line chart visualizes the trend in total sales over the years, providing a historical perspective on sales performance.
- **Sales by Fat Content**: A pie chart and bar chart breakdown the sales based on fat content, comparing "Low Fat" and "Regular" products.
- **Sales by Item Type**: A bar chart shows the sales distribution across different product categories, highlighting the best and worst-performing categories.
- **Fat content by outlet location**: A clustered bar chart shows the fat content of items by outlet location.
- **Sales by Outlet Size and Location**: These visuals present the sales distribution based on outlet size and location, providing insights into how outlet characteristics impact sales. Donut chart and Funnel chart were used for these visualizations.
- **Sales by Outlet Type**: The table visual displays the number of items, item visibility, total sales, and average sales across different outlet types, offering a detailed comparison.

## Conclusion
The analysis of the Blinkit dataset involved thorough data cleaning, exploratory data analysis, and the development of a predictive model to forecast product sales. The Power BI dashboard provides an interactive platform to visualize and explore the data, offering valuable insights to stakeholders. The model achieved an accuracy of **0.6976**, and the report highlighted areas for potential improvement, such as enhancing the model's ability to predict regular-fat items.
