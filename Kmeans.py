import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import pickle

# Page title and description
st.title('KMeans Clustering App')
st.write("""
This app performs KMeans clustering on the input data and displays clustering results.
""")

# Upload CSV data
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Load the KMeans model from file
@st.cache_resource
def load_model():
    with open('kmeans_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Perform clustering and display results
if uploaded_file is not None:
    # Load data
    @st.cache_data
    def load_data(file):
        return pd.read_csv(file)

    data = load_data(uploaded_file)
    
    # Show the raw data
    st.subheader('Raw Data')
    st.write(data.head())
    
    # Check the shape of the data
    st.write('Shape of dataset:', data.shape)
    
    # Data preprocessing
    # Identify and handle non-numeric columns
    non_numeric_cols = data.select_dtypes(exclude=['number']).columns
    if not non_numeric_cols.empty:
        st.write(f"Non-numeric columns found: {non_numeric_cols.tolist()}")
        st.write("Please remove or convert non-numeric columns to proceed.")
        st.stop()
    
    # Assume the last column is the target (if it exists)
    X = data.iloc[:, :-1]  # Features
    y = data.iloc[:, -1]   # Target (if exists)
    
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)
    
    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)
    
    # Sidebar - Get user input for clustering
    st.sidebar.title('Clustering Settings')
    n_clusters = st.sidebar.slider('Select number of clusters', 2, 10, 2)
    
    # Load the KMeans model
    kmeans = load_model()
    
    # Train the KMeans model
    kmeans.n_clusters = n_clusters  # Update number of clusters
    kmeans.fit(X_scaled)
    
    # Predict clusters
    labels = kmeans.labels_
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(X_scaled, labels)
    st.write(f'Silhouette Score for {n_clusters} clusters:', silhouette_avg)
    
    # Dimensionality reduction and plotting
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # Create a DataFrame for plotting
    df_plot = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
    df_plot['Cluster'] = labels
    
    # Plot clusters using PCA
    st.subheader('Clustering Visualization (PCA)')
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(df_plot['PCA1'], df_plot['PCA2'], c=df_plot['Cluster'], cmap='viridis')
    legend = ax.legend(*scatter.legend_elements(), title='Clusters')
    ax.add_artist(legend)
    ax.set_xlabel('PCA1')
    ax.set_ylabel('PCA2')
    st.pyplot(fig)
    
    # Show cluster centers
    st.subheader('Cluster Centers')
    cluster_centers = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X.columns)
    st.write(cluster_centers)
