from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        idx, hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        System._hardware[idx].install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        idx, hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        System._hardware[idx].install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_idx, hardware = System.find_hardware_by_name(hardware_name)
        software_idx, software = System.find_software_by_name(software_name)
        if not hardware or not software:
            return "Some of the components do not exist"
        System._hardware[hardware_idx].uninstall(software)
        System._software.pop(software_idx)

    @staticmethod
    def analyze():
        result = 'System Analysis\n'
        result += f'Hardware Components: {len(System._hardware)}\n'
        result += f'Software Components: {len(System._software)}\n'
        total_software_memory = sum([s.memory_consumption for s in System._software])
        total_hardware_memory = sum([h.memory for h in System._hardware])
        result += f'Total Operational Memory: {total_software_memory} / {total_hardware_memory}\n'
        total_software_capacity = sum([s.capacity_consumption for s in System._software])
        total_hardware_capacity = sum([h.capacity for h in System._hardware])
        result += f'Total Capacity Taken: {total_software_capacity} / {total_hardware_capacity}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            total_express_software = len([s for s in hardware.software_components if s.software_type == 'Express'])
            total_light_software = len([s for s in hardware.software_components if s.software_type == 'Light'])
            memory_usage = sum([s.memory_consumption for s in hardware.software_components])
            capacity_usage = sum([s.capacity_consumption for s in hardware.software_components])
            software_components_names = [s.name for s in hardware.software_components]
            result += f'Hardware Component - {hardware.name}\n'
            result += f'Express Software Components: {total_express_software}\n'
            result += f'Light Software Components: {total_light_software}\n'
            result += f'Memory Usage: {memory_usage} / {hardware.memory}\n'
            result += f'Capacity Usage: {capacity_usage} / {hardware.capacity}\n'
            result += f'Type: {hardware.hardware_type}\n'
            if not software_components_names:
                result += 'Software Components: None\n'
            else:
                result += f'Software Components: {", ".join(software_components_names)}\n'
        return result

    @staticmethod
    def find_hardware_by_name(hardware_name):
        for idx in range(len(System._hardware)):
            hardware = System._hardware[idx]
            if hardware.name == hardware_name:
                return idx, hardware
        return 0, None

    @staticmethod
    def find_software_by_name(software_name):
        for idx in range(len(System._software)):
            software = System._software[idx]
            if software.name == software_name:
                return idx, software
        return 0, None
