# Personal Portfolio Website

A modern, responsive personal portfolio website built with Django that showcases professional experience, projects, education, skills, and certifications.

## 🌟 Features

- **Dynamic Content Management**: Admin interface for easy content updates
- **Responsive Design**: Built with the Luther template for optimal viewing across devices
- **Portfolio Showcase**: Display projects with multiple image sizes and descriptions
- **Professional Timeline**: Experience and education sections with date ranges
- **Skills & Expertise**: Organized display of technical skills and competencies
- **Certifications**: Showcase professional certifications with company logos
- **Resume Integration**: Downloadable resume functionality
- **Media Management**: Organized image upload and storage system

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript (Luther Template)
- **Database**: SQLite (development)
- **Image Processing**: Pillow 11.3.0
- **WSGI Server**: Gunicorn 23.0.0 (production)
- **Static Files**: WhiteNoise 6.9.0 (production)
- **Python**: 3.11.0

## 📁 Project Structure

```
personal_portfolio/
├── home/                       # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View controllers
│   ├── urls.py                # URL routing
│   ├── admin.py               # Admin interface
│   └── migrations/            # Database migrations
├── personal_portfolio/         # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── templates/                  # HTML templates
├── static/                     # Static files (CSS, JS, images)
├── media/                      # User-uploaded media files
├── luther-1.0.0/              # Original template files
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
├── build.sh                    # Render build script
├── Procfile                    # Heroku deployment configuration
└── manage.py                   # Django management script
```

## 🗃️ Database Models

### Core Models:
- **Intro**: Personal introduction, profile picture, and resume
- **Expertise**: Technical skills and competencies
- **Experience**: Professional work history with company details
- **Education**: Academic background and qualifications
- **Project**: Portfolio projects with multiple image formats
- **Certificates**: Professional certifications and credentials

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11.0 or higher
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd personal_portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv my_venv
```

### 3. Activate Virtual Environment
```bash
# Windows
my_venv\Scripts\activate

# macOS/Linux
source my_venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies included:**
- Django 5.2.4
- Pillow 11.3.0 (Image processing)
- Gunicorn 23.0.0 (WSGI server for production)
- WhiteNoise 6.9.0 (Static files serving)
- SQLparse 0.5.3 (SQL parsing)
- ASGIREF 3.9.1 (ASGI utilities)
- TZData 2025.2 (Timezone data)

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view your portfolio website.

## 🔧 Configuration

### Admin Access
- **URL**: `http://127.0.0.1:8000/admin/`
- **Default Credentials** (for development):
  - Username: `portfolio`
  - Password: `portfolio`

### Media Files
The project handles various types of media files:
- **Profile Pictures**: `media/personal/`
- **Project Images**: `media/projects/` (small, big, relative sizes)
- **Certificates**: `media/certificates/` (logos and certificate images)

### Static Files
- **CSS**: `static/css/`
- **JavaScript**: `static/js/`
- **Images**: `static/images/`

## 📝 Content Management

### Adding Content via Admin Panel:

1. **Personal Info**: Update intro section with profile picture and resume
2. **Skills**: Add technical expertise and competencies
3. **Experience**: Manage work history with date ranges
4. **Education**: Add academic qualifications
5. **Projects**: Upload project details with multiple image formats
6. **Certificates**: Showcase professional certifications

### Image Requirements:
- **Projects**: Provide small, big, and relative-sized images
- **Certificates**: Company logos and certificate images
- **Profile**: Professional headshot

## 🎨 Customization

### Template Customization
The project uses the Luther template. Customize the appearance by modifying:
- `templates/index.html` - Main template structure
- `static/css/styles.css` - Custom styling
- `static/js/main.js` - Interactive functionality

### Color Scheme
Default theme uses dark colors with professional styling. Modify CSS variables to change the color scheme.

## 🚀 Deployment

### Render Deployment (Ready to Deploy!)

Your project is already configured for Render deployment with:
- ✅ `requirements.txt` - Dependencies specification
- ✅ `runtime.txt` - Python version specification (3.11.0)
- ✅ `build.sh` - Render build script
- ✅ `gunicorn` - Production WSGI server
- ✅ `whitenoise` - Static files serving
- ✅ PostgreSQL support via `dj-database-url`

#### Quick Render Deploy:

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create Render Account & Connect Repository**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New" → "Web Service"
   - Connect your GitHub repository (`personal-porfolio`)

3. **Configure Web Service Settings**
   - **Name**: `personal-portfolio`
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn personal_portfolio.wsgi:application`

4. **Add Environment Variables**
   ```
   SECRET_KEY=your-secret-key-here-generate-new-one
   DEBUG=False
   DJANGO_SETTINGS_MODULE=personal_portfolio.settings
   ```

5. **Add PostgreSQL Database**
   - Click "New" → "PostgreSQL"
   - Name: `portfolio-db`
   - Link it to your web service (DATABASE_URL will be auto-added)

6. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app

#### Environment Variables Required:
- `SECRET_KEY`: Generate a new secret key for production
- `DEBUG`: Set to `False`
- `DJANGO_SETTINGS_MODULE`: `personal_portfolio.settings`
- `DATABASE_URL`: Automatically provided by Render PostgreSQL

#### Post-Deployment Setup:
```bash
# Access Render shell to create superuser
# Go to your service dashboard → Shell tab
python manage.py createsuperuser
```

### Alternative: Heroku Deployment

Your project also supports Heroku with the existing `Procfile`:
- ✅ `Procfile` - Heroku process configuration

#### Quick Heroku Deploy:
```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-portfolio-name

# Add environment variables
heroku config:set SECRET_KEY='your-secret-key-here'
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations and create superuser
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Production Considerations:
1. **Security**: Update `SECRET_KEY` and set `DEBUG = False`
2. **Database**: Configure PostgreSQL or MySQL for production
3. **Static Files**: WhiteNoise is already configured for static file serving
4. **WSGI Server**: Gunicorn is included for production deployment
5. **Environment Variables**: Use environment variables for sensitive settings

### Quick Production Setup:
```bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn personal_portfolio.wsgi:application
```

### Recommended Hosting:
- **Render** (Ready to deploy! See deployment section above)
- **Heroku** (Also ready to deploy! See alternative deployment)
- DigitalOcean
- AWS
- PythonAnywhere
- Railway

## 📂 File Organization

### Media Upload Paths:
- Personal files: `media/personal/`
- Project images: `media/projects/big_img/`, `media/projects/small_img/`, `media/projects/relative_img/`
- Certificates: `media/certificates/big_img/`, `media/certificates/logo/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the Django documentation for framework-specific questions
- Review the Luther template documentation for frontend customization

## 🔄 Version History

- **v1.0.0**: Initial release with full portfolio functionality
- Django 5.2.4 integration
- Luther template implementation
- Complete admin interface
- Media management system

---

**Note**: Remember to update the `SECRET_KEY` and configure proper security settings before deploying to production.
