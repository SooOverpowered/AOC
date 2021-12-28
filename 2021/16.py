conversions = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
               '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


def sum_version(packet):
    version = int(packet[0:3], 2)
    typeID = int(packet[3:6], 2)
    if typeID == 4:
        curr = 6
        output = ''
        while packet[curr] == '1':
            output += packet[curr+1:curr+5]
            curr += 5
        output += packet[curr+1:curr+5]
        length = 6+len(output)//4*5
        return (version, length)
    else:
        length_type_id = int(packet[6])
        if length_type_id == 0:
            bit_length = int(packet[7:22], 2)
            sub_packets_data = packet[22:22+bit_length]
            length = 22+bit_length
            output = version
            while len(sub_packets_data) != 0:
                temp = sum_version(sub_packets_data)
                output += temp[0]
                sub_packets_data = sub_packets_data[temp[1]:]
            return (output, length)
        elif length_type_id == 1:
            sub_packet_count = int(packet[7:18], 2)
            sub_packets_data = packet[18:]
            sub_packets_length = 0
            output = version
            while sub_packet_count > 0:
                temp = sum_version(sub_packets_data)
                output += temp[0]
                sub_packets_length += temp[1]
                sub_packets_data = sub_packets_data[temp[1]:]
                sub_packet_count -= 1
            return (output, 18+sub_packets_length)


def packet_result(packet):
    version = int(packet[0:3], 2)
    typeID = int(packet[3:6], 2)
    if typeID == 4:
        curr = 6
        output = ''
        while packet[curr] == '1':
            output += packet[curr+1:curr+5]
            curr += 5
        output += packet[curr+1:curr+5]
        length = 6+len(output)//4*5
        return (int(output, 2), length)
    else:
        length_type_id = int(packet[6])
        if length_type_id == 0:
            return parse_lenID_0(packet, typeID)
        elif length_type_id == 1:
            return parse_lenID_1(packet, typeID)


def parse_lenID_0(packet, typeID):
    bit_length = int(packet[7:22], 2)
    sub_packets_data = packet[22:22+bit_length]
    length = 22+bit_length
    outputs = []
    while len(sub_packets_data) != 0:
        temp = packet_result(sub_packets_data)
        outputs.append(temp[0])
        sub_packets_data = sub_packets_data[temp[1]:]
    if typeID == 0:
        return (sum(outputs), length)
    elif typeID == 1:
        temp = 1
        for res in outputs:
            temp *= res
        return (temp, length)
    elif typeID == 2:
        return (min(outputs), length)
    elif typeID == 3:
        return (max(outputs), length)
    elif typeID == 5:
        if outputs[0] > outputs[1]:
            return (1, length)
        else:
            return (0, length)
    elif typeID == 6:
        if outputs[0] < outputs[1]:
            return (1, length)
        else:
            return (0, length)
    elif typeID == 7:
        if outputs[0] == outputs[1]:
            return (1, length)
        else:
            return (0, length)


def parse_lenID_1(packet, typeID):
    sub_packet_count = int(packet[7:18], 2)
    sub_packets_data = packet[18:]
    sub_packets_length = 0
    outputs = []
    while sub_packet_count > 0:
        temp = packet_result(sub_packets_data)
        outputs.append(temp[0])
        sub_packets_length += temp[1]
        sub_packets_data = sub_packets_data[temp[1]:]
        sub_packet_count -= 1
    length = 18+ sub_packets_length
    if typeID == 0:
        return (sum(outputs), length)
    elif typeID == 1:
        temp = 1
        for res in outputs:
            temp *= res
        return (temp, length)
    elif typeID == 2:
        return (min(outputs), length)
    elif typeID == 3:
        return (max(outputs), length)
    elif typeID == 5:
        if outputs[0] > outputs[1]:
            return (1, length)
        else:
            return (0, length)
    elif typeID == 6:
        if outputs[0] < outputs[1]:
            return (1, length)
        else:
            return (0, length)
    elif typeID == 7:
        if outputs[0] == outputs[1]:
            return (1, length)
        else:
            return (0, length)


def part1(data):
    binarydata = ''
    for hex in data:
        binarydata += conversions[hex]
    return sum_version(binarydata)[0]


def part2(data):
    binarydata = ''
    for hex in data:
        binarydata += conversions[hex]
    return packet_result(binarydata)[0]


if __name__ == '__main__':
    import runner
    runner.run(day=16)
