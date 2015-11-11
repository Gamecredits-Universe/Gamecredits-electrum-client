Electrum-GMC - lightweight Gamecredits client
==========================================

::

  Licence: GNU GPL v3
  Original Author: Thomas Voegtlin
  Port Maintainer: Pooler
  Language: Python
  Homepage: https://electrum-gmc.org/



1. GETTING STARTED
------------------

To run Electrum from this directory, just do::

    ./electrum-gmc

If you install Electrum on your system, you can run it from any
directory.

If you have pip, you can do::

    python setup.py sdist
    sudo pip install --pre dist/Electrum-GMC-2.0.tar.gz


If you don't have pip, install with::

    python setup.py sdist
    sudo python setup.py install



To start Electrum from your web browser, see
http://electrum-gmc.org/gamecredits_URIs.html



2. HOW OFFICIAL PACKAGES ARE CREATED
------------------------------------

On Linux/Windows::

    pyrcc4 icons.qrc -o gui/qt/icons_rc.py
    python setup.py sdist --format=zip,gztar

On Mac OS X::

    # On port based installs
    sudo python setup-release.py py2app

    # On brew installs
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip

    sudo hdiutil create -fs HFS+ -volname "Electrum-GMC" -srcfolder dist/Electrum-GMC.app dist/electrum-gmc-VERSION-macosx.dmg
