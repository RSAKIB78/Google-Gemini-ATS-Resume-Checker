# Google-Gemini-ATS-System

This project is a web application that integrates with the Google Gemini API to process and analyze PDF resumes in the context of a job description. The application allows users to upload a resume and a job description to receive a response based on the input prompts provided.

## Features

- Upload PDF resumes
- Provide Job Description
- Process and analyze resumes using the Google Gemini API
- Display responses based on different input prompts

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Google-Gemini-ATS-System.git
    cd Google-Gemini-ATS-System
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Install other dependencies:
    ```sh
    brew install poppler
    ```


## Usage

1. Run the application:
    ```sh
    streamlit run app.py
    ```

2. Add your Gemini API key to .env

3. Open your web browser and go to `http://localhost:8501`.

4. Upload a PDF resume and click the appropriate button to get a response.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or feedback, please contact [sakibrhmn78@gmail.com](mailto:sakibrhmn78@gmail.com).

---