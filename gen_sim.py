wfs = []
wc = {}
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
class step:
    def __init__(self, module: str, run_time: int, start_time: int) -> None:
        self.module = module
        self.run_time = run_time
        self.start_time = start_time
    def __str__(self):
            return str({"module": self.module, "start_time": self.start_time})
class wf:
    def __init__(self, name: str,  run_time: int, steps) -> None:
        self.run_time = run_time
        self.name = name
        self.steps = steps
        self.completed = False
        self.step_index = 0
    def __str__(self):
        return str({"run_time": self.run_time, "name": self.name, "completed": self.completed, "steps": [str(x) for x in self.steps]})
class block: 
    def __init__(self, flow, start_time, end_time) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.flow = flow
    def __str__(self):
        return str({"start_time": self.start_time, "flow": self.flow, "end_time": self.end_time})
       

if __name__ == "__main__":
    wfs = [wf("flow_1", 0, [step("A", 40, 0), step("B", 30, 0)]), wf("flow_2", 0, [step("A", 40, 0), step("C", 30, 0)])]
    wc = {"A": [], "B": [], "C": []}
    all_complete = False
    while not(all_complete):
        all_complete = True
        for wf in wfs: 
            if not(wf.completed):
                step = wf.steps[wf.step_index]
                step.start_time = wf.run_time
                for old_block in wc[step.module]:
                    if old_block.end_time > step.start_time:
                        step.start_time = old_block.end_time
                wc[step.module].append(block(wf.name, step.start_time, step.start_time + step.run_time))
                wf.run_time = step.start_time + step.run_time
                wf.step_index += 1
                if wf.step_index == len(wf.steps):
                    wf.completed = True
                all_complete = all_complete and wf.completed

    for wf in wfs:
        print(str(wf))
    for module in wc.keys():
        print(module)
        print([str(x) for x in wc[module]])
    fig, ax = plt.subplots()
    for i, wf in enumerate(wfs):
        for step in wf.steps:
            print(step)
            print(i)
            ax.add_patch(Rectangle((i*15, step.start_time), 10, step.run_time, edgecolor=[0, 0, 0]))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    plt.show()
    
                
                
            
            