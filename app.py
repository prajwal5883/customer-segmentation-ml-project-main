import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score


st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

st.title("Customer Segmentation using K-Means Clustering")
st.write("This project groups customers based on income, spending score, age, and purchase frequency.")


uploaded_file = st.file_uploader("Upload Customer CSV File", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    st.subheader("Dataset Information")
    st.write("Rows:", data.shape[0])
    st.write("Columns:", data.shape[1])

    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    data.drop_duplicates(inplace=True)

    if "Gender" in data.columns:
        le = LabelEncoder()
        data["Gender"] = le.fit_transform(data["Gender"])

    data["Customer_Value"] = data["Annual_Income"] * data["Spending_Score"] / 100
    data["Engagement_Score"] = data["Spending_Score"] + data["Purchase_Frequency"]

    features = data[
        [
            "Age",
            "Gender",
            "Annual_Income",
            "Spending_Score",
            "Purchase_Frequency",
            "Customer_Value",
            "Engagement_Score",
        ]
    ]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    st.sidebar.header("Model Settings")
    k = st.sidebar.slider("Select Number of Clusters", 2, 10, 5)

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    data["Cluster"] = kmeans.fit_predict(scaled_features)

    silhouette = silhouette_score(scaled_features, data["Cluster"])
    db_score = davies_bouldin_score(scaled_features, data["Cluster"])

    st.subheader("Model Evaluation")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Silhouette Score", round(silhouette, 3))

    with col2:
        st.metric("Davies-Bouldin Score", round(db_score, 3))

    st.subheader("Cluster Visualization")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        x=data["Annual_Income"],
        y=data["Spending_Score"],
        hue=data["Cluster"],
        palette="Set1",
        s=100,
        ax=ax
    )
    ax.set_title("Customer Segments")
    ax.set_xlabel("Annual Income")
    ax.set_ylabel("Spending Score")
    st.pyplot(fig)

    st.subheader("Cluster Summary")
    cluster_summary = data.groupby("Cluster")[
        ["Age", "Annual_Income", "Spending_Score", "Purchase_Frequency", "Customer_Value"]
    ].mean()

    st.dataframe(cluster_summary)

    def recommendation(row):
        income = row["Annual_Income"]
        spending = row["Spending_Score"]

        if income >= 35000 and spending >= 70:
            return "Premium Customer - Give VIP offers and loyalty rewards"
        elif income >= 35000 and spending < 40:
            return "High Income Low Spending - Use personalized marketing"
        elif income < 25000 and spending >= 70:
            return "Budget Active Customer - Give discount coupons"
        elif income < 25000 and spending < 40:
            return "Low Value Customer - Send engagement campaigns"
        else:
            return "Average Customer - Regular offers and updates"

    data["Business_Recommendation"] = data.apply(recommendation, axis=1)

    st.subheader("Final Customer Segments")
    st.dataframe(data)

    csv = data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Segmented Customer Report",
        data=csv,
        file_name="customer_segments_report.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a customer CSV file to start.")