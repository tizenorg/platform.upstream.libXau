Name:           libXau
Version:        1.0.7
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

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

%build

./autogen.sh
%reconfigure

make %{?_smp_mflags}

%install
%make_install


%remove_docs


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%dir %{_includedir}/X11
%{_includedir}/X11/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
