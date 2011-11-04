# revision 22406
# category Package
# catalog-ctan /macros/latex/contrib/physymb
# catalog-date 2011-05-10 11:06:42 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-physymb
Version:	0.2
Release:	1
Summary:	Assorted macros for Physicists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/physymb
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physymb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physymb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/physymb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package contains a large collection of small macros that
may be useful to physicists and occasionally some
mathematicians. It streamlines writing Dirac notation,
derivatives, vector variables, unit vectors, scientific
notation, elementary particles, and many other things.

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
%{_texmfdistdir}/tex/latex/physymb/physymb.sty
%doc %{_texmfdistdir}/doc/latex/physymb/README
%doc %{_texmfdistdir}/doc/latex/physymb/physymb.pdf
#- source
%doc %{_texmfdistdir}/source/latex/physymb/physymb.dtx
%doc %{_texmfdistdir}/source/latex/physymb/physymb.ins
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
