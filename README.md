# hast_qgis_plugin
Repository for all of the code that makes up the qgis plugin for Hastighedskort Studie (HAST)


# Creating a QGIS plugin
![Image](https://user-images.githubusercontent.com/56345889/228541727-17eacf0e-2a14-4140-abd5-297d64ebf6ba.png)
[link to docs](https://docs.qgis.org/3.28/en/docs/pyqgis_developer_cookbook/plugins/plugins.html) 
## UI part
![Image](https://user-images.githubusercontent.com/56345889/228542545-f9a45ca2-7869-4585-92d2-5524ff2d3646.png)
### QT Designer
To use qt designer for extending/altering the UI, install the package `pip install pyqt5-tools`
Open the app on mac with `open -a Designer`.
*For windows, check tutorial [here](https://www.youtube.com/watch?v=FVpho_UiDAY)*

# The Speedmap layers
The files named `hastighedsgraenser2008-01-21` in the folder `layers/Speedmap/` are speed limits recorded through the project "[Pay as you Speed](https://vbn.aau.dk/da/projects/spar-på-farten)" (Spar på farten). 
Pay as you Speed examines if an ecomomic incentive makes people less inclined to drive faster than the speed limit. They do this by giving project participants an onboard GPS tracker, and if it reports that the participant does not exceed the speed limit it reduces their insurance premiums.