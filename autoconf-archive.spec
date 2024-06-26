#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x41BC28FE99089D72 (simons@cryp.to)
#
Name     : autoconf-archive
Version  : 2023.02.20
Release  : 15
URL      : https://mirrors.kernel.org/gnu/autoconf-archive/autoconf-archive-2023.02.20.tar.xz
Source0  : https://mirrors.kernel.org/gnu/autoconf-archive/autoconf-archive-2023.02.20.tar.xz
Source1  : https://mirrors.kernel.org/gnu/autoconf-archive/autoconf-archive-2023.02.20.tar.xz.sig
Source2  : 41BC28FE99089D72.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: autoconf-archive-info = %{version}-%{release}
Requires: autoconf-archive-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Autoconf Archive
================
The GNU Autoconf Archive is a collection of more than 500 macros for [GNU
Autoconf](https://www.gnu.org/software/autoconf) that have been contributed
as free software by friendly supporters of the cause from all over the
Internet. Every single one of those macros can be re-used without imposing
any restrictions whatsoever on the licensing of the generated configure
script. In particular, it is possible to use all those macros in configure
scripts that are meant for non-free software. This policy is unusual for a
Free Software Foundation project. The FSF firmly believes that software
ought to be free, and software licenses like the GPL are specifically
designed to ensure that derivative work based on free software must be
free as well. In case of Autoconf, however, an exception has been made,
because Autoconf is at such a pivotal position in the software development
tool chain that the benefits from having this tool available as widely as
possible outweigh the disadvantage that some authors may choose to use it,
too, for proprietary software.

%package dev
Summary: dev components for the autoconf-archive package.
Group: Development
Provides: autoconf-archive-devel = %{version}-%{release}
Requires: autoconf-archive = %{version}-%{release}

%description dev
dev components for the autoconf-archive package.


%package doc
Summary: doc components for the autoconf-archive package.
Group: Documentation
Requires: autoconf-archive-info = %{version}-%{release}

%description doc
doc components for the autoconf-archive package.


%package info
Summary: info components for the autoconf-archive package.
Group: Default

%description info
info components for the autoconf-archive package.


%package license
Summary: license components for the autoconf-archive package.
Group: Default

%description license
license components for the autoconf-archive package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 41BC28FE99089D72' gpg.status
%setup -q -n autoconf-archive-2023.02.20
cd %{_builddir}/autoconf-archive-2023.02.20
pushd ..
cp -a autoconf-archive-2023.02.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713223706
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713223706
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/autoconf-archive
cp %{_builddir}/autoconf-archive-%{version}/COPYING %{buildroot}/usr/share/package-licenses/autoconf-archive/e88f6aea9379eb98a7bbea965fc7127a64b41ad9 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/autoconf\-archive/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/autoconf-archive.info
/usr/share/info/autoconf-archive.info-1
/usr/share/info/autoconf-archive.info-2
/usr/share/info/autoconf-archive.info-3
/usr/share/info/autoconf-archive.info-4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/autoconf-archive/e88f6aea9379eb98a7bbea965fc7127a64b41ad9
