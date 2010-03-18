tinchy
======

Uh, so... tinchy
----------------

**tin·chy** _adj._ smaller than tiny.

Yep, it's a really simply and small personal URL shortener that takes fatty URLS and makes them tinchy.

tinchy urls are in the form of http://my-tinchy-domain/abc

Dependancies
------------

Just [Python 2.5+][py]. You need [Bottle][bottle] too but I've included that file in the repository, it will just work if bottle and tinchy are in the same directory. No database needed, tinchy uses shelve (which is included in Python) to persist URLs.

Give it to me in bullets
------------------------

* Personal URL shortener.
* <40 lines of code.
* [Bottle][bottle] is the only dependancy and it's only one file.
* No database needed.
* Good for storing a few thousand personal URLs, if you expect to be storing tens of thousands then look somewhere else. This is not a bit.ly clone :).
* Do whatever you want with it.
* I hope it wont blow up but if it does then sorry :(

  [py]: http://python.org/
  [bottle]: http://bottle.paws.de/
