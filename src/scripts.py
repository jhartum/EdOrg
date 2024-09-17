import subprocess


def setup():
    subprocess.run(["poetry", "install"])
    subprocess.run(["npm", "i"])
    subprocess.run(["cp", ".env.example", ".env"])


def runserver():
    subprocess.run(["poetry", "run", "uvicorn", "src.main:app", "--host=0.0.0.0", "--port=8000"])


def check():
    subprocess.run(["poetry", "run", "ruff", "check", "."])
    subprocess.run(["poetry", "run", "pyright"])


def format():
    subprocess.run(["poetry", "run", "ruff", "check", "--fix", "."])
    subprocess.run(["poetry", "run", "ruff", "format", "."])
