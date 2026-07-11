%global tl_name lcg
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Generate random integers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lcg
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The lcg package generates random numbers (integers) via a linear
congruential generator (Schrage's method). The random numbers are
written to a counter. The keyval package is used for the user to provide
values for the range and a seed, and for the name of the counter to be
used.

