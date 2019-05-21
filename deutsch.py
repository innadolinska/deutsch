import cirq
from cirq import H, X, CNOT, measure


def oracle_method(first_param, second_param, secret_function):
    if secret_function[0]:
        yield CNOT(first_param, second_param), X(second_param)

    if secret_function[1]:
        yield CNOT(first_param, second_param)


def deutsch_dircuit_method(first_param, second_param, oracle):
    result = cirq.Circuit()
    result.append([X(second_param), H(second_param), H(first_param)])
    result.append(oracle)
    result.append([H(first_param), measure(first_param, key='result')])
    return result

if __name__ == '__main__':
    first_param, second_param = cirq.LineQubit.range(2)

    bits = [int(input("bit = ")) for _ in range(2)]
    secretFunction = []
    for bit in bits:
        if bit > 0:
            secretFunction.append(1);
        else:
            secretFunction.append(0);

    oracle = oracle_method(first_param, second_param, secretFunction)
    print('Secret function: f(x) = <{}>'.format(', '.join(str(e) for e in secretFunction)))

    circuit = deutsch_dircuit_method(first_param, second_param, oracle)
    print('Circuit method result:   ')
    print(circuit)
    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    print('Result of f(0)⊕f(1):  ')
    print(result)