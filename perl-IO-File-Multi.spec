%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	File-Multi
Summary:	IO::File::Multi perl module
Summary(pl):	Modu³ perla IO::File::Multi
Name:		perl-IO-File-Multi
Version:	1.02
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Obsoletes:	perl-FileHandle-Multi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::File::Multi - Print to multiple filehandles with one output call.

%description -l pl
IO::File::Multi umo¿liwia drukowanie do wielu uchwytów pliku
jednocze¶nie przy jednorazowym wywo³aniu funkcji print() lub printf().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/IO/File/Multi.pm
%{_mandir}/man3/*
