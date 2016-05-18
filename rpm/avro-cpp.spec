Name:    avro-cpp
Version: %{__version}
Release: %{__release}%{?dist}

Summary: Apache Avro data serialization C++ library
Group:   Development/Libraries/C and C++
License: ASL 2.0
URL:     http://avro.apache.org
Source:	 avro-cpp-%{version}.tar.gz

Patch0: 0001-rpm-cmake-install-dirs.patch

BuildRequires: cmake jansson-devel boost-devel
Requires: boost-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Apache Avro™ is a data serialization system.
Avro provides:
 * Rich data structures.
 * A compact, fast, binary data format.
 * A container file, to store persistent data.
 * Remote procedure call (RPC).
 * Simple integration with dynamic languages.

%package devel
Summary: Apache Avro data serialization C++ library (Development Environment)
Group:   Development/Libraries/C and C++
Requires: %{name} = %{version}

%description devel
Apache Avro™ is a data serialization system.
Avro provides:
 * Rich data structures.
 * A compact, fast, binary data format.
 * A container file, to store persistent data.
 * Remote procedure call (RPC).
 * Simple integration with dynamic languages.

This package contains headers and libraries required to build applications
using avro-cpp.




%prep
%setup -q -n %{name}-%{version}

%patch0

%build
%cmake . -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(444,root,root)
%{_libdir}/libavrocpp.so.*
%defattr(-,root,root)
%doc LICENSE


%files devel
%defattr(-,root,root)
%{_includedir}/avro
%defattr(444,root,root)
%{_libdir}/libavrocpp_s.a
%{_libdir}/libavrocpp.so
%{_bindir}/avrogencpp
%doc LICENSE


%changelog
* Mon May 16 2016 Magnus Edenhill <magnus@confluent.io> 1.8.0-0
- Initial RPM
