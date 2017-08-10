Introduction
============

What's this?
------------
**obs-ws-rc** is a Python 3.5+ library that allows you to establish client
connections to the `obs-websocket <https://github.com/Palakis/obs-websocket/>`_
plugin for OBS Studio.

It's based on **asyncio**-approach which it inherited from the underlying
WebSocket library - `websockets <https://github.com/aaugustin/websockets/>`_

Performing requests
-------------------
Firstly, **obs-websocket**'s protocol provides you with the ability to send
*requests* and retrieve *responses* to and from OBS Studio.

Let's see how it's done with **obs-ws-rc**:

.. literalinclude:: ../examples/2. Make requests/make_requests.py


Listening to events
-------------------
Secondly, the plugin sends *events* from time to time.
This library lets you listen to these events and handle them:

.. literalinclude:: ../examples/1. Indefinite event handling/indefinite_event_handling.py


Protocol description
--------------------
The protocol *requrests*, *responses* and *events* are declared in the
`PROTOCOL.md
<https://github.com/Palakis/obs-websocket/blob/master/PROTOCOL.md>`_ by
the authors of the **obs-websocket** plugin.

However, there are minor mistakes in that file.
And the field naming of the original protocol is inconsistent.
For example, there're fields like ``authRequired``, at the same time there're
plenty of fields that use a hyphen as a word separator (like
``kbits-per-sec``).

This library internally maps such fields to more pythonic names
(``auth_required`` and ``kbits_per_sec`` as such) - that allows for convenient
passing fields as keyword arguments.

The version of the protocol used by this library can be found in
``./obswsrc/protocol.json``.
