set(PYSOURCE

  __init__.py
  analysis/test_ab01.py
  analysis/test_ab04md.py
  analysis/test_ab08n.py
  analysis/test_ag08bd.py
  analysis/test_ab13bd.py
  analysis/test_ab13md.py
  analysis/test_ab08bd.py
  analysis/test_analysis.py)

install(FILES ${PYSOURCE}
        DESTINATION slycot/tests/analysis)