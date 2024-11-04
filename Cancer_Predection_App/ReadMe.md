# Cancer Prediction App

Welcome to the **Cancer Prediction App**! This application leverages machine learning techniques to predict the likelihood of breast cancer based on user input. The app is designed to be user-friendly, making it accessible for both medical professionals and individuals seeking to understand their risk of breast cancer.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Features

- **User Input:** Simple interface for entering patient data.
- **Prediction:** Instant prediction results based on the input data.
- **Interactive Visualizations:** Graphical representation of prediction results.
- **Responsive Design:** Works seamlessly on both desktop and mobile devices.
- **Educational Resources:** Includes a section for learning more about breast cancer.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (for serving the machine learning model)
- **Machine Learning Libraries:** Scikit-learn, Pandas, NumPy
- **Data Visualization:** Plotly, Matplotlib
- **Deployment:** Docker, Heroku (or any other hosting service)
- **Version Control:** Git, GitHub

## Installation

To get started with the Cancer Prediction App, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Sheris-Milly/Cancer_Predection_App.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd Cancer_Predection_App
    ```

3. **Install dependencies**:
    It is recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv env
    source env/bin/activate # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

4. **Start the Application:**

   Start the Flask backend:

   ```bash
   cd server
   python app.py
   ```

   Open your browser and navigate to `http://localhost:3000` to view the app.

   ## Docker Setup

To run the application using Docker:

1. **Build the Docker image**:
    ```bash
    docker build -t breast-cancer-prediction-app .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5000:5000 breast-cancer-prediction-app
    ```

## Deployment to Google Cloud Platform (GCP)

This section provides instructions on how to deploy the Cancer Prediction App using a Docker image on Google Cloud Platform.

### Prerequisites

Before you begin, ensure you have the following:

- A Google Cloud account. If you don't have one, you can [sign up here](https://cloud.google.com/).
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed on your local machine.
- Docker installed on your local machine.
- A GCP project created.

### Step 1: Build the Docker Image

1. Navigate to the server directory where your `Dockerfile` is located.

   ```bash
   cd server
   ```

2. Build the Docker image. Replace `your-image-name` with a name for your image.

   ```bash
   docker build -t your-image-name .
   ```

### Step 2: Tag the Docker Image

Tag the Docker image for Google Container Registry (GCR). Replace `YOUR_PROJECT_ID` with your actual GCP project ID.

```bash
docker tag your-image-name gcr.io/YOUR_PROJECT_ID/your-image-name
```

### Step 3: Push the Docker Image to Google Container Registry

Authenticate with Google Cloud:

```bash
gcloud auth login
```

Set your project ID:

```bash
gcloud config set project YOUR_PROJECT_ID
```

Push the Docker image to GCR:

```bash
docker push gcr.io/YOUR_PROJECT_ID/your-image-name
```

### Step 4: Deploy the Docker Image to Google Cloud Run

1. Deploy the image to Cloud Run. This command will create a new service named `your-service-name` from the Docker image. Replace the service name and image name as needed.

   ```bash
   gcloud run deploy your-service-name --image gcr.io/YOUR_PROJECT_ID/your-image-name --platform managed
   ```

2. Follow the prompts to select a region and allow unauthenticated invocations (if desired).

### Step 5: Access Your Deployed App

Once the deployment is complete, you will receive a URL where your Cancer Prediction App is hosted. You can access your app by navigating to this URL in your web browser.

### Cleanup

To avoid incurring charges, remember to delete your Cloud Run service when you no longer need it:

```bash
gcloud run services delete your-service-name --platform managed
```

## Usage

1. **Enter Patient Data:** Fill in the form with the required patient details.
2. **Get Prediction:** Click on the "Predict" button to receive the prediction results.
3. **View Results:** The application will display the prediction and any relevant visualizations.

## How It Works

The Cancer Prediction App utilizes a machine learning model trained on historical patient data. The model analyzes input features to provide a prediction of breast cancer risk. Here’s a brief overview of the process:

1. **Data Collection:** Historical data is collected and preprocessed.
2. **Model Training:** The data is used to train machine learning models (e.g., Random Forest, Gradient Boosting).
3. **Prediction:** User input is fed into the trained model to generate a prediction.

## Model Training

If you are interested in how the machine learning model is trained, refer to the `model.py` script in the directory. The model is evaluated and optimized using techniques like GridSearchCV  to ensure accuracy.

## Contributing

We welcome contributions to the Cancer Prediction App! If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact Information

For any inquiries, please contact:

- **Name:** [Imad Agjoud](https://www.linkedin.com/in/imad-agjoud/)
- **Email:** imadagjoud@gmail.com

----------

- **Name:** [Wassef ARAGOU](https://www.linkedin.com/in/wassef-aragou-7569a9270/)

- **Email:** aragou.wassef@gmail.com

---
- **Name:** [Mouad MALIH](https://www.linkedin.com/in/mouad-malih-756116288?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BefR4o3ClTtKrEOru3mmYhQ%3D%3D)
- **Email:** mouad.malih.17@gmail.com
---

Thank you for using the Cancer Prediction App! We hope it proves helpful in understanding breast cancer prediction.
## Acknowledgments

- Thanks to Dr.Lamrani Youssef for their guidance.
