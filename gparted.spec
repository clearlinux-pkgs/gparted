#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 94c6be0
#
# Source0 file verified with key 0x17A6D3FF338C9570 (gedakc@gmail.com)
#
Name     : gparted
Version  : 1.7.0
Release  : 14
URL      : https://sourceforge.net/projects/gparted/files/gparted/gparted-1.7.0/gparted-1.7.0.tar.gz
Source0  : https://sourceforge.net/projects/gparted/files/gparted/gparted-1.7.0/gparted-1.7.0.tar.gz
Source1  : https://sourceforge.net/projects/gparted/files/gparted/gparted-1.7.0/gparted-1.7.0.tar.gz.sig
Source2  : 17A6D3FF338C9570.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: gparted-bin = %{version}-%{release}
Requires: gparted-data = %{version}-%{release}
Requires: gparted-libexec = %{version}-%{release}
Requires: gparted-license = %{version}-%{release}
Requires: gparted-locales = %{version}-%{release}
Requires: gparted-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glibmm-2.4)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(libparted)
BuildRequires : polkit
BuildRequires : polkit-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 17A6D3FF338C9570' gpg.status
%setup -q -n gparted-1.7.0
cd %{_builddir}/gparted-1.7.0
pushd ..
cp -a gparted-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738271819
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-doc
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-doc
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1738271819
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gparted
cp %{_builddir}/gparted-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gparted/dfac199a7539a404407098a2541b9482279f690d || :
cp %{_builddir}/gparted-%{version}/lib/gtest/LICENSE %{buildroot}/usr/share/package-licenses/gparted/5a2314153eadadc69258a9429104cd11804ea304 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang gparted
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gparted

%files data
%defattr(-,root,root,-)
/usr/share/applications/gparted.desktop
/usr/share/icons/hicolor/16x16/apps/gparted.png
/usr/share/icons/hicolor/22x22/apps/gparted.png
/usr/share/icons/hicolor/24x24/apps/gparted.png
/usr/share/icons/hicolor/32x32/apps/gparted.png
/usr/share/icons/hicolor/48x48/apps/gparted.png
/usr/share/icons/hicolor/scalable/apps/gparted.svg
/usr/share/metainfo/gparted.appdata.xml
/usr/share/polkit-1/actions/org.gnome.gparted.policy

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gpartedbin
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

