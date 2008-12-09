# TODO
# - fix kopete-tool-{avdeviceconfig,smpppdcs} summaries/descriptions (copy-pastos!)
# - what about non-applied libgadu patch?
# - kill internal libgadu copy
# - BR phonon-devel
#
# Conditional build:
#
%define		_state		unstable
%define		orgname		kdenetwork
%define		qtver		4.4.3

Summary:	K Desktop Environment - network applications
Summary(es.UTF-8):	K Desktop Environment - aplicaciones de red
Summary(pl.UTF-8):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR.UTF-8):	K Desktop Environment - aplicações de rede
Name:		kde4-kdenetwork
Version:	4.1.82
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	5d9183ae6a5028a27204693889d89c76
Patch0:		%{name}-freenx.patch
Patch1:		%{name}-FindDecibel.patch
URL:		http://www.kde.org/
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	cmake >= 2.6.2
BuildRequires:	decibel-devel >= 0.7.0
BuildRequires:	gmp-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libgadu-devel >= 1.4
BuildRequires:	libidn-devel
BuildRequires:	libiw-devel >= 27
BuildRequires:	libjpeg-devel
BuildRequires:	libmsn-devel >= 4.0
#BuildRequires:	libnxcl-devel >= 1.0-0.r612.1
BuildRequires:	libotr-devel >= 3.2.0
BuildRequires:	libtool
BuildRequires:	libvncserver-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	meanwhile-devel >= 1.0.1
BuildRequires:	openslp-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	ortp-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-base
BuildRequires:	qca-devel >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sqlite3-devel
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kdenetwork4
Conflicts:	kdenetwork4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE network applications. Package includes:
- KGet - file downloader
- KNewsticker - News Ticker
- KPPP - PPP dialer
- krdc - remote desktop connection
- krfb - virtual desktops

%description -l pl.UTF-8
Aplikacje sieciowe KDE. Pakiet zawiera następujące programy:
- KGet - ściągacz plików
- KNewsticker - aplet wyświetlający nowości
- KPPP - program do nawiązywania połączeń modemowych
- krdc - zdalny pulpit
- krfb - wirtualne biurka

%package libkopete
Summary:	kopete library
Summary(pl.UTF-8):	Biblioteka kopete
Group:		X11/Libraries
Requires:	kde4-kdelibs >= %{version}

%description libkopete
kopete library.

%description libkopete -l pl.UTF-8
Biblioteka kopete.

%package libkopete_msn
Summary:	MSN protocol shared library
Summary(pl.UTF-8):	Biblioteka współdzielona dla protokołu MSN
Group:		X11/Libraries
Requires:	%{name}-libkopete = %{version}-%{release}

%description libkopete_msn
MSN protocol shared library.

%description libkopete_msn -l pl.UTF-8
Biblioteka współdzielona dla protokołu MSN.

%package libkopete_oscar
Summary:	Shared library which adds OSCAR protocol support
Summary(pl.UTF-8):	Biblioteka dodająca obsługę protokołu OSCAR
Group:		X11/Applications/Networking
Requires:	%{name}-libkopete = %{version}-%{release}

%description libkopete_oscar
A shared library which adds OSCAR protocol support needed eg. by AIM
and ICQ.

%description libkopete_oscar -l pl.UTF-8
Biblioteka dodająca obsługę protokołu OSCAR, używanego między
innymi przez AIM i ICQ.

%package libkopete_otr
Summary:	Shared library which adds OTR protocol support
Summary(pl.UTF-8):	Biblioteka dodająca obsługę protokołu OTR
Group:		X11/Applications/Networking
Requires:	%{name}-libkopete = %{version}-%{release}

%description libkopete_otr
A shared library which adds OTR protocol support needed eg. AIM and
ICQ.

%description libkopete_otr -l pl.UTF-8
Biblioteka dodająca obsługę protokołu OTR, używanego między
innymi przez AIM i ICQ.

%package libkopete_videodevice
Summary:	Video input device support library for kopete
Summary(pl.UTF-8):	Biblioteka z obsługą urządzeń wejścia video dla kopete
Group:		X11/Libraries
Requires:	%{name}-libkopete = %{version}-%{release}

%description libkopete_videodevice
Video input device support library for kopete.

%description libkopete_videodevice -l pl.UTF-8
Biblioteka z obsługą urządzeń wejścia video dla kopete.

%package devel
Summary:	kdenetwork header files
Summary(pl.UTF-8):	Pliki nagłówkowe kdenetwork
Group:		X11/Development/Libraries
Requires:	%{name}-libkopete_msn = %{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{version}-%{release}
Requires:	%{name}-libkopete_otr = %{version}-%{release}
Requires:	%{name}-libkopete_videodevice = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

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
Requires:	kde4-kdebase >= %{version}

%description filesharing
File sharing plugins.

%description filesharing -l pl.UTF-8
Wtyczki obsługujące współdzielenie plików.

%package kdnssd
Summary:	DNS-SD Services Watcher
Summary(pl.UTF-8):	Nadzorowanie usług DNS-SD
License:	Artistic
Group:		X11/Applications

%description kdnssd
DNS-SD Services Watcher.

%description kdnssd -l pl.UTF-8
Nadzorowanie usług DNS-SD.

%package kget
Summary:	File downloand manager
Summary(pl.UTF-8):	Zarządca ściągania plików
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Requires:	kde4-kdebase-workspace >= %{version}

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
Requires:	%{name}-libkopete = %{version}-%{release}
Requires:	kde4-kdebase >= %{version}
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
Requires:	%{name}-kopete = %{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{version}-%{release}
Obsoletes:	kopete-protocol-aim

%description kopete-protocol-aim
Kopete plugin which adds AIM protocol support.

%description kopete-protocol-aim -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu AIM.

%package kopete-protocol-bonjour
Summary:	Kopete plugin which adds Bonjour protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Bonjour
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-protocol-bonjour
Kopete plugin which adds Bonjour protocol support.

%description kopete-protocol-bonjour -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Bonjour.

%package kopete-protocol-gg
Summary:	Kopete plugin which adds GaduGadu protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu GaduGadu
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Obsoletes:	kopete-protocol-gg

%description kopete-protocol-gg
Kopete plugin which adds GaduGadu protocol support.

%description kopete-protocol-gg -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu GaduGadu.

%package kopete-protocol-groupwise
Summary:	Kopete plugin which adds Groupwise protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Groupwise
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
#Suggests:	qt-plugin-qca-tls
Obsoletes:	kopete-protocol-groupwise

%description kopete-protocol-groupwise
Kopete plugin which adds Groupwise protocol support.

%description kopete-protocol-groupwise -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Groupwise.

%package kopete-protocol-icq
Summary:	Kopete plugin which adds ICQ protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu ICQ
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Requires:	%{name}-libkopete_oscar = %{version}-%{release}
Obsoletes:	kopete-protocol-icq

%description kopete-protocol-icq
Kopete plugin which adds ICQ protocol support.

%description kopete-protocol-icq -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu ICQ.

%package kopete-protocol-jabber
Summary:	Kopete plugin which adds Jabber protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Jabber
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
#Suggests:	qt-plugin-qca-tls
Obsoletes:	kopete-protocol-jabber

%description kopete-protocol-jabber
Kopete plugin which adds Jabber protocol support.

%description kopete-protocol-jabber -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Jabber.

%package kopete-protocol-meanwhile
Summary:	Kopete plugin which adds Meanwhile protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Meanwhile
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-protocol-meanwhile
Kopete plugin which adds Meanwhile protocol support.

%description kopete-protocol-meanwhile -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Meanwhile.

%package kopete-protocol-wlm
Summary:	Kopete plugin which adds WLM (Windows Live Messenger) protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu WLM
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-protocol-wlm
Kopete plugin which adds WLM (Windows Live Messenger) protocol support.

%description kopete-protocol-wlm -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu WLM (Windows Live Messenger).

%package kopete-protocol-msn
Summary:	Kopete plugin which adds MSN protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu MSN
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Requires:	%{name}-libkopete_msn = %{version}-%{release}
Obsoletes:	kopete-protocol-msn

%description kopete-protocol-msn
Kopete plugin which adds MSN protocol support.

%description kopete-protocol-msn -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu MSN.

%package kopete-protocol-sms
Summary:	Kopete plugin which adds SMS contact support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę kontaktów SMS
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Obsoletes:	kopete-protocol-sms

%description kopete-protocol-sms
Kopete plugin which adds SMS contact support.

%description kopete-protocol-sms -l pl.UTF-8
Wtyczka Kopete dodająca obsługę kontaktów SMS.

%package kopete-protocol-testbed
Summary:	A sample plugin for kopete
Summary(pl.UTF-8):	Przykładowa wtyczka dla kopete.
Group:		X11/Development/Libraries
Requires:	%{name}-kopete = %{version}-%{release}

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
Requires:	%{name}-kopete = %{version}-%{release}
Obsoletes:	kopete-protocol-winpopup

%description kopete-protocol-winpopup
Kopete plugin which adds WinPopUp messaging support.

%description kopete-protocol-winpopup -l pl.UTF-8
Wtyczka Kopete dodająca obsługę komunikacji przez WinPopUp.

%package kopete-protocol-yahoo
Summary:	Kopete plugin which adds Yahoo protocol support
Summary(pl.UTF-8):	Wtyczka Kopete dodająca obsługę protokołu Yahoo
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Obsoletes:	kopete-protocol-yahoo

%description kopete-protocol-yahoo
Kopete plugin which adds Yahoo protocol support.

%description kopete-protocol-yahoo -l pl.UTF-8
Wtyczka Kopete dodająca obsługę protokołu Yahoo.

%package kopete-tool-autoaway
Summary:	Kopete autoaway plugin
Summary(pl.UTF-8):	Wtyczka Kopete do automatycznego przechodzenia w stan zajęty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
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
Requires:	%{name}-kopete = %{version}-%{release}
Obsoletes:	kopete-tool-alias

%description kopete-tool-alias
Kopete plugin to add custom aliases for commands.

%description kopete-tool-alias -l pl.UTF-8
Wtyczka Kopete do dodawania własnych aliasów dla poleceń.

%package kopete-tool-avdeviceconfig
Summary:	Kopete avdeviceconfig plugin
Summary(pl.UTF-8):	Wtyczka Kopete do automatycznego przechodzenia w stan zajęty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-tool-avdeviceconfig
Kopete plugin which automatically changes status to away. Conditions
are configurable.

%description kopete-tool-avdeviceconfig -l pl.UTF-8
Wtyczka Kopete automatycznie zmieniająca status na zajęty. Warunki,
po zaistnieniu których ma nastąpić, są konfigurowalne.

%package kopete-tool-autoreplace
Summary:	Kopete plugin which autoreplaces some text you can choose
Summary(pl.UTF-8):	Wtyczka Kopete do automatycznej zamiany tekstu
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-tool-autoreplace
Kopete plugin which autoreplaces some text you can choose.

%description kopete-tool-autoreplace -l pl.UTF-8
Wtyczka Kopete do automatycznej zamiany tekstu.

%package kopete-tool-contactnotes
Summary:	Kopete tool which adds personal notes to your contacts
Summary(pl.UTF-8):	Narzędzie Kopete do dodawania notatek do kontaktów
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Obsoletes:	kopete-tool-contactnotes

%description kopete-tool-contactnotes
Kopete tool which allows adding personal notes to your contacts.

%description kopete-tool-contactnotes -l pl.UTF-8
Narzędzie Kopete umożliwiające dodawanie notatek do kontaktów.

%package kopete-tool-highlight
Summary:	A highlighter plugin for Kopete
Summary(pl.UTF-8):	Wtyczka Kopete podkreślająca wybrane teksty
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Obsoletes:	kopete-tool-highlight

%description kopete-tool-highlight
A highlighter plugin for Kopete.

%description kopete-tool-highlight -l pl.UTF-8
Wtyczka Kopete podkreślająca wybrane teksty.

%package kopete-tool-latex
Summary:	A LaTeX plugin for Kopete
Summary(pl.UTF-8):	Wtyczka Kopete renderująca tekst w formacie LaTeXa
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-tool-latex
A LaTeX plugin for Kopete.

%description kopete-tool-latex -l pl.UTF-8
Wtyczka Kopete renderująca tekst w formacie LaTeXa.

%package kopete-tool-history
Summary:	A history plugin for Kopete
Summary(pl.UTF-8):	Wtyczka Kopete obsługująca historię rozmów
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-tool-history
A history plugin for Kopete.

%description kopete-tool-history -l pl.UTF-8
Wtyczka Kopete obsługująca historię rozmów.

%package kopete-tool-importer
Summary:	Contact importer for Kopete
Summary(pl.UTF-8):	Importer kontaktów dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

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
Requires:	%{name}-kopete = %{version}-%{release}

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
Requires:	%{name}-kopete = %{version}-%{release}

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
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-tool-spellcheck
A spell checking plugin for Kopete.

%description kopete-tool-spellcheck -l pl.UTF-8
Wtyczka Kopete sprawdzająca pisownie.

%package kopete-tool-texteffect
Summary:	Kopete plugin that adds nice effects to your messages
Summary(pl.UTF-8):	Wtyczka Kopete dodająca ładne efekty do wiadomości
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-tool-texteffect
Kopete plugin that adds nice effects to your messages.

%description kopete-tool-texteffect -l pl.UTF-8
Wtyczka Kopete dodająca ładne efekty do wiadomości.

%package kopete-tool-translator
Summary:	Kopete plugin which uses babelfish to translate messages
Summary(pl.UTF-8):	Wtyczka Kopete wykorzystująca babelfish do tłumaczenia wiadomości
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}

%description kopete-tool-translator
This Kopete plugin uses web translating engines (like Altavista's
babelfish or Google) to translate messages.

%description kopete-tool-translator -l pl.UTF-8
Ta wtyczka Kopete wykorzystuje babelfish do tłumaczenia wiadomości.

%package kopete-tool-webpresence
Summary:	Web contactlist presenter for Kopete
Summary(pl.UTF-8):	Wyświetlacz listy kontaktów na WWW dla Kopete
Group:		X11/Applications/Networking
Requires:	%{name}-kopete = %{version}-%{release}
Requires:	libxml2 >= 2.4.8
Requires:	libxslt >= 1.0.7

%description kopete-tool-webpresence
This Kopete plugin shows the status of your IM accounts on a webpage.

%description kopete-tool-webpresence -l pl.UTF-8
Ta wtyczka Kopete pokazuje status (całej lub części) listy
kontaktów na stronie WWW.

%package kppp
Summary:	KDE PPP dialer
Summary(pl.UTF-8):	Program do połączeń modemowych dla KDE
Summary(pt_BR.UTF-8):	O discador para Internet
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
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

%package krfb
Summary:	Virtual Desktops
Summary(pl.UTF-8):	Wirtualne biurka
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
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

%prep
%setup -q -n %{orgname}-%{version}
%patch1 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libkopete	-p /sbin/ldconfig
%postun	libkopete	-p /sbin/ldconfig

%if 0
%post	libkopete_msn	-p /sbin/ldconfig
%postun	libkopete_msn	-p /sbin/ldconfig
%endif

%post	libkopete_oscar	-p /sbin/ldconfig
%postun	libkopete_oscar	-p /sbin/ldconfig

%post	libkopete_otr	-p /sbin/ldconfig
%postun	libkopete_otr	-p /sbin/ldconfig

%post	libkopete_videodevice	-p /sbin/ldconfig
%postun	libkopete_videodevice	-p /sbin/ldconfig

%post	kget		-p /sbin/ldconfig
%postun	kget		-p /sbin/ldconfig

%post	kopete		-p /sbin/ldconfig
%postun	kopete		-p /sbin/ldconfig

%files libkopete
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete.so.?

%if 0
%files libkopete_msn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete_msn_shared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_msn_shared.so.?
%endif

%files libkopete_oscar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete_oscar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_oscar.so.?

%files libkopete_otr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete_otr_shared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_otr_shared.so.?

%files libkopete_videodevice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkopete_videodevice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_videodevice.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiris_kopete.so
%attr(755,root,root) %{_libdir}/libkopete.so
#%attr(755,root,root) %{_libdir}/libkopete_msn_shared.so
%attr(755,root,root) %{_libdir}/libkopete_oscar.so
%attr(755,root,root) %{_libdir}/libkopete_otr_shared.so
%attr(755,root,root) %{_libdir}/libkopete_videodevice.so
%attr(755,root,root) %{_libdir}/libkopeteaddaccountwizard.so
%attr(755,root,root) %{_libdir}/libkopetechatwindow_shared.so
%attr(755,root,root) %{_libdir}/libkopeteidentity.so
%attr(755,root,root) %{_libdir}/libkopeteprivacy.so
%attr(755,root,root) %{_libdir}/libkopetestatusmenu.so
%attr(755,root,root) %{_libdir}/liboscar.so
%{_includedir}/kopete

%files filesharing
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_fileshare.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kcmsambaconf.so
%attr(755,root,root) %{_libdir}/kde4/fileshare_propsdlgplugin.so
%{_datadir}/kde4/services/fileshare.desktop
%{_datadir}/kde4/services/fileshare_propsdlgplugin.desktop
%{_datadir}/kde4/services/kcmsambaconf.desktop
%{_iconsdir}/hicolor/16x16/apps/kcmsambaconf.png
%{_datadir}/kde4/services/ServiceMenus/smb2rdc.desktop

%files kdnssd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kded_dnssdwatcher.so
%attr(755,root,root) %{_libdir}/kde4/kio_zeroconf.so
%{_datadir}/apps/remoteview/zeroconf.desktop
%{_datadir}/kde4/services/kded/dnssdwatcher.desktop
%{_datadir}/kde4/services/zeroconf.protocol
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml

%files kget
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kget
%attr(755,root,root) %{_libdir}/kde4/kget_bittorrentfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_contentfetchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_kiofactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_metalinkfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_mirrorsearchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_multisegkiofactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_bittorrentfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_contentfetchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_mirrorsearchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_multisegkiofactory.so
%attr(755,root,root) %{_libdir}/kde4/khtml_kget.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kget.so
%attr(755,root,root) %{_libdir}/kde4/plasma_kget_barapplet.so
%attr(755,root,root) %{_libdir}/kde4/plasma_kget_panelbar.so
%attr(755,root,root) %{_libdir}/kde4/plasma_kget_piechart.so
%attr(755,root,root) %{_libdir}/libkgetcore.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkgetcore.so.?
%attr(755,root,root) %{_libdir}/libkgetcore.so
%{_datadir}/apps/desktoptheme/default/widgets/kget.svg
%{_datadir}/apps/kget
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/config.kcfg/kget.kcfg
%{_datadir}/config.kcfg/kget_multisegkiofactory.kcfg
%{_datadir}/config.kcfg/kget_mirrorsearchfactory.kcfg
%{_datadir}/config.kcfg/kget_contentfetchfactory.kcfg
%{_datadir}/kde4/services/kget_bittorrentfactory_config.desktop
%{_datadir}/kde4/services/kget_contentfetchfactory.desktop
%{_datadir}/kde4/services/kget_contentfetchfactory_config.desktop
%{_datadir}/kde4/services/kget_mirrorsearchfactory_config.desktop
%{_datadir}/kde4/services/kget_multisegkiofactory_config.desktop
%{_datadir}/kde4/services/ServiceMenus/kget_download.desktop
%{_datadir}/kde4/services/kget_bittorrentfactory.desktop
%{_datadir}/kde4/services/kget_kiofactory.desktop
%{_datadir}/kde4/services/kget_metalinkfactory.desktop
%{_datadir}/kde4/services/kget_multisegkiofactory.desktop
%{_datadir}/kde4/services/kget_mirrorsearchfactory.desktop
%{_datadir}/kde4/services/kgetbarapplet-default.desktop
%{_datadir}/kde4/services/kgetpanelbarapplet-default.desktop
%{_datadir}/kde4/services/kgetpiechartapplet-default.desktop
%{_datadir}/kde4/services/plasma-engine-kget.desktop
%{_datadir}/kde4/servicetypes/kget_plugin.desktop
%{_desktopdir}/kde4/kget.desktop
%{_iconsdir}/*/*/*/*kget*
%{_kdedocdir}/en/kget

#%files knewsticker
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/plasma_applet_knewsticker.so
#%{_datadir}/kde4/services/plasma-knewsticker-default.desktop
#%{_iconsdir}/*/*/*/knewsticker.png
#%{_kdedocdir}/en/knewsticker

%files kopete
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kopete
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_accountconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_addbookmarks.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_appearanceconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_behaviorconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_chatwindowconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_otr.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_pipes.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_pluginconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_privacy.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_statusconfig.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_urlpicpreview.so
%attr(755,root,root) %{_libdir}/kde4/kopete_addbookmarks.so
%attr(755,root,root) %{_libdir}/kde4/kopete_chatwindow.so
%attr(755,root,root) %{_libdir}/kde4/kopete_emailwindow.so
%attr(755,root,root) %{_libdir}/kde4/kopete_otr.so
%attr(755,root,root) %{_libdir}/kde4/kopete_pipes.so
%attr(755,root,root) %{_libdir}/kde4/kopete_privacy.so
%attr(755,root,root) %{_libdir}/kde4/kopete_qq.so
%attr(755,root,root) %{_libdir}/kde4/kopete_statistics.so
%attr(755,root,root) %{_libdir}/kde4/kopete_testbed.so
%attr(755,root,root) %{_libdir}/kde4/kopete_urlpicpreview.so
%attr(755,root,root) %{_libdir}/kde4/libkrichtexteditpart.so

%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-account-0.10.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-account-kconf_update.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-account-kconf_update.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-jabberproxytype-kconf_update.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-jabberproxytype-kconf_update.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-initialstatus.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-initialstatus.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-nameTracking.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-pluginloader.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-pluginloader.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-pluginloader2.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/kopete-pluginloader2.upd

#### ???
%attr(755,root,root) %{_libdir}/libiris_kopete.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libiris_kopete.so.?
%attr(755,root,root) %{_libdir}/libkopeteaddaccountwizard.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libkopeteaddaccountwizard.so.?
%attr(755,root,root) %{_libdir}/libkopetechatwindow_shared.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libkopetechatwindow_shared.so.?
%attr(755,root,root) %{_libdir}/libkopeteidentity.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libkopeteidentity.so.?
%attr(755,root,root) %{_libdir}/libkopeteprivacy.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libkopeteprivacy.so.?
%attr(755,root,root) %{_libdir}/liboscar.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/liboscar.so.?
%attr(755,root,root) %{_libdir}/libkopetestatusmenu.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libkopetestatusmenu.so.?
####

%dir %{_datadir}/apps/kopete
%dir %{_datadir}/apps/kopete/icons
%dir %{_datadir}/apps/kopete/icons/crystalsvg
%dir %{_datadir}/apps/kopete/icons/crystalsvg/*
#%dir %{_datadir}/apps/kopete/icons/crystalsvg/*/*
%dir %{_datadir}/apps/kopete/icons/oxygen
%dir %{_datadir}/apps/kopete/icons/oxygen/*
%dir %{_datadir}/apps/kopete/icons/oxygen/*/apps
%dir %{_datadir}/apps/kopete/icons/hicolor
%dir %{_datadir}/apps/kopete/icons/hicolor/*
%dir %{_datadir}/apps/kopete/icons/hicolor/*/apps
#%dir %{_datadir}/apps/kopete/pics

%{_datadir}/apps/kopete/*rc
%{_datadir}/apps/kopete/icons/*/*/actions
%{_datadir}/apps/kopete/icons/*/*/apps/testbed_protocol.png
%{_datadir}/apps/kopete/icons/*/*/apps/qq_protocol.png
%{_datadir}/apps/kopete/icons/*/*/apps/preferences-plugin-text-effect-kopete.png
%{_datadir}/apps/kopete/icons/*/*/apps/preferences-text-autocorrection-kopete.png
%{_datadir}/apps/kopete/icons/*/*/apps/preferences-text-highlighting-kopete.png
#%{_datadir}/apps/kopete/pics/statistics
%{_datadir}/apps/kopete/styles
%{_datadir}/apps/kopete_otr
%{_datadir}/apps/kopete_privacy
%{_datadir}/apps/kopete_statistics
%{_datadir}/apps/kopeterichtexteditpart
%{_datadir}/config/kopeterc
%{_datadir}/config.kcfg/kopeteappearancesettings.kcfg
%{_datadir}/config.kcfg/kopetebehaviorsettings.kcfg
%{_datadir}/config.kcfg/kopetestatussettings.kcfg
%{_datadir}/config.kcfg/urlpicpreview.kcfg
%{_datadir}/config.kcfg/kopete_otr.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Kopete.xml
%{_datadir}/dbus-1/interfaces/org.kde.kopete.Client.xml
%{_datadir}/dbus-1/interfaces/org.kde.kopete.Statistics.xml
%{_datadir}/kde4/services/chatwindow.desktop
%{_datadir}/kde4/services/emailwindow.desktop
%{_datadir}/kde4/services/kopete_accountconfig.desktop
%{_datadir}/kde4/services/kopete_addbookmarks.desktop
%{_datadir}/kde4/services/kopete_appearanceconfig.desktop
%{_datadir}/kde4/services/kopete_behaviorconfig.desktop
%{_datadir}/kde4/services/kopete_chatwindowconfig.desktop
%{_datadir}/kde4/services/kopete_pluginconfig.desktop
%{_datadir}/kde4/services/kopete_statistics.desktop
%{_datadir}/kde4/services/kopete_qq.desktop
%{_datadir}/kde4/services/kopete_testbed.desktop
%{_datadir}/kde4/services/kopete_urlpicpreview.desktop
%{_datadir}/kde4/services/kconfiguredialog
%{_datadir}/kde4/services/kopete_privacy.desktop
%{_datadir}/kde4/services/kopete_pipes.desktop
%{_datadir}/kde4/services/kopete_statusconfig.desktop
%{_datadir}/kde4/services/kopete_otr.desktop
%{_datadir}/kde4/servicetypes/kopeteplugin.desktop
%{_datadir}/kde4/servicetypes/kopeteprotocol.desktop
%{_datadir}/kde4/servicetypes/kopeteui.desktop
%{_datadir}/sounds/Kopete_Event.ogg
%{_datadir}/sounds/Kopete_Received.ogg
%{_datadir}/sounds/Kopete_Sent.ogg
%{_datadir}/sounds/Kopete_User_is_Online.ogg
%{_desktopdir}/kde4/kopete.desktop
%{_iconsdir}/*/*/*/kopete.png
%{_iconsdir}/*/*/actions/*
%{_iconsdir}/oxygen/*/*/kopete*
%{_iconsdir}/oxygen/*/status/object-locked-*
%{_iconsdir}/*/scalable/apps/kopete.svgz
%{_kdedocdir}/en/kopete

%files kopete-protocol-aim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_aim.so
%{_datadir}/apps/kopete/icons/*/*/*/*aim*
%{_datadir}/kde4/services/aim.protocol
%{_datadir}/kde4/services/kopete_aim.desktop

%files kopete-protocol-bonjour
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_bonjour.so
%{_datadir}/apps/kopete/icons/*/*/*/bonjour_protocol.png
%{_datadir}/kde4/services/kopete_bonjour.desktop

%files kopete-protocol-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_gadu.so
%attr(755,root,root) %{_libdir}/libgadu_kopete.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libgadu_kopete.so.1
%attr(755,root,root) %{_libdir}/libgadu_kopete.so
%{_datadir}/apps/kopete/icons/*/*/*/gadu*
%{_datadir}/apps/kopete/icons/*/*/*/gg*
%{_datadir}/kde4/services/kopete_gadu.desktop

%files kopete-protocol-groupwise
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_groupwise.so
%attr(755,root,root) %{_libdir}/libqgroupwise.so
%{_datadir}/apps/kopete/icons/*/*/*/groupwise_protocol.png
%{_datadir}/apps/kopete_groupwise
%{_datadir}/kde4/services/kopete_groupwise.desktop

%files kopete-protocol-icq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_icq.so
%{_datadir}/apps/kopete/icons/*/*/*/*icq*
%{_datadir}/kde4/services/kopete_icq.desktop

%files kopete-protocol-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete*jabber*.so
%{_datadir}/apps/kopete_jabber
%{_datadir}/apps/kopete/icons/*/*/*/jabber*.png
%{_datadir}/kde4/services/xmpp.protocol
%{_datadir}/kde4/services/kopete_jabber.desktop

#%files kopete-protocol-msn
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/kopete_msn.so
#%{_datadir}/apps/kopete_msn
#%{_datadir}/apps/kopete/icons/*/*/*/msn_*.png
#%{_datadir}/kde4/services/kopete_msn.desktop

%files kopete-protocol-meanwhile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_meanwhile.so
%{_datadir}/apps/kopete/icons/*/*/*/meanwhile_*.png
%{_datadir}/kde4/services/kopete_meanwhile.desktop

%files kopete-protocol-wlm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_wlm.so
%{_datadir}/apps/kopete/icons/*/*/*/wlm_*.png
%{_datadir}/kde4/services/kopete_wlm.desktop
%dir %{_datadir}/apps/kopete_wlm
%{_datadir}/apps/kopete_wlm/wlmchatui.rc

%files kopete-protocol-sms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_sms.so
%{_datadir}/apps/kopete/icons/*/*/*/sms*
%{_datadir}/kde4/services/kopete_sms.desktop

%files kopete-protocol-winpopup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/winpopup*.sh
%attr(755,root,root) %{_libdir}/kde4/kopete_wp.so
%{_datadir}/apps/kopete/icons/*/*/*/wp*
%{_datadir}/kde4/services/kopete_wp.desktop
# FIXME: to samba-client instead?
#%dir %attr(777,root,root) /var/lib/winpopup
#%config(noreplace) %verify(not md5 mtime size) /etc/samba/winpopup.conf

%files kopete-protocol-yahoo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_yahoo.so
%attr(755,root,root) %{_libdir}/libkyahoo.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libkyahoo.so.1
%attr(755,root,root) %{_libdir}/libkyahoo.so
%{_datadir}/apps/kopete_yahoo
%{_datadir}/apps/kopete/icons/*/*/*/yahoo*
%{_datadir}/kde4/services/kopete_yahoo.desktop

%files kopete-tool-alias
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_alias.so
%attr(755,root,root) %{_libdir}/kde4/kopete_alias.so
%{_datadir}/kde4/services/kconfiguredialog/kopete_alias_config.desktop
%{_datadir}/kde4/services/kopete_alias.desktop

%files kopete-tool-autoreplace
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_autoreplace.so
%attr(755,root,root) %{_libdir}/kde4/kopete*autoreplace*.so
%{_datadir}/kde4/services/kopete_autoreplace.desktop
%{_datadir}/kde4/services/kconfiguredialog/kopete_autoreplace_config.desktop

%files kopete-tool-avdeviceconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_avdeviceconfig.so
%{_datadir}/apps/kopete/icons/*/*/*/kopete_avdevice.png
%{_datadir}/kde4/services/kopete_avdeviceconfig.desktop

%files kopete-tool-contactnotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kopete_contactnotes.so
%{_datadir}/apps/kopete_contactnotes
%{_datadir}/kde4/services/kopete_contactnotes.desktop

%files kopete-tool-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kopete_latexconvert.sh
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_latex.so
%attr(755,root,root) %{_libdir}/kde4/kopete_latex.so
%{_datadir}/apps/kopete/icons/*/*/apps/latex.png
%{_datadir}/apps/kopete_latex
%{_datadir}/config.kcfg/latexconfig.kcfg
%{_datadir}/kde4/services/kconfiguredialog/kopete_addbookmarks_config.desktop
%{_datadir}/kde4/services/kconfiguredialog/kopete_latex_config.desktop
%{_datadir}/kde4/services/kopete_latex.desktop

%files kopete-tool-highlight
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_highlight.so
%attr(755,root,root) %{_libdir}/kde4/kopete*highlight*.so
%{_datadir}/kde4/services/kopete_highlight.desktop
%{_datadir}/kde4/services/kconfiguredialog/kopete_highlight_config.desktop

%files kopete-tool-history
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_history.so
%attr(755,root,root) %{_libdir}/kde4/kopete_history.so
%{_datadir}/apps/kopete_history
%{_datadir}/config.kcfg/historyconfig.kcfg
%{_datadir}/kde4/services/kopete_history.desktop
%{_datadir}/kde4/services/kconfiguredialog/kopete_history_config.desktop

%files kopete-tool-nowlistening
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_nowlistening.so
%attr(755,root,root) %{_libdir}/kde4/kopete*nowlistening*.so
%{_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{_datadir}/kde4/services/kconfiguredialog/kopete_nowlistening_config.desktop
%{_datadir}/kde4/services/kopete_nowlistening.desktop

%files kopete-tool-texteffect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_texteffect.so
%attr(755,root,root) %{_libdir}/kde4/kopete*texteffect*.so
%{_datadir}/kde4/services/kconfiguredialog/kopete_texteffect_config.desktop
%{_datadir}/kde4/services/kopete_texteffect.desktop

%files kopete-tool-translator
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_translator.so
%attr(755,root,root) %{_libdir}/kde4/kopete_translator.so
%{_datadir}/apps/kopete_translator
%{_datadir}/kde4/services/kconfiguredialog/kopete_translator_config.desktop
%{_datadir}/kde4/services/kopete_translator.desktop

%files kopete-tool-webpresence
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kopete_webpresence.so
%attr(755,root,root) %{_libdir}/kde4/kopete*webpresence*.so
%{_datadir}/apps/kopete/webpresence
%{_datadir}/kde4/services/kconfiguredialog/kopete_webpresence_config.desktop
%{_datadir}/kde4/services/kopete_webpresence.desktop

%files kppp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_datadir}/apps/kppp
%{_datadir}/dbus-1/interfaces/org.kde.kppp.xml
%{_desktopdir}/kde4/Kppp.desktop
%{_desktopdir}/kde4/kppplogview.desktop
%{_iconsdir}/*/*/*/kppp.png
%{_kdedocdir}/en/kppp

%files krfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krdc
%attr(755,root,root) %{_bindir}/krfb
%{_datadir}/apps/krdc
%{_datadir}/apps/krfb
%{_datadir}/config.kcfg/krdc.kcfg
%{_datadir}/kde4/services/rdp.protocol
%{_datadir}/kde4/services/vnc.protocol
%{_desktopdir}/kde4/krdc.desktop
%{_desktopdir}/kde4/krfb.desktop
%{_kdedocdir}/en/krdc
%{_kdedocdir}/en/krfb
