# revision 31474
# category Package
# catalog-ctan /macros/latex/contrib/lcg
# catalog-date 2013-08-19 14:43:09 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-lcg
Version:	1.3
Release:	5
Summary:	Generate random integers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lcg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The lcg package generates random numbers (integers) via a
linear congruential generator (Schrage's method). The random
numbers are written to a counter. The keyval package is used
for the user to provide values for the range and a seed, and
for the name of the counter to be used.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lcg/lcg.sty
%doc %{_texmfdistdir}/doc/latex/lcg/lcg.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lcg/lcg.dtx
%doc %{_texmfdistdir}/source/latex/lcg/lcg.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
