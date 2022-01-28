import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..")))

import fmteach.whlang.parser 
import fmteach.whlang.typechecker

import tests.whlang.typechecker.parseable

import pytest

@pytest.mark.parametrize("filepath", list(tests.whlang.typechecker.parseable.getFiles ()))
def test_parser_parseablee (filepath):
    with open (filepath,'r') as  ff:
        parser = fmteach.whlang.parser.Parser ()
        typechecker = fmteach.whlang.typechecker.Typechecker  ()
        obj = parser.ParseString (ff.read())
        assert(typechecker.Check (obj) )

