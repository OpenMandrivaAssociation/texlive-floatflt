%global tl_name floatflt
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.31
Release:	%{tl_revision}.1
Summary:	Wrap text around floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/floatflt
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can float text around figures and tables which do not span
the full width of a page; it improves upon floatfig, and allows
tables/figures to be set left/right or alternating on even/odd pages.

