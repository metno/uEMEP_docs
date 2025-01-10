.. include:: ../custom_roles.txt

Coding style
============

The aim of this style guide is the make the uEMEP code base as easy as possible to read and collaborate on.

.. note::
   
   The style guide is currently not complete or finalized.

Module structure
----------------

- Structure code in modules (:code:`module`)
- In most cases, module variables should be :code:`private` by default. Declare public variables and procedures using the :code:`public` keyword
- Use explicit import when possible (i.e., `use module, only: var, func` is better than `ude module`)

**Example of module structure:**

.. code-block:: fortran

    module module_name

        use module, only: imported_variable, imported_procedure

        implicit none
        private

        public :: public_function
        
        real, public :: public_real
        real :: private_real

    contains

        function public_function(par) result(res)
            real, intent(in) :: par
            real :: res
            ...
        end public_function

        subroutine private_subroutine(par, res)
            real, intent(in) :: par
            real, intent(out) :: res
            ...
        end subroutine private_subroutine

    end module module_name

Indentation and white space
---------------------------

- Indent using 4 spaces
- Lines should be no longer than 132 characters, including indentation
- Use vertical white space to structure code into logical units
- Use horizontal white space to help reader, e.g.,
    
    - :code:`a = 2.0` is better than :code:`a=2.0`
    - :code:`2.0 + 3.0*sqrt(r) - 2.0` is better than :code:`2.0+3.0*sqrt(r)-2.0`
    - :code:`if (i == 1 .and. l <= limit) then` is better than :code:`if(i==1.and.l<=limit)then`

Variable names
--------------

- Variables names should be lower case only
- Use descriptive variable names, and use underscore to seperate words (e.g., `use_meteorology`)

Values
------

- Explicitly state preceeding or exceeding zeroes (e.g., :code:`2.0` and :code:`0.5` is better than :code:`2.` and :code:`.5`)


