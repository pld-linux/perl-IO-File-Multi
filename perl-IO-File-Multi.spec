%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	File-Multi
Summary:	IO::File::Multi perl module
Summary(pl):	Modu³ perla IO::File::Multi
Name:		perl-IO-File-Multi
Version:	1.02
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ad39ab26c2b3554d883b896ab7e18cc
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-FileHandle-Multi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::File::Multi - Print to multiple filehandles with one output call.

%description -l pl
IO::File::Multi umo¿liwia pisanie do wielu uchwytów pliku
jednocze¶nie przy jednorazowym wywo³aniu funkcji print() lub printf().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/IO/File
%{perl_vendorlib}/IO/File/Multi.pm
%{_mandir}/man3/*
