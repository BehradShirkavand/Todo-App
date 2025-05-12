# Todo-App

A simple Todo application built with Django. This project demonstrates fundamental CRUD operations (Create, Read, Update, Delete) and serves as an introductory example for beginners learning Django.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About the Project

This Todo application is a beginner-friendly project that highlights the basics of Django development. It allows users to create, view, update, and delete their tasks in a streamlined interface.

The application is built with **Python** and **Django** for the backend and uses **HTML** for the frontend. It provides a simple yet effective demonstration of how Django's Model-View-Template (MVT) architecture works.

### Why Use It?

- Perfect for beginners exploring Django.
- A practical example of implementing CRUD operations.
- Offers a foundational understanding of how Django handles routing, forms, and database models.

## Features

- Add new tasks.
- View a list of tasks.
- Edit existing tasks.
- Delete completed or unnecessary tasks.
- Simple and user-friendly interface.

## Technologies Used

- **Python** (68.2% of the code)
- **HTML** (31.8% of the code)
- **Django Framework**

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or later
- pip (Python package manager)
- A virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BehradShirkavand/Todo-App.git
   cd Todo-App
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

Once the application is running, you can perform the following actions:

- **Add a Task**: Use the form to input a task and add it to the list.
- **View Tasks**: See all the tasks displayed on the main page.
- **Edit Tasks**: Click the edit button next to a task to modify it.
- **Delete Tasks**: Remove tasks that are no longer needed.

Feel free to experiment with the app to understand Django's functionality better.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- Tutorials and guides that inspired this project.
- Open-source contributors who make coding accessible and enjoyable for everyone.
