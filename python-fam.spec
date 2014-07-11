%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Summary:	Python FAM module
Name:		python-fam
Version:	1.1.1
Release:	14
Patch1:		python-fam-1.1.1-fixcrash.patch
License:	GPLv2
Group:		Development/Python
Url:		http://python-fam.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/python-fam/%{name}-%{version}.tar.bz2
Patch0:		python-fam-1.0.2-gamin.patch
BuildRequires:	fam-devel
BuildRequires:  python-devel

%description
Python FAM is a wrapper module around libfam from the FAM project. It
allows Python programs to monitor files and directories. An example
script is included.

%prep
%setup -q
%apply_patches
chmod 755 test.py

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc test.py
%{py_platsitedir}/*

