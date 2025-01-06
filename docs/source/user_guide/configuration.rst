Configuration A-Z
=================

This page contains a list of all configuration options in uEMEP in alphabetic order.

alternative_meteorology_type
----------------------------

Used to specify the meteorology type if an alternative meteorology is used.

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"meps"`

See also: :ref:`user_guide/configuration:use_alternative_meteorology_flag`

.. code-block:: fortran

    ! Example: Set the alternative meteorology type to default value
    alternative_meteorology_type = "meps"

annual_calculations
-------------------

Used to specify if uEMEP should perform annual calculations. If annual calculations in turned on, uEMEP will use a rotationally symmetric Gaussian plume model.

- Type: Boolean (:code:`logical`)
- Default value: :code:`.false.`

See also: :code:`user_guide/configuration:hourly_calculations`

.. code-block:: fortran

    ! Set uEMEP to perform annual calculations
    annual_calculations = .true.

auto_adjustment_for_summertime
------------------------------

Used to specify if summer time should be automatically set. If turned on, then the time is automatically shifted forward by one hour (default) in the period March 31 to October 27.

- Type: Boolean (:code:`logical`)
- Default value: :code:`.true.`

See also: :ref:`user_guide/configuration:emission_timeprofile_hour_shift`

.. code-block:: fortran

    ! Example: Turn off automatically setting summer time
    auto_adjustment_for_summertime = .false.

auto_select_OSM_country_flag
----------------------------

Used to specify if uEMEP should automatically detect and select for which countries OSM data should be read. 

- Type: Boolean (:code:`logical`)
- Default value: :code:`.false.`

See also: :ref:`user_guide/configuration:filename_boundingbox`

calculate_EMEP_source
---------------------

See also: :ref:`user_guide/configuration:calculate_source`

comp_name_nc
------------

- Type: Text string array (:code:`character(len=256), dimension(n_compound_nc_index)`)
- Default value: Please see the `set_constants routine <https://metno.github.io/uEMEP/proc/uemep_set_constants.html>`_ in the `code documentation <https://metno.github.io/uEMEP/index.html>`_ for details.

EMEP_emission_grid_interpolation_flag
-------------------------------------

Used to specify the interpolation method for the EMEP emissions if redistribution of EMEP emissions using proxy data are used as the downscaling method.

Three methods are available:

1. None (returns the EMEP grid)
2. Area weighted (quick, biliniar interpolation, see equation :eq:`eq:area_weighting`)
3. Emission weighted (slow, see equation :eq:`eq:emis_weihting`)

- Type: Integer (:code:`integer`)
- Default value: :code:`0`

See also:

.. code-block:: fortran

    ! Example: Change interpolation method to be area weighted
    EMEP_emission_grid_interpolation_flag = 1

EMEP_grid_interpolation_flag
----------------------------

Used to specify the interpolation method used for the EMEP grid moving window. 

Three methods are available:

0. None (returns the EMEP grid)
1. Area weighted (quick, biliniar interpolation, see equation :eq:`eq:area_weighting`)
2. Emission weighted (slow, see equation :eq:`eq:emis_weihting`)

- Type: Integer (:code:`integer`)
- Default value: :code:`0`

See also:

.. code-block:: fortran

    ! Example: Set EMEP grid interpolation method to be area weighted
    EMEP_grid_interpolation_flag = 1

EMEP_meteo_grid_interpolation_flag
----------------------------------

Used to specify the interpolation method used for the altenative EMEP grid moving window and an alternative meteorology is used. 

Two methods are available:

0. None (returns the EMEP grid)
1. Area weighted (quick, biliniar interpolation, see equation :eq:`eq:area_weighting`)

- Type: Integer (:code:`integer`)
- Default value: :code:`1`

See also: :ref:`user_guide/configuration:use_alternative_meteorology_flag`

.. code-block:: fortran

    ! Example: Turn off grid interpolation for the EMEP meteorology grid
    EMEP_meteo_grid_interpolation_flag = 0

calculate_source
----------------

Used to specify which emission sources should be included in the calculation. All emission sources are set to false by default, but at least one emission source should be included for uEMEP to run. 

- Type: Boolean array (:code:`logical, dimension(n_source_nc_index)`)
- Default value: :code:`.false.`

See also: :ref:`user_guide/configuration:calculate_EMEP_source`

.. code-block:: fortran

    ! Example: Include traffic as an emission source
    calculate_source(traffic_index) = .true.

emission_naming_template_str
----------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"Sec<n>_Emis_mgm2_"`

emission_timeprofile_hour_shift
-------------------------------

Used to specify the number of hours for time summer time shifting. 

- Type: Integer (:code:`integer`)
- Default value: :code:`1`

See also: :ref:`user_guide/configuration:auto_adjustment_for_summertime`

.. code-block:: fortran

    ! Example: Set the hour time shift to the default value (1 hour)
    emission_timeprofile_hour_shift = 1

end_time_meteo_nc_index
-----------------------

Used to set the last time index of the alternative EMEP NetCDF file if an alternative meteorology is used.

- Type: Integer scalar (:code:`integer`)
- Default value: :code:`1`

See also: :ref:`user_guide/configuration:start_time_meteo_nc_index`, :ref:`user_guide/configuration:use_alternative_meteorology_flag`

.. code-block:: fortran

    ! Example: Set the last time index value to an alternative value
    end_time_meteo_nc_index = 24

end_time_nc_index
-----------------

Used to set the last time index of the EMEP NetCDF file. 

- Type: Integer scalar (:code:`integer`)
- Default value: :code:`1`

See also: :ref:`user_guide/configuration:start_time_nc_index`

.. code-block:: fortran

    ! Example: Set the last time index value to an alternative value
    end_time_nc_index = 24

file_tag
--------

Used to tag the output of a uEMEP simulation.

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

.. code-block:: fortran

    ! Example: Include the text string "uemep_demonstration" in the output filename
    file_tag = "uemep_demonstration"

filename_agriculture
--------------------

Used to specify the filenames of the agriculture data. Currently, 2 filenames can be specified.

- Type: Text string array (:code:`character(len=256), dimension(2)`)
- Default value: No default

.. code-block:: fortran

    ! Example: Set the filename of the agriculture data
    filename_agriculture(1) = "<agriculture_file_name.dat>"

filename_boundingbox
--------------------

Used to specify the filename of the countries bounding box data. This file contains coordinates to create boxes around countries and is used to automatically select for which countries OSM data are read.

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`) 

See also: :ref:`user_guide/configuration:auto_select_OSM_country_flag`

.. code-block:: fortran

    ! Example: Set the filename of the bounding box data
    filename_boundingbox = "<filename_of_bounding_box.txt>"

filename_date_output_grid
-------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"<replace_date>_<replace_hour>"`

filename_EMEP
-------------

Used to specify the filenames of the EMEP NetCDF forcing data. Currently, 4 names can be specified. The first text string is used to specify the filename of the EMEP data including the meteorological data. The second text string is used to specify the filename of the EMEP local fractions data. The third text string is used to specify the filename of alternative EMEP meteorological data if necessary.

- Type: Text string array (:code:`character(len=256), dimension(4)`)
- Default value: No default

See also: :ref:`user_guide/configuration:pathname_EMEP`, :ref:`user_guide/configuration:use_alternative_meteorology_flag`

.. code-block:: fortran

    ! Example: Set the filenames of the EMEP meteorology and local fractions files
    filename_EMEP(1) = "<emep_file_data.nc>"
    filename_EMEP(2) = "<emep_local_fractions_data.nc>"

filename_heating
----------------

- Type: Text string array (:code:`character(len=256), dimension(10)`)
- Default value: No default

filename_industry
-----------------

- Type: Text string array (:code:`character(len=256), dimension(10)`)
- Default value: No default

filename_landuse
----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

filename_log_file
-----------------

Used to specify the filename of the log file. Set to empty to write to the terminal.

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`uEMEP_log.txt`

See also: :ref:`user_guide/configuration:pathname_log_file`

.. code-block:: fortran

    ! Example: Write uEMEP log output to the terminal windows
    filename_log_file = ""

filename_mrl
------------

- Type: Text string array (:code:`character(len=256), dimension(50)`)
- Default value: No default

filename_population
-------------------

- Type: Text string array (:code:`character(len=256), dimension(n_population_index)`)
- Default value: No default

filename_receptor
-----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

filename_region_id
------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

filename_region_mask
--------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

filename_rl
-----------

- Type: Text string array (:code:`character(len=256), dimension(2)`)
- Default value: No default

filename_rl_change
------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

filename_ship
-------------

Used to specify the shipping proxy file names if :code:`calculate_source(shipping_index) = .true.`.

- Type: Text string (:code:`character(len=256), dimension(2)`)
- Default value: No default

See also: :ref:`user_guide/configuration:pathname_ship`, :ref:`user_guide/configuration:calculate_source`, :ref:`user_guide/configuration:read_shipping_from_netcdf_flag`

.. code-block:: fortran

    ! Example: Set the filename of the shipping proxy data
    filename_ship(1) = "<shipping_proxy_data.nc>"

filename_tiles
--------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

filename_timeprofile
--------------------

Used to specify the time profile file name.

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

See also: :ref:`user_guide/configuration:pathname_timeprofile`

.. code-block:: fortran

    ! Example: Set the filename of the time profile data
    filename_timeprofile = "<filename_of_timeprofile_data>"

finished_filename
-----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`"finished/"`)

finished_subpath
----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`""`

forecast_hour_str
-----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"00"`

h_emis
------

Used to specify the emission height (in meters) for each emission source (first dimension) and subsource (second dimension), i.e., :code:`h_emis(source_index,subsource_index)`. Subsources are currently not used in uEMEP.

- Type: Decimal number array (:code:`real, dimension(n_source_index,n_possible_subsource)`)
- Default values:

  - Traffic: :code:`2.0`
  - Shipping: :code:`70.0`
  - Heating: :code:`15.0`
  - Agriculture: :code:`1.0`
  - Industry: :code:`100.0`
  - Aviation: :code:`10.0`
  - Fugitive: :code:`5.0`
  - Livestock: :code:`5.0`
  - Solvents: :code:`15.0`
  - Offroad: :code:`5.0`
  - Waste: :code:`15.0`
  - Other: :code:`15.0`

See also: :ref:`user_guide/configuration:sig_y_00`, :ref:`user_guide/configuration:sig_z_00`

.. code-block:: fortran

    ! Example 1: Change the height of traffic emissions to 1 meter
    h_emis(traffic_index,1) = 1.0

    ! Example 2: Change the height of heating emissions to 10 meters
    h_emis(heating_index,1) = 10.0

hourly_calculations
-------------------

Used to specify if uEMEP should perform hourly calculations. If hourly calculations in turned on, uEMEP will use a standard Gaussian plume model (see :ref:`user_guide/model_description:Gaussian plume model for hourly calculations`).

- Type: Boolean (:code:`logical`)
- Default value: :code:`.false.`

See also: :ref:`user_guide/configuration:annual_calculations`

.. code-block:: fortran

    ! Set uEMEP to perform hourly calculations
    hourly_calculations = .true.

infile_region_heating_scaling
-----------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

inpath_region_heating_scaling
-----------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

input_comp_name
---------------

Used to specify compounds included in the uEMEP calculation. Compounds can be set to either single compounds or using named list which will specify several compounds.

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

Valid values for single compounds are: :code:`nox, no2, pm25, pm10, nh3`

Valid values for using lists are:

- :code:`all_totals`: Includes the compounds 
- :code:`gp_totals`: Includes the compounds :code:`nox,no2`

.. code-block:: fortran

    ! Example 1: Set to calculate for pm25 only
    input_comp_name = "pm25"

    ! Example 2: Set to calculate for all compounds in the all_totals list
    input_comp_name = "all_totals"

limit_heating_delta
-------------------

Used to limit the resolution (in meters) of the residential heating data. Is ignored if the smaller than the target subgrid resolution.

- Type: Decimal number (:code:`real`)
- Default value: :code:`250.0`

See also: :ref:`user_guide/configuration:subgrid_delta`

.. code-block:: fortran

    ! Example: Change the lower limit resolution of the shipping data to 150 m
    limit_heating_delta = 150.0

limit_industry_delta
--------------------

Used to limit the resolution (in meters) of the industry data. Is ignored if the smaller than the target subgrid resolution.

- Type: Decimal number (:code:`real`)
- Default value: :code:`250.0`

See also: :ref:`user_guide/configuration:subgrid_delta`

.. code-block:: fortran

    ! Example: Change the lower limit resolution of the industry data to 150 m
    limit_heating_delta = 150.0

limit_population_delta
----------------------

Used to limit the resolution (in meters) of the population data. Is ignored if the smaller than the target subgrid resolution.

- Type: Decimal number (:code:`real`)
- Default value: :code:`250.0`

See also: :ref:`user_guide/configuration:subgrid_delta`

.. code-block:: fortran

    ! Example: Change the lower limit resolution of the population data to 150 m
    limit_heating_delta = 150.0

limit_shipping_delta
--------------------

Used to limit the resolution (in meters) of the shipping data. Is ignored if smaller than the target subgrid resolution.

- Type: Decimal number (:code:`real`)
- Default value: :code:`250.0`

See also: :ref:`user_guide/configuration:subgrid_delta`

.. code-block:: fortran

    ! Example: Change the lower limit resolution of the shipping data to 150 m
    limit_shipping_delta = 150.0

local_fraction_naming_template_str
----------------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"sec<n>_local_fraction"`

NORTRIP_hour_str
----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"01"`

NORTRIP_replacement_hour_str
----------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"<>"`

pathname_agriculture
--------------------

- Type: Text string array (:code:`character(len=256), dimension(2)`)
- Default value: No default

pathname_boundingbox
--------------------

Used to specify the absolute path of the countries bounding box data.

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`) 

See also: :ref:`user_guide/configuration:auto_select_OSM_country_flag`, :ref:`user_guide/configuration:filename_boundingbox`

.. code-block:: fortran

    ! Example: Set the filename of the bounding box data
    filename_boundingbox = "<filename_of_bounding_box.txt>"

pathname_EMEP
-------------

Used to specify the absolute path of the EMEP NetCDF forcing data. Currently, 4 paths can be specified. The first text string is used to specify the location of the EMEP data including the meteorological data. The second text string is used to specify the location of the EMEP local fractions data. The third text string is used to specify the location of alternative EMEP meteorological data if necessary.

- Type: Text string array (:code:`character(len=256), dimension(4)`)
- Default value: No default

See also: :ref:`user_guide/configuration:filename_EMEP`, :ref:`user_guide/configuration:use_alternative_meteorology_flag`

.. code-block:: fortran

    ! Example: Set the path of the EMEP meteorology and local fractions
    pathname_EMEP(1) = "<path_to_emep_data>"
    pathname_EMEP(2) = "<path_to_emep_local_fractions_data>"

pathname_emissions_for_EMEP
---------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

pathname_heating
----------------

- Type: Text string array (:code:`character(len=256), dimension(10)`)
- Default value: No default

pathname_industry
-----------------

- Type: Text string array (:code:`character(len=256), dimension(10)`)
- Default value: No default

pathname_landuse
----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

pathname_log_file
-----------------

Used to specify the absolute path of the log file.

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

See also: :ref:`user_guide/configuration:filename_log_file`

.. code-block:: fortran

    ! Example: Set the path where the log file should be stored
    pathname_log_file = "<path_to_log_file>"

pathname_mrl
------------

- Type: Text string array (:code:`character(len=256), dimension(50)`)
- Default value: No default

pathname_output_grid
--------------------

Used to specify the absolute path of the uEMEP output. 

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

See also:

.. code-block:: fortran

    ! Example: Set the path of the uEMEP output
    pathname_output_grid = "<path_to_uemep_output>"

pathname_population
-------------------

- Type: Text string array (:code:`character(len=256), dimension(n_population_index)`)
- Default value: No default

pathname_receptor
-----------------

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

pathname_region_id
------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

pathname_region_mask
--------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

pathname_rl
-----------

Used to specify the absolute path of the roadlink input files if :code:`calculate_source(traffic_index) = .true.`.

- Type: Text string (:code:`character(len=256), dimension(2)`)
- Default value: No default

See also: :ref:`user_guide/configuration:calculate_source`, :ref:`user_guide/configuration:filename_rl`

.. code-block:: fortran

    ! Example: Set the path of the roadlink files
    pathname_rl(1) = "<path/to/roadlink/files/>"

pathname_rl_change
------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

pathname_ship
-------------

Used to specify the absolute path of the shipping proxy data if :code:`calculate_source(shipping_index) = .true.`.

- Type: Text string (:code:`character(len=256), dimension(2)`)
- Default value: No default

See also: :ref:`user_guide/configuration:filename_ship`, :ref:`user_guide/configuration:calculate_source`, :ref:`user_guide/configuration:read_shipping_from_netcdf_flag`

.. code-block:: fortran

    ! Example: Set the path of the shipping proxy data
    pathname_ship(1) = "<path/to/shipping/proxy/data/>"

pathname_tiles
--------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

pathname_timeprofile
--------------------

Used to specify the absolute path of the time profile data.

- Type: Text string (:code:`character(len=256)`)
- Default value: No default

See also: :ref:`user_guide/configuration:filename_timeprofile`

.. code-block:: fortran

    ! Example: Set the path of the time profile data
    pathname_timeprofile = "<path/to/time/profile/data/>"

projection_attributes
---------------------

Used to specify the attributes of the uEMEP projection. Currently 10 attributes can be set:

- Type: Decimal number (:code:`real, dimension(10)`)
- Default value: No default

See also: :ref:`user_guide/configuration:projection_type`

.. code-block:: fortran

    ! Set the projection attributes of the LCC projection
    projection_attributes(1) = 10.0
    projection_attributes(2) = 52.0
    projection_attributes(3) = 4321000.0
    projection_attributes(4) = 3210000.0
    projection_attributes(5) = 6378137.0
    projection_attributes(6) = 298.2572221

projection_type
---------------

Used to specify the projection type used by uEMEP and in the NetCDF output.

Currently, uEMEP supports seven projections:

1. Universal Transverse Mercator (UTM)
2. Rijks-Driehoek coordinates (RD)
3. Luxembourgh Transverse Mercator (LTM)
4. Lambert Azimuthal Equal Area (LAEA)
5. Lambert Conformal Conic (LCC)
6. Polar Stereographic (PS)
7. Latitude-Longitude (LL)

- Type: Integer (:code:`integer`)
- Default value: :code:`1`

See also: :ref:`user_guide/configuration:utm_zone`, :ref:`user_guide/configuration:projection_attributes`

.. code-block:: fortran

    ! Example: Set the projection type to LAEA
    projection_type = 4

read_shipping_from_netcdf_flag
------------------------------

Used to specify that shipping proxy data are in NetCDF format if the shipping emission source is included in the calculation. Currently this option is used for reading a global shipping data set and assumes the projection to be latitude-longitude.

- Type: Boolean (:code:`logical`)
- Default value: :code:`.false.`

See also: :ref:`user_guide/configuration:calculate_source`, :ref:`user_guide/configuration:pathname_ship`, :ref:`user_guide/configuration:filename_ship`

.. code-block:: fortran

    ! Example: Read shipping proxy data from netcdf
    read_shipping_from_netcdf_flag = .true.

region_name
-----------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

replacement_date_str
--------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"<>"`

replacement_hour_str
--------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"<>"`

replacement_yesterday_date_str
------------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"[]"`

save_emissions_for_EMEP_projection
----------------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`lambert`

save_emissions_for_EMEP_region
------------------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`NO`

save_tile_tag
-------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

select_country_by_name
----------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: Empty (:code:`""`)

sig_y_00
--------

Used to specify the initial horizontal dispersion parameter for each emission source (first dimension) and subsource (second dimension), i.e., :code:`sig_y_00(source_index,subsource_index)`. Subsources are currently not used in uEMEP.

- Type: Decimal number array (:code:`real, dimension(n_source_index,n_possible_subsource)`)
- Default values: 
  
  - Traffic: :code:`1.0`
  - Shipping: :code:`5.0`
  - Heating: :code:`5.0`
  - Agriculture: :code:`5.0`
  - Industry: :code:`5.0`
  - Aviation: :code:`25.0`
  - Other: :code:`10.0`

See also: :ref:`user_guide/configuration:h_emis`, :ref:`user_guide/configuration:sig_z_00`

.. code-block:: fortran

    ! Example: Set the initial horizontal dispersion parameter for traffic emissions to 2.0
    sig_y_00(traffic_index,1) = 2.0

sig_z_00
--------

Used to specify the initial vertical dispersion parameter for each emission source (first dimension) and subsource (second dimension), i.e., :code:`sig_z_00(source_index,subsource_index)`. Subsources are currently not used in uEMEP.

- Type: Decimal number array (:code:`real, dimension(n_source_index,n_possible_subsource)`)
- Default values: 

  - Traffic: :code:`1.0`
  - Shipping: :code:`5.0`
  - Heating: :code:`10.0`
  - Agriculture: :code:`10.0`
  - Industry: :code:`10.0`
  - Aviation: :code:`10.0`
  - Other: :code:`10.0`

See also: :ref:`user_guide/configuration:h_emis`, :ref:`user_guide/configuration:sig_y_00`

.. code-block:: fortran

    ! Example: Set the initial vertical dispersion parameter for shipping emissions to 10.0
    sig_z_00(shipping_index,1) = 10.0

tile_tag
--------

- Type: Text string (:code:`character(len=256)`)
- Default value: No default (:code:`""`)

start_time_meteo_nc_index
-------------------------

Used to set the first time index of the alternative EMEP NetCDF file if an alternative meteorology is used.

- Type: Integer (:code:`integer`)
- Default value: :code:`1`

See also: :ref:`user_guide/configuration:end_time_meteo_nc_index`, :ref:`user_guide/configuration:use_alternative_meteorology_flag`

.. code-block:: fortran

    ! Example: Set the first time index value to the default value
    start_time_meteo_nc_index = 1

start_time_nc_index
-------------------

Used to set the first time index of the EMEP NetCDF file.

- Type: Integer (:code:`integer`)
- Default value: :code:`1`

See also: :ref:`user_guide/configuration:end_time_nc_index`

.. code-block:: fortran

    ! Example: Set the first time index value to the default value
    start_time_nc_index = 1

subgrid_max
-----------

Used to specify the upper spatial boundary of the subgrid for each horizontal dimension individually. Value and units are dependent on :ref:`user_guide/configuration:projection_type` and :ref:`user_guide/configuration:projection_attributes`.

- Type: Decimal number (:code:`real`)
- Default value: No default

See also: :ref:`user_guide/configuration:subgrid_min`, :ref:`user_guide/configuration:subgrid_delta`, :ref:`user_guide/configuration:projection_type`, :ref:`user_guide/configuration:projection_attributes`

.. code-block:: fortran

    ! Example: Set the upper subgrid boundary using LCC coordinates (units in meters)
    subgrid_max(x_dim_index) = 4850000.0
    subgrid_max(y_dim_index) = 3400000.0

subgrid_min
-----------

Used to specify the lower spatial boundary of the subgrid for each horizontal dimension individually. Value and units are dependent on :ref:`user_guide/configuration:projection_type` and :ref:`user_guide/configuration:projection_attributes`.

- Type: Decimal number (:code:`real`)
- Default value: No default

See also: :ref:`user_guide/configuration:subgrid_max`, :ref:`user_guide/configuration:subgrid_delta`, :ref:`user_guide/configuration:projection_type`, :ref:`user_guide/configuration:projection_attributes`

.. code-block:: fortran

    ! Example: Set the lower subgrid boundary using LCC coordinates (units in meters)
    subgrid_min(x_dim_index) = 4600000.0
    subgrid_min(y_dim_index) = 3150000.0

subgrid_delta
-------------

Used to set resolution (in meters) of the subgrids for each horizontal dimension individually.

- Type: Decimal number (:code:`real, dimension(2)`)
- Default value: No default

See also: :ref:`user_guide/configuration:subgrid_min`, :ref:`user_guide/configuration:subgrid_max`

.. code-block:: fortran

    ! Set the resolution of the subgrids to 250 meters
    subgrid_delta(x_dim_index) = 250.0
    subgrid_delta(y_dim_index) = 250.0

use_alternative_meteorology_flag
--------------------------------

Used to specify if an alternative meteorology should be used. If :code:`use_alternative_meteorology_flag` is set to :code:`.true.`, then :ref:`user_guide/configuration:pathname_EMEP` and :ref:`user_guide/configuration:filename_EMEP` pointing to the alternative meteorology should also be specified. 

- Type: Boolean (:code:`logical`)
- Default value: :code:`.false.`

See also: :ref:`user_guide/configuration:pathname_EMEP`, :ref:`user_guide/configuration:filename_EMEP`, :ref:`user_guide/configuration:alternative_meteorology_type` 

.. code-block:: fortran

    ! Specify that an alternative meteorology should be used
    use_alternative_meteorology_flag = .true.

use_single_time_loop_flag
-------------------------

- Type: Boolean (:code:`logical`)
- Default value: :code:`.false.`

utm_zone
--------

Used to set the UTM zone if the projection type is either UTM or LTM.

- Type: Integer (:code:`integer`)
- Default value: :code:`33`

See also: :ref:`user_guide/configuration:projection_type`

.. code-block:: fortran

    ! Example: Set the utm zone to the default value
    utm_zone = 33

var_name_landuse_nc
-------------------

- Type: Text string array (:code:`character(len=256), dimension(num_var_landuse_nc)`)
- Default value:

    - Other variables: :code:`"Band1"`

var_name_nc
-----------

Used to override NetCDF variable names if these differ from the default names.

- Type: Text string array (:code:`character(len=256), dimension(num_var_nc_name,n_pollutant_nc_index,n_source_nc_index)`)
- Default value: Please see the `set_constants routine <https://metno.github.io/uEMEP/proc/uemep_set_constants.html>`_ in the `code documentation <https://metno.github.io/uEMEP/index.html>`_ for details.

See also:

.. code-block:: fortran

    ! Example: Override the variable name for the o3 concentration (default: "o3")
    var_name_nc(conc_nc_index,o3_nc_index,allsource_nc_index) = "conc_o3"

var_name_population_nc
----------------------

- Type: Text string array (:code:`character(len=256), dimension(num_var_population_nc)`)
- Default value:

    - Population variable name: :code:`"Band1"`
    - Dwelling variable name: :code:`"Band1"`
    - Other variable names: No default

varname_region_mask
-------------------

- Type: Text string (:code:`character(len=256)`)
- Default value: :code:`"region_index"`
