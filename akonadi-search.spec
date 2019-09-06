#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi-search
Version  : 19.08.1
Release  : 12
URL      : https://download.kde.org/stable/applications/19.08.1/src/akonadi-search-19.08.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.1/src/akonadi-search-19.08.1.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.1/src/akonadi-search-19.08.1.tar.xz.sig
Summary  : Libraries and daemons to implement searching in Akonadi
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: akonadi-search-bin = %{version}-%{release}
Requires: akonadi-search-data = %{version}-%{release}
Requires: akonadi-search-lib = %{version}-%{release}
Requires: akonadi-search-license = %{version}-%{release}
Requires: akonadi-search-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcalcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : krunner-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : xapian-core-dev

%description
No detailed description available

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
%setup -q -n akonadi-search-19.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567739474
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567739474
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-search
cp COPYING %{buildroot}/usr/share/package-licenses/akonadi-search/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadi-search/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang akonadi_search

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/akonadi_indexing_agent

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/agents/akonadiindexingagent.desktop
/usr/share/kservices5/plasma-krunner-pimcontacts.desktop
/usr/share/kservices5/plasma-krunner-pimcontacts_config.desktop
/usr/share/qlogging-categories5/akonadi-search.categories
/usr/share/qlogging-categories5/akonadi-search.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/AkonadiSearch/Core/query.h
/usr/include/KF5/AkonadiSearch/Core/resultiterator.h
/usr/include/KF5/AkonadiSearch/Core/search_core_export.h
/usr/include/KF5/AkonadiSearch/Core/searchstore.h
/usr/include/KF5/AkonadiSearch/Core/term.h
/usr/include/KF5/AkonadiSearch/Debug/akonadisearchdebugdialog.h
/usr/include/KF5/AkonadiSearch/Debug/akonadisearchdebugsearchpathcombobox.h
/usr/include/KF5/AkonadiSearch/Debug/search_debug_export.h
/usr/include/KF5/AkonadiSearch/PIM/collectionquery.h
/usr/include/KF5/AkonadiSearch/PIM/contactcompleter.h
/usr/include/KF5/AkonadiSearch/PIM/contactquery.h
/usr/include/KF5/AkonadiSearch/PIM/emailquery.h
/usr/include/KF5/AkonadiSearch/PIM/indexeditems.h
/usr/include/KF5/AkonadiSearch/PIM/notequery.h
/usr/include/KF5/AkonadiSearch/PIM/query.h
/usr/include/KF5/AkonadiSearch/PIM/resultiterator.h
/usr/include/KF5/AkonadiSearch/PIM/search_pim_export.h
/usr/include/KF5/AkonadiSearch/Xapian/search_xapian_export.h
/usr/include/KF5/AkonadiSearch/Xapian/xapiandatabase.h
/usr/include/KF5/AkonadiSearch/Xapian/xapiandocument.h
/usr/include/KF5/AkonadiSearch/Xapian/xapianqueryparser.h
/usr/include/KF5/AkonadiSearch/Xapian/xapiansearchstore.h
/usr/include/KF5/AkonadiSearch/Xapian/xapiantermgenerator.h
/usr/include/KF5/akonadi_search_version.h
/usr/lib64/cmake/KF5AkonadiSearch/KF5AkonadiSearchConfig.cmake
/usr/lib64/cmake/KF5AkonadiSearch/KF5AkonadiSearchConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiSearch/KF5AkonadiSearchTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiSearch/KF5AkonadiSearchTargets.cmake
/usr/lib64/libKF5AkonadiSearchCore.so
/usr/lib64/libKF5AkonadiSearchDebug.so
/usr/lib64/libKF5AkonadiSearchPIM.so
/usr/lib64/libKF5AkonadiSearchXapian.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiSearchCore.so.5
/usr/lib64/libKF5AkonadiSearchCore.so.5.12.1
/usr/lib64/libKF5AkonadiSearchDebug.so.5
/usr/lib64/libKF5AkonadiSearchDebug.so.5.12.1
/usr/lib64/libKF5AkonadiSearchPIM.so.5
/usr/lib64/libKF5AkonadiSearchPIM.so.5.12.1
/usr/lib64/libKF5AkonadiSearchXapian.so.5
/usr/lib64/libKF5AkonadiSearchXapian.so.5.12.1
/usr/lib64/qt5/plugins/akonadi/akonadi_search_plugin.so
/usr/lib64/qt5/plugins/akonadi/calendarsearchstore.so
/usr/lib64/qt5/plugins/akonadi/contactsearchstore.so
/usr/lib64/qt5/plugins/akonadi/emailsearchstore.so
/usr/lib64/qt5/plugins/akonadi/notesearchstore.so
/usr/lib64/qt5/plugins/kcm_krunner_pimcontacts.so
/usr/lib64/qt5/plugins/krunner_pimcontacts.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-search/COPYING
/usr/share/package-licenses/akonadi-search/COPYING.LIB

%files locales -f akonadi_search.lang
%defattr(-,root,root,-)

