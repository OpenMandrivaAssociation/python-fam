Summary:	Python FAM module
Name:		python-fam
Version:	2.0.13
Release:	1
License:	GPLv2
Group:		Development/Python
Url:		http://python-fam.sourceforge.net/
Source0:	https://files.pythonhosted.org/packages/a8/8f/d500d7be5662bb2606f289c7d26d8c99125c4a4ca7cf39faa144f0d3a94f/fam-2.0.13.tar.gz
BuildRequires:	fam-devel
BuildRequires:  pkgconfig(python)

%description
Python FAM is a wrapper module around libfam from the FAM project. It
allows Python programs to monitor files and directories. An example
script is included.

%prep
%setup -qn fam-%{version}
%apply_patches

%build
find . -name "*.py" -exec 2to3 -w {} \;
%py_build

%install
%py_install

%files
%{python_sitelib}/*
