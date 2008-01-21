# TODO
# - fix kopete-tool-{avdeviceconfig,smpppdcs} summaries/descriptions (copy-pastos!)
# - what about non-applied libgadu patch?
# - fix or kill skype support
# - kill internal libgadu copy
#
# Conditional build:
%bcond_without	xmms			# without xmms support
%bcond_without	hidden_visibility	# no gcc hidden visibility
%bcond_with	skype			# with skype support (incomplete!)

%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}
#
Summary:	K Desktop Environment - network applications
Summary(es.UTF-8):	K Desktop Environment - aplicaciones de red
Summary(pl.UTF-8):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR.UTF-8):	K Desktop Environment - aplicações de rede
%define	orgname	kdenetwork
Name:		kdenetwork4
Version:	4.0.0
Release:	0.1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	f362bd34b589800845abfb99589d4cfc
Source1:	%{orgname}-kopetestyles.tar.bz2
# Source1-md5:	642aa6bf71c37c90ce23e3c4c3a90922
Source2:	%{orgname}-lisa.init
Source3:	%{orgname}-lisa.sysconfig
Source4:	%{orgname}-lisarc
Source5:	winpopup-install.sh
URL:		http://www.kde.org/
BuildRequires:	cmake
BuildRequires:	kdebase4-workspace-devel >= %{version}
BuildRequires:	kdelibs4-devel >= %{_minlibsevr}
BuildRequires:	libgadu-devel >= 1.4
BuildRequires:	libidn-devel
BuildRequires:	libiw-devel >= 27
BuildRequires:	libtool
BuildRequires:	libvncserver-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	meanwhile-devel >= 1.0.1
BuildRequires:	openslp-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	ortp-devel
BuildRequires:	pcre-devel
BuildRequires:	qca >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sqlite-devel
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE network applications. Package includes:
- KDict - Online dictionary client
- KGet - file downloader
- KNewsticker - News Ticker
- KPF - Public fileserver applet
- KPPP - PPP dialer
- krdc - remote desktop connection
- krfb - virtual desktops
- KSirc - IRC client
- KTalkd - takt daemon
- KXmlRpcd - XmlRpc Daemon
- Lanbrowser - LAN Browser
- KWiFiManager - wireless network manager

%description -l pl.UTF-8
Aplikacje sieciowe KDE. Pakiet zawiera następujące programy:
- KDict - klient słownika
- KGet - ściągacz plików
- KNewsticker - aplet wyświetlający nowości
- KPF - applet publicznego serwera plików
- KPPP - program do nawiązywania połączeń modemowych
- krdc - zdalny pulpit
- krfb - wirtualne biurka
- KSirc - klient IRC
- KTalkd - demon Talk
- KXmlRpcd - demon XmlRpc
- Lanbrowser - przeglądarka LAN-u
- KWiFiManager - zarządca sieci bezprzewodowej

%description -l pt_BR.UTF-8
Aplicações de Rede para o KDE.

Incluídos neste pacote:

kmail: leitor de correio knu: utilitários de rede korn: ferramenta de
monitoração da caixa de correio kppp: configuração fácil para
conexão PPP krn: leitor de notícias

%package devel
Summary:	kdenetwork header files
Summary(pl.UTF-8):	Pliki nagłówkowe kdenetwork
Group:		X11/Development/Libraries
Requires:	%{name}-libkopete_msn = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_videodevice = %{epoch}:%{version}-%{release}
Requires:	%{name}-librss = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
Obsoletes:	kdenetwork-librss-devel
Obsoletes:	kdenetwork-rss-devel

%description devel
kdenetwork header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe kdenetwork.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para compilar aplicações que usem as
bibliotecas do kdenetwork.

%package filesharing
Summary:	File sharing plugins
Summary(pl.UTF-8):	Wtyczki obsługujące współdzielenie plików
Group:		X11/Applications
Requires:	kdebase-core >= %{_minlibsevr}
Obsoletes:	kcm_sambaconf

%description filesharing
File sharing plugins.

%description filesharing -l pl.UTF-8
Wtyczki obsługujące współdzielenie plików.

%package kdict
Summary:	A DICT protocol client
Summary(pl.UTF-8):	Klient protokołu DICT
License:	Artistic
Group:		X11/Applications
Provides:	kdict

%description kdict
A graphical client for the DICT protocol used for several online
dictionaries (like dict.org). It enables you to search through
dictionary databases for a word or phrase, then displays suitable
definitions. KDict tries to ease basic as well as advanced queries. A
separate list offers a convenient way to deal with the enormous number
of matching words that a advanced query can return.

%description kdict -l pl.UTF-8
Graficzny klient dla protokołu DICT używanego przez kilka
słowników online (jak np. dict.org). Pozwala przeszukiwać
słownikowe bazy danych pod kątem słów lub zwrotów, a następnie
wyświetlać pasujące definicje. KDict próbuje ułatwić podstawowe
i zaawansowane zapytania. Oddzielna lista oferuje wygodny sposób
radzenia sobie z dużą liczbą pasujących słów, którą może
zwrócić zaawansowane zapytanie.

%description kdict -l pt_BR.UTF-8
kdict é um utilitário de dicionário que usa servidores dictd da
Internet.

%package kdnssd
Summary:	DNS-SD Services Watcher
Summary(pl.UTF-8):	Nadzorowanie usług DNS-SD
License:	Artistic
Group:		X11/Applications

%description kdnssd
DNS-SD Services Watcher.

%description kdnssd -l pl.UTF-8
Nadzorowanie usług DNS-SD.

%package kinetd
Summary:	KDE Internet Daemon
Summary(pl.UTF-8):	Demon internetowy KDE
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdenetwork-krfb < 9:3.1-6

%description kinetd
A KDE daemon that listen on TCP ports and starts programs when a
client connects. Configurable using DCOP.

%description kinetd -l pl.UTF-8
Demon KDE nasłuchujący na portach TCP i uruchamiający programy po
połączeniu klienta. Jest konfigurowalny przy użyciu DCOP.

%package kfile-torrent
Summary:	Meta information plugin for BitTorrent files (*.torrent)
Summary(pl.UTF-8):	Wtyczka pobierająca metainformacje z plików BitTorrenta (*.torrent)
Group:		X11/Applications
Requires:	konqueror >= %{_minbaseevr}

%description kfile-torrent
This is a meta information plugin for BitTorrent files (*.torrent).

It doesn't depend on BitTorrent or any non-standard library being
installed.

%description kfile-torrent -l pl.UTF-8
Wtyczka pobierająca metainformacje z plików BitTorrenta (*.torrent).

Nie jest zależna od BitTorrenta ani od żadnych niestandardowych
bibliotek.

%package kget
Summary:	File downloand manager
Summary(pl.UTF-8):	Zarządca ściągania plików
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kget
A GetRight-like file download manager with resuming support and
Konqueror/Mozilla integration.

%description kget -l pl.UTF-8
Zarządca ściągania plików podobny do GetRighta z obsługą
wznawiania oraz integracją z Konquerorem/Mozillą.

%package knewsticker
Summary:	KDE News Ticker
Summary(pl.UTF-8):	News Ticker dla KDE
Summary(pt_BR.UTF-8):	Miniaplicativo de exibição de notícias para o painel Kicker
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description knewsticker
KNewsTicker is an applet for the KDE panel (also known as Kicker)
which provides an easy and convenient way to access the news as
reported by many news sites (such as Slashdot, Linux Weekly News or
Freshmeat). It can be used with virtually any website that provides
RSS/RDF feeds.

%description knewsticker -l pl.UTF-8
KNewsTicker to aplet dla panelu KDE (znanego także jako Kicker)
dostarczający łatwy i wygodny sposób dostępu do nowinek
ogłaszanych przez wiele serwisów z nowościami (takimi jak Slashdot,
Linux Weekly News czy Freshmeat). Może być używany z właściwie
każdą stroną udostępniającą feedy RSS/RDF.

%description knewsticker -l pt_BR.UTF-8
Miniaplicativo de exibição de notícias para o painel Kicker.

%package kopete
Summary:	Multi-protocol plugin-based instant messenger
Summary(pl.UTF-8):	Komunikator obsługujący wiele protokołów
Group:		X11/Applications
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdenetwork-kit
Obsoletes:	kopete
Obsoletes:	kopete-plugin-protocols-aim
Obsoletes:	kopete-plugin-protocols-gg
Obsoletes:	kopete-plugin-protocols-icq
Obsoletes:	kopete-plugin-protocols-irc
Obsoletes:	kopete-plugin-protocols-jabber
Obsoletes:	kopete-plugin-protocols-msn
Obsoletes:	kopete-plugin-protocols-oscar
Obsoletes:	kopete-plugin-protocols-sms
Obsoletes:	kopete-plugin-protocols-winpopup
Obsoletes:	kopete-plugin-protocols-yahoo
Obsoletes:	kopete-plugin-tools-autoaway
Obsoletes:	kopete-plugin-tools-autoreplace
Obsoletes:	kopete-plugin-tools-conectionstatus
Obsoletes:	kopete-plugin-tools-contactnotes
Obsoletes:	kopete-plugin-tools-cryptography
Obsoletes:	kopete-plugin-tools-highlight
Obsoletes:	kopete-plugin-tools-history
Obsoletes:	kopete-plugin-tools-importer
Obsoletes:	kopete-plugin-tools-motionaway
Obsoletes:	kopete-plugin-tools-nowlistening
Obsoletes:	kopete-plugin-tools-spellcheck
Obsoletes:	kopete-plugin-tools-texteffect
Obsoletes:	kopete-plugin-tools-translator
Obsoletes:	kopete-plugin-tools-webpresence

%description kopete
Kopete is a flexible and extendable multiple protocol instant
messaging system designed as a plugin-based system. All protocols are
plugins and allow modular installment, configuration, and usage
without the main application knowing anything about the plugin being
loaded. The goal of Kopete is to provide users with a standard and
easy to use interface between all of their instant messaging systems,
but at the same time also providing developers with the ease of
writing plugins to support a new protocol. The core Kopete development
team provides a handful of plugins that most users can use, in
addition to templates for new developers to base a plugin off of.

%description kopete -l pl.UTF-8
Kopete to rozszerzalny i rozbudowywalny komunikator obsługujący
wiele protokołów, zaprojektowany w oparciu o wtyczki. Wszystkie
protokoły są wtyczkami, co pozwala na modularną instalację,
konfigurację i używanie bez potrzeby obsługi ładowanych wtyczek w
głównej aplikacji. Celem Kopete jest wyposażenie użytkowników w
standardowy i łatwy w użyciu interfejs pomiędzy wszystkimi
systemami komunikatorów, a jednocześnie zapewnienie programistom
łatwości pisania wtyczek obsługujących nowe protokoły. Załoga
programistów Kopete udostępnia podręczny zestaw wtyczek używanych
przez większość użytkowników oraz szablony dla nowych
programistów, na których można opierać nowe wtyczki.

%package kopete-protocol-aim
Summary:	Kopete plugin which adds AIM protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu AIM
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-aim

%description kopete-protocol-aim
Kopete plugin which adds AIM protocol support.

%description kopete-protocol-aim -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu AIM.

%package kopete-protocol-gg
Summary:	Kopete plugin which adds GaduGadu protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu GaduGadu
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-gg

%description kopete-protocol-gg
Kopete plugin which adds GaduGadu protocol support.

%description kopete-protocol-gg -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu GaduGadu.

%package kopete-protocol-groupwise
Summary:	Kopete plugin which adds Groupwise protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Groupwise
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-groupwise
#Suggests:	qt-plugin-qca-tls

%description kopete-protocol-groupwise
Kopete plugin which adds Groupwise protocol support.

%description kopete-protocol-groupwise -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Groupwise.

%package kopete-protocol-icq
Summary:	Kopete plugin which adds ICQ protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu ICQ
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-icq

%description kopete-protocol-icq
Kopete plugin which adds ICQ protocol support.

%description kopete-protocol-icq -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu ICQ.

%package kopete-protocol-irc
Summary:	Kopete plugin which adds IRC support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę IRC-a
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-irc

%description kopete-protocol-irc
Kopete plugin which adds IRC support.

%description kopete-protocol-irc -l pl.UTF-8
Wtyczka Kopete dodająca obsługę IRC-a.

%package kopete-protocol-jabber
Summary:	Kopete plugin which adds Jabber protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Jabber
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-jabber
#Suggests:	qt-plugin-qca-tls

%description kopete-protocol-jabber
Kopete plugin which adds Jabber protocol support.

%description kopete-protocol-jabber -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Jabber.

%package kopete-protocol-msn
Summary:	Kopete plugin which adds MSN protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu MSN
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkopete_msn = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-msn

%description kopete-protocol-msn
Kopete plugin which adds MSN protocol support.

%description kopete-protocol-msn -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu MSN.

%package kopete-protocol-meanwhile
Summary:	Kopete plugin which adds Lotus Sametime protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Lotus Sametime
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-meanwhile

%description kopete-protocol-meanwhile
Kopete plugin which adds meanwhile Lotus Sametime support.

%description kopete-protocol-meanwhile -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Lotus Sametime.

%package kopete-protocol-skype
Summary:	Kopete plugin which adds Skype protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Skype
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	skype

%description kopete-protocol-skype
Kopete plugin which adds Skype protocol support.

%description kopete-protocol-skype -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Skype.

%package kopete-protocol-sms
Summary:	Kopete plugin which adds SMS contact support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę kontaktów SMS
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-sms

%description kopete-protocol-sms
Kopete plugin which adds SMS contact support.

%description kopete-protocol-sms -l pl.UTF-8
Wtyczka Kopete dodająca obsługę kontaktów SMS.

%package kopete-protocol-testbed
Summary:	A sample plugin for kopete
Summary(pl.UTF-8):	Przykładowa wtyczka dla kopete.
Group:		X11/Development/Libraries
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}

%description kopete-protocol-testbed
A sample plugin for kopete, which allows developers to learn the
kopete programming interface.

%description kopete-protocol-testbed -l pl.UTF-8
Przykładowa wtyczka do kopete, ułatwiająca developerom zapoznanie
się z interfejsem programowania biblioteki kopete.

%package kopete-protocol-winpopup
Summary:	Kopete plugin which adds WinPopUp messaging support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę komunikacji przez WinPopUp
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-winpopup

%description kopete-protocol-winpopup
Kopete plugin which adds WinPopUp messaging support.

%description kopete-protocol-winpopup -l pl.UTF-8
Wtyczka Kopete dodająca obsługę komunikacji przez WinPopUp.

%package kopete-protocol-yahoo
Summary:	Kopete plugin which adds Yahoo protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Yahoo
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-protocol-yahoo

%description kopete-protocol-yahoo
Kopete plugin which adds Yahoo protocol support.

%description kopete-protocol-yahoo -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Yahoo.

%package kopete-tool-autoaway
Summary:	Kopete autoaway plugin
Summary(pl.UTF-8):	Wtyczka Kopete do automatycznego przechodzenia w stan zajęty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-autoaway

%description kopete-tool-autoaway
Kopete plugin which automatically changes status to away. Conditions
are configurable.

%description kopete-tool-autoaway -l pl.UTF-8
Wtyczka Kopete automatycznie zmieniająca status na zajęty. Warunki,
po zaistnieniu których ma nastąpić, są konfigurowalne.

%package kopete-tool-alias
Summary:	Kopete plugin to add custom aliases for commands
Summary(pl.UTF-8):	Wtyczka Kopete do dodawania własnych aliasów dla poleceń
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-alias
Conflicts:	kdenetwork-kopete < 10:3.2.90.040312-1

%description kopete-tool-alias
Kopete plugin to add custom aliases for commands.

%description kopete-tool-alias -l pl.UTF-8
Wtyczka Kopete do dodawania własnych aliasów dla poleceń.

%package kopete-tool-avdeviceconfig
Summary:	Kopete avdeviceconfig plugin
Summary(pl.UTF-8):	Wtyczka Kopete do automatycznego przechodzenia w stan zajęty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-avdeviceconfig

%description kopete-tool-avdeviceconfig
Kopete plugin which automatically changes status to away. Conditions
are configurable.

%description kopete-tool-avdeviceconfig -l pl.UTF-8
Wtyczka Kopete automatycznie zmieniająca status na zajęty. Warunki,
po zaistnieniu których ma nastąpić, są konfigurowalne.

%package kopete-tool-smpppdcs
Summary:	Kopete smpppdcs plugin
Summary(pl.UTF-8):	Wtyczka Kopete do automatycznego przechodzenia w stan zajęty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-smpppdcs

%description kopete-tool-smpppdcs
Kopete plugin which automatically changes status to away. Conditions
are configurable.

%description kopete-tool-smpppdcs -l pl.UTF-8
Wtyczka Kopete automatycznie zmieniająca status na zajęty. Warunki,
po zaistnieniu których ma nastąpić, są konfigurowalne.

%package kopete-tool-autoreplace
Summary:	Kopete plugin which autoreplaces some text you can choose
Summary(pl.UTF-8):	Wtyczka Kopete do automatycznej zamiany tekstu
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-autoreplace

%description kopete-tool-autoreplace
Kopete plugin which autoreplaces some text you can choose.

%description kopete-tool-autoreplace -l pl.UTF-8
Wtyczka Kopete do automatycznej zamiany tekstu.

%package kopete-tool-connectionstatus
Summary:	Kopete Internet connection detector
Summary(pl.UTF-8):	Wykrywacz połączeń internetowych dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Provides:	kdenetwork-kopete-tool-conectionstatus
Obsoletes:	kdenetwork-kopete-tool-conectionstatus
Obsoletes:	kopete-tool-connectionstatus

%description kopete-tool-connectionstatus
Kopete tool which automatically detects whether the internet
connection is available or not.

%description kopete-tool-connectionstatus -l pl.UTF-8
Narzędzie Kopete automatycznie sprawdzające, czy dostępne jest
połączenie do Internetu.

%package kopete-tool-contactnotes
Summary:	Kopete tool which adds personal notes to your contacts
Summary(pl.UTF-8):	Narzędzie Kopete do dodawania notatek do kontaktów
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-contactnotes

%description kopete-tool-contactnotes
Kopete tool which allows adding personal notes to your contacts.

%description kopete-tool-contactnotes -l pl.UTF-8
Narzędzie Kopete umożliwiające dodawanie notatek do kontaktów.

%package kopete-tool-cryptography
Summary:	Kopete messages encryptor
Summary(pl.UTF-8):	Program do szyfrowania wiadomości dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-cryptography

%description kopete-tool-cryptography
OpenPGP messages encryptor for Kopete.

%description kopete-tool-cryptography -l pl.UTF-8
Program dla Kopete do szyfrowania wiadomości przy pomocy OpenPGP.

%package kopete-tool-highlight
Summary:	A highlighter plugin for Kopete
Summary(pl.UTF-8):	Wtyczka Kopete podkreślająca wybrane teksty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-highlight

%description kopete-tool-highlight
A highlighter plugin for Kopete.

%description kopete-tool-highlight -l pl.UTF-8
Wtyczka Kopete podkreślająca wybrane teksty.

%package kopete-tool-latex
Summary:	A LaTeX plugin for Kopete
Summary(pl.UTF-8):	Wtyczka Kopete renderująca tekst w formacie LaTeXa
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-latex
Conflicts:	kdenetwork-kopete < 10:3.4.89-1

%description kopete-tool-latex
A LaTeX plugin for Kopete.

%description kopete-tool-latex -l pl.UTF-8
Wtyczka Kopete renderująca tekst w formacie LaTeXa.

%package kopete-tool-history
Summary:	A history plugin for Kopete
Summary(pl.UTF-8):	Wtyczka Kopete obsługująca historię rozmów
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-history

%description kopete-tool-history
A history plugin for Kopete.

%description kopete-tool-history -l pl.UTF-8
Wtyczka Kopete obsługująca historię rozmów.

%package kopete-tool-importer
Summary:	Contact importer for Kopete
Summary(pl.UTF-8):	Importer kontaktów dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-importer

%description kopete-tool-importer
Kopete tool which allows importing contacts from other instant
messengers.

%description kopete-tool-importer -l pl.UTF-8
Narzędzie Kopete umożliwiające importowanie kontaktów z innych
komunikatorów.

%package kopete-tool-motionaway
Summary:	Kopete plugin which sets away status when not detecting movement near the computer
Summary(pl.UTF-8):	Wtyczka Kopete zmieniająca status na zajęty jeśli nie wykrywa ruchu wokół komputera
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-motionaway

%description kopete-tool-motionaway
This Kopete plugin sets away status when not detecting movement near
the computer.

%description kopete-tool-motionaway -l pl.UTF-8
Ta wtyczka Kopete zmienia status na zajęty jeśli nie wykrywa ruchu
wokół komputera.

%package kopete-tool-nowlistening
Summary:	Playlist informer for Kopete
Summary(pl.UTF-8):	Informator o playliście dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-nowlistening

%description kopete-tool-nowlistening
This Kopete plugin tells selected live chats what you're currently
listening to in xmms/kscd/noatun.

%description kopete-tool-nowlistening -l pl.UTF-8
Ta wtyczka Kopete wypisuje podczas wybranych rozmów nazwę aktualnie
słuchanej piosenki w xmms/kscd/noatun.

%package kopete-tool-spellcheck
Summary:	A spell checking plugin for Kopete
Summary(pl.UTF-8):	Wtyczka Kopete sprawdzająca pisownie
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-spellcheck

%description kopete-tool-spellcheck
A spell checking plugin for Kopete.

%description kopete-tool-spellcheck -l pl.UTF-8
Wtyczka Kopete sprawdzająca pisownie.

%package kopete-tool-texteffect
Summary:	Kopete plugin that adds nice effects to your messages
Summary(pl.UTF-8):	Wtyczka Kopete dodająca ładne efekty do wiadomości
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-texteffect

%description kopete-tool-texteffect
Kopete plugin that adds nice effects to your messages.

%description kopete-tool-texteffect -l pl.UTF-8
Wtyczka Kopete dodająca ładne efekty do wiadomości.

%package kopete-tool-translator
Summary:	Kopete plugin which uses babelfish to translate messages
Summary(pl.UTF-8):	Wtyczka Kopete wykorzystująca babelfish do tłumaczenia wiadomości
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Obsoletes:	kopete-tool-translator

%description kopete-tool-translator
This Kopete plugin uses web translating engines (like Altavista's
babelfish or Google) to translate messages.

%description kopete-tool-translator -l pl.UTF-8
Ta wtyczka Kopete wykorzystuje babelfish do tłumaczenia wiadomości.

%package kopete-tool-webpresence
Summary:	Web contactlist presenter for Kopete
Summary(pl.UTF-8):	Wyświetlacz listy kontaktów na WWW dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{epoch}:%{version}-%{release}
Requires:	libxml2 >= 2.4.8
Requires:	libxslt >= 1.0.7
Obsoletes:	kopete-tool-webpresence

%description kopete-tool-webpresence
This Kopete plugin shows the status of your IM accounts on a webpage.

%description kopete-tool-webpresence -l pl.UTF-8
Ta wtyczka Kopete pokazuje status (całej lub części) listy
kontaktów na stronie WWW.

%package kpf
Summary:	Public fileserver applet
Summary(pl.UTF-8):	Applet publicznego serwera plików
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description kpf
kpf provides simple file sharing using HTTP (the Hyper Text Transfer
Protocol), which is the same protocol used by web sites to provide
data to your web browser. kpf is strictly a public fileserver, which
means that there are no access restrictions to shared files. Whatever
you select for sharing is available to anyone.

kpf is designed to be used for sharing files with friends, not to act
like a fully-fledged web server such as Apache. kpf was primarily
conceived as an easy way to share files with others while chatting on
IRC (Internet Relay Chat, or "chat rooms".)

Typical usage: kpf is set up to serve files from the public_html
folder in your home folder. You wish to make a file available to some
people with whom you are chatting online. Rather than send them each
an email with the file attached (some may not even be interested,) you
copy the file into your public_html folder and announce to those
listening that your file is available at
<http://www.mymachine.net:8001/thefile>.

%description kpf -l pl.UTF-8
kpf umożliwia proste uwspólnianie plików przy użyciu protokołu
HTTP (Hyper Text Transfer Protocol), tego samego, który jest używany
dla stron WWW, aby dostarczyć dane do przeglądarki. Ściślej
mówiąc kpf jest publicznym serwerem plików, co oznacza, że nie ma
ograniczeń dostępu do współdzielonych plików. Wszystko co
wybierze się do dzielenia, jest dostępne dla każdego.

kpf jest zaprojektowany w celu dzielenia plików z przyjaciółmi, a
nie działania jako pełnoprawny serwer WWW, taki jak Apache. kpf był
początkowo rozwijany głównie jako prosty sposób współdzielenia
plików z innymi podczas rozmawiania przez IRC.

Typowy przypadek użycia: kpf jest konfigurowany do serwowania plików
z podkatalogu public_html w katalogu domowym. Chcemy uczynić plik
dostępnym dla ludzi, z którymi akurat rozmawiamy. Zamiast wysyłać
plik pocztą jako załącznik (niektórzy mogą nawet nie być
zainteresowani), kopiujemy plik do katalogu public_html i ogłaszamy,
że plik jest dostępny jako http://www.mojkomputer.net:8001/plik .

%package kppp
Summary:	KDE PPP dialer
Summary(pl.UTF-8):	Program do połączeń modemowych dla KDE
Summary(pt_BR.UTF-8):	O discador para Internet
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	ppp

%description kppp
KPPP is a dialer and front end for pppd. It allows for interactive
script generation and network setup. It will automate the dialing in
process to your ISP while letting you conveniently monitor the entire
process.

Once connected KPPP will provide a rich set of statistics and keep
track of the time spent online for you.

A built-in terminal and script generator will enable you to set up
your connection with ease. You will no longer need an additional
terminal program such as seyon or minicom to test and setup your
connection.

KPPP features elaborate phone cost accounting, which enables you to
easily track your online costs.

%description kppp -l pl.UTF-8
KPPP to program do nawiązywania połączeń modemowych i frontend dla
pppd. Pozwala na interaktywne generowanie skryptów i konfiguracji
sieci. Automatyzuje proces dzwonienia do swojego ISP umożliwiając
jednocześnie wygodne monitorowanie całego procesu.

Po połączeniu KPPP udostępnia bogate statystyki i śledzi czas
spędzony online.

Wbudowany terminal i generator skryptów umożliwia łatwe
skonfigurowanie połączenia. Nie trzeba już dodatkowego programu
terminalowego, takiego jak seyon czy minicom, do testowania i
ustawiania połączenia.

KPPP ma wypracowane naliczanie kosztów telefonów, pozwalające
łatwo śledzić koszt czasu online.

%description kppp -l pt_BR.UTF-8
O discador para Internet.

%package ksirc
Summary:	KDE IRC client
Summary(pl.UTF-8):	Klient IRC dla KDE
Summary(pt_BR.UTF-8):	Cliente de IRC do KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	perl-IO-Socket-SSL
Requires:	perl-Socket6 >= 0.11

%description ksirc
KSirc is the default KDE IRC client. It supports scripting with Perl
and has a lot of compatibility with mIrc for general use.

%description ksirc -l pl.UTF-8
KSirc to domyślny klient IRC dla KDE. Obsługuje skrypty perlowe i
jest w dużym stopniu kompatybilny z mIrcem przy ogólnym używaniu.

%description ksirc -l pt_BR.UTF-8
Cliente de IRC do KDE.

%package krfb
Summary:	Virtual Desktops
Summary(pl.UTF-8):	Wirtualne biurka
Group:		X11/Applications
Requires:	%{name}-kinetd = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Suggests:	rdesktop

%description krfb
Remote Desktop Connection is a client application that allows you to
view or even control the desktop session on another machine that is
running a compatible (VNC) server. You would typically use Remote
Desktop Connection with the KDE VNC server, which is Desktop Sharing
(also provided in this package), since it closely matches the special
features of Remote Desktop Connection.

%description krfb -l pl.UTF-8
Remote Desktop Connection to aplikacja kliencka umożliwiająca
oglądanie a nawet sterowanie sesją na innej maszynie z działającym
kompatybilnym serwerem (VNC). Zwykle używa się Remote Desktop
Connection z użyciem serwera KDE VNC, czyli "dzielenia pulpitu"
(także dostarczanego przez ten pakiet), jako że najlepiej pasuje do
specjalnych możliwości Remote Desktop Connection.

%package ktalkd
Summary:	Talk daemon
Summary(pl.UTF-8):	Daemon talk
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description ktalkd
A talk daemon replacement. Support the talk protocol and features an
answering machine plus a possibility to inform you about incoming
messages.

%description ktalkd -l pl.UTF-8
Zamiennik demona talk. Obsługuje protokół talk i ma automatyczną
sekretarkę oraz możliwość informowania o przychodzących
wiadomościach.

%package kwifimanager
Summary:	Wireless LAN
Summary(pl.UTF-8):	Bezprzewodowy LAN
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Requires:	wireless-tools
Obsoletes:	kwifimanager

%description kwifimanager
The KWiFiManager suite is a set of tools which allows you to manage
your wireless LAN PC-Card under the K Desktop Environment. It provides
information about your current connection and lets you set up up to
four independent configurations which can be loaded automatically when
KDE is started. KWiFiManager supports every wireless LAN card that
uses the wireless extensions interface.

%description kwifimanager -l pl.UTF-8
Oprogramowanie KWiFiManager to zbiór narzędzi umożliwiających
zarządzanie bezprzewodową kartą LAN w środowisku KDE. Dostarcza
informacje o bieżącym połączeniu oraz pozwala ustawić do czterech
niezależnych konfiguracji, które mogą być ładowane automatycznie
przy starcie KDE. KWiFiManager obsługuje wszystkie bezprzewodowe
karty LAN używające interfejsu rozszerzeń bezprzewodowych.

%package kxmlrpcd
Summary:	KDE XmlRpc Daemon
Summary(pl.UTF-8):	Deamon XmlRpc dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}

%description kxmlrpcd
KDE XmlRpc Daemon.

%description kxmlrpcd -l pl.UTF-8
Demon XmlRpc dla KDE.

%package lanbrowser
Summary:	KDE LAN Browser
Summary(pl.UTF-8):	Przeglądarka LAN-u dla KDE
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires:	konqueror >= %{_minbaseevr}
Requires:	rc-scripts
Requires:	samba-client
Provides:	lisa
Obsoletes:	kdenetwork-lisa
Obsoletes:	lisa

%description lanbrowser
A browser for Samba shares in your Local Area Network.

%description lanbrowser -l pl.UTF-8
Przeglądarka dla udziałów Samby w sieci lokalnej.

%package libkopete
Summary:	kopete library
Summary(pl.UTF-8):	Biblioteka kopete
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdenetwork-kopete < 10:3.1.93.031114-3

%description libkopete
kopete library.

%description libkopete -l pl.UTF-8
Biblioteka kopete.

%package libkopete_msn
Summary:	MSN protocol shared library
Summary(pl.UTF-8):	Biblioteka współdzielona dla protokołu MSN
Group:		X11/Libraries
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-kopete-protocol-msn < 10:3.1.93.031114-3

%description libkopete_msn
MSN protocol shared library.

%description libkopete_msn -l pl.UTF-8
Biblioteka współdzielona dla protokołu MSN.

%package libkopete_videodevice
Summary:	Video input device support library for kopete
Summary(pl.UTF-8):	Biblioteka z obsługą urządzeń wejścia video dla kopete
Group:		X11/Libraries
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}

%description libkopete_videodevice
Video input device support library for kopete.

%description libkopete_videodevice -l pl.UTF-8
Biblioteka z obsługą urządzeń wejścia video dla kopete.

%package libkopete_oscar
Summary:	Shared library which adds OSCAR protocol support
Summary(pl.UTF-8):	Biblioteka dodająca obsługę protokołu OSCAR
Group:		X11/Applications/Networking
Requires:	%{name}-libkopete = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-kopete-protocol-oscar < 10:3.1.93.031114-3

%description libkopete_oscar
A shared library which adds OSCAR protocol support needed eg. by AIM
and ICQ.

%description libkopete_oscar -l pl.UTF-8
Biblioteka dodająca obsługę protokołu OSCAR, używanego między
innymi przez AIM i ICQ.

%package librss
Summary:	RSS library
Summary(pl.UTF-8):	Biblioteka RSS
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdenetwork-rss < 10:3.1.93.031114-3

%description librss
Library for RSS/RDF/XML parsers in KDE.

%description librss -l pl.UTF-8
Biblioteka dla parserów RSS/RDF/XML w KDE.

%package rss
Summary:	RSS parsers used by different applications
Summary(pl.UTF-8):	Programy parsujące nagłówki RSS używane przez różne aplikacje
Group:		X11/Applications
Requires:	%{name}-librss = %{epoch}:%{version}-%{release}

%description rss
RSS parsers used by different applications.

%description rss -l pl.UTF-8
Programy parsujące nagłówki RSS używane przez różne aplikacje.

%prep
%setup -q -n %{orgname}-%{version}

%build
export QTDIR=%{_prefix}
mkdir build
cd build
%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
        ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post lanbrowser
/sbin/chkconfig --add lisa
%service lisa restart "Lisa daemon"

%preun lanbrowser
if [ "$1" = "0" ]; then
	%service lisa stop
	/sbin/chkconfig --del lisa
fi

%post	libkopete	-p /sbin/ldconfig
%postun	libkopete	-p /sbin/ldconfig

%post	libkopete_msn	-p /sbin/ldconfig
%postun	libkopete_msn	-p /sbin/ldconfig

%post	libkopete_oscar	-p /sbin/ldconfig
%postun	libkopete_oscar	-p /sbin/ldconfig

%post	librss		-p /sbin/ldconfig
%postun	librss		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libkopete.so
#%attr(755,root,root) %{_libdir}/libkopete_msn_shared.so
#%attr(755,root,root) %{_libdir}/libkopete_oscar.so
#%attr(755,root,root) %{_libdir}/libkopete_videodevice.so
#%attr(755,root,root) %{_libdir}/librss.so
#%{_includedir}/kopete
#%{_includedir}/rss

%files filesharing
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/fileshare_propsdlgplugin.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_fileshare.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kcmsambaconf.so
#%{_datadir}/services/fileshare_propsdlgplugin.desktop
#%{_desktopdir}/kde/fileshare.desktop
#%{_desktopdir}/kde/kcmsambaconf.desktop
#%{_iconsdir}/hicolor/16x16/apps/kcmsambaconf.png

%files kdict 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kdict
#%attr(755,root,root) %{_libdir}/kde4/kdict_panelapplet.so
#%attr(755,root,root) %{_libdir}/kde4/kdict.so
#%attr(755,root,root) %{_libdir}/libkdeinit_kdict.so
#%{_datadir}/apps/kdict
#%{_datadir}/apps/kicker/applets/kdictapplet.desktop
#%{_desktopdir}/kde/kdict.desktop
#%{_iconsdir}/*/*/*/kdict*

%files kdnssd
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kded_dnssdwatcher.so
#%attr(755,root,root) %{_libdir}/kde4/kio_zeroconf.so
#%{_datadir}/apps/remoteview/zeroconf.desktop
#%{_datadir}/apps/zeroconf
#%{_datadir}/services/kded/dnssdwatcher.desktop
#%{_datadir}/services/zeroconf.protocol

%files kfile-torrent
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kfile_torrent.so
#%{_datadir}/services/kfile_torrent.desktop

%files kget 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kget
#%attr(755,root,root) %{_libdir}/kde4/khtml_kget.so
#%{_datadir}/apps/kget
#%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.desktop
#%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.rc
#%{_datadir}/apps/konqueror/servicemenus/kget_download.desktop
#%{_datadir}/mimelnk/application/x-kgetlist.desktop
#%{_datadir}/sounds/KGet*.ogg
#%{_desktopdir}/kde/kget.desktop
#%{_iconsdir}/*/*/*/*kget*

%files kinetd
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kded_kinetd.so
#%{_datadir}/apps/kinetd
#%{_datadir}/services/kded/kinetd.desktop
#%{_datadir}/servicetypes/kinetdmodule.desktop

%files knewsticker 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/knewstickerstub
#%attr(755,root,root) %{_libdir}/kde4/knewsticker_panelapplet.so
#%{_datadir}/apps/knewsticker
#%{_datadir}/apps/kicker/applets/knewsticker.desktop
#%{_datadir}/apps/kconf_update/kn*
#%{_datadir}/applnk/.hidden/knewstickerstub.desktop
#%{_desktopdir}/kde/knewsticker*.desktop
#%{_iconsdir}/*/*/*/knewsticker.png

%files kopete 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kopete
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_addbookmarks.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_accountconfig.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_appearanceconfig.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_behaviorconfig.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_netmeeting.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_identityconfig.so
#%attr(755,root,root) %{_libdir}/kde4/kopete_addbookmarks.so
#%attr(755,root,root) %{_libdir}/kde4/kopete_chatwindow.so
#%attr(755,root,root) %{_libdir}/kde4/kopete_emailwindow.so
#%attr(755,root,root) %{_libdir}/kde4/kopete_statistics.so
#%attr(755,root,root) %{_libdir}/kde4/libkrichtexteditpart.so
#%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-account-0.10.pl
#%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-account-kconf_update.sh
#%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.sh
#%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-jabberproxytype-kconf_update.sh
#%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-pluginloader.pl
#%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-pluginloader2.sh
#%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-account-kconf_update
#%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-nameTracking-kconf_update
#%attr(755,root,root) %{_libdir}/kconf_update_bin/kopete-pluginloader2-kconf_update
#%dir %{_datadir}/apps/kopete
#%dir %{_datadir}/apps/kopete/icons
#%dir %{_datadir}/apps/kopete/icons/crystalsvg
#%dir %{_datadir}/apps/kopete/icons/crystalsvg/*
#%dir %{_datadir}/apps/kopete/icons/crystalsvg/*/*
#%dir %{_datadir}/apps/kopete/icons/hicolor
#%dir %{_datadir}/apps/kopete/icons/hicolor/*
#%dir %{_datadir}/apps/kopete/icons/hicolor/*/*
#%dir %{_datadir}/apps/kopete/pics
#%dir %{_datadir}/apps/kopeterichtexteditpart
#%{_datadir}/apps/kconf_update/kopete-account-kconf_update.upd
#%{_datadir}/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.upd
#%{_datadir}/apps/kconf_update/kopete-jabberproxytype-kconf_update.upd
#%{_datadir}/apps/kconf_update/kopete-nameTracking.upd
#%{_datadir}/apps/kconf_update/kopete-pluginloader.upd
#%{_datadir}/apps/kconf_update/kopete-pluginloader2.upd
#%{_datadir}/apps/kopete/*rc
#%{_datadir}/apps/kopete/icons/*/*/actions/kgpg_key?.png
#%{_datadir}/apps/kopete/icons/*/*/actions/logging.png
#%{_datadir}/apps/kopete/pics/statistics
#%{_datadir}/apps/kopete/styles
#%{_datadir}/apps/kopete_statistics
#%{_datadir}/apps/kopeterichtexteditpart/kopeterichtexteditpartfull.rc
#%{_datadir}/config.kcfg/kopete.kcfg
#%{_datadir}/config.kcfg/kopeteidentityconfigpreferences.kcfg
#%{_datadir}/mimelnk/application/x-kopete-emoticons.desktop
#%{_datadir}/services/chatwindow.desktop
#%{_datadir}/services/emailwindow.desktop
#%{_datadir}/services/invitation.protocol
#%{_datadir}/services/kopete_accountconfig.desktop
#%{_datadir}/services/kopete_addbookmarks.desktop
#%{_datadir}/services/kopete_appearanceconfig.desktop
#%{_datadir}/services/kopete_behaviorconfig.desktop
#%{_datadir}/services/kopete_identityconfig.desktop
#%{_datadir}/services/kopete_statistics.desktop
#%{_datadir}/servicetypes/kopeteplugin.desktop
#%{_datadir}/servicetypes/kopeteprotocol.desktop
#%{_datadir}/servicetypes/kopeteui.desktop
#%{_datadir}/sounds/Kopete_Event.ogg
#%{_datadir}/sounds/Kopete_Received.ogg
#%{_datadir}/sounds/Kopete_Sent.ogg
#%{_datadir}/sounds/Kopete_User_is_Online.ogg
#%{_desktopdir}/kde/kopete.desktop

%files kopete-protocol-aim
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*aim*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/*aim*
#%{_datadir}/apps/kopete/icons/hicolor/*/*/*aim*
#%{_datadir}/services/aim.protocol
#%{_datadir}/services/kopete_aim.desktop

%files kopete-protocol-gg
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*gadu*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gadu*
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/gg*
#%{_datadir}/services/kopete_gadu.desktop

%files kopete-protocol-groupwise
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*groupwise*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/groupwise*
#%{_datadir}/apps/kopete_groupwise
#%{_datadir}/services/kopete_groupwise.desktop

%files kopete-protocol-icq
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*icq*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/*icq*
#%{_datadir}/apps/kopete/icons/hicolor/*/*/*icq*
#%{_datadir}/services/kopete_icq.desktop

%files kopete-protocol-irc
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*irc*.so
#%{_datadir}/apps/kopete/ircnetworks.xml
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/irc*
#%{_datadir}/services/kopete_irc.desktop
#%{_datadir}/services/irc.protocol

%files kopete-protocol-jabber
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*jabber*.so
#%attr(755,root,root) %{_libdir}/kde4/kio_jabberdisco.so
#%{_datadir}/apps/kopete_jabber
#%{_datadir}/services/jabberdisco.protocol
#%{_datadir}/services/kopete_jabber.desktop

%files kopete-protocol-meanwhile
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*meanwhile*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/meanwhile*
#%{_datadir}/services/kopete_meanwhile.desktop

%files kopete-protocol-msn
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_msn.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*msn*.so
#%attr(755,root,root) %{_libdir}/kde4/kopete_netmeeting.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/msn*
#%{_datadir}/apps/kopete_msn
#%{_datadir}/apps/kopete_netmeeting
#%{_datadir}/services/kconfiguredialog/kopete_msn_config.desktop
#%{_datadir}/services/kconfiguredialog/kopete_netmeeting_config.desktop
#%{_datadir}/services/kopete_msn.desktop
#%{_datadir}/services/kopete_netmeeting.desktop

%if %{with skype}
%files kopete-protocol-skype
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete*skype*.so
%{_datadir}/apps/kopete/icons/*/*/*/call.png
%{_datadir}/apps/kopete/icons/*/*/*/contact_ffc_overlay.png
%{_datadir}/apps/kopete/icons/*/*/*/contact_unknown_overlay.png
%{_iconsdir}/*/*/*/call.png
%{_datadir}/apps/kopete/icons/*/*/*/*skype*
%{_datadir}/services/kopete_skype.desktop
%{_datadir}/apps/kopete_skype
%endif

%files kopete-protocol-sms
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*sms*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/sms*
#%{_datadir}/services/kopete_sms.desktop

%files kopete-protocol-winpopup
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/winpopup*.sh
#%attr(755,root,root) %{_libdir}/kde4/kopete*wp*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/wp*
#%{_datadir}/services/kopete_wp.desktop
# FIXME: to samba-client instead?
#%dir %attr(777,root,root) /var/lib/winpopup
#%config(noreplace) %verify(not md5 mtime size) /etc/samba/winpopup.conf

%files kopete-protocol-yahoo
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete_yahoo.so
#%{_datadir}/apps/kopete_yahoo
#%{_datadir}/apps/kopete/icons/*/*/*/yahoo*
#%{_datadir}/services/kopete_yahoo.desktop

%files kopete-tool-alias
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_alias.so
#%attr(755,root,root) %{_libdir}/kde4/kopete_alias.so
#%{_datadir}/services/kconfiguredialog/kopete_alias_config.desktop
#%{_datadir}/services/kopete_alias.desktop

%files kopete-tool-autoreplace
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_autoreplace.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*autoreplace*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/autoreplace.png
#%{_datadir}/services/kopete_autoreplace.desktop
#%{_datadir}/services/kconfiguredialog/kopete_autoreplace_config.desktop

%files kopete-tool-avdeviceconfig
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_avdeviceconfig.so
#%{_datadir}/services/kopete_avdeviceconfig.desktop
#%{_datadir}/apps/kopete/icons/*/*/*/kopete_avdevice.png

%files kopete-tool-connectionstatus
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*connectionstatus*.so
#%{_datadir}/services/kopete_connectionstatus.desktop

%files kopete-tool-contactnotes
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete*contactnotes*.so
#%{_datadir}/apps/kopete_contactnotes
#%{_datadir}/services/kopete_contactnotes.desktop

%files kopete-tool-cryptography
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_cryptography.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*cryptography*.so
#%{_datadir}/apps/kopete_cryptography
#%{_datadir}/services/kopete_cryptography.desktop
#%{_datadir}/services/kconfiguredialog/kopete_cryptography_config.desktop

%files kopete-tool-latex
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kopete_latexconvert.sh
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_latex.so
#%attr(755,root,root) %{_libdir}/kde4/kopete_latex.so
#%{_datadir}/apps/kopete/icons/crystalsvg/32x32/apps/latex.png
#%{_datadir}/config.kcfg/latexconfig.kcfg
#%{_datadir}/apps/kopete_latex
#%{_datadir}/services/kconfiguredialog/kopete_addbookmarks_config.desktop
#%{_datadir}/services/kconfiguredialog/kopete_latex_config.desktop
#%{_datadir}/services/kopete_latex.desktop

%files kopete-tool-highlight
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_highlight.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*highlight*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/highlight.png
#%{_datadir}/services/kopete_highlight.desktop
#%{_datadir}/services/kconfiguredialog/kopete_highlight_config.desktop

%files kopete-tool-history
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_history.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*history*.so
#%{_datadir}/apps/kopete_history
#%{_datadir}/config.kcfg/historyconfig.kcfg
#%{_datadir}/services/kopete_history.desktop
#%{_datadir}/services/kconfiguredialog/kopete_history_config.desktop

%files kopete-tool-nowlistening
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_nowlistening.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*nowlistening*.so
#%{_datadir}/config.kcfg/nowlisteningconfig.kcfg
#%{_datadir}/services/kconfiguredialog/kopete_nowlistening_config.desktop
#%{_datadir}/services/kopete_nowlistening.desktop

%files kopete-tool-smpppdcs
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_smpppdcs.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*smpppdcs*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/smpppdcs.png
#%{_datadir}/config.kcfg/smpppdcs.kcfg
#%{_datadir}/services/kconfiguredialog/kopete_smpppdcs_config.desktop
#%{_datadir}/services/kopete_smpppdcs.desktop

%files kopete-tool-texteffect
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_texteffect.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*texteffect*.so
#%{_datadir}/apps/kopete/icons/crystalsvg/*/*/texteffect.png
#%{_datadir}/services/kconfiguredialog/kopete_texteffect_config.desktop
#%{_datadir}/services/kopete_texteffect.desktop

%files kopete-tool-translator
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_translator.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*translator*.so
#%{_datadir}/apps/kopete_translator
#%{_datadir}/services/kconfiguredialog/kopete_translator_config.desktop
#%{_datadir}/services/kopete_translator.desktop

%files kopete-tool-webpresence
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_webpresence.so
#%attr(755,root,root) %{_libdir}/kde4/kopete*webpresence*.so
#%{_datadir}/apps/kopete/webpresence
#%{_datadir}/services/kconfiguredialog/kopete_webpresence_config.desktop
#%{_datadir}/services/kopete_webpresence.desktop

%files kpf
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kpf_panelapplet.so
#%attr(755,root,root) %{_libdir}/kde4/kpfpropertiesdialog.so
#%{_datadir}/apps/kicker/applets/kpfapplet.desktop
#%{_datadir}/services/kpfpropertiesdialogplugin.desktop
#%{_iconsdir}/*/*/*/kpf*

%files kppp 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kppplogview
#%attr(755,root,root) %{_bindir}/kppp
#%{_datadir}/apps/kppp
#%{_desktopdir}/kde/Kppp.desktop
#%{_desktopdir}/kde/kppplogview.desktop
#%{_iconsdir}/*/*/*/kppp.png

%files krfb 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/krdc
#%attr(755,root,root) %{_bindir}/krfb
#%attr(755,root,root) %{_bindir}/krfb_httpd
#%attr(755,root,root) %{_libdir}/kde4/kcm_krfb.so
#%{_datadir}/apps/krdc
#%{_datadir}/apps/krfb
#%{_datadir}/services/kinetd_krfb.desktop
#%{_datadir}/services/kinetd_krfb_httpd.desktop
#%{_datadir}/services/rdp.protocol
#%{_datadir}/services/vnc.protocol
#%{_datadir}/apps/konqueror/servicemenus/smb2rdc.desktop
#%{_desktopdir}/kde/kcmkrfb.desktop
#%{_desktopdir}/kde/krfb.desktop
#%{_desktopdir}/kde/krdc.desktop
#%{_iconsdir}/*/*/*/krdc*
#%{_iconsdir}/[!l]*/*/*/krfb*

%files ksirc 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/ksirc
#%attr(755,root,root) %{_bindir}/dsirc
#%attr(755,root,root) %{_libdir}/libkdeinit_ksirc.so
#%attr(755,root,root) %{_libdir}/kde4/ksirc.so
#%attr(755,root,root) %{_libdir}/kde4/libkntsrcfilepropsdlg.so
#%{_datadir}/config/ksircrc
#%{_datadir}/apps/ksirc
#%{_datadir}/services/kntsrcfilepropsdlg.desktop
#%{_desktopdir}/kde/ksirc.desktop
#%{_iconsdir}/[!l]*/*/*/ksirc*

%files ktalkd 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/ktalkd
#%attr(755,root,root) %{_bindir}/ktalkdlg
#%attr(755,root,root) %{_bindir}/mail.local
#%attr(755,root,root) %{_libdir}/kde4/kcm_ktalkd.so
#%{_datadir}/config/ktalkdrc
#%{_datadir}/sounds/ktalkd.wav
#%{_desktopdir}/kde/kcmktalkd.desktop
#%{_iconsdir}/*/*/*/ktalkd.png

%files kwifimanager 
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kwifimanager
#%attr(755,root,root) %{_libdir}/libkwireless.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_wifi.so
#%{_datadir}/apps/kicker/applets/kwireless.desktop
#%{_datadir}/apps/kwifimanager
#%{_desktopdir}/kde/kcmwifi.desktop
#%{_desktopdir}/kde/kwifimanager.desktop
#%{_iconsdir}/*/*/apps/kwifimanager.*

%files lanbrowser 
%defattr(644,root,root,755)
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lisarc
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/lisa
#%attr(754,root,root) /etc/rc.d/init.d/lisa
#%attr(755,root,root) %{_bindir}/reslisa
#%attr(755,root,root) %{_bindir}/lisa
#%attr(755,root,root) %{_libdir}/kde4/kio_lan.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_lanbrowser.so
#%{_datadir}/apps/lisa
#%{_datadir}/apps/remoteview/lan.desktop
#%{_datadir}/services/rlan.protocol
#%{_datadir}/services/lan.protocol
#%{_datadir}/apps/konqsidebartng/virtual_folders/services/lisa.desktop
#%{_datadir}/applnk/.hidden/kcmkiolan.desktop
#%{_datadir}/applnk/.hidden/kcmlisa.desktop
#%{_datadir}/applnk/.hidden/kcmreslisa.desktop

%files libkopete
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libkopete.so.*.*.*

%files libkopete_videodevice
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libkopete_videodevice.so.*.*.*

%files libkopete_msn
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libkopete_msn_shared.so.*.*.*

%files libkopete_oscar
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libkopete_oscar.so.*.*.*

%files librss
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/librss.so.*.*.*

%files rss
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/feedbrowser
#%attr(755,root,root) %{_bindir}/rssclient
#%attr(755,root,root) %{_bindir}/rssservice
#%{_datadir}/services/rssservice.desktop
