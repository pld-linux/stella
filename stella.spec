Summary:	An Atari 2600 Video Computer System emulator
Summary(pl):	Emulator Atari 2600 Video Computer System
Name:		stella
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/stella/%{name}-%{version}-src.tar.gz
# Source0-md5:	b9318f82a180ff0a404fca78511b2772
Patch0:		%{name}-conf.patch
URL:		http://stella.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Atari 2600 Video Computer System (VCS), introduced in 1977, was
the most popular home video game system of the early 1980's. This
emulator will run most Atari ROM images, so that you can play your
favorite old Atari 2600 games on your PC.

%description -l pl
Atari 2600 Video Computer System (VCS), kt�ry mia� premier� w 1977
roku, by� najpopularniejszym systemem domowych gier video wczesnych
lat 1980-tych. Ten emulator potrafi uruchomi� wi�kszo�� obraz�w Atari
ROM, wi�c mo�na gra� w swoje ulubione stare gry z Atari 2600 na PC.

%prep
%setup -q
%patch0 -p1

%build
cd src/build
%{__make} linux-x \
	CC=%{__cc} \
	CXX=%{__cxx}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install src/build/stella.x11 $RPM_BUILD_ROOT%{_bindir}/%{name}
install src/stellarc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce.txt Changes.txt Todo.txt docs/*.html
%attr(755,root,root) %{_bindir}/stella
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/stellarc
