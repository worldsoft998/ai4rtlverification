import hpi
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

@hpi.bfm
class alu_bfm:
    def __init__(self):
        # Build and train ANN: Input=10D state vector (e.g., coverage hints), Output= [a, b, op] scaled
        self.model = MLPRegressor(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=200, random_state=42)
        self.scaler = StandardScaler()
        
        # Synthetic training data: 1000 samples of "good" stimuli (biased to edges for optimization)
        # Input: Random state vectors
        X = np.random.uniform(-1, 1, (1000, 10))
        # Output: Biased random a/b (-128 to 127), op (0-7); e.g., favor extremes
        a_train = np.random.choice([-128, -1, 0, 1, 127], 1000, p=[0.2, 0.15, 0.2, 0.15, 0.3])
        b_train = np.random.choice([-128, -1, 0, 1, 127], 1000, p=[0.2, 0.15, 0.2, 0.15, 0.3])
        op_train = np.random.randint(0, 8, 1000)
        y = np.column_stack([a_train, b_train, op_train])
        
        # Scale and train
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
    
    @hpi.export_task()  # Export to SV: SV calls this Python method; types inferred as outputs (int, int, byte)
    def get_stimulus(self, a, b, op):
        # Generate state vector (in real use: from SV coverage data)
        state = np.random.uniform(-1, 1, (1, 10))
        state_scaled = self.scaler.transform(state)
        pred = self.model.predict(state_scaled)[0]
        
        # Scale predictions to ALU ranges; assign to outputs (py-hpi handles .value for mutability)
        a.value = int(np.clip(pred[0], -128, 127))
        b.value = int(np.clip(pred[1], -128, 127))
        op.value = int(np.clip(pred[2], 0, 7))
        
        print(f"ANN generated stimulus: a={a.value}, b={b.value}, op={op.value}")

# Optional entry point (if running Python-driven test; not needed for UVM calls)
@hpi.entry
def run_example():
    bfm = hpi.rgy.get_bfm('alu_bfm')  # Get registered BFM instance
    a, b, op = [None] * 3  # Dummy for demo
    for _ in range(5):
        bfm.get_stimulus(a, b, op)