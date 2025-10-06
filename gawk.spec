Name:       gawk
Summary:    The GNU version of the awk text processing utility
Version:    3.1.5
Release:    5
Epoch:      1
License:    GPLv2+
URL:        http://www.gnu.org/software/gawk/gawk.html
Source0:    ftp://ftp.gnu.org/gnu/gawk/gawk-%{version}.tar.bz2
Patch0:     gawk-3.1.3-getpgrp_void.patch
Patch1:     gawk-3.1.5-free.patch
Patch2:     gawk-3.1.5-fieldwidths.patch
Patch3:     gawk-3.1.5-binmode.patch
Patch4:     gawk-3.1.5-num2str.patch
Patch5:     gawk-3.1.5-wconcat.patch
Patch6:     gawk-3.1.5-internal.patch
Patch7:     gawk-3.1.5-syntaxerror.patch
Patch8:     gawk-3.1.5-numflags.patch
Patch9:     gawk-3.1.5-ipv6.patch
Patch10:    gawk-3.1.5-freewstr.patch
Patch11:    gawk-3.1.5-mbread.patch
Patch12:    gawk-aarch64.patch
Patch13:    gawk-3.1.5-gcc15.patch
Requires:   /bin/mktemp
BuildRequires:  bison
Provides:   awk

%description
The gawk package contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs.

Install the gawk package if you need a text processing utility. Gawk is
considered to be a standard Linux tool for processing text.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man and info pages for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build

export CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
%configure --disable-static \
    --bindir=/bin

%make_build

%install
%make_install

chmod a-x COPYING
mkdir -p $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT/usr/bin
ln -s ../../bin/gawk awk
ln -s ../../bin/gawk gawk
popd
%find_lang gawk

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        AUTHORS ChangeLog FUTURES LIMITATIONS PROBLEMS README

%lang_package

%files
%license COPYING
/bin/*
/usr/bin/*
%{_libexecdir}/awk
%{_datadir}/awk

%files doc
%{_infodir}/%{name}*.*
%{_mandir}/man1/*%{name}.*
%{_docdir}/%{name}-%{version}
