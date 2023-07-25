# Sentigovt24

## Installation

### Database: 
Buat di pgAdmin4 dengan konfigurasi berikut.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sentigovt',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Project Installation:
1. Create virtual environment (python -m venv env)
2. Activate virtual environment (env/Scripts/activate.bat)
3. Upgrade latest pip version (pip install --upgrade pip)
4. Install Requirements (pip install -r requirements.txt)
5. Create database migrations (python manage.py makemigrations)
6. Applying migrations (python manage.py migrate)

### Running Application
`py manage.py runserver`

### Tailwind Installation:
1. Make sure Node.js and NPM are installed on your system. You can download it from https://nodejs.org/en/download/ and follow the instructions.
2. Install Tailwind version 3.3.2 (npm install -D tailwindcss@3.3.2)
3. Create a configuration file Tailwind (npx tailwindcss init)
4. Change configuration file Tailwind (tailwind.config.js)
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.{html,js}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
5. Create new file CSS (tailwind.css) in directory static/css and add import Tailwind
```css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
```
6. Compress tailwind (npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/tailwind-output.css)
7. Add some directory in setting.py
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### Running Application
`py manage.py runserver`



