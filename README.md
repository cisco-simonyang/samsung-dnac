# Samsung DNAC 클라이언트 화면

## how to run it.
 docker build --tag dnac-client:1.0 .
 docker run -p 5000:5000 dnac-client:1.0


# flask-bootstrap

[Publication Revision 1]

##This is a Python Flask foundation web development package. It contains a basic root template with commonly used style sheets and various useful third party JavaScript libraries.

##Below is a list of knowledge areas that would be essential for the pack to be well understood and extendible. Further work on seperate complexity graded packages will be considered. However, it is best to abide by good practices from day one and I have tried to follow good design principals.

###[Flask Blueprints](http://flask.pocoo.org/docs/0.11/blueprints/)
###[Unit testing](https://docs.python.org/2/library/unittest.html)
###[Jinja templating](http://jinja.pocoo.org/)
###[HTTP](https://www.w3.org/Protocols/)
###Python configuration files

This small foundation project was inspired the frustration of starting new projects without a personal base to work from. As a junior or even student developer, habits such as project templates are great for reducing tedious efforts such as finding packages to link to a project, maintaining versions in templates etc...

Additionally, as the content pack grows, developers may be exposed to libraries unbeknownst to them. This is a great boost for third party development efforts. Support the ladies and gentlemen making the web a weird and wonderful place. Usage is contribution!

##Notes:

#### Bootstrap must be loaded before JQuery and any subsequent JQuery extensions.

#### Sass [http://sass-lang.com/] is a great tool for managing custom stylesheets. Extended syntax features make it much easier to manage much larger stylesheets and greatly encourages happier pixel pushing. Custom stylesheets included in the static/css folder are all generated using the Sass precompiler.

### CSS
Bootstrap: CSS files - http://getbootstrap.com/ [Bootstrap JavaScript Required]


### JavaScript
JQuery: feature-rich library 
http://jquery.com/

MomentJS: Date/Time library 
http://momentjs.com/

Bootstrap: JavaScript files
http://getbootstrap.com/ [Bootstrap CSS Required]

JQueryUI: Pretty awesome UI interaction feature library
http://jqueryui.com/

