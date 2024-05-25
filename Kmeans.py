from flask import Flask, request, render_template, redirect, url_for, flash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import pickle
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flashing messages

# Load the KMeans model from file
def load_model():
    with open('kmeans_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in the request')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        
        if file and file.filename.endswith('.csv'):
            try:
                data = pd.read_csv(file)
            except Exception as e:
                flash(f'Error reading CSV file: {e}')
                return redirect(request.url)
            
            # Check for non-numeric columns
            non_numeric_cols = data.select_dtypes(exclude=['number']).columns
            if not non_numeric_cols.empty:
                flash(f"Non-numeric columns found: {non_numeric_cols.tolist()}. Please remove or convert non-numeric columns to proceed.")
                return redirect(request.url)
            
            # Assume the last column is the target (if it exists)
            X = data.iloc[:, :-1]  # Features
            y = data.iloc[:, -1] if data.shape[1] > 1 else None  # Target (if exists)
            
            # Handle missing values
            imputer = SimpleImputer(strategy='mean')
            X_imputed = imputer.fit_transform(X)
            
            # Scale the data
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X_imputed)
            
            # Get the number of clusters from the form
            n_clusters = int(request.form.get('n_clusters', 2))
            
            # Load the KMeans model
            kmeans = load_model()
            
            # Train the KMeans model
            kmeans.n_clusters = n_clusters  # Update number of clusters
            kmeans.fit(X_scaled)
            
            # Predict clusters
            labels = kmeans.labels_
            
            # Calculate silhouette score
            silhouette_avg = silhouette_score(X_scaled, labels)
            
            # Dimensionality reduction and plotting
            pca = PCA(n_components=2)
            X_pca = pca.fit_transform(X_scaled)
            
            # Create a DataFrame for plotting
            df_plot = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
            df_plot['Cluster'] = labels
            
            # Ensure the static directory exists
            if not os.path.exists('static'):
                os.makedirs('static')
            
            # Plot clusters using PCA
            fig, ax = plt.subplots(figsize=(10, 6))
            scatter = ax.scatter(df_plot['PCA1'], df_plot['PCA2'], c=df_plot['Cluster'], cmap='viridis')
            legend = ax.legend(*scatter.legend_elements(), title='Clusters')
            ax.add_artist(legend)
            ax.set_xlabel('PCA1')
            ax.set_ylabel('PCA2')
            plt.savefig('static/plot.png')
            plt.close(fig)
            
            # Show cluster centers
            cluster_centers = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=X.columns)
            
            return render_template('index.html', 
                                   data_preview=data.head().to_html(), 
                                   shape=data.shape, 
                                   silhouette_avg=silhouette_avg, 
                                   n_clusters=n_clusters, 
                                   cluster_centers=cluster_centers.to_html(), 
                                   img_url='static/plot.png')
        else:
            flash('Allowed file type is CSV')
            return redirect(request.url)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
