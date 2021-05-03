#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x17A6D3FF338C9570 (gedakc@gmail.com)
#
Name     : gparted
Version  : 1.3.0
Release  : 8
URL      : https://sourceforge.net/projects/gparted/files/gparted/gparted-1.3.0/gparted-1.3.0.tar.gz
Source0  : https://sourceforge.net/projects/gparted/files/gparted/gparted-1.3.0/gparted-1.3.0.tar.gz
Source1  : https://sourceforge.net/projects/gparted/files/gparted/gparted-1.3.0/gparted-1.3.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: gparted-bin = %{version}-%{release}
Requires: gparted-data = %{version}-%{release}
Requires: gparted-libexec = %{version}-%{release}
Requires: gparted-license = %{version}-%{release}
Requires: gparted-locales = %{version}-%{release}
Requires: gparted-man = %{version}-%{release}
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : parted-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glibmm-2.4)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(libparted)
BuildRequires : pkgconfig(sigc++-2.0)
BuildRequires : polkit
BuildRequires : polkit-dev

%description
GPARTED
=======
Gparted is the GNOME Partition Editor for creating, reorganizing, and
deleting disk partitions.

%package bin
Summary: bin components for the gparted package.
Group: Binaries
Requires: gparted-data = %{version}-%{release}
Requires: gparted-libexec = %{version}-%{release}
Requires: gparted-license = %{version}-%{release}

%description bin
bin components for the gparted package.


%package data
Summary: data components for the gparted package.
Group: Data

%description data
data components for the gparted package.


%package libexec
Summary: libexec components for the gparted package.
Group: Default
Requires: gparted-license = %{version}-%{release}

%description libexec
libexec components for the gparted package.


%package license
Summary: license components for the gparted package.
Group: Default

%description license
license components for the gparted package.


%package locales
Summary: locales components for the gparted package.
Group: Default

%description locales
locales components for the gparted package.


%package man
Summary: man components for the gparted package.
Group: Default

%description man
man components for the gparted package.


%prep
%setup -q -n gparted-1.3.0
cd %{_builddir}/gparted-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620063927
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-doc
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1620063927
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gparted
cp %{_builddir}/gparted-1.3.0/COPYING %{buildroot}/usr/share/package-licenses/gparted/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/gparted-1.3.0/lib/gtest/LICENSE %{buildroot}/usr/share/package-licenses/gparted/5a2314153eadadc69258a9429104cd11804ea304
%make_install
%find_lang gparted

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gparted

%files data
%defattr(-,root,root,-)
/usr/share/appdata/gparted.appdata.xml
/usr/share/applications/gparted.desktop
/usr/share/icons/hicolor/16x16/apps/gparted.png
/usr/share/icons/hicolor/22x22/apps/gparted.png
/usr/share/icons/hicolor/24x24/apps/gparted.png
/usr/share/icons/hicolor/32x32/apps/gparted.png
/usr/share/icons/hicolor/48x48/apps/gparted.png
/usr/share/icons/hicolor/scalable/apps/gparted.svg
/usr/share/polkit-1/actions/org.gnome.gparted.policy

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gpartedbin

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gparted/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/gparted/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/gparted.8

%files locales -f gparted.lang
%defattr(-,root,root,-)

