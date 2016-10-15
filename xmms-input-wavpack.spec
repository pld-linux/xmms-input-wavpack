Summary:	XMMS plugin for playing wavpack files
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzająca pliki wavpack
Name:		xmms-input-wavpack
Version:	1.0.3
Release:	3
License:	GPL v2+
Group:		X11/Applications/Sound
#Source0Download: http://www.wavpack.com/downloads.html
Source0:	http://www.wavpack.com/xmms-wavpack-%{version}.tar.bz2
# Source0-md5:	c92a94d4d2e914a46b5a3f145e298c63
URL:		http://www.wavpack.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.10
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	wavpack-devel >= 4.40
BuildRequires:	xmms-devel >= 1.2.10
Requires:	glib >= 1.2.10
Requires:	gtk+ >= 1.2.2
Requires:	wavpack >= 4.40
Requires:	xmms >= 1.2.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS plugin for playing wavpack files.

%description -l pl.UTF-8
Wtyczka wejściowa dla XMMS-a odtwarzająca pliki wavpack.

%prep
%setup -q -n xmms-wavpack-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{xmms_input_plugindir}/libwavpack.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_input_plugindir}/libwavpack.so
