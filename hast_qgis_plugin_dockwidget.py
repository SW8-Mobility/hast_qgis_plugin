# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HastQgisPluginDockWidget
                                 A QGIS plugin
 This plugin provides a layer of speed limits from a set of gps coordinates
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-04-04
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Alexander Nesheim,  Alexander Højgaard, Casper Kjærhus, Freja Herreborg, Jakob Gregersen
        email                : cs-23-sw-8-04@student.aau.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.core import QgsProject  # type: ignore
from qgis.PyQt import QtGui, QtWidgets, uic  # type: ignore
from qgis.PyQt.QtCore import pyqtSignal  # type: ignore

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "hast_qgis_plugin_dockwidget_base.ui")
)


class HastQgisPluginDockWidget(QtWidgets.QDockWidget, FORM_CLASS):  # type: ignore
    closingPlugin = pyqtSignal()

    def __init__(self, iface, parent=None):
        """Constructor."""
        super(HastQgisPluginDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        self.calculateSpeedLimitButton.clicked.connect(self.insert_spedmap_layer)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def insert_spedmap_layer(self):
        speedmap_name = "2008_data_layer"
        if not len(QgsProject.instance().mapLayersByName(speedmap_name)) != 0:
            self.iface.addVectorLayer(
                "/Users/lille/Speedmap/hastighedsgraenser2008-01-21.shp",
                speedmap_name,
                "ogr",
            )
