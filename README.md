# How We Eat

*My project is a recipe uploading platform, with image handling, a search feature, the ability to browse recipes based on cuisine and course, and includes a menu creation feature where users can make themed menus that link suggested recipes together.*

## Installation

Project requires no additional packages, but you will need to generate a secret key for settings.py.

## Distictiveness 

The application is disctinct from our assigned projects.  It is not an e-commerce, social media, or communication platform.
I challenged myself to implement several features beyond the scope of the course's assignments including:

* A search feature, which queries the database to search for recipes or menus via their name, and to search for recipes that include a specific ingredient.
* Database image handling, which allows users to upload images from their local device.
* Javascript logic for showing and hiding expanded details about a recipe.


## Files

* Static folder containing CSS styling and JavaScript files.

* Javascript file:
* * recipe expansion: javascript detects "read more" buttons, and when clicked, displays the pre-generated but hidden html containing the directions for any given recipe on the index page
* * recipe deletion: javascript detects delete buttons, and when clicked, triggers a fetch call to the delete API while also removing the recipe from the DOM with a brief animation
* * menu deletion: javascript detects delete buttons while browsing menus, and when clicked, initiates a fetch call to a menu delete API, and then redirects the user to the homepage

* Template folder with a layout file and html files for each page of the application.
* forms.py file, with Django forms for recipe and menu creation.  Additionally a recipe edit form, that allows users to edit all details of their previously created recipes.
* models.py file, which includes the Djano User class, and two additional models for user-submitted recipes and menus.
* urls.py file, directing static and dynamic urls, as well as an API route for an asynchronous delete feature via JavaScript.

* views.py:
* * a default, index view that returns the 10 most recently uploaded recipes
* * user registration, login, and logout views
* * an add_recipe view, which displays the recipe creation form, and then handles the POST request to upload data to the database
* * a browse recipe view, that returns uploaded menues and cuisine categores to display on a browse page
* * menu, course, and cuisine browse views, which take strings passed via urls to dynamically display futher browse options and queries
* * a menu_create view, which displays the menu creation form, and handles the POST request to save paired recipe items to the menu database
* * the search view, which determines if the user is searching for a menu, recipe name, or ingredient, with conditional logic returning navigable search results from database queries
* * a profile view, which queries database to display all recipes uploaded by a certain user
* * an edit view, which gets recipe information from database, prepopulates an edit form with the exisiting recipe informaiton, allowing the user to change or correct their recipes
* * a delete menu view, which verifies that the user is deleting only their own database objects, and deletes menus from database via JSON data and an API url path
* * a delete recipe view, which eliminates an item from the recipe database via JSON data & API url path 