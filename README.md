# Customer Segmentation using K-Means Clustering

## 📌 Project Overview
This project is a **Customer Segmentation Dashboard** built using **Python**, **Streamlit**, and **Machine Learning (K-Means Clustering)**.

It helps businesses analyze customer behavior and group customers based on:

- Age
- Gender
- Annual Income
- Spending Score
- Purchase Frequency

The dashboard also provides:
- Customer cluster visualization
- Model evaluation metrics
- Business recommendations
- Downloadable customer reports

---

## 🚀 Features

✅ Upload customer dataset (CSV)  
✅ Data preprocessing and cleaning  
✅ Feature engineering  
✅ K-Means clustering algorithm  
✅ Interactive Streamlit dashboard  
✅ Cluster visualization using Seaborn & Matplotlib  
✅ Silhouette Score and Davies-Bouldin Score evaluation  
✅ Business recommendation generation  
✅ Download segmented customer report  

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📂 Project Structure

```bash
Customer-Segmentation/
│
├── app.py
├── Customer_Segmentation.ipynb
├── customers.csv
├── customer_segmentation_output.csv
├── README.md
```

---

## 📊 Machine Learning Algorithm

### K-Means Clustering
The project uses the **K-Means Clustering Algorithm** to group customers into clusters based on customer behavior patterns.

### Evaluation Metrics
- **Silhouette Score**
- **Davies-Bouldin Score**

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Dataset Columns

| Column Name | Description |
|---|---|
| Age | Customer Age |
| Gender | Male/Female |
| Annual_Income | Annual income of customer |
| Spending_Score | Spending behavior score |
| Purchase_Frequency | Frequency of purchases |

---

## 📈 Generated Features

### Customer Value

```python
Customer_Value = (Annual_Income * Spending_Score) / 100
```

### Engagement Score

```python
Engagement_Score = Spending_Score + Purchase_Frequency
```

---

## 📌 Business Recommendations

The dashboard automatically generates business recommendations such as:

- Premium Customer → VIP offers
- Budget Active Customer → Discount coupons
- High Income Low Spending → Personalized marketing
- Low Value Customer → Engagement campaigns

---

## 📥 Output

The final segmented customer report can be downloaded as:

```bash
customer_segments_report.csv
```

---

## 👨‍💻 Author

**Prajwal SY**

---

## 📜 License

This project is for educational and learning purposes.
