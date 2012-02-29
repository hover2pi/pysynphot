"""Custom exceptions for pysynphot to raise"""


class PysynphotError(Exception):
    """parent class"""
    def __init__(self,msg):
        Exception.__init__(self,msg)

# Exceptions to do with table access
class TableFormatError(PysynphotError):
    def __init__(self, msg, rows=None):
        PysynphotError.__init__(self, msg)

        # Save rows with wrong values as an attribute so calling code
        # can access it directly
        self.rows = rows

        # Also make this info go into the visibly displayed message in
        # Python 2.7 (self.args) and Python 2.5/6 (self.message)
        args = list(self.args)
        args.append("Invalid entries at or about row: "+str(rows))

        self.args = tuple(args)
        self.message = self.args
        
class DuplicateWavelength(TableFormatError):
    pass

class ZeroWavelength(TableFormatError):
    pass


class UnsortedWavelength(TableFormatError):
    pass

class BadRow(TableFormatError):
    pass


# Exceptions to do with overlap checking
class OverlapError(PysynphotError):
    pass

class PartialOverlap(OverlapError):
    pass

class DisjointError(OverlapError):
    pass

# Exceptions to do with graph table traversal
class GraphtabError(PysynphotError):
    pass

class UnusedKeyword(GraphtabError):
    pass

class IncompleteObsmode(GraphtabError):
    pass

class AmbiguousObsmode(GraphtabError):
    pass


# Exceptions for undefined optional values
class UndefinedBinset(PysynphotError):
    pass
    
    
# Exceptions for interpolation/extrapolation
class ExtrapolationNotAllowed(PysynphotError):
    pass
    
    
# Exceptions for catalog problems
class ParameterOutOfBounds(PysynphotError):
    pass


# if two sources in Composite* spectrum shouldn't go together
class IncompatibleSources(PysynphotError):
    pass
