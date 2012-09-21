%define name fb2png
%define version 0.1
%define release %mkrel 13

Summary: Take screenshots from the framebuffer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: fb2png-0.1-index.html
License: GPL
Url: http://www.minlinux.org/projects/fb2png/
Group: System/Kernel and hardware
BuildRequires:	gcc
BuildRequires:	libpng-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Patch0: fb2png-0.1-libpng-needs-libm.patch
Patch1: fb2png-0.1-zlib-include.patch

%description
Utility to make screenshots from framebuffer

%prep
%setup -q
%patch0 -p1
%patch1 -p0
cp %{SOURCE1} index.html

%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
%makeinstall BINDIR=%{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc index.html
%{_bindir}/*

