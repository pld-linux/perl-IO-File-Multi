%include	/usr/lib/rpm/macros.perl
Summary:	IO-File-Multi perl module
Summary(pl):	Modu³ perla IO-File-Multi
Name:		perl-IO-File-Multi
Version:	1.02
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-File-Multi-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Obsoletes:	perl-FileHandle-Multi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-File-Multi - Print to multiple filehandles with one output call.

%description -l pl
IO-File-Multi umo¿liwia drukowanie do wielu uchwytów pliku
jednocze¶nie przy jednorazowym wywo³aniu funkcji print() lub printf().

%prep
%setup -q -n IO-File-Multi-%{version}

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
