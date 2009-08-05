%define upstream_name    OpenOffice-OOBuilder
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl OO interface for creating OpenOffice documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/OpenOffice/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Archive::Zip)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
