%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Summary: Python FAM module
Name: python-fam
Version: 1.1.1
Release: %mkrel 8
Source0: http://prdownloads.sourceforge.net/python-fam/%{name}-%{version}.tar.bz2
Patch0: python-fam-1.0.2-gamin.patch
# (fc) 1.1.1-5mdv fix crash (Debian)
Patch1: python-fam-1.1.1-fixcrash.patch
License: GPL
Group: Development/Python
URL: http://python-fam.sourceforge.net/
%py_requires -d
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: fam-devel

%description
Python FAM is a wrapper module around libfam from the FAM project. It
allows Python programs to monitor files and directories. An example
script is included.

%prep
%setup -q
%patch0 -p1 -b .gamin
%patch1 -p1 -b .fixcrash
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




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-7mdv2011.0
+ Revision: 667932
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-6mdv2011.0
+ Revision: 523767
- rebuilt for 2010.1

* Thu Mar 19 2009 Frederic Crozat <fcrozat@mandriva.com> 1.1.1-5mdv2009.1
+ Revision: 357878
- Patch1 (Debian): fix crash in memory management

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 1.1.1-4mdv2009.1
+ Revision: 319836
- rebuild for new python

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2009.0
+ Revision: 225129
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2mdv2008.1-current
+ Revision: 125926
- kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.1-2mdv2007.0
+ Revision: 96538
- Rebuild against new python
- Import python-fam

* Fri Dec 09 2005 Frederic Lepied <flepied@mandriva.com> 1.1.1-1mdk
- New release 1.1.1

* Sun Dec 19 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.0.2-5mdk
- Buildrequires fam-devel
- fix to compile with gamin

