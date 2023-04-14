# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HastQgisPlugin
                                 A QGIS plugin
 This plugin provides a layer of speed limits from a set of gps coordinates
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-04-04
        copyright            : (C) 2023 by Alexander Nesheim,  Alexander Højgaard, Casper Kjærhus, Freja Herreborg, Jakob Gregersen
        email                : cs-23-sw-8-04@student.aau.dk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HastQgisPlugin class from file HastQgisPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hast_qgis_plugin import HastQgisPlugin  # type: ignore

    return HastQgisPlugin(iface)
