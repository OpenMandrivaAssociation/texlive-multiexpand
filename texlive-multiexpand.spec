%global tl_name multiexpand
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Variations on the primitive command \expandafter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/multiexpand
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiexpand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiexpand.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiexpand.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides two user commands; one that performs multiple
expansions, and one that does multiple \expandafter operations, in a
single macro call. The author suggests that the same effect could be
provided by use of the command variant mechanisms of LaTeX 3 (see, for
example, the interface documentation of the experimental LaTeX 3
kernel).

