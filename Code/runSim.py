from Simulator.Sim import LC3_Simulator

if __name__ == "__main__":
    machine_state = LC3_Simulator.create_simulation(r"C:\lc3_assembly_work\similaritytest.obj2")
    print(machine_state)