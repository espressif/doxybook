<a href="https://www.espressif.com">
    <img src="https://www.espressif.com/sites/all/themes/espressif/logo-black.svg" align="right" height="20" />
</a>

# CHANGELOG

> All notable changes to this project are documented in this file.
> This list is not exhaustive - only important changes, fixes, and new features in the code are reflected here.

<div style="text-align: center;">
    <a href="https://keepachangelog.com/en/1.1.0/">
        <img alt="Static Badge" src="https://img.shields.io/badge/Keep%20a%20Changelog-v1.1.0-salmon?logo=keepachangelog&logoColor=black&labelColor=white&link=https%3A%2F%2Fkeepachangelog.com%2Fen%2F1.1.0%2F">
    </a>
    <a href="https://www.conventionalcommits.org/en/v1.0.0/">
        <img alt="Static Badge" src="https://img.shields.io/badge/Conventional%20Commits-v1.0.0-pink?logo=conventionalcommits&logoColor=black&labelColor=white&link=https%3A%2F%2Fwww.conventionalcommits.org%2Fen%2Fv1.0.0%2F">
    </a>
    <a href="https://semver.org/spec/v2.0.0.html">
        <img alt="Static Badge" src="https://img.shields.io/badge/Semantic%20Versioning-v2.0.0-grey?logo=semanticrelease&logoColor=black&labelColor=white&link=https%3A%2F%2Fsemver.org%2Fspec%2Fv2.0.0.html">
    </a>
</div>
<hr>

## v0.3.0 (2025-08-06)

### ✨ New Features

- Add Group Support *(HalfSweet - 02ff254)*


## v0.2.5 (2025-07-10)

### 🐛 Bug Fixes

- **windows**: close temp filestream first before moving the file *(Fu Hanxi - 64a703e)*


## v0.2.4 (2025-05-23)


## v0.2.3 (2025-05-23)

### 🐛 Bug Fixes

- add groups while template rendering *(Fu Hanxi - 2efafb7)*


## v0.2.2 (2024-10-25)

### 🐛 Bug Fixes

- excape pipe symbol in the markdown table *(suda-morris - 13a58d2)*
- will create the file correctly when only pass the filename *(Fu Hanxi - 17ee98b)*


## v0.2.1 (2023-09-20)

### 🐛 Bug Fixes

- better error message while pre-commit *(Fu Hanxi - bd15744)*
- swallow doxygen traceback, print stderr with color, if not windows *(Fu Hanxi - b5e4654)*


## v0.2.0 (2023-09-18)

### ✨ New Features

- Support only single-markdown file, remove other markdown types *(Fu Hanxi - b19611f)*

### 🐛 Bug Fixes

- add extra blank lines before list items *(Fu Hanxi - 1802dcb)*
- spacing between ref and paras *(Fu Hanxi - d72d309)*
- some mypy complains *(Fu Hanxi - 91a1d8d)*
- add extra line between details and variables if variable exists *(Fu Hanxi - 4c15133)*
- support list in details *(Fu Hanxi - 8881ba5)*

### 📖 Documentation

- add pre-commit guide *(Fu Hanxi - 4f22405)*


## v0.1.0 (2023-08-10)

### ✨ New Features

- **cpp**: add cpp support *(Fu Hanxi - 58eed59)*
- **c**: improve template output *(Fu Hanxi - 9cd5788)*
- **c**: improve node id without anchor declaration for files *(Fu Hanxi - aefb772)*
- show brief and detailed descriptions for struct members *(Ivan Grokhotkov - 0a6a9d0)*
- show brief and detailed description for C functions *(Ivan Grokhotkov - 95a561b)*
- combine Classes and Types section into "Structures and Types" *(Ivan Grokhotkov - 6e37763)*
- call doxygen inside *(Fu Hanxi - 9b59a13)*
- output could be a file *(Fu Hanxi - 98e908b)*
- add SUPPORTED_LANGS constant *(Fu Hanxi - d5423f8)*
- improve node id without anchor declaration *(Fu Hanxi - 61936b1)*
- use new pyproject.toml *(Fu Hanxi - 03e4b9e)*
- make itself pre-commit hook *(Fu Hanxi - 2723af3)*
- add command "generate-templates" to generate the default template files *(Fu Hanxi - be18544)*
- support target "single-markdown" for c *(Fu Hanxi - 165f125)*
- `node.query` support optional arguments *(Fu Hanxi - 3c04825)*
- update getchildren() to list() *(Fu Hanxi - 109d908)*

### 🐛 Bug Fixes

- **build**: add cpp keyword *(Fu Hanxi - 3acffc5)*
- **build**: remove external data *(Fu Hanxi - 8a41e3c)*
- use empty footer to be compatible with pre-commit workflow *(Ivan Grokhotkov - 6ef13cd)*
- correctly check for presence of brief description *(Ivan Grokhotkov - dd76165)*
- location_url_safe remove more special characters *(Fu Hanxi - f377447)*
- use name_url_safe instead of location_url_safe *(Fu Hanxi - 668d14f)*
- check doxygen output *(Fu Hanxi - 916c82d)*
- rename `run` argument `input` since it's a python keyword *(Fu Hanxi - 2fe93ff)*
- entry for pre-commit hook *(Fu Hanxi - 6c81766)*
- missing empty line for a list *(Fu Hanxi - a5c9394)*
- filesystem loader with `--template-dirs` *(Fu Hanxi - 85d0b31)*
- add manifest.in for template files *(Fu Hanxi - b967be4)*
- console_script *(Fu Hanxi - 124ead7)*
- strip the strings *(Fu Hanxi - 45ff9c0)*
- relative import error *(Fu Hanxi - 2913ad2)*

### 🔧 Code Refactoring

- move the old python templates into `templates_python` *(Fu Hanxi - c53fe9c)*

---

<div style="text-align: center;">
    <small>
        <b>
            <a href="https://www.github.com/espressif/cz-plugin-espressif">Commitizen Espressif plugin</a>
        </b>
    <br>
        <sup><a href="https://www.espressif.com">Espressif Systems CO LTD. (2025)</a><sup>
    </small>
</div>
