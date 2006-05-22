Summary:	Battles of Antargis - medieval RTS
Summary(pl):	Battles of Antargis - osadzona w ¶redniowieczu gra typu RTS
Name:		antargis
Version:	0.1.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://download.berlios.de/antargis/%{name}-%{version}.tar.gz
# Source0-md5:	94f8173e2eb1fea4d9d2949803055f87
URL:		http://antargis.berlios.de/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rake
BuildRequires:	ruby-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Battles of Antargis is a medieval realtime strategy game. You are a
hero who was betrayed and you have to unify the kingdom and rebuild
the old empire. Old myths will pass your way.

The game is currently in heavy development and taking up pace. The
current features include:

- A short tutorial giving you an introduction to the gameplay
- Beginning of a real campaign

%description -l pl
Battles of Antargis jest strategi± czasu rzeczywistego osadzon± w
czasach ¶redniowiecznych. Gracz jest bohaterem, który zosta³ zdradzony
przez towarzyszy i postanawia zjednoczyæ królestwo oraz odbudowaæ
potêgê starego imperium. Dawne mity bêd± przecinaæ mu drogê.

Gra jest obecnie intensywnie rozwijana. Aktualnie zawiera:
- krótkie wprowadzenie do gry
- pocz±tek w³a¶ciwej kampanii

%prep
%setup -q

%build
rake \
	CC="%{__cc}" \
	CXX="%{__cxx}"

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
