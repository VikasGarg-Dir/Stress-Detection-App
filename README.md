# Stress Level Detector

### Problem : 

Considering today’s lifestyle, people just sleep forgetting the benefits sleep provides to the human body. Smart-Yoga Pillow (SaYoPillow) is proposed to help in understanding the relationship between stress and sleep and to fully materialize the idea of “Smart-Sleeping” by proposing an edge device. An edge processor with a model analyzing the physiological changes that occur during sleep along with the sleeping habits is proposed. Based on these changes during sleep, stress prediction for the following day is proposed. The secure transfer of the analyzed stress data along with the average physiological changes to the IoT cloud for storage is implemented. A secure transfer of any data from the cloud to any third-party applications is also proposed. A user interface is provided allowing the user to control the data accessibility and visibility. SaYoPillow is novel, with security features as well as consideration of sleeping habits for stress reduction, with an accuracy of up to 96%.

### Solution:

This Web app will help you to detects a person's stress level by analysing the values of several features using the Decision Tree Classifier.

### Idea: 
Building an application that can detect the presence of a mental stress or the possible causes of mental ailments due to stress by indicating the highly relevant factors. 

### Layout

```
├───__pycache__
├───database
│   └───chat_history.json
├───images
│   └───home.png
│   └───icon.jpg
├───Tabs
│   └───__pycache__
│   └───chatbot_1.py
│   └───chatbot.py
│   └───config.toml
|   └─── data.py
|   └─── home.py
|   └─── predict.py
|   └─── visualize.py
├─── venv
├─── .gitignore
├─── chatbot_using_ollama.py
├─── config.toml
└─── main.py
└─── README.md
└─── requirements.txt
└─── SaYoPillow.csv
└─── test_ollama.py
└─── web_functions.py
```


### Note:
**Incase the application demo doesn't start real quick, you can get an idea about how it looks like from the screenshots**

![image](https://user-images.githubusercontent.com/64016811/199024653-a24bb46e-5bde-4f6c-876d-a7c4b02c0218.png)
![image](https://user-images.githubusercontent.com/64016811/199024804-5b4bd63a-528d-4c3c-94ce-2463ab83d5ce.png)
![image](https://user-images.githubusercontent.com/64016811/199026180-fafca016-8955-4301-bc63-3ec978b2c27e.png)
![image](https://user-images.githubusercontent.com/64016811/199025795-61a199f2-67e2-40e9-a076-97e72ca01cd0.png)
![image](https://user-images.githubusercontent.com/64016811/199024885-c3c519d2-b67d-40a7-9804-ea9c7ad938af.png)
![image](https://user-images.githubusercontent.com/64016811/199025007-87d895ee-f812-4987-9acd-e46a88d2055e.png)


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them.

- Python (version 3.9)
- seaborn
- streamlit
- numpy
- matplotlib
- pandas
- scikit_learn

### Installation

1. **Clone the repository:**

    ```bash
   https://github.com/VikasGarg-Dir/Stress-Detection-App.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repo
    ```

3. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/Mac
    # or
    .\venv\Scripts\activate  # On Windows
    ```

4. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

   This command installs all the necessary libraries specified in `requirements.txt`.

5. **Testing is done by hosting ollama and using it endpoint of '/api/generate' to generate response;**

6. **Finally api is being used to generate response for final Stress-detection app;**