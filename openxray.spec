%define git 20240114
Name:           openxray
Version:        0.%{git}
Release:        1
Summary:        X-Ray Engine Linux port by OpenXRay team
License:        Custom
Group:          Games/3D/Shoot
URL:            https://github.com/OpenXRay/xray-16
Source0:        xray-16-%{git}.tar.xz

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  liblockfile-devel
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(cryptopp)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)

%description
OpenXRay is an improved version of the X-Ray Engine, the game engine
used in the world-famous S.T.A.L.K.E.R. game series by GSC Game World.

Currently the following games are supported:
 * S.T.A.L.K.E.R.: Call of Pripyat
 * S.T.A.L.K.E.R.: Clear Sky

To play one of the S.T.A.L.K.E.R. games with OpenXRay you need the
original game files.
See: %{_docdir}/openxray/README.SUSE for details.

%prep
%autosetup -n xray-16-%{git} -p1

%build
#mkdir build && cd build
# FIXME: you should use the %%cmake macros
#        compilation does not work with obs-provided %%optflags!
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build

%install
#cd build
%make_install -C build
# FIXME: .gitattributes should not be part of the installed files
rm %{buildroot}%{_datadir}/openxray/gamedata/shaders/.gitattributes
%fdupes %{buildroot}%{_datadir}

%files
