Summary:	Python FAM module
Name:		python-fam
Version:	1.1.1
Release:	18
Patch1:		python-fam-1.1.1-fixcrash.patch
License:	GPLv2
Group:		Development/Python
Url:		http://python-fam.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/python-fam/%{name}-%{version}.tar.bz2
Patch0:		python-fam-1.0.2-gamin.patch
BuildRequires:	fam-devel
BuildRequires:  pkgconfig(python2)

%description
Python FAM is a wrapper module around libfam from the FAM project. It
allows Python programs to monitor files and directories. An example
script is included.

%prep
%setup -q
%apply_patches
chmod 755 test.py

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=%{buildroot}

%files
%doc test.py
%{py2_platsitedir}/*

