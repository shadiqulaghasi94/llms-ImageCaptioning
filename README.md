# Image Captioning Project

This README provides instructions on setting up the environment, installing required libraries, and running the code for the Image Captioning project.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Setting Up the Environment

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/ImageCaptioning.git
    cd ImageCaptioning
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

## Installing Required Libraries

1. **Upgrade pip**:
    ```bash
    pip install --upgrade pip
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    Ensure the `requirements.txt` file contains all necessary libraries for the project.

## Running the Code

1. **Run the Main Script**:
    ```bash
    python extract_data_from_webpage.py --url <webpage_url> --extract ["text"|"images"]
    ```

    Replace `<webpage_url>` with the URL of the webpage to extract data from and `["text"|"images"]` with the data you want to extract: summaries of long paragraphs or images with their captions, respectively.

## Additional Notes

- If you encounter any issues, ensure all dependencies are correctly installed and the dataset is properly configured.
- Refer to the project documentation for detailed explanations of the code and its functionality.

