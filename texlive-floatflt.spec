# revision 23445
# category Package
# catalog-ctan /macros/latex/contrib/floatflt
# catalog-date 2008-08-20 21:25:58 +0200
# catalog-license other-nonfree
# catalog-version 1.31
Name:		texlive-floatflt
Version:	1.31
Release:	1
Summary:	Wrap text around floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/floatflt
License:	OTHER-NONFREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/floatflt.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Float text around figures and tables which do not span the full
width of a page, improving upon floatfig, allowing
tables/figures to be set left/right or alternating on even/odd
pages.

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
%{_texmfdistdir}/tex/latex/floatflt/floatflt.sty
%doc %{_texmfdistdir}/doc/latex/floatflt/README
%doc %{_texmfdistdir}/doc/latex/floatflt/floatexm.tex
%doc %{_texmfdistdir}/doc/latex/floatflt/floatfge.tex
%doc %{_texmfdistdir}/doc/latex/floatflt/floatfig.txt
%doc %{_texmfdistdir}/doc/latex/floatflt/floatflt.pdf
#- source
%doc %{_texmfdistdir}/source/latex/floatflt/floatflt.dtx
%doc %{_texmfdistdir}/source/latex/floatflt/floatflt.ins
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
