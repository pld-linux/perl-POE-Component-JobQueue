#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-JobQueue
Summary:	POE::Component::JobQueue - a component to manage queues and worker pools
Summary(pl):	POE::Component::JobQueue - komponent do zarz±dzania kolejkami i robotnikami
Name:		perl-POE-Component-JobQueue
Version:	0.53
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af14d62682d23f65c0a34b89fbdd832f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::JobQueue manages a finite pool of worker sessions as
they handle an arbitrarily large number of tasks.  It often is used as
a form of flow control, preventing a large group of tasks from
exhausting some sort of resource.

%description -l pl
POE::Component::JobQueue zarz±dza skoñczon± pul± sesji robotników
wykonuj±cych dowolnie du¿± liczbê zadañ. Jest czêsto u¿ywany jako
forma kontroli przep³ywu, nie pozwalaj±c du¿ej grupie zadañ na
wyczerpanie jakiego¶ rodzaju zasobu.

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
%doc CHANGES
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
