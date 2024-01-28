

Convertion Table
----------------


============            ============
                Doing
------------------------------------

Arturo Types            Python Types
============            ============
:word                   str
:label                  "key"
:string (simple)        str
:char                   str
:block                  list
============            ============
                
                TODO
------------------------------------

Arturo Types            Python Types
============            ============
:literal                str
:integer                int
:floating               float
:logical                bool
:null                   None
:color                  str
:path                   list[str]
:pathLabel              ...
:symbols                ...
:complex                ...
:rational               tuple[int, int]
:type                   str
:regex                  str
:inline                 list
:date                   ...
:database               ...
:binary                 ...
:bytecode               ...
:attribute              ...
:attributeLabel         ...
============            ============


Notes
-----
``:label`` is translated to a ``dict``'s key.
``:label`` is not supported inside ``:block``.

