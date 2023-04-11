# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = "cs-23-sw-8-04@student.aau.dk"
__date__ = "2023-04-04"
__copyright__ = "Copyright 2023, Alexander Nesheim,  Alexander Højgaard, Casper Kjærhus, Freja Herreborg, Jakob Gregersen"

import unittest

from qgis.PyQt.QtWidgets import QDockWidget  # type: ignore

from hast_qgis_plugin_dockwidget import HastQgisPluginDockWidget  # type: ignore
from test.test_resources import HastQgisPluginDialogTest  # type: ignore

from .utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class HastQgisPluginDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = HastQgisPluginDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass


if __name__ == "__main__":
    suite = unittest.makeSuite(HastQgisPluginDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
