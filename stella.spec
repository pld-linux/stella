Summary:	An Atari 2600 Video Computer System emulator
Summary(pl.UTF-8):	Emulator Atari 2600 Video Computer System
Name:		stella
Version:	2.4
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/stella/%{name}-%{version}-src.tar.gz
# Source0-md5:	538233e42e9cfddf2bc99433e11bb454
Patch0:		%{name}-desktop.patch
URL:		http://stella.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Atari 2600 Video Computer System (VCS), introduced in 1977, was
the most popular home video game system of the early 1980's. This
emulator will run most Atari ROM images, so that you can play your
favorite old Atari 2600 games on your PC.

%description -l pl.UTF-8
Atari 2600 Video Computer System (VCS), który miał premierę w 1977
roku, był najpopularniejszym systemem domowych gier video wczesnych
lat 1980-tych. Ten emulator potrafi uruchomić większość obrazów Atari
ROM, więc można grać w swoje ulubione stare gry z Atari 2600 na PC.

%prep
%setup -q
%patch0 -p1

%build
./configure \
	--prefix=%{_prefix}
%{__make} \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_sysconfdir}}

install src/emucore/stella.pro $RPM_BUILD_ROOT%{_sysconfdir}
install src/common/stella.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce.txt Changes.txt Readme.txt Todo.txt docs
%attr(755,root,root) %{_bindir}/stella
%config %{_sysconfdir}/stella.pro
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
