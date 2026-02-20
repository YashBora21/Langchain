import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from genai!")
    print(os.environ.get("GEMINI_API_KEY"))


if __name__ == "__main__":
    main()
