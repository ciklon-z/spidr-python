This client (and API) connects to the Space Physics Interactive Data Resource (SPIDR) to obtain space weather data.

http://spidr.ngdc.noaa.gov/spidr/

```

Installation:
------------------

% python setup.py install


Usage Example Post-Installation:
------------------

If for no other reason than to confirm install succeeded, you can...

% python
% >>> from spidr_python import spidr_api
% >>> spidr_api.get_data('iono_fof2.bc840','20100101','20100102')

```

spidr\_python.py also has simple examples of integration.