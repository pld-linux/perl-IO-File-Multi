%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	IO-File-Multi perl module
Summary(pl):	Modu� perla IO-File-Multi
Name:		perl-IO-File-Multi
Version:	1.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-File-Multi-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
IO-File-Multi - Print to multiple filehandles with one output call.

%description -l pl
IO-File-Multi umo�liwia drukowanie do wielu uchwyt�w pliku jednocze�nie
przy jednorazowym wywo�aniu funkcji print() lub printf().

%prep
%setup -q -n IO-File-Multi-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/IO/File/Multi
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/IO/File/Multi.pm
%{perl_sitearch}/auto/IO/File/Multi

%{_mandir}/man3/*
