# About the base html

Consider base html is our template, template provide us an object oriented notions of inheritence and a way to reuse to the production of textual data, such as web pages.

### Now lets design our base html which we use as template for web page creation

<!doctype html> // This is standard HTML5 markup.
<html>
<head>
<title>{{ the_title }}</title> //This is a Jinja2 directive, which indicates that a value will be provided prior to rendering (think of this an argument to the template).

<link rel="stylesheet" href="static/hf.css" /> // the look of website is defined in hf.css file
</head>
<body>
{% block body %}
{% endblock %} //These Jinja2 directives indica stituted a block of HTML will be sub is to be here prior to rendering, and inherits provided by any page that from this one.
</body>
</html>

