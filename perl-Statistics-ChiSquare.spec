#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	ChiSquare
Summary:	Statistics::ChiSquare Perl module
Summary(cs):	Modul Statistics::ChiSquare pro Perl
Summary(da):	Perlmodul Statistics::ChiSquare
Summary(de):	Statistics::ChiSquare Perl Modul
Summary(es):	Módulo de Perl Statistics::ChiSquare
Summary(fr):	Module Perl Statistics::ChiSquare
Summary(it):	Modulo di Perl Statistics::ChiSquare
Summary(ja):	Statistics::ChiSquare Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Statistics::ChiSquare ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Statistics::ChiSquare
Summary(pl):	Modu³ Perla Statistics::ChiSquare
Summary(pt):	Módulo de Perl Statistics::ChiSquare
Summary(pt_BR):	Módulo Perl Statistics::ChiSquare
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Statistics::ChiSquare
Summary(sv):	Statistics::ChiSquare Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Statistics::ChiSquare
Summary(zh_CN):	Statistics::ChiSquare Perl Ä£¿é
Name:		perl-Statistics-ChiSquare
Version:	0.3
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics::ChiSquare - How random is your data?

%description -l pl
Statistics::ChiSquare - Jak bardzo losowe s± twoje dane?

%prep
%setup -q -n %{pdir}

%build
cd ChiSquare-%{version}
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

cd ChiSquare-%{version}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChiSquare-%{version}/Changes
%{perl_sitelib}/Statistics/ChiSquare.pm
# empty autosplit.ix
#%dir %{perl_sitelib}/auto/Statistics/ChiSquare
#%%{perl_sitelib}/auto/Statistics/ChiSquare/autosplit.ix
%{_mandir}/man3/*
