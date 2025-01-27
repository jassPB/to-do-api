# To-Do API

## Overview

The **To-Do API** is a RESTful API designed to manage task lists. It provides endpoints for creating, retrieving, updating, and deleting tasks. This project aims to simplify task management and serve as a foundation for learning API development and best practices.

---

## Features

- **CRUD Operations:** Create, Read, Update, and Delete tasks.
- **Task Prioritization:** Add priority levels to tasks for better organization.
- **Due Dates:** Set deadlines for tasks.
- **Scalable Design:** Structured to allow future feature additions, such as user authentication and advanced filtering.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or higher
- A virtual environment tool (e.g., `venv`, `virtualenv`)
- Database (e.g., SQLite, PostgreSQL, or MongoDB)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/jassPB/to-do-api.git
   cd to-do-api
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   - Create a `.env` file in the root directory and define the following:
     ```env
     DATABASE_URL=sqlite:///tasks.db
     DEBUG=True
     ```

5. **Run Database Migrations (if applicable):**
   ```bash
   python manage.py migrate
   ```

6. **Start the Server:**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

| Method | Endpoint         | Description                   |
|--------|------------------|-------------------------------|
| GET    | `/tasks`         | Retrieve all tasks.           |
| GET    | `/tasks/<id>`    | Retrieve a single task by ID. |
| POST   | `/tasks`         | Create a new task.            |
| PUT    | `/tasks/<id>`    | Update an existing task.      |
| DELETE | `/tasks/<id>`    | Delete a task by ID.          |

---

## Usage Examples

### Example 1: Creating a New Task
```bash
POST /tasks
Content-Type: application/json

{
  "title": "Complete project",
  "description": "Finish the API development project",
  "priority": "high",
  "due_date": "2025-01-30"
}
```

### Example 2: Retrieving All Tasks
```bash
GET /tasks
```
Response:
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the API development project",
    "priority": "high",
    "due_date": "2025-01-30"
  }
]
```

---

## Testing

1. **Run Unit Tests:**
   ```bash
   python -m unittest discover tests/
   ```

2. **Run All Tests with Coverage:**
   ```bash
   pytest --cov=src
   ```

---

## Contributing

We welcome contributions to improve this project! To contribute:

1. **Fork the Repository:** Click the "Fork" button at the top-right corner of the repository page.
2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/<your-username>/to-do-api.git
   cd to-do-api
   ```
3. **Create a Feature Branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Commit Your Changes:**
   ```bash
   git add .
   git commit -m "Add your feature or fix description"
   ```
5. **Push Your Branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Submit a Pull Request:** Go to your forked repository, click "Compare & pull request," and describe your changes.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project.

---

## Contact

If you have any questions or feedback, feel free to open an issue or reach out to the repository owner.

---