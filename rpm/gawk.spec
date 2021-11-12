Name:       gawk
Summary:    The GNU version of the awk text processing utility
Version:    4.2.1
Release:    1
License:    GPLv3+ and GPLv2+ and LGPLv2+ and BSD
URL:        https://github.com/sailfishos/gawk
Source0:    %{name}-%{version}.tar.bz2
Source1:    LICENSE.GPLv2
Source2:    LICENSE.LGPLv2
Source3:    LICENSE.BSD
BuildRequires:  bison
BuildRequires:  texinfo
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
Obsoletes: %{name}-docs

%description doc
Man and info pages for %{name}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build

%configure --disable-static

%make_build

%install
%make_install

rm -f %{buildroot}%{_bindir}/gawk-*
rm -f %{buildroot}%{_infodir}/dir

# Create additional symlinks:
ln -sf gawk %{buildroot}%{_bindir}/awk
ln -sf gawk.1.gz %{buildroot}%{_mandir}/man1/awk.1.gz

ln -sf awk %{buildroot}%{_datadir}/gawk
ln -sf awk %{buildroot}%{_libexecdir}/gawk

# Remove public header for now
rm %{buildroot}/%{_includedir}/gawkapi.h

%find_lang %{name}

%lang_package

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*awk
%{_libdir}/*awk
%{_libexecdir}/*awk
%{_datadir}/*awk
%{_sysconfdir}/profile.d/gawk.*

%files doc
%defattr(-,root,root,-)
%doc NEWS README POSIX.STD README_d/README.multibyte
%{_infodir}/%{name}*.*
%{_mandir}/man1/*
%{_mandir}/man3/*
