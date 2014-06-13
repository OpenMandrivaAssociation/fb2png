Summary:	Take screenshots from the framebuffer
Name:		fb2png
Version:	0.1
Release:	22
Group:		System/Kernel and hardware
License:	GPLv2
Url:		http://www.minlinux.org/projects/fb2png/
Source0:	%{name}-%{version}.tar.bz2
Source1:	fb2png-0.1-index.html
Patch0:		fb2png-0.1-libpng-needs-libm.patch
Patch1:		fb2png-0.1-zlib-include.patch
Patch2:		fb2png-0.1-cflags-ldflags.patch

BuildRequires:	pkgconfig(libpng)

%description
Utility to make screenshots from framebuffer

%prep
%setup -q
%apply_patches
cp %{SOURCE1} index.html

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
%makeinstall BINDIR=%{buildroot}%{_bindir}

%files
%doc index.html
%{_bindir}/*

