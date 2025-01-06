# uEMEP documentation

This repository contains the documentation for the [uEMEP model](https://github.com/metno/uEMEP). The documentation is hosted at [Read the Docs](https://uemep.readthedocs.io).

## Building the documentation

The documentation is build using Sphinx. To build the documentation locally:

```bash
# Clone the repository
git clone https://github.com/metno/uEMEP_docs.git
cd uEMEP_docs

# Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt

# Build documentation
sphinx-build -M html docs/source/ docs/build/
```
After the initial build process, the documentation can be build using the generated `Makefile` directory. Please note that due to caching, it is sometimes necessary to run `make clean` prior to building the documentation.

```bash
# Build documentation
cd docs
make html
```

The documentation can then be accessed by opening `docs/build/html/index.html`.

## Contributing

We welcome contributions from the community. Whether you want to improve the documentation, report errors, suggest new sections, or discuss other issues, your input is valued. 

For contributing directly to the documentation, please fork the repository, make your changes, and submit a pull request with a description of what you have improved. For any other suggestions, errors or issues, please use the issue tracker to communicate with us.
