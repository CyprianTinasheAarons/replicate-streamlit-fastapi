# Flux 1.1 Pro Image Generator

This project is a simple web application that generates images using the Flux 1.1 Pro model.

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set your Replicate API token:
   - Copy the `env.sh.example` file to `env.sh`
   - Replace `<paste-your-token-here>` with your actual Replicate API token
   - Source the environment file:
     ```
     source env.sh
     ```

## Running the Application

1. Start the FastAPI backend:
   ```
   python main.py
   ```

2. In a new terminal, start the Streamlit frontend:
   ```
   streamlit run client.py
   ```

3. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)

## Usage

1. Enter a prompt in the text input field
2. Click the "Generate Image" button
3. Wait for the image to be generated and displayed

## Files

- `main.py`: FastAPI backend server
- `client.py`: Streamlit frontend client
- `env.sh`: Environment variables (API token)

## Note

Make sure you have a valid Replicate API token and sufficient credits to use the Flux 1.1 Pro model.

