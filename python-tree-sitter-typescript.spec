Name:		python-tree-sitter-typescript
Version:	0.23.2
Release:	1
Summary:	Tree-sitter typescript grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-typescript
Source0:	https://files.pythonhosted.org/packages/1e/fc/bb52958f7e399250aee093751e9373a6311cadbe76b6e0d109b853757f35/tree_sitter_typescript-0.23.2.tar.gz
# PyPI sdist omits src/tree_sitter/*.h
Source1:	tree-sitter-c-headers.tar.xz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for typescript, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_typescript-0.23.2
tar -xf %{SOURCE1}

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_typescript*
