# ACTIVAR ENT VIRTUAL
# crear proyecto 
python3 -m venv venv
./venv/Scripts/activate
pip install Django
pip freeze > requirements.txt
django-admin
django-admin startproject config .
python manage.py
python manage.py runserver
python manage.py migrate
python manage.py make migrations
python manage.py createsuperuser
django-admin startapp blog

# GLOSARIO


- [CSS](https://developer.mozilla.org/es/docs/Web/CSS)
- [HTML](https://devdocs.io/html/)
- [JS](https://developer.mozilla.org/es/docs/Web/JavaScript)
- [NodeJS](https://nodejs.org/es/docs/)
- [Babel](https://babeljs.io/docs/en/)
- [Github](https://desktop.github.com/)
- [Git](https://git-scm.com/downloads)
- [Vue.js](https://www.vuemastery.com/pdf/Vue-Essentials-Cheat-Sheet.pdf)

## Instalation comands
```
npm install
```
## Project setup
```
npm i
```

### Compiles and hot-reloads for development
```
npm run serve
```
```
npm run publish
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## util links

(https://awesomejs.dev/for/vue-cli/pkg/245665373358129666/)
