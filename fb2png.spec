Summary:	Take screenshots from the framebuffer
Name:		fb2png
Version:	0.1
Release:	16
Group:		System/Kernel and hardware
License:	GPL
Url:		http://www.minlinux.org/projects/fb2png/
Source0:	%{name}-%{version}.tar.bz2
Source1:	fb2png-0.1-index.html
Patch0:		fb2png-0.1-libpng-needs-libm.patch
Patch1:		fb2png-0.1-zlib-include.patch
BuildRequires:	gcc
BuildRequires:	pkgconfig(libpng)

%description
Utility to make screenshots from framebuffer

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} index.html

%build
%make

%install
install -d %{buildroot}%{_bindir}
%makeinstall BINDIR=%{buildroot}%{_bindir}

%files
%doc index.html
%{_bindir}/*

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-12mdv2011.0
+ Revision: 664290
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-11mdv2011.0
+ Revision: 605118
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-10mdv2010.1
+ Revision: 522624
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-9mdv2010.0
+ Revision: 424427
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.1-8mdv2009.1
+ Revision: 364942
- fix patch num

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1-8mdv2009.0
+ Revision: 220780
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.1-7mdv2008.1
+ Revision: 149715
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Apr 27 2007 Pixel <pixel@mandriva.com> 0.1-6mdv2008.0
+ Revision: 18591
- rebuild


* Thu Oct 13 2005 Pixel <pixel@mandriva.com> 0.1-5mdk
- rebuild

* Fri Jun 04 2004 Pixel <pixel@mandrakesoft.com> 0.1-4mdk
- rebuild

* Mon Apr 21 2003 Pixel <pixel@mandrakesoft.com> 0.1-3mdk
- fix build

* Tue Jan 08 2002 Stefan van der Eijk <stefan@eijk.nu> 0.1-2mdk
- add BuildRequires

* Wed Dec 12 2001 Pixel <pixel@mandrakesoft.com> 0.1-1mdk
- initial spec

