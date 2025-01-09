.. include:: ../custom_roles.txt

Unit Testing
============

uEMEP uses a custom unit testing system, which is inspired by URL, and is integrated with :bash:`cmake` and :bash:`ctest`. Unit tests are stored in the :bash:`test` directory.

Writing tests
-------------

The unit testing system are simple Fortran programs and should not have any external dependencies. They have the following overall structure:

.. code-block:: fortran

    program test_example_module

        use example_module

        implicit none

        ! Variables
        logical :: ok = .true. ! Overall test suite check
        real :: expected, result ! Individual test check
        real :: test_par ! Test parameter

        ! Test case 1: Expected return value
        test_par = 2.0
        expected = 42.0
        result = example_function(test_par)
        if (abs(expected - result) >= 1.0e-5) then
            ok = .false.
            print "(a)", "Test case 1 failed!"
        end if

        ! Return test summary
        if (ok) then
            print "(a)", "test_example_module: All tests passed."
        else
            print "(a)", "test_example_module: One or more tests failed."
            stop 1
        end if

    end program test_example

Including tests in the build system
-----------------------------------

By default, unit tests are build automatically when uEMEP is compiled. To add a new unit test to the build system, add the unit test filename, excluding the :code:`test_` prefix in the :code:`foreach` loop in :bash:`./test/CMakeLists.txt`.

.. code-block:: cmake

    foreach(execid
        utility_functions
        read_namefile_routines
        time_functions
        uemep_logger
        io_functions
        )

        add_executable(test_${execid} test/test_${execid}.f90)
        target_link_libraries(test_${execid} PRIVATE uemeplib ${NETCDF_LIBRARIES})
        add_test(NAME test_${execid} COMMAND test_${execid})
    endforeach()

The new unit test will then be built the next time uEMEP is compiled.

Running tests
-------------

Run the unit tests from the build directory as:

.. code-block:: bash

    # Run all unit tests
    make test

In addition, as each unit test is a standalone fortran program, unit tests can also be run individually, e.g.:

.. code-block:: bash

    # Run units tests for a single module
    ./test_io_functions
