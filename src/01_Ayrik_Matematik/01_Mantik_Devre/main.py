from abc import ABC, abstractmethod
from typing import Optional, Union

class LogicGate(ABC):
    """
    Abstract Base Class representing a generic Logic Gate.
    Acts as the fundamental atom of our digital logic universe.
    """
    def __init__(self, label: str):
        self.label = label
        self.output: Optional[int] = None

    @abstractmethod
    def perform(self) -> int:
        """Performs the logic operation and returns the result (0 or 1)."""
        pass

class BinaryGate(LogicGate):
    """
    Represents a logic gate with two input pins (A and B).
    Examples: AND, OR, XOR.
    """
    def __init__(self, label: str):
        super().__init__(label)
        self.pin_a: Union['LogicGate', int, None] = None
        self.pin_b: Union['LogicGate', int, None] = None

    def set_next_pin(self, source: Union['LogicGate', int]):
        """Connects a source to the first available pin."""
        if self.pin_a is None:
            self.pin_a = source
        elif self.pin_b is None:
            self.pin_b = source
        else:
            raise RuntimeError(f"Error: NO EMPTY PINS on Gate {self.label}")

class AndGate(BinaryGate):
    """
    Implements the AND logic operation.
    Output is 1 only if both inputs are 1.
    """
    def perform(self) -> int:
        val_a = self.pin_a.perform() if isinstance(self.pin_a, LogicGate) else self.pin_a
        val_b = self.pin_b.perform() if isinstance(self.pin_b, LogicGate) else self.pin_b
        return 1 if val_a == 1 and val_b == 1 else 0

class OrGate(BinaryGate):
    """
    Implements the OR logic operation.
    Output is 1 if at least one input is 1.
    """
    def perform(self) -> int:
        val_a = self.pin_a.perform() if isinstance(self.pin_a, LogicGate) else self.pin_a
        val_b = self.pin_b.perform() if isinstance(self.pin_b, LogicGate) else self.pin_b
        return 1 if val_a == 1 or val_b == 1 else 0

class NotGate(LogicGate):
    """
    Implements the NOT logic operation (Inverter).
    Output is the inverse of the input.
    """
    def __init__(self, label: str):
        super().__init__(label)
        self.pin: Union['LogicGate', int, None] = None

    def set_next_pin(self, source: Union['LogicGate', int]):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError(f"Error: PIN BUSY on Gate {self.label}")

    def perform(self) -> int:
        val = self.pin.perform() if isinstance(self.pin, LogicGate) else self.pin
        return 0 if val == 1 else 1

class Wrapper(LogicGate):
    """
    Wraps a raw value (0 or 1) into a performable LogicGate object.
    Used to feed static inputs into the circuit.
    """
    def __init__(self, value: int):
        super().__init__("Val")
        self.value = value
    
    def perform(self) -> int:
        return self.value

if __name__ == "__main__":
    print("--- 🏛️ Mantık Devresi Simülatörü (Logic Circuit Simulator) ---")
    
    # Circuit: NOT (A AND B) -> NAND Logic
    g1 = AndGate("G1")
    g2 = NotGate("G2")
    
    # Inputs: A=1, B=1
    val_a = Wrapper(1)
    val_b = Wrapper(1)
    
    print(f"🔌 Connecting inputs A=1, B=1 to AND Gate...")
    g1.set_next_pin(val_a)
    g1.set_next_pin(val_b)
    
    print(f"🔌 Connecting AND Gate output to NOT Gate...")
    g2.set_next_pin(g1)
    
    result = g2.perform()
    print(f"✨ Final Output (NAND): {result}")
