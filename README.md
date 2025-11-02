# 🌍 ALX Travel App

A Django REST API backend for a travel application, providing endpoints for managing travel listings and related services.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Database Setup](#database-setup)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **RESTful API**: Clean and well-structured REST API endpoints
- **Listings Management**: Handle travel listings and related data
- **Authentication**: Secure user authentication system
- **API Documentation**: Auto-generated API documentation with Swagger/ReDoc
- **CORS Support**: Cross-Origin Resource Sharing enabled
- **MySQL Database**: Robust database integration
- **Environment Configuration**: Secure environment variable management
- **Celery Integration**: Asynchronous task processing

## 🛠 Tech Stack

- **Backend Framework**: Django 4.2.7
- **API Framework**: Django REST Framework 3.14.0
- **Database**: MySQL 
- **Documentation**: drf-yasg (Swagger/OpenAPI)
- **Task Queue**: Celery 5.3.4
- **Environment Management**: django-environ
- **CORS**: django-cors-headers
- **Python Version**: 3.8+

## 📁 Project Structure

```
alx_travel_app/
├── .env                          # Environment variables
├── .gitignore                    # Git ignore rules
├── README.md                     # Project documentation
├── venv/                         # Virtual environment
└── alx_travel_app/              # Main project directory
    ├── manage.py                 # Django management script
    └── alx_travel_app/          # Django project package
        ├── __init__.py
        ├── settings.py           # Django settings
        ├── urls.py              # Main URL configuration
        ├── wsgi.py              # WSGI configuration
        ├── asgi.py              # ASGI configuration
        ├── requirement.txt       # Python dependencies
        └── listings/            # Listings app
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py        # Database models
            ├── views.py         # API views
            ├── urls.py          # App URL patterns
            ├── tests.py         # Unit tests
            └── migrations/      # Database migrations
```

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **MySQL 5.7+ or 8.0+**
- **pip** (Python package installer)
- **virtualenv** (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/J-Mwema/alx_travel_app.git
cd alx_travel_app
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
cd alx_travel_app
pip install -r alx_travel_app/requirement.txt
```

## ⚙️ Configuration

### 1. Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here

# Database Configuration
DB_NAME=alx_travel_db
DB_USER=your-mysql-username
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
```

### 2. Database Setup

1. **Create MySQL Database**:
```sql
CREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. **Update Database Credentials**:
   - Update the `.env` file with your MySQL credentials

## 🏃‍♂️ Running the Application

### 1. Navigate to Project Directory

```bash
cd alx_travel_app
source venv/bin/activate  # Activate virtual environment
cd alx_travel_app
```

### 2. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 4. Start Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 📚 API Documentation

### Available Endpoints

- **Base URL**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **Listings API**: `http://127.0.0.1:8000/listings/`

### Interactive API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/redoc/`

### Sample API Response

```json
{
    "message": "Listings API is working!"
}
```

## 🗄️ Database Setup

The application uses MySQL as the primary database. Ensure you have:

1. **MySQL Server** installed and running
2. **Database created** with the name specified in `.env`
3. **User permissions** configured for the database
4. **Connection parameters** properly set in `.env`

## 💻 Development

### Running Checks

```bash
# Django system check
python manage.py check

# Check for missing migrations
python manage.py makemigrations --check

# Validate models
python manage.py validate
```

### Development Server Options

```bash
# Run on specific port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000

# Run with specific settings
python manage.py runserver --settings=alx_travel_app.settings
```

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test listings

# Run with coverage (if installed)
coverage run --source='.' manage.py test
coverage report
```

## 🚀 Deployment

### Environment Setup

1. **Production Environment Variables**:
```env
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
SECRET_KEY=your-production-secret-key
```

2. **Static Files**:
```bash
python manage.py collectstatic
```

3. **Security Checklist**:
```bash
python manage.py check --deploy
```

### Deployment Options

- **Docker**: Containerize the application
- **Heroku**: Deploy to Heroku platform
- **AWS/GCP**: Deploy to cloud platforms
- **VPS**: Deploy to Virtual Private Server

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Commit changes**: `git commit -am 'Add new feature'`
4. **Push to branch**: `git push origin feature/new-feature`
5. **Submit a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Write unit tests for new features
- Update documentation as needed
- Use meaningful commit messages

## 🔧 Troubleshooting

### Common Issues

1. **MySQL Connection Error**:
   - Verify MySQL server is running
   - Check database credentials in `.env`
   - Ensure database exists

2. **Module Import Error**:
   - Verify virtual environment is activated
   - Check Python path and Django settings

3. **Migration Issues**:
   - Delete migration files and run `makemigrations` again
   - Check for circular dependencies

### Getting Help

- Check the [Django Documentation](https://docs.djangoproject.com/)
- Review [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- Open an issue in the repository

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **J-Mwema** - *Initial work* - [GitHub](https://github.com/J-Mwema)

## 🙏 Acknowledgments

- ALX Software Engineering Program
- Django and DRF communities
- Contributors and maintainers

---

**Happy Coding! 🚀**

For more information, please contact the development team or open an issue in the repository.