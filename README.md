# 🛠️ Flask REST API – User Management

A simple yet powerful **REST API** built with Flask to manage user data.  
This project demonstrates the fundamentals of API design, HTTP methods, and CRUD operations—all using an easy-to-run Python backend.

---

# 🎯 Objective

- Create and expose a RESTful API for **user data management**.
- Support basic operations: **GET**, **POST**, **PUT**, and **DELETE**.

---

# 🧰 Tools & Stack

- Python 3.x
- Flask – lightweight web framework
- Postman or cURL – for testing API endpoints

---

# 🚀 Features & Endpoints

- GET /users – Retrieve a list of all users  
- GET /users/<id> – Retrieve a single user by ID  
- POST /users – Create a new user  
- PUT /users/<id> – Update an existing user  
- DELETE /users/<id> – Delete a user  

✅ Uses an in-memory data store (e.g., Python dictionary or list) for simplicity.  
✅ Input validation and error handling via proper HTTP status codes (200, 201, 400, 404).

---

# 🗂️ Project Structure

flask_rest_api/
├── app.py # Main Flask application
├── users_data.py # In-memory user storage model
├── requirements.txt
└── README.md # Project documentation

yaml
Copy
Edit

---

# Install dependencies:
bash
Copy
Edit
pip install Flask

---

# ▶️ How to Run
Start the Flask server:
-bash
-Copy
-Edit
-python app.py
-By default, it runs on http://127.0.0.1:5000/.

---

# 🧪 Testing the API
 Postman, cURL.

 ---

 ╔════════════════════════════════════════════╗
║   🛠️  Flask REST API – User Manager     ║
╚════════════════════════════════════════════╝

Operations:
1. List all users
2. Get user by ID
3. Create new user
4. Update existing user
5. Delete a user
6. Exit

---

📸 Preview
![image alt](https://github.com/tulsidounekarr/NewsHeadlines-Scraper/blob/15086e7a96bbdc08b896232ea1e4e9a23dd219fc/image.jpg)

---

👨‍💻 Author

- GitHub: [@tulsidounekarr](https://github.com/tulsidounekarr)

---

 📄 License

This project is open-source and available under the [MIT License](LICENSE).




 


