# Dockerized ML Model Serving with FastAPI

This project is an example of how to deploy a Machine Learning (ML) model using Docker and FastAPI. Docker is a platform for building, shipping, and running applications in containers, while FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. Together, Docker and FastAPI provide a powerful platform for deploying machine learning models as web services.

## Folder Structure

The project has the following folder structure:

.
├── app
│   └── app.py
├── data
│   └── USA_Housing.csv
├── models
│   └── linear_regression_model.pkl
├── Dockerfile
├── inference.py
├── linear.ipynb
├── requirements.txt
├── tests
│   └── test_app.py
└── assets
    └── logo.png


- `app`: Contains the main FastAPI file (app.py), which defines the API endpoints for making predictions.
- `data`: Contains the USA_Housing.csv file, which is the dataset used to train the model.
- `models`: Contains the trained linear regression model saved as linear_regression_model.pkl.
- `Dockerfile`: The Dockerfile that specifies the environment to run the application.
- `inference.py`: A script that can be used to test the API locally before deploying.
- `linear.ipynb`: A Jupyter Notebook containing the code used to train the linear regression model.
- `requirements.txt`: A file listing the required Python libraries for the application.
- `tests`: Contains unit tests for the application.
- `assets`: Contains any additional files used by the application, such as images or logos.


## Running the Application
To run the application, you can use Docker. First, make sure you have Docker installed on your machine. Then, navigate to the root folder of the project and build the Docker image using the following command:

```
docker build -t <image-name> .
```

Replace `<image-name>` with a name of your choice for the Docker image. This command will create a Docker image based on the instructions in the `Dockerfile`.

Once the Docker image is built, you can run the container using the following command:

```
docker run -p 8000:8000 <image-name>
```

This command will start a container running the Docker image and map port 8000 of the container to port 8000 of your local machine. You can then access the FastAPI application by visiting `http://localhost:8000/docs` in your web browser.