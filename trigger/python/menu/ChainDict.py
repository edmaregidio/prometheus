
__all__ = ["electron_chainDict", "photon_chainDict"]


electron_chainDict = {

    "signature"         : ['e'],
    "extraInfo"         : ['ringer', 'noringer'],
    "idInfo"            : ['tight','medium','loose','vloose','lhtight','lhmedium','lhloose','lhvloose', 'etcut'],
    "isoInfo"           : ['ivarloose', 'ivarmedium', 'ivartight', 'iloose', 'icaloloose', 'icalomedium', 'icalotight' ],
    "ringerVersion"     : ['v1','v2','v6','v7','v8','v9','v10','v11'], # for fastcalo
    "ringerVersion_el"  : ['v1_el', 'v2_el'], # for fastelectron
    "ringerExtraInfo"   : ['r2'],
    }


photon_chainDict = {

    "signature"         : ['g'],
    "extraInfo"         : ['ringer', 'noringer'],
    "idInfo"            : ['tight','medium','loose','etcut'],
    "isoInfo"           : [],
    "ringerVersion"     : ['v1','v2'], # for fastcalo
    "ringerVersion_el"  : [], # for fastelectron
    "ringerExtraInfo"   : [],
    }





