%define name perl-OpenOffice-OOBuilder
%define pkgname OpenOffice-OOBuilder
%define version 0.09
%define release %mkrel 1

Summary:	Perl OO interface for creating OpenOffice documents
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/OpenOffice/%{pkgname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{pkgname}/
BuildRequires:	perl-devel
BuildRequires:  perl(Archive::Zip)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot/

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
%setup -q -n %{pkgname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%{perl_vendorlib}/
%{_mandir}/*/*

