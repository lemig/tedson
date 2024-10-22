# FastAPI User Profile Generator

This project uses FastAPI to create an API endpoint that generates user profiles using a language model.

## Testing the API

To test the API, you can use the following curl command:

```bash
curl -X POST "http://localhost:8000/AskLLM" \
     -H "Content-Type: application/json" \
     -d '{"text": "Create a user profile with the fields name, last_name and id"}'
```

This command sends a POST request to the `/AskLLM` endpoint with a JSON payload containing the prompt text. The API will respond with a generated user profile in JSON format.

## Running the Application

1. Install the required dependencies:

   ```
   pip install fastapi uvicorn outlines
   ```

2. Run the FastAPI application:

   ```
   uvicorn main:app --reload
   ```

3. The API will be available at `http://localhost:8000`.

## API Endpoints

- `/AskLLM` (POST): Generates a user profile based on the provided prompt.

## Project Structure

- `main.py`: Contains the FastAPI application and endpoint definitions.
- `user.py`: Defines the User model.
- `README.md`: This file, containing project information and usage instructions.
XXXXXX
