Development
===========

To setup this package in development mode, do:

..code:: sh
    $ pip uninstall sjk # only if sjk was previously installed
    $ cd $PROJECT_DIRECTORY
    $ pip install -e .
    $ ln -s -t $PREFIX/share/jupyter/kernels/ $PWD/kernelspecs/*

To remove the "development" package, do:

..code:: sh
    $ rm $PREFIX/lib/python/site-packages/sjk.egg-link
    $ # remove "sjk" line from $PREFIX/lib/pyhton/site-packages/easy-install.pth
    $ rm $PREFIX/share/jupyter/kernels/sjk-*

To build a package and publish it to PyPI, do:

..code:: sh
    $ python3 -m build --sdist
    $ python3 -m build --wheel
    $ twine upload dist/sjk-$VERSION*

For twine to work, you will need to have your PyPI api token in .pypirc
