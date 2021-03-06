# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreIdentifiedObject import CoreIdentifiedObject

class CoreReportingGroup(CoreIdentifiedObject):

    def __init__(self, PowerSystemResource=None, *args, **kw_args):
        """Initialises a new 'CoreReportingGroup' instance.

        @param PowerSystemResource: 
        """
        self._PowerSystemResource = []
        self.PowerSystemResource = [] if PowerSystemResource is None else PowerSystemResource

        super(CoreReportingGroup, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PowerSystemResource"]
    _many_refs = ["PowerSystemResource"]

    def getPowerSystemResource(self):
        """
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        for p in self._PowerSystemResource:
            filtered = [q for q in p.ReportingGroup if q != self]
            self._PowerSystemResource._ReportingGroup = filtered
        for r in value:
            if self not in r._ReportingGroup:
                r._ReportingGroup.append(self)
        self._PowerSystemResource = value

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def addPowerSystemResource(self, *PowerSystemResource):
        for obj in PowerSystemResource:
            if self not in obj._ReportingGroup:
                obj._ReportingGroup.append(self)
            self._PowerSystemResource.append(obj)

    def removePowerSystemResource(self, *PowerSystemResource):
        for obj in PowerSystemResource:
            if self in obj._ReportingGroup:
                obj._ReportingGroup.remove(self)
            self._PowerSystemResource.remove(obj)

