#
# Conditional build:
%bcond_without	apidocs	# Sphinx documentation
%bcond_without	tests	# unit tests

%define		module	pyasn1

Summary:	ASN.1 tools for Python
Summary(pl.UTF-8):	Narzędzia ASN.1 dla Pythona
Name:		python3-%{module}
Version:	0.6.3
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyasn1/
Source0:	https://files.pythonhosted.org/packages/source/p/pyasn1/%{module}-%{version}.tar.gz
# Source0-md5:	b7a8127ed5fc251943e47dbef51ea6c8
URL:		https://github.com/etingof/pyasn1
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 2.044
BuildRequires:	rpm-pythonprov
%if %{with apidocs}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is dedicated to implementation of ASN.1 types (concrete
syntax) and codecs (transfer syntaxes) for Python programming
environment.

%description -l pl.UTF-8
Celem tego projektu jest implementacja typów (konkretnej składni) i
kodowania (składni przesyłania) ASN.1 dla środowiska programowania
Python.

%package apidocs
Summary:	Documentation for ASN.1 Python module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona ASN.1
Group:		Documentation

%description apidocs
Documentation for ASN.1 Python module.

%description apidocs -l pl.UTF-8
Dokumentacja do modułu Pythona ASN.1.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m tests
%endif

%if %{with apidocs}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.rst README.md SECURITY.md TODO.rst
%{py3_sitescriptdir}/pyasn1
%{py3_sitescriptdir}/pyasn1-%{version}.dist-info

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,pyasn1,*.html,*.js}
%endif
