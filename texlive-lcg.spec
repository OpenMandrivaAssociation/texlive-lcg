Name:		texlive-lcg
Version:	31474
Release:	2
Summary:	Generate random integers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lcg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
