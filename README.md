Michigan Bitcoiners Website
===========================

Prerequisites
-------------

1) Install the Less CSS processor, which is used to compile style.less to
style.css. If you have node.js installed, you can install Less with the
command:

    npm install -g less

See http://lesscss.org/ for information about Less.

Development Process
-------------------

Make changes to index.dev.html and style.less. index.dev.html includes
less.js, and reads style.less. This allows you tomodify style.less and see
the changes by refreshing index.dev.html.

The Semantic Grid system (http://semantic.gs/) is used for layout. This is
a Less-based system for column layout.

There is an issue using Chrome with less.js. It may be necessary to use
another browser such as Firefox to see the changes to the stylesheet
when refreshing index.dev.html.

index.html and style.css are generated during the deployment process.

Deployment
----------

Before deploying the files to the server, compile style.less to
style.css. On a *nix system this can be done with the command:

    lessc css/style.less css/style.css

or with the shell script:

    makecss.sh

Compile index.dev.html to index.html with the command:

    python productionize_html.py < index.dev.html > index.html
