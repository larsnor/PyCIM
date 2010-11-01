# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WindingTest(IdentifiedObject):
    """Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.
    """

    def __init__(self, phaseShift=0.0, fromTapStep=0, noLoadLoss=0.0, toTapStep=0, excitingCurrent=0.0, loadLoss=0.0, leakageImpedance=0.0, voltage=0.0, To_TransformerWinding=None, From_TransformerWinding=None, *args, **kw_args):
        """Initializes a new 'WindingTest' instance.

        @param phaseShift: The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param fromTapStep: The tap step number for the 'from' winding of the test pair. 
        @param noLoadLoss: The no load loss kW 'to' winding open-circuited) from the test report. 
        @param toTapStep: The tap step number for the 'to' winding of the test pair. 
        @param excitingCurrent: The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage 
        @param loadLoss: The load loss kW ('to' winding short-circuited) from the test report. 
        @param leakageImpedance: The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding. 
        @param voltage: The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param To_TransformerWinding: The winding to which the test was conducted.  Note that although the 'from' side of the test is required, the 'to' side of a test is not always required.
        @param From_TransformerWinding: The winding from which the test was conducted
        """
        #: The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        self.phaseShift = phaseShift

        #: The tap step number for the 'from' winding of the test pair. 
        self.fromTapStep = fromTapStep

        #: The no load loss kW 'to' winding open-circuited) from the test report. 
        self.noLoadLoss = noLoadLoss

        #: The tap step number for the 'to' winding of the test pair. 
        self.toTapStep = toTapStep

        #: The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage 
        self.excitingCurrent = excitingCurrent

        #: The load loss kW ('to' winding short-circuited) from the test report. 
        self.loadLoss = loadLoss

        #: The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding. 
        self.leakageImpedance = leakageImpedance

        #: The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        self.voltage = voltage

        self._To_TransformerWinding = None
        self.To_TransformerWinding = To_TransformerWinding

        self._From_TransformerWinding = None
        self.From_TransformerWinding = From_TransformerWinding

        super(WindingTest, self).__init__(*args, **kw_args)

    def getTo_TransformerWinding(self):
        """The winding to which the test was conducted.  Note that although the 'from' side of the test is required, the 'to' side of a test is not always required.
        """
        return self._To_TransformerWinding

    def setTo_TransformerWinding(self, value):
        if self._To_TransformerWinding is not None:
            filtered = [x for x in self.To_TransformerWinding.To_WindingTest if x != self]
            self._To_TransformerWinding._To_WindingTest = filtered

        self._To_TransformerWinding = value
        if self._To_TransformerWinding is not None:
            self._To_TransformerWinding._To_WindingTest.append(self)

    To_TransformerWinding = property(getTo_TransformerWinding, setTo_TransformerWinding)

    def getFrom_TransformerWinding(self):
        """The winding from which the test was conducted
        """
        return self._From_TransformerWinding

    def setFrom_TransformerWinding(self, value):
        if self._From_TransformerWinding is not None:
            filtered = [x for x in self.From_TransformerWinding.From_WindingTest if x != self]
            self._From_TransformerWinding._From_WindingTest = filtered

        self._From_TransformerWinding = value
        if self._From_TransformerWinding is not None:
            self._From_TransformerWinding._From_WindingTest.append(self)

    From_TransformerWinding = property(getFrom_TransformerWinding, setFrom_TransformerWinding)
