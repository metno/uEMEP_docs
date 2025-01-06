.. include:: ../substitutions.txt

Model Description
=================

This page includes a description of the uEMEP model.

Introduction
------------

Methodology
-----------

uEMEP can use two downscaling methods, both of which are employing Gaussian dispersion modeling to achieve redistribution of concentrations in high resolution (:footcite:t:`denby2020`). Both methods also utilize the "local fraction" feature in the EMEP model (:footcite:t:`wind2020`) to avoid double counting of emissions and to allow near-seamless integration of the two models:

1. Emission redistribution
2. Independent emissions

Subgrid calculation method
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::
    :label: eq:total_subgrid_conc

    C_{SG}(i,j) = C_{SG,local}(i,j) + C_{SG,nonlocal}(i,j)

.. math::
    :label: eq:local_subgrid_conc

    C_{SG,local}(i,j) = \sum_{i'=1}^{n_{x}} \sum_{j'=1}^{n_{y}} \frac{E_{SG,local}(i',j')}{U(i,j,i',j')} I\left(r(i,j,i',j'),h(i',j'),z(i,j)\right)

Where :math:`E_{SG,local}` is the emission in each subgrid, :math:`U` is the wind speed which in uEMEP is dependent on the source and receptor subgrid values (see :ref:`user_guide/model_description:Gaussian plume model for hourly calculations`). :math:`n_{x}` and :math:`n_{y}` are the extent of the subgrid calculation window...

.. math::
    :label: eq:local_subgrid_emis

    E_{SG,local}(i',j') = E_{G}(I,J) \frac{P_{emission}(i',j')}{ \sum_{i'=1}^{n_{x}} \sum_{j'=1}^{n_{y}} P_{emission}(i',j') }

EMEP non-local contribution calculation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. eq 4
.. math::
    :label: eq:local_grid_conc

    C_{G,local}(I,J,I_{lf},J_{lf},s) = LF(I,J,I_{lf},J_{lf},s) \; C_{G}(I,J)

.. eq 5
.. math::
    :label: eq:nonlocal_grid_conc

    C_{G,nonlocal}(I,J) = C_{G}(I,J) - \left\{ \sum_{I'=-n_{mw}/2}^{+n_{mw}/2} \sum_{J'=-n_{mw}/2}^{+n_{mw}/2} \sum_{s=1}^{n_{source}} \; C_{G,local}(I,J,I',J',s) \right\}

Moving windows calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. eq 6
.. math::
    :label: eq:emep_local_contr

    C_{G,local}(i,j,s) = \sum_{I'=-n_{mw}/2}^{+n_{mw}/2} \sum_{J'=-n_{mw}/2}^{+n_{mw}/2} C_{G,local}(I,J,I',J',s) \; w(i,j,I',J',s)

.. eq 7
.. math::
    :label: eq:area_weighting

    w_{a}(i,j,I',J') = \frac{\{ a(i,j) \cap A(I',J') \}}{A(I',J')}

.. eq 8
.. math::
    :label: eq:emis_weihting

    w_{e}(i,j,I',J',s) = \frac{ \sum e(i,j,I',J',s) :\in \{ a(i,j) \cap A(I',J') \} } { \sum e(i,j,I',J',s) :\in \{ A(I',J') \} }

.. eq 9
.. math::
    :label: eq:emep_nonlocal_contr

.. eq 10
.. math::
    :label: eq:nonlocal_subgrid_contr

    C_{SG,nonlocal}(i,j) = \frac{1}{n_{source}} \sum_{s=1}^{n_{source}} \left\{ (C_{G,local}(i,j,s) + C_{G,nonlocal}(i,j,s)) \right\} - \sum_{s=1}^{n_{source}} \left\{ C_{G,local}(i,j,s) \right\}

Processes and parameterization
------------------------------

Gaussian plume model for hourly calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A standard Gaussian narrow plume dispersion model formulation is used in the subgrid dispersion calculations with multiple reflections from the surface (:math:`z = 0`) and boundary layer height (:math:`z = H`). Generally, the Gaussian plume calculation can be written as:

.. eq 11
.. math::
    :label: eq:standard_gaussian
 
    C(x,y,z) = \frac{Q}{U} I(x,y,z)

.. eq 12
.. math::
    :label: eq:std_gaussian_plume_intensity

    I(x,y,z) = \frac{1}{2 \pi \sigma_{y} \sigma_{z}} \mathrm{exp}\left(\frac{-y^{2}}{2 \sigma_{y}^{2}}\right) \sum_{i=1}^{i=6} \left\{ \mathrm{exp}(\frac{-(z - h_{i})^{2}}{2 \sigma_{z}^{2}}) \right\}

.. eq 13
.. math::
    :label: eq:plume_emission_height

    h_{i} = [ h_{emis}, -h_{emis}, 2H - h_{emis}, 2H + h_{emis}, -2H + h_{emis}, -2H - h_{emis} ]

.. eq 14
.. math::
    :label: eq:std_gaussian_well_mixed_plume_intensity

    I(x,y,z) = \frac{1}{\sqrt{2 \pi} \sigma_{y} H} \mathrm{exp}\left(\frac{-y^{2}}{2 \sigma_{2}^{2}}\right)

.. eq 15a
.. math::
    :label: eq:dispersion_param_z

    \sigma_{z}(t) = \sigma_{z0} + \sqrt{2 K_{z}(z) t f_{t}}

.. eq 15b
.. math::
    :label: eq:dispersion_param_y

    \sigma_{y}(t) = \sigma_{y0} + \sqrt{2 K_{y}(z) t f_{t}}

.. eq 16
.. math::
    :label: eq:factor_langrangian_integral_timescale

    f_{t} = 1 + \left(\frac{\tau_{l}}{t} \mathrm{exp}\left(- \frac{t}{\tau_{l}}\right) - 1\right)

Where :math:`\tau_{l}` is the Lagrangian integral timescale, calculated following :footcite:t:`hanna1981` as:

.. eq 17
.. math::
    :label: eq:lagrangian_integral_timescale

    \tau_{l} = 0.6 \frac{\mathrm{max}(z_{emis}, z_{\tau min})}{u_{*}}

Where :math:`z_{emis}` is the emission height, :math:`z_{\tau min}` is the minimum emission height (2 meters), and :math:`u_{*}` is the friction velocity.

.. eq 18
.. math::
    :label: eq:lagrangian_integral_timescale_time

    t = \frac{\mathrm{max}(x_{min},x)}{U(z)}

Where :math:`x_{min}` is half a subgrid, :math:`U(z)` is the vertical wind speed profile, and :math:`x` is the down-plume distance.

.. eq 19
.. math::
    :label: eq:plume_mass_center_int

    z_{cm} = \frac{\int_{0}^{H} z I(z) dz}{\int_{0}^{H} I(z) dz}

Solving this integral analytically yields:

.. eq 20
.. math::
    :label: eq:plume_mass_center_solved

    z_{cm} = &\frac{\sigma_{z}}{\sqrt{2\pi}} \sum_{i=1}^{i=6} \mathrm{exp}\left( \frac{-h_{i}^{2}}{2\sigma_{z}^{2}} \right) - \mathrm{exp}\left( \frac{-(H - h_{i})^{2}}{2\sigma_{z}^{2}} \right)

    &+ \frac{h_{i}}{2} \left( \mathrm{erf}\left( \frac{h_{i}}{\sqrt{2}\sigma_{z}}\right) + \mathrm{erf}\left( \frac{(H - h_{i})}{\sqrt{2}\sigma_{z}} \right) \right)

For the the well-mixed case where :math:`\sigma_{z} > 0.9H`:

.. eq 21
.. math::
    :label: eq:plume_mass_center_well_mixed

    z_{cm} = 0.5H

The vertical wind profile is calculated based on decreasing turbulent shear with height following :footcite:t:`gryning2007`:

.. eq 22
.. math::
    :label: eq:vertical_wind_profile

    U(z) = \frac{u_{* 0}}{\kappa} \left( \mathrm{log}\left( \frac{z}{z_{0}} \right) - \psi_{m} + \kappa \frac{z}{z_{l}} \left( 1 - \frac{z}{2H} \right) - \frac{z}{H} \left( 1 + b \frac{z}{2L} \right) \right) \; \mathrm{for} \; L \ge 0

    U(z) = \frac{u_{* 0}}{\kappa} \left( \mathrm{log}\left( \frac{z}{z_{0}} \right) - \psi_{m} + \kappa \frac{z}{z_{l}} \left( 1 - \frac{z}{2H} \right) - \frac{z}{H} \frac{((az - L) \phi_{m} + L)}{a(p + 1)} \right) \; \mathrm{for} \; L < 0

.. eq 23
.. math::
    :label: eq:horiz_eddy_diff_ky

    K_{y}(z) = \frac{\sigma_{v}(z)^{2}}{\sigma_{w}(z)^{2}} K_{z}(z)

Rotationally symmetric Gaussian plume model for annual mean calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. eq 24
.. math::
    :label: eq: dispersion_param_power_function

    \sigma_{y,z} = \sigma_{0(y,z)} + a_{y,z} x^{b_{y,z}}

.. eq 25
.. math::
    :label: eq:rotationally_symmetric_gaussian_plume_intensity

    I_{rot}(r,z) =& \frac{1}{\pi \sqrt{2\pi}r\varepsilon_{z}\sqrt{1 + B}} \mathrm{erf}\left( \frac{\pi \sqrt{1 + B}}{\sqrt{2}\varepsilon_{\theta}} \right)

    &\sum_{i=1}^{i=6} \left\{ \mathrm{exp} \left( \frac{-(z - h_{i})^{2}}{2\varepsilon_{z}^{2}} \right) \right\}

where

.. eq 26a
.. math:: 
    :label: eq:epsilon_z

    \varepsilon_{z} = \sigma_{0z} + a_{z} r^{b_{z}}

.. eq 26b
.. math::
    :label: eq:epsilon_theta

    \varepsilon_{\theta} = \frac{1}{r} \left( \sigma_{0y} + a_{y} r^{b_{y}} \right)

.. eq 26c
.. math::
    :label: eq:b

    B = -\varepsilon_{\theta}^{2} \left( \frac{b_{z}(\varepsilon_{z} - \sigma_{0z})}{r \varepsilon_{\theta}} + \frac{b_{y}(r\varepsilon_{\theta} - \sigma_{0y})}{\varepsilon_{z}} \right)

.. eq 27
.. math::
    :label: :label: eq:rotationally_symmetric_gaussian_plume_intensity_taylor_exp

    I_{rot}(r,z) =& \frac{1}{2 \pi r \varepsilon_{z} \varepsilon_{\theta}} \left( 1 - \frac{\pi^{2} (1 + B)}{6\varepsilon_{\theta}^{2}} + \frac{\pi^{4}(1 + B)^{2}}{40\varepsilon_{\theta}^{4}} \right)

    &\sum_{i=1}^{i=6} \left\{ \mathrm{exp} \left( \frac{-(z - h_{i})^{2}}{2\varepsilon_{z}^{2}} \right) \right\} \; \mathrm{for} \; B < -1

Initial dispersion
^^^^^^^^^^^^^^^^^^

.. eq 28
.. math::
    :label: eq:initial_dispersion

    \sigma_{0y} = \sigma_{init,y} + 0.8 \frac{\Delta y}{2}

|NO2| chemistry for hourly means
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. eq 29a,b,c
.. math::
    :label: eq:no2_reactions

    \mathrm{NO + O_{3} \to NO_{2} + O_{2}} \qquad \mathrm{(a)}

    \mathrm{NO_{2}} + hv \to \mathrm{NO + O} \qquad \mathrm{(b)}

    \mathrm{O_{2} + O} + M \to \mathrm{O_{3}} + M \qquad \mathrm{(c)}

.. eq 30
.. math::
    :label: eq:no2_diff_eqn

    \frac{\mathrm{d[NO_{2}]}}{\mathrm{d}t} = k_{1} \mathrm{[NO][O_{3}]} - J \mathrm{[NO_{2}]}

.. eq 31
.. math::
    :label: eq:reaction_rate

    k_{1} = 1.4 \times 10^{-12} \mathrm{exp} \left( \frac{-1310}{T_{air}} \right) (\mathrm{cm^{3} \; s^{-1}})

References
----------

.. footbibliography:: 