#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	POE
%define		pnam	Component-JobQueue
Summary:	POE::Component::JobQueue - a component to manage queues and worker pools
Summary(pl.UTF-8):	POE::Component::JobQueue - komponent do zarządzania kolejkami i robotnikami
Name:		perl-POE-Component-JobQueue
Version:	0.571
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4b6d96b08ac72fb4ba131017f36407a2
URL:		http://search.cpan.org/dist/POE-Component-JobQueue/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 1:1.007
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::JobQueue manages a finite pool of worker sessions as
they handle an arbitrarily large number of tasks. It often is used as
a form of flow control, preventing a large group of tasks from
exhausting some sort of resource.

%description -l pl.UTF-8
POE::Component::JobQueue zarządza skończoną pulą sesji robotników
wykonujących dowolnie dużą liczbę zadań. Jest często używany jako
forma kontroli przepływu, nie pozwalając dużej grupie zadań na
wyczerpanie jakiegoś rodzaju zasobu.

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
