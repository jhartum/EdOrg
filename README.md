# Education Organization Website Using Litestar and HTMX

This repository contains the source code for a dynamic and responsive website developed for an educational organization.
The project leverages the **Litestar** framework for the backend, **HTMX** for front-end interactivity, and **UIkit** for a modern and consistent design system.

## Core Technologies

- **Litestar**: A backend framework that emphasizes simplicity and performance, supporting easy API creation and database integration.
- **HTMX**: Enhances user interactions with AJAX-like functionality directly in the HTML, minimizing the need for extensive JavaScript.
- **UIkit**: A lightweight and modular front-end framework that provides a cohesive and stylish user interface with pre-designed components and utilities.
- **TinyDB**: A lightweight, document-oriented database that stores data in JSON format, ideal for small to medium-sized datasets without requiring a full-fledged database server.

## Development Tools

- **Pyright**: A static type checker for Python that helps ensure type safety in your codebase.
- **Ruff**: A fast Python linter and formatter that enforces code quality and style standards.

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

3. **Create the Environment Configuration File**:

   ```bash
   cp .env.example .env
   ```

4. **Start the Development Server**:

   ```bash
   poetry run runserver
   ```

5. **Access the Site**: Open your browser and navigate to `http://localhost:8000`.

## Build and run the application with Docker

```bash
docker build -t edorg . && docker run -d -p 8000:8000 edorg
```

## Linting

```bash
poetry run check
```

## Formatting

```bash
poetry run format
```
