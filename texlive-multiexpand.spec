Name:		texlive-multiexpand
Version:	45943
Release:	2
Summary:	Variations on the primitive command \expandafter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multiexpand
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiexpand.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiexpand.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiexpand.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides two user commands; one that performs
multiple expansions, and one that does multiple \expandafter
operations, in a single macro call. The package requires eTeX's
\numexpr command. The author suggests that the same effect
could be provided by use of the command variant mechanisms of
LaTeX 3 (see, for example, the interface documentation of the
experimental LaTeX 3 kernel).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/multiexpand
%doc %{_texmfdistdir}/doc/generic/multiexpand
#- source
%doc %{_texmfdistdir}/source/generic/multiexpand

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
