Summary:	Mingw32 GNU binary utility development utilities - DirectX 5.0 API
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla Mingw32 - API DirectX 5.0
Name:		crossmingw32-dx50
Version:	5.0
Release:	2
Epoch:		1
License:	Free (libs), (c) Microsoft Corporation (headers)
Group:		Development/Libraries
# headers are Copyright (C) 19xx Microsoft Corporation - what about license???
# (even if distributable, are they "Free"?!)
Source0:	http://www.libsdl.org/extras/win32/common/directx-devel.tar.gz
# Source0-md5:	389a36e4d209c0a76bea7d7cb6315315
URL:		http://www.libsdl.org/extras/win32/common/
Requires:	crossmingw32-runtime
Provides:	crossmingw32-w32api-dx = 5.0
Obsoletes:	crossmingw32-w32api-dx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		arch		%{_prefix}/%{target}

%define		__unzip		unzip -q -o
# strip fails on static COFF files
%define		no_install_post_strip 1

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains DirectX 5.0 API includes and libraries.

%description -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera pliki nagłówkowe i biblioteki API DirectX 5.0.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/{include,lib}

cp -fa include/* $RPM_BUILD_ROOT%{arch}/include
cp -fa lib/* $RPM_BUILD_ROOT%{arch}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/d3dtypes.h
%{arch}/include/ddraw.h
%{arch}/include/dinput.h
%{arch}/include/dsound.h
%{arch}/include/directx.h
%{arch}/lib/libdsound.a
%{arch}/lib/libddraw.a
%{arch}/lib/libdplayx.a
%{arch}/lib/libdinput.a
%{arch}/lib/libdxguid.a
