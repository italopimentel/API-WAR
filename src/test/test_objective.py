from objective import Objective

def objective():
    return Objective("Destruir totalmente OS EXÉRCITOS PRETOS.")

def test_initial_values():
    obj = objective()  
    assert obj.get_objective() == "Destruir totalmente OS EXÉRCITOS PRETOS."
