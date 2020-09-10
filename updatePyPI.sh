rm -r ./dist ./build ./shlnb.egg-info
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*
python3 -m pip install --upgrade shlnb


# 2. Delete the /dist /build /...-info directories`.
# 3. Update the version number and required_modules (if necessary) in setup.py.
# 4. Update the changelog in the package's README.md (NOT in this README.md).
# 5. In terminal, navigate using the `cd` command to [[MODULE-NAME1]]. To regenerate updated /dist directory, run in terminal: `python3 setup.py sdist bdist_wheel`
# 6. (Optional) Update package git repo, make sure to include package release version in commit message.
# 7. Upload updated package to PyPI by entering in terminal: `python3 -m twine upload --repository pypi dist/*`
# 8. Update package installed on computer by entering in terminal `python3 -m pip install [[MODULE-NAME]] --upgrade`. Check that the module has been successfully update by entering `python3 -m pip show [[MODULE-NAME]]`