

Convertion Table
================


======================= =============== ====================================================
                    Doing
--------------------------------------------------------------------------------------------
     Arturo Types        Python Types                         Notes
======================= =============== ====================================================
``:word``                ``str``        interpreted as a str
``:label``                              is a ``dict``'s key, always needs a r-value
``:string`` (simple)     ``str``             
``:char``                ``str``        chars in Python are intepreted as ``str``
``:integer``             ``int``
``:floating``            ``float``      ``d.`` is an ``:integer``
``:rational``            ``(int, int)``  
``:color``               ``str``
``:block``               ``list``       can't assign values
``:dictionary``          ``dict``       gets pairs of kind (:label :any)
======================= =============== ====================================================
                

======================= ============
                TODO
------------------------------------

Arturo Types            Python Types
======================= ============
:literal                str
:logical                bool
:null                   None
:path                   list[str]
:pathLabel              ...
:symbols                ...
:complex                ...
:type                   str
:regex                  str
:inline                 list
:date                   ...
:database               ...
:binary                 ...
:bytecode               ...
:attribute              ...
:attributeLabel         ...
======================= ============