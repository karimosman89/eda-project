# Exploratory Data Analysis (EDA) Project

## Overview
This project performs exploratory data analysis (EDA) on a given dataset. It includes generating summary statistics, visualizations, and correlation heatmaps.

## Project Structure

            eda-project /
                        │ 
                        ├── data/ # Data files 
                                │ 
                                └── dataset.csv # Example dataset 
                        ├── src/ 
                               │ 
                               ├── eda.py # EDA script 
                               │ 
                               └── utils.py # Utility functions
                        ├── tests/ # Test scripts 
                                 │ 
                                 └── test_utils.py # Unit tests for utilities 
                        ├── requirements.txt # Dependencies 
                        └── README.md # Project documentation 


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/karimosman89/eda-project.git
   cd eda-project

2. Install the required packages:

   
          pip install -r requirements.txt


## Usage

1. Prepare your dataset in the **/data** directory and name it **dataset.csv**.
2. Run the EDA script:
   
          python src/eda.py

   
## Testing    


     python -m unittest discover -s tests

## License

This project is licensed under the MIT License.
