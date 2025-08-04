
#!/bin/bash
set -e

# Build the project
echo "Building the project..."
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

# Install requirements using pip directly
pip install -r requirements.txt

echo "Collect static files..."
python manage.py collectstatic --noinput --clear