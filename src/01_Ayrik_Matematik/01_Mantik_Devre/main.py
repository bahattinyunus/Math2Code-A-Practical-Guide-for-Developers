class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def perform(self):
        raise NotImplementedError

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
    def perform(self):
        a = self.pin_a.perform() if isinstance(self.pin_a, LogicGate) else self.pin_a
        b = self.pin_b.perform() if isinstance(self.pin_b, LogicGate) else self.pin_b
        return a and b

class OrGate(BinaryGate):
    def perform(self):
        a = self.pin_a.perform() if isinstance(self.pin_a, LogicGate) else self.pin_a
        b = self.pin_b.perform() if isinstance(self.pin_b, LogicGate) else self.pin_b
        return a or b

class NotGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: PIN BUSY")

    def perform(self):
        val = self.pin.perform() if isinstance(self.pin, LogicGate) else self.pin
        return 0 if val == 1 else 1

class Wrapper(LogicGate):
    """Wraps a raw value (0 or 1) into a performable object."""
    def __init__(self, value):
        super().__init__("Val")
        self.value = value
    
    def perform(self):
        return self.value

if __name__ == "__main__":
    print("--- Mantık Devresi Simülatörü ---")
    
    # Devre: NOT (A AND B) -> NAND Gate
    g1 = AndGate("G1")
    g2 = NotGate("G2")
    
    # Inputs
    val_a = Wrapper(1)
    val_b = Wrapper(1)
    
    g1.set_next_pin(val_a)
    g1.set_next_pin(val_b)
    
    g2.set_next_pin(g1)
    
    print(f"Inputs: A=1, B=1")
    print(f"Gate 1 (AND) Output: {g1.perform()}")
    print(f"Gate 2 (NOT) Output: {g2.perform()}")
