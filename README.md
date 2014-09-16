DEVELOPMENT GUIDELINES
======================

Prerequisites
-------------

1) Install the Less CSS processor, which is used to compile style.less to
style.css. If you have node.js installed, you can install Less with the
command:

    npm install -g less

See http://lesscss.org/ for information about Less.

2) Install the Fabric deployment manager (optional). Bruce Webber uses this
to deploy the files to the server. See http://www.fabfile.org/.

Development Process
-------------------

index.dev.html includes less.js, and reads style.less. This allows you to
modify style.less and see the changes by refreshing index.dev.html.

Before deploying the files to the server, style.less must be compiled to
style.css. On a *nix system this can be done with the command:

    lessc css/style.less css/style.css

or with the shell script:

    makecss.sh

If any changes have been made to index.dev.html, these have to be reflected in
index.html. The easiest way to do this is to run productionize_html.py with
the command:

    python productionize_html.py < index.dev.html > index.html
