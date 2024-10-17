%define upstream_name    OpenOffice-OOBuilder
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl OO interface for creating OpenOffice documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/OpenOffice/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Zip)
BuildArch:	noarch

%description
This is a collection of modules to create OpenOffice documents. 
At this moment OpenOffice spreadsheets (calc documents) are 
supported. Other OpenOffice documents will follow depending 
on time and feedback. 

The modules present in this collection are:

  OpenOffice::OOBuilder - The base class. For each OpenOffice 
      document type, another class will be inherited from this
      base class.
      
  OpenOffice::OOCBuilder - For creating OpenOffice calc documents:
      spreadsheets, documents with the sxc extension.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc README 
%{perl_vendorlib}/
%{_mandir}/*/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 655151
- rebuild for updated spec-helper

* Wed Aug 05 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 410066
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.09-3mdv2009.0
+ Revision: 241809
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 26 2007 Pascal Terjan <pterjan@mandriva.org> 0.09-1mdv2008.0
+ Revision: 55904
- 0.09

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.08-4mdv2008.0
+ Revision: 16470
- Rebuild to have consistent mkrel


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Mon Nov 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-2mdk
- Fix BuildRequires

* Mon Sep 05 2005 Pascal Terjan <pterjan@mandriva.org> 0.08-1mdk
- First version of the package

