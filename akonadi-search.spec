#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v16
# autospec commit: b858a2a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi-search
Version  : 24.05.2
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.05.2/src/akonadi-search-24.05.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.2/src/akonadi-search-24.05.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.2/src/akonadi-search-24.05.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Libraries and daemons to implement searching in Akonadi
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: akonadi-search-bin = %{version}-%{release}
Requires: akonadi-search-data = %{version}-%{release}
Requires: akonadi-search-lib = %{version}-%{release}
Requires: akonadi-search-license = %{version}-%{release}
Requires: akonadi-search-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : krunner-dev
BuildRequires : qt6base-dev
BuildRequires : xapian-core-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Akonadi Search
Xapian-based indexing and query infrastructure for Akonadi.

%package bin
Summary: bin components for the akonadi-search package.
Group: Binaries
Requires: akonadi-search-data = %{version}-%{release}
Requires: akonadi-search-license = %{version}-%{release}

%description bin
bin components for the akonadi-search package.


%package data
Summary: data components for the akonadi-search package.
Group: Data

%description data
data components for the akonadi-search package.


%package dev
Summary: dev components for the akonadi-search package.
Group: Development
Requires: akonadi-search-lib = %{version}-%{release}
Requires: akonadi-search-bin = %{version}-%{release}
Requires: akonadi-search-data = %{version}-%{release}
Provides: akonadi-search-devel = %{version}-%{release}
Requires: akonadi-search = %{version}-%{release}

%description dev
dev components for the akonadi-search package.


%package lib
Summary: lib components for the akonadi-search package.
Group: Libraries
Requires: akonadi-search-data = %{version}-%{release}
Requires: akonadi-search-license = %{version}-%{release}

%description lib
lib components for the akonadi-search package.


%package license
Summary: license components for the akonadi-search package.
Group: Default

%description license
license components for the akonadi-search package.


%package locales
Summary: locales components for the akonadi-search package.
Group: Default

%description locales
locales components for the akonadi-search package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n akonadi-search-24.05.2
cd %{_builddir}/akonadi-search-24.05.2
pushd ..
cp -a akonadi-search-24.05.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720622803
mkdir -p clr-build
pushd clr-build
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
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

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
export SOURCE_DATE_EPOCH=1720622803
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-search
cp %{_builddir}/akonadi-search-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi-search/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-search/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi-search/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-search/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi-search/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-search/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/akonadi-search/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-search/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi-search/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadi-search/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadi-search/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/akonadi-search/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/akonadi-search-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/akonadi-search/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/akonadi-search-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/akonadi-search/83531e59fb16ef6f78484389fd0551b70a226866 || :
cp %{_builddir}/akonadi-search-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi-search/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang akonadi_search
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/akonadi_html_to_text
/V3/usr/bin/akonadi_indexing_agent
/usr/bin/akonadi_html_to_text
/usr/bin/akonadi_indexing_agent

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/agents/akonadiindexingagent.desktop
/usr/share/qlogging-categories6/akonadi-search.categories
/usr/share/qlogging-categories6/akonadi-search.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/AkonadiSearch/Core/Query
/usr/include/KPim6/AkonadiSearch/Core/ResultIterator
/usr/include/KPim6/AkonadiSearch/Core/SearchStore
/usr/include/KPim6/AkonadiSearch/Core/Term
/usr/include/KPim6/AkonadiSearch/Debug/akonadisearchdebugdialog.h
/usr/include/KPim6/AkonadiSearch/Debug/akonadisearchdebugsearchpathcombobox.h
/usr/include/KPim6/AkonadiSearch/Debug/search_debug_export.h
/usr/include/KPim6/AkonadiSearch/PIM/collectionquery.h
/usr/include/KPim6/AkonadiSearch/PIM/contactcompleter.h
/usr/include/KPim6/AkonadiSearch/PIM/contactquery.h
/usr/include/KPim6/AkonadiSearch/PIM/emailquery.h
/usr/include/KPim6/AkonadiSearch/PIM/indexeditems.h
/usr/include/KPim6/AkonadiSearch/PIM/notequery.h
/usr/include/KPim6/AkonadiSearch/PIM/query.h
/usr/include/KPim6/AkonadiSearch/PIM/resultiterator.h
/usr/include/KPim6/AkonadiSearch/PIM/search_pim_export.h
/usr/include/KPim6/AkonadiSearch/Xapian/search_xapian_export.h
/usr/include/KPim6/AkonadiSearch/Xapian/xapiandatabase.h
/usr/include/KPim6/AkonadiSearch/Xapian/xapiandocument.h
/usr/include/KPim6/AkonadiSearch/Xapian/xapianqueryparser.h
/usr/include/KPim6/AkonadiSearch/Xapian/xapiansearchstore.h
/usr/include/KPim6/AkonadiSearch/Xapian/xapiantermgenerator.h
/usr/include/KPim6/AkonadiSearch/akonadi_search_version.h
/usr/include/KPim6/AkonadiSearch/core/query.h
/usr/include/KPim6/AkonadiSearch/core/resultiterator.h
/usr/include/KPim6/AkonadiSearch/core/searchstore.h
/usr/include/KPim6/AkonadiSearch/core/term.h
/usr/include/KPim6/AkonadiSearch/search_core_export.h
/usr/lib64/cmake/KPim6AkonadiSearch/KPim6AkonadiSearchConfig.cmake
/usr/lib64/cmake/KPim6AkonadiSearch/KPim6AkonadiSearchConfigVersion.cmake
/usr/lib64/cmake/KPim6AkonadiSearch/KPim6AkonadiSearchTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6AkonadiSearch/KPim6AkonadiSearchTargets.cmake
/usr/lib64/libKPim6AkonadiSearchCore.so
/usr/lib64/libKPim6AkonadiSearchDebug.so
/usr/lib64/libKPim6AkonadiSearchPIM.so
/usr/lib64/libKPim6AkonadiSearchXapian.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6AkonadiSearchCore.so.6.1.2
/V3/usr/lib64/libKPim6AkonadiSearchDebug.so.6.1.2
/V3/usr/lib64/libKPim6AkonadiSearchPIM.so.6.1.2
/V3/usr/lib64/libKPim6AkonadiSearchXapian.so.6.1.2
/V3/usr/lib64/qt6/plugins/kf6/krunner/kcms/kcm_krunner_pimcontacts.so
/V3/usr/lib64/qt6/plugins/kf6/krunner/krunner_pimcontacts.so
/V3/usr/lib64/qt6/plugins/pim6/akonadi/akonadi_search_plugin.so
/V3/usr/lib64/qt6/plugins/pim6/akonadi/calendarsearchstore.so
/V3/usr/lib64/qt6/plugins/pim6/akonadi/contactsearchstore.so
/V3/usr/lib64/qt6/plugins/pim6/akonadi/emailsearchstore.so
/V3/usr/lib64/qt6/plugins/pim6/akonadi/notesearchstore.so
/usr/lib64/libKPim6AkonadiSearchCore.so.6
/usr/lib64/libKPim6AkonadiSearchCore.so.6.1.2
/usr/lib64/libKPim6AkonadiSearchDebug.so.6
/usr/lib64/libKPim6AkonadiSearchDebug.so.6.1.2
/usr/lib64/libKPim6AkonadiSearchPIM.so.6
/usr/lib64/libKPim6AkonadiSearchPIM.so.6.1.2
/usr/lib64/libKPim6AkonadiSearchXapian.so.6
/usr/lib64/libKPim6AkonadiSearchXapian.so.6.1.2
/usr/lib64/qt6/plugins/kf6/krunner/kcms/kcm_krunner_pimcontacts.so
/usr/lib64/qt6/plugins/kf6/krunner/krunner_pimcontacts.so
/usr/lib64/qt6/plugins/pim6/akonadi/akonadi_search_plugin.so
/usr/lib64/qt6/plugins/pim6/akonadi/calendarsearchstore.so
/usr/lib64/qt6/plugins/pim6/akonadi/contactsearchstore.so
/usr/lib64/qt6/plugins/pim6/akonadi/emailsearchstore.so
/usr/lib64/qt6/plugins/pim6/akonadi/notesearchstore.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-search/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-search/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/akonadi-search/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/akonadi-search/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/akonadi-search/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/akonadi-search/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/akonadi-search/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/akonadi-search/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi-search/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-search/83531e59fb16ef6f78484389fd0551b70a226866
/usr/share/package-licenses/akonadi-search/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi-search/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/akonadi-search/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadi_search.lang
%defattr(-,root,root,-)

