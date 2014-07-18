%bcond_with x

Name:           libXau
Version:        1.0.8
Release:        2
License:        MIT
Summary:        X Authorization routines
Url:            http://www.x.org/
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXau.manifest
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%if !%{with x}
ExclusiveArch:
%endif

%description
This is a very simple mechanism for providing individual access to an X Window
System display.It uses existing core protocol and library hooks for specifying
authorization data in the connection setup block to restrict use of the display
to only those clients that show that they know a server-specific key
called a "magic cookie".

%package devel
Summary:        Development components for the libXau library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Development headers and files for %{name}

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen --disable-static

make %{?_smp_mflags}

%install
%make_install


%remove_docs


%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%{_libdir}/*.so.*

%files devel
%manifest %{name}.manifest
%dir %{_includedir}/X11
%{_includedir}/X11/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
