Michigan Bitcoiners Website
===========================

Prerequisites
-------------

1) Install the Less CSS processor, which is used to compile style.less to
style.css. If you have node.js installed, you can install Less with the
command:

    npm install -g less

Alternatively, on Ubuntu you can use apt-get to install the packages nodejs
and node_less.

See http://lesscss.org/ for information about Less.

If you will be deploying the files to the server, install Fabric
(http://www.fabfile.org/).

Development Process
-------------------

Make changes to index.dev.html and style.less. index.dev.html includes
less.js, and reads style.less. This allows you to modify style.less and see
the changes by refreshing index.dev.html.

The Semantic Grid system (http://semantic.gs/) is a Less-based system for
column layout.

There is an issue using Chrome with less.js. It may be necessary to use
another browser such as Firefox to see the changes to the stylesheet
when refreshing index.dev.html.

index.html and style.css are generated during the deployment process.

Deployment
----------

The deployment process requires Fabric, mentioned above. Fabric runs
fabfile.py, which imports fabfile_env.py, which contains the configuration
details for the particular environment.

fabfile_env.py should be copied from a source file such as fabfile_env.dev.py
or fabfile_env.prod.py. These source files may be versioned; fabfile_env.py
should not.

To deploy the files to the server, enter the command:

    fab deploy

This will commit and push changes to the git repository, pull them to the
server, and compile style.css and index.html on the server. See fabfile.py
for more selective commands..
