.. include:: ../custom_roles.txt

Unit Testing
============

uEMEP uses a custom unit testing system, which is inspired by URL, and is integrated with :bash:`cmake` and :bash:`ctest`. Thus, running the unit tests is as simple as running :bash:`make test` in the build directory.

Unit tests are stored in the :bash:`test` directory and is 

Writing unit tests
------------------

Building the unit tests
-----------------------

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

As each unit test is a standalone fortran program, unit tests can also be run individually.



