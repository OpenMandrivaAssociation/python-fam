%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Summary: Python FAM module
Name: python-fam
Version: 1.1.1
Release: %mkrel 3
Source0: http://prdownloads.sourceforge.net/python-fam/%{name}-%{version}.tar.bz2
Patch0: python-fam-1.0.2-gamin.patch
License: GPL
Group: Development/Python
URL: http://python-fam.sourceforge.net/
Requires: python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: python-devel, fam-devel

%description
Python FAM is a wrapper module around libfam from the FAM project. It
allows Python programs to monitor files and directories. An example
script is included.

%prep
%setup -q
%patch0 -p1 -b .gamin
chmod 755 test.py

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc test.py
%py_platsitedir/*


