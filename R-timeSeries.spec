%bcond_with bootstrap
%global packname  timeSeries
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2130.92
Release:          2
Summary:          Rmetrics - Financial Time Series Objects
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core R-graphics R-grDevices R-methods R-stats R-utils
Requires:         R-timeDate R-RUnit
%if %{without bootstrap}
Requires:         R-robustbase
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-graphics
BuildRequires:    R-grDevices R-methods R-stats R-utils R-timeDate R-RUnit
%if %{without bootstrap}
BuildRequires:    R-robustbase
%endif

%description
Environment for teaching "Financial Engineering and Computational Finance"

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests
