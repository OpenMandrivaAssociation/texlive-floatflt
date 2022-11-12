Name:		texlive-floatflt
Version:	25540
Release:	1
Summary:	Wrap text around floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/floatflt
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can float text around figures and tables which do
not span the full width of a page; it improves upon floatfig,
and allows tables/figures to be set left/right or alternating
on even/odd pages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/floatflt/floatflt.sty
%doc %{_texmfdistdir}/doc/latex/floatflt/README
%doc %{_texmfdistdir}/doc/latex/floatflt/floatexm.tex
%doc %{_texmfdistdir}/doc/latex/floatflt/floatfge.tex
%doc %{_texmfdistdir}/doc/latex/floatflt/floatfig.txt
%doc %{_texmfdistdir}/doc/latex/floatflt/floatflt.pdf
#- source
%doc %{_texmfdistdir}/source/latex/floatflt/floatflt.dtx
%doc %{_texmfdistdir}/source/latex/floatflt/floatflt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
