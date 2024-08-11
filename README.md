# Education Organization Website Using Litestar and HTMX

This repository contains the source code for a dynamic and responsive website developed for an educational organization. 
The project leverages the **Litestar** framework for the backend, **HTMX** for front-end interactivity, and **UIkit** for a modern and consistent design system.

## Technologies Used
- **Litestar**: Provides the backend functionality with a focus on simplicity and performance, supporting easy API creation and database integration.
- **HTMX**: Enhances user interactions with AJAX-like functionality directly in the HTML, reducing the need for extensive JavaScript.
- **UIkit**: A lightweight and modular front-end framework that helps create a cohesive and stylish user interface with pre-designed components and utilities.
- **TinyDB**: A lightweight, document-oriented database that stores data in JSON format, making it easy to use for small to medium-sized datasets without the need for a full-fledged database server.

## Setup and Installation
To get started with this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jhartum/EdOrg.git
   cd EdOrg
   ```

2. **Install Dependencies**:
   ```bash
   poetry install
   npm i
   ```

3. **Start the Development Server**:
   ```bash
   poetry run uvicorn src.main:app --host=0.0.0.0 --port=8000
   ```

4. **Access the Site**: Open your browser and navigate to `http://localhost:8000`.
