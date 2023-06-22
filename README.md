# django-models

- Lab: Class 27 - Django Models
- Author: Manuch Sadri

## Overview

Django has a powerful Object Relational Mapper (ORM) that allows us to persist data using Python instead of SQL. Today you’ll build out a project with one model and wire up that model using Django Views.

## Feature Tasks and Requirements

### Model

- [X] create `snack_tracker_project` project
- [X] create `snacks` app
- [X] Add `snacks` app to project
- [X] create `Snack` model
  - [X] make sure it extends from proper base class
  - [X] add `name` as a CharField with maximum length of 64 characters.
  - [X] add `purchaser` ForeignKey related to Django’s built in user model with CASCADE delete option.
    - [X] from `django.contrib.auth import get_user_model`
  - [X] add `description` TextField
- [X] add model to admin
- [X] modify `Snack` model have user friendly display in admin
- [X] create migrations and migrate data
- [X] create a super user
- [X] run development server
- [X] Add a few snacks via Admin panel
- [X] create another user and more snacks via Admin panel
- [X] confirm that snacks behave as expected with proper name, purchaser and description.

### Views

- [X] create `SnackListView`
  - [X] extend `ListView`
  - [X] give a template of `snack_list.html`
  - [X] associate `Snack` model
- [X] update url patterns for project
  - [X] empty path should `include` snacks.urls
- [X] update snacks app urls
  - [X] empty sub-path should be handled by SnackListView
    - [X] Don’t forget to use `as_view()`
- [X] add detail view
  - [X] link `snack_detail.html` template
  - [X] associate `Snack` model
- [X] update app urlpatterns to handle detail view
  - [X] account for primary key in url
  - [X] path would look like `localhost:8000/1/` to get to snack with id of 1

### Templates

- [X] Add `templates` folder in root of project
  - [X] register `templates` folder in project settings TEMPLATES section
- [X] create `base.html` ancestor template
  - [X] add main html document
  - [X] use `Django Templating Language` to allow child templates to insert content
- [X] create `snack_list.html` template
  - [X] extend base template
  - [X] use `Django Templating Language` to display each snack’s name
- [X] view home page (aka snack_list) and confirm snacks showing properly
- [X] create `snack_detail.html` template
  - [X] template should extend base
  - [X] content should display snack’s name, description and purchaser
- [X] add link in snack_list template to related detail page for each snack
- [X] Add a link back to Home (aka snack_list) page from detail page.

### UAT

- [X] Test Snack pages
  - [X] NOTE make sure test extends TestCase instead of SimpleTestCase used in previous class.
  - [X] verify status code
  - [X] verify correct template use
  - [X] use url name instead of hard coded path
    - [X] TIP: django.urls.reverse will help with that.
- [X] We can’t easily test SnackDetailView just yet.
  - [X] Can you figure out why?
