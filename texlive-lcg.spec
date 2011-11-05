# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/lcg
# catalog-date 2008-09-10 22:47:41 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-lcg
Version:	1.2
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The lcg package generates random numbers (integers) via a
linear congruential generator (Schrage's method). The random
numbers are written to a counter. The keyval package is used to
set values for the range, a seed, and the name of the counter.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lcg/lcg.sty
%doc %{_texmfdistdir}/doc/latex/lcg/lcg.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lcg/lcg.dtx
%doc %{_texmfdistdir}/source/latex/lcg/lcg.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
