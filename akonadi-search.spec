#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi-search
Version  : 23.08.0
Release  : 59
URL      : https://download.kde.org/stable/release-service/23.08.0/src/akonadi-search-23.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.0/src/akonadi-search-23.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.0/src/akonadi-search-23.08.0.tar.xz.sig
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
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : krunner-dev
BuildRequires : plasma-framework-dev
BuildRequires : qt6base-dev
BuildRequires : xapian-core-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
%setup -q -n akonadi-search-23.08.0
cd %{_builddir}/akonadi-search-23.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693025881
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1693025881
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
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang akonadi_search
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/akonadi_indexing_agent
/usr/bin/akonadi_indexing_agent

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/agents/akonadiindexingagent.desktop
/usr/share/qlogging-categories5/akonadi-search.categories
/usr/share/qlogging-categories5/akonadi-search.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/AkonadiSearch/Core/Query
/usr/include/KPim5/AkonadiSearch/Core/ResultIterator
/usr/include/KPim5/AkonadiSearch/Core/SearchStore
/usr/include/KPim5/AkonadiSearch/Core/Term
/usr/include/KPim5/AkonadiSearch/Debug/akonadisearchdebugdialog.h
/usr/include/KPim5/AkonadiSearch/Debug/akonadisearchdebugsearchpathcombobox.h
/usr/include/KPim5/AkonadiSearch/Debug/search_debug_export.h
/usr/include/KPim5/AkonadiSearch/PIM/collectionquery.h
/usr/include/KPim5/AkonadiSearch/PIM/contactcompleter.h
/usr/include/KPim5/AkonadiSearch/PIM/contactquery.h
/usr/include/KPim5/AkonadiSearch/PIM/emailquery.h
/usr/include/KPim5/AkonadiSearch/PIM/indexeditems.h
/usr/include/KPim5/AkonadiSearch/PIM/notequery.h
/usr/include/KPim5/AkonadiSearch/PIM/query.h
/usr/include/KPim5/AkonadiSearch/PIM/resultiterator.h
/usr/include/KPim5/AkonadiSearch/PIM/search_pim_export.h
/usr/include/KPim5/AkonadiSearch/Xapian/search_xapian_export.h
/usr/include/KPim5/AkonadiSearch/Xapian/xapiandatabase.h
/usr/include/KPim5/AkonadiSearch/Xapian/xapiandocument.h
/usr/include/KPim5/AkonadiSearch/Xapian/xapianqueryparser.h
/usr/include/KPim5/AkonadiSearch/Xapian/xapiansearchstore.h
/usr/include/KPim5/AkonadiSearch/Xapian/xapiantermgenerator.h
/usr/include/KPim5/AkonadiSearch/akonadi_search_version.h
/usr/include/KPim5/AkonadiSearch/core/query.h
/usr/include/KPim5/AkonadiSearch/core/resultiterator.h
/usr/include/KPim5/AkonadiSearch/core/searchstore.h
/usr/include/KPim5/AkonadiSearch/core/term.h
/usr/include/KPim5/AkonadiSearch/search_core_export.h
/usr/lib64/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchConfig.cmake
/usr/lib64/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchConfigVersion.cmake
/usr/lib64/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchTargets.cmake
/usr/lib64/libKPim5AkonadiSearchCore.so
/usr/lib64/libKPim5AkonadiSearchDebug.so
/usr/lib64/libKPim5AkonadiSearchPIM.so
/usr/lib64/libKPim5AkonadiSearchXapian.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5AkonadiSearchCore.so.5.24.0
/V3/usr/lib64/libKPim5AkonadiSearchDebug.so.5.24.0
/V3/usr/lib64/libKPim5AkonadiSearchPIM.so.5.24.0
/V3/usr/lib64/libKPim5AkonadiSearchXapian.so.5.24.0
/V3/usr/lib64/qt5/plugins/kf5/krunner/kcms/kcm_krunner_pimcontacts.so
/V3/usr/lib64/qt5/plugins/kf5/krunner/krunner_pimcontacts.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/akonadi_search_plugin.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/calendarsearchstore.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/contactsearchstore.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/emailsearchstore.so
/V3/usr/lib64/qt5/plugins/pim5/akonadi/notesearchstore.so
/usr/lib64/libKPim5AkonadiSearchCore.so.5
/usr/lib64/libKPim5AkonadiSearchCore.so.5.24.0
/usr/lib64/libKPim5AkonadiSearchDebug.so.5
/usr/lib64/libKPim5AkonadiSearchDebug.so.5.24.0
/usr/lib64/libKPim5AkonadiSearchPIM.so.5
/usr/lib64/libKPim5AkonadiSearchPIM.so.5.24.0
/usr/lib64/libKPim5AkonadiSearchXapian.so.5
/usr/lib64/libKPim5AkonadiSearchXapian.so.5.24.0
/usr/lib64/qt5/plugins/kf5/krunner/kcms/kcm_krunner_pimcontacts.so
/usr/lib64/qt5/plugins/kf5/krunner/krunner_pimcontacts.so
/usr/lib64/qt5/plugins/pim5/akonadi/akonadi_search_plugin.so
/usr/lib64/qt5/plugins/pim5/akonadi/calendarsearchstore.so
/usr/lib64/qt5/plugins/pim5/akonadi/contactsearchstore.so
/usr/lib64/qt5/plugins/pim5/akonadi/emailsearchstore.so
/usr/lib64/qt5/plugins/pim5/akonadi/notesearchstore.so

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

