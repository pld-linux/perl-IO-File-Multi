#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	File-Multi
Summary:	IO::File::Multi perl module
Summary(pl.UTF-8):	Moduł perla IO::File::Multi
Name:		perl-IO-File-Multi
Version:	1.02
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ad39ab26c2b3554d883b896ab7e18cc
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-FileHandle-Multi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::File::Multi - Print to multiple filehandles with one output call.

%description -l pl.UTF-8
IO::File::Multi umożliwia pisanie do wielu uchwytów pliku
jednocześnie przy jednorazowym wywołaniu funkcji print() lub printf().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/IO/File
%{perl_vendorlib}/IO/File/Multi.pm
%{_mandir}/man3/*
