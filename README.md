API Automation Framework 🧪⚙️

A simple and effective API automation testing framework in Python using Pytest, Requests and Allure Reports — designed for REST API testing with structure, reports, and reusability.

📌 Features

✔️ Modular structure with reusable utilities ✔ API tests organized with Pytest ✔ Easy-to-configure fixtures (in conftest.py) ✔ Interactive test reporting with Allure ✔ Lightweight and extendable

🗂️ Project Structure . 
├── api/ # API helper functions / clients 
├── tests/ # Test cases for different API endpoints 
├── utils/ # Utility functions and helpers 
├── conftest.py # Global fixtures for pytest 
├── requirements.txt # Python dependencies 
├── .gitignore # Git ignores (including .venv) 
|__ reports/

📦 Requirements

Install dependencies:

pip install -r requirements.txt

▶️ Running Tests Run all tests: pytest -v

📊 Allure Reporting

Allure Reports help generate interactive test result dashboards, making it easier to visualize and analyze test execution outcomes. You’ll see passed, failed, and skipped tests, detailed test steps, and attach logs or response data.

Generate Allure Results pytest --alluredir=reports/allure

View Report allure serve reports/allure
