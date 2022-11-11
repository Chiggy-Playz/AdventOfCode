# https://adventofcode.com/2015/day/7

from typing import Dict, Union, Optional
from enum import Enum
from pprint import pprint

with open("Inputs/day7.txt") as f:
    instructions = f.readlines()

limit = 2 ** 16 - 1

values: Dict[str, int] = {}

class Operation(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"
    NOTHING = "NOTHING"


class Operand:
    def __init__(self, value: Union[str, int]) -> None:
        try:
            self._value = int(value)
        except ValueError:
            self._value = value

    def value(self) -> int:
        if isinstance(self._value, int):
            return self._value
        if self._value in values:
            return values[self._value]
        
        value = wires[self._value].compute_value()
        values[self._value] = value
        return value

    def __repr__(self) -> str:
        return str(self._value)

class Instruction:
    def __init__(
        self,
        operand_a: Operand,
        operand_b: Optional[Operand] = None,
        operation: Operation = Operation.NOTHING,
    ) -> None:
        self.operand_a = operand_a
        self.operand_b = operand_b
        self.operation = operation

    def __repr__(self) -> str:
        if self.operation == Operation.NOTHING:
            return f"{self.operand_a}"
        elif self.operation == Operation.NOT:
            return f"NOT {self.operand_a}"
        return f"{self.operand_a} {self.operation.name} {self.operand_b}"

    def compute_value(self) -> int:

        if self.operation == Operation.NOTHING:
            return self.operand_a.value()
        elif self.operation == Operation.NOT:
            return limit - self.operand_a.value()
        elif self.operation == Operation.AND:
            assert self.operand_b
            return self.operand_a.value() & self.operand_b.value()
        elif self.operation == Operation.OR:
            assert self.operand_b
            return self.operand_a.value() | self.operand_b.value()
        elif self.operation == Operation.LSHIFT:
            assert self.operand_b
            return self.operand_a.value() << self.operand_b.value()
        else:  # RSHIFT
            assert self.operand_b
            return self.operand_a.value() >> self.operand_b.value()



wires: Dict[str, Instruction] = {}

def parse_instructions():
    for instruction in instructions:
        # If the instruction has 2 operands
        if ("NOT" not in instruction) and (not instruction.islower()):
            # instruction is: a OP b -> out
            operand_1, operation, operand_2, _, output = instruction.split(" ")
            operand_1 = Operand(operand_1)

            operand_2 = Operand(operand_2)

            operation = getattr(Operation, operation)
            wires[output.strip()] = Instruction(operand_1, operand_2, operation)
        elif "NOT" in instruction:
            # instruction is: NOT a -> out
            _, operand, _, output = instruction.split()
            operation = Operation.NOT
            operand = Operand(operand)

            wires[output.strip()] = Instruction(operand, None, operation)
        else:
            # instruction is: a -> out
            operand, _, output = instruction.split(" ")
            operand = Operand(operand)

            wires[output.strip()] = Instruction(operand)

parse_instructions()

wire = "a"
wire_value = wires[wire].compute_value()
pprint(wire_value)

# Part 2

values.clear()
values['b'] = wire_value

parse_instructions()

print(wires[wire].compute_value())