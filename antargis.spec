Summary:	Battles of Antargis - medieval RTS
Summary(pl.UTF-8):	Battles of Antargis - osadzona w średniowieczu gra typu RTS
Name:		antargis
Version:	0.2.1.5
Release:	0.1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://download.berlios.de/antargis/%{name}-%{version}.tgz
# Source0-md5:	600705414e82aa48758d443a3e9d5455
URL:		http://antargis.berlios.de/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rake
BuildRequires:	ruby-devel
BuildRequires:	ruby-RubyGems
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battles of Antargis is a medieval realtime strategy game. You are a
hero who was betrayed and you have to unify the kingdom and rebuild
the old empire. Old myths will pass your way.

The game is currently in heavy development and taking up pace. The
current features include:

- A short tutorial giving you an introduction to the gameplay
- Beginning of a real campaign

%description -l pl.UTF-8
Battles of Antargis jest strategią czasu rzeczywistego osadzoną w
czasach średniowiecznych. Gracz jest bohaterem, który został zdradzony
przez towarzyszy i postanawia zjednoczyć królestwo oraz odbudować
potęgę starego imperium. Dawne mity będą przecinać mu drogę.

Gra jest obecnie intensywnie rozwijana. Aktualnie zawiera:
- krótkie wprowadzenie do gry
- początek właściwej kampanii

%prep
%setup -q

%build
rake \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CPPLAGS="%{rpmcflags} -I/usr/lib/ruby/%{ruby_version}/*-linux/"

%install
rm -rf $RPM_BUILD_ROOT

rake install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
