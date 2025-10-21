# ATM Simulation System (DSS Bank of India)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

This project is an **ATM Simulator** created for the AISSCE 2025-26 Computer Project. It aims to replicate the core functionalities of a real-world ATM using a web interface built with Python and Flask. It provides a secure and interactive environment for users to perform basic banking transactions like withdrawals, deposits, and fund transfers.

This simulation serves as a practical application of Python programming, web development (HTML/CSS), and data handling, all within a real-world financial scenario.

## ✨ Key Features

This project simulates the following core ATM functionalities:

* **User Authentication:** Secure login page for users to authenticate via Card Number and PIN.
* **Main Dashboard:** A central home page displaying all available banking services.
* **Account Balance:** Page to view the current account balance.
* **Cash Withdrawal:** Allows users to withdraw cash from their savings or current accounts. Enforces pre-set withdrawal limits.
* **Cash Deposit:** Allows users to add funds to their account.
* **Fund Transfer:** A feature to send money to another (simulated) account.
* **PIN Change:** Securely change the account PIN, complete with an OTP-based verification step.
* **Transaction History:** A "Mini Statement" page to view the last few transactions.
* **Downloadable Reports:** Users can view and download a CSV file of their recent account activity.
* **Exception Handling:**
    * **Session Timeout:** Automatically logs the user out after a period of inactivity.
    * **Failed Logins:** Locks the account after multiple failed login attempts.
* **Sponsor Page:** A fictional sponsor page displayed after transactions.

## 🛠️ Tech Stack

* **Backend:** **Python 3.12+** with the **Flask** web framework.
* **Frontend:** **HTML**, **CSS**, and **JavaScript**.
* **Database:** **SQLite3** for storing user data, account details, and transaction logs.
* **Data Files:** **CSV** and text files are used for generating downloadable reports and managing data.
* **Core Python Libraries:** `flask`, `sqlite3`, `random`, `datetime`, `os`, `csv`.

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

You will need the following software installed on your system:
* [Python 3.12 or higher](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads/) (for cloning the repository)
* A web browser and a code editor (like [VS Code](https://code.visualstudio.com/))

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create a virtual environment:**
    (This is highly recommended to keep project dependencies separate)
    ```sh
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    (First, you'll need to create a `requirements.txt` file if you haven't. Just run `pip freeze > requirements.txt` after installing Flask.)
    ```sh
    pip install -r requirements.txt
    ```
    *If you don't have a `requirements.txt` file, just install Flask:*
    ```sh
    pip install Flask
    ```

4.  **Run the application:**
    ```sh
    python app.py
    ```

5.  **Access the application:**
    Open your web browser and go to:
    [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/)

## 👥 Project Team

This project was developed by:

* **Dhruv Rana:** Backend Development (Python, Flask, logic, authentication)
* **Spandan Basu:** Backend Development (Python, Flask, logic, authentication)
* **Soumyaditya Ghosh:** Frontend Development (HTML, CSS, UI design)

## 📋 Scope and Limitations

Please note that this is an educational simulation.

* **No Real Banking:** The application does not connect to any real banking servers or APIs.
* **Simulated OTP:** The OTP verification is simulated and is not sent to a real mobile device.
* **Single-User:** The system is built as a single-user session model and does not support concurrent users.
* **Mock Transfers:** Fund transfers are mock and do not validate external account details.

## 🔮 Future Scope

Potential features to be added in the future include:

* Integration with a real SMS or Email gateway (like Twilio) for OTP delivery.
* Simulation of biometric (fingerprint/face) authentication.
* An AI/ML model to detect and flag abnormal transaction behavior.
* A separate admin dashboard for viewing user stats and activity logs.

## 📜 License

This project is licensed under the MIT License.
