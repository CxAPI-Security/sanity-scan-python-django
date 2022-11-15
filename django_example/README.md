## Description

- Django is built from a project (e.g. django_example)
- It can contain multiple `apps` that have a function (in our case `hello`)
- Django digests the routes from a special variable called `urlpatterns`.
  - In a URLconf module (file) - a mapping between URL path expressions to Python functions (views).

For more information read here:
https://docs.djangoproject.com/en/4.1/topics/http/urls/#registering-custom-path-converters

### Development

`python manage.py runserver`

### Routes

- /hello - Basic get request
- /hello/param (http://127.0.0.1:8000/hello/asd) showing how to get a parameter
- /adhoc - ad hoc include function directly in route.
- <sub>-<sub_id>/hello - a sub path example (http://127.0.0.1:8000/sub-1/hello/).
