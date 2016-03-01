"""
Calculating values by formulas.
ComputeChanges on models via InitialAssignments.
"""

from __future__ import print_function
import tellurium as te

antimonyStr = '''
model testcase_03()
  J0: S1 -> S2; k1*S1
  S1 = 10.0; S2 = 0.0;
  k1 = 0.5;
end
'''

phrasedmlStr = '''
  mod1 = model "testcase_03"
  mod2 = model mod1 with S2=S1+4
  sim1 = simulate uniform(0, 10, 100)
  task1 = run sim1 on mod1
  task2 = run sim1 on mod2
  plot "Example plot" task1.time vs task1.S1, task1.S2, task2.S1, task2.S2
'''

# phrasedml experiment
exp = te.experiment(antimonyStr, phrasedmlStr)

# python code
import os
with open(os.path.realpath(__file__) + 'code.py', 'w') as f:
    f.write(exp._toPython(phrasedmlStr))

# execute python
import os
exp.execute(phrasedmlStr, workingDir=os.getcwd())
