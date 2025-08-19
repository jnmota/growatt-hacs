"""Device defaults for a Growatt Inverter."""

from .base import (
    GrowattDeviceRegisters,
    custom_function,
    FIRMWARE_REGISTER,
    SERIAL_NUMBER_REGISTER,
    DEVICE_TYPE_CODE_REGISTER,
    NUMBER_OF_TRACKERS_AND_PHASES_REGISTER,
    ATTR_INVERTER_ENABLED,
    ATTR_INVERTER_MODEL,
    ATTR_MODBUS_VERSION,
    ATTR_STATUS_CODE,
    ATTR_DERATING_MODE,
    ATTR_FAULT_CODE,
    ATTR_WARNING_CODE,
    ATTR_INPUT_POWER,
    ATTR_INPUT_ENERGY_TOTAL,
    ATTR_INPUT_1_VOLTAGE,
    ATTR_INPUT_1_AMPERAGE,
    ATTR_INPUT_1_POWER,
    ATTR_INPUT_1_ENERGY_TODAY,
    ATTR_INPUT_1_ENERGY_TOTAL,
    ATTR_INPUT_2_VOLTAGE,
    ATTR_INPUT_2_AMPERAGE,
    ATTR_INPUT_2_POWER,
    ATTR_INPUT_2_ENERGY_TODAY,
    ATTR_INPUT_2_ENERGY_TOTAL,
    ATTR_INPUT_3_VOLTAGE,
    ATTR_INPUT_3_AMPERAGE,
    ATTR_INPUT_3_POWER,
    ATTR_INPUT_3_ENERGY_TODAY,
    ATTR_INPUT_3_ENERGY_TOTAL,
    ATTR_OUTPUT_POWER,
    ATTR_OUTPUT_ENERGY_TODAY,
    ATTR_OUTPUT_ENERGY_TOTAL,
    ATTR_OUTPUT_REACTIVE_POWER,
    ATTR_OUTPUT_REACTIVE_ENERGY_TODAY,
    ATTR_OUTPUT_REACTIVE_ENERGY_TOTAL,
    ATTR_OUTPUT_1_VOLTAGE,
    ATTR_OUTPUT_1_AMPERAGE,
    ATTR_OUTPUT_1_POWER,
    ATTR_OUTPUT_2_VOLTAGE,
    ATTR_OUTPUT_2_AMPERAGE,
    ATTR_OUTPUT_2_POWER,
    ATTR_OUTPUT_3_VOLTAGE,
    ATTR_OUTPUT_3_AMPERAGE,
    ATTR_OUTPUT_3_POWER,
    ATTR_OPERATION_HOURS,
    ATTR_GRID_FREQUENCY,
    ATTR_TEMPERATURE,
    ATTR_IPM_TEMPERATURE,
    ATTR_BOOST_TEMPERATURE,
    ATTR_P_BUS_VOLTAGE,
    ATTR_N_BUS_VOLTAGE,
    ATTR_OUTPUT_PERCENTAGE,
    ATTR_SOC_PERCENTAGE,
    ATTR_DISCHARGE_POWER,
    ATTR_CHARGE_POWER,
    ATTR_POWER_TO_USER,
    ATTR_POWER_TO_GRID,
    ATTR_POWER_USER_LOAD,
    ATTR_ENERGY_TO_USER_TODAY,
    ATTR_ENERGY_TO_USER_TOTAL,
    ATTR_ENERGY_TO_GRID_TODAY,
    ATTR_ENERGY_TO_GRID_TOTAL,
    ATTR_DISCHARGE_ENERGY_TODAY,
    ATTR_DISCHARGE_ENERGY_TOTAL,
    ATTR_CHARGE_ENERGY_TODAY,
    ATTR_CHARGE_ENERGY_TOTAL,
    ATTR_AC_CHARGE_ENABLED,
    ATTR_SERIAL_NUMBER,
    ATTR_PAC_TO_GRID_TOTAL,
    ATTR_PAC_TO_USER_TOTAL,
)




MAXIMUM_DATA_LENGTH_120 = 100


def model(registers) -> str:
    mo = (registers[0] << 16) + registers[1]
    return "A{:X} B{:X} D{:X} T{:X} P{:X} U{:X} M{:X} S{:X}".format(
        (mo & 0xF0000000) >> 28,
        (mo & 0x0F000000) >> 24,
        (mo & 0x00F00000) >> 20,
        (mo & 0x000F0000) >> 16,
        (mo & 0x0000F000) >> 12,
        (mo & 0x00000F00) >> 8,
        (mo & 0x000000F0) >> 4,
        (mo & 0x0000000F)
    )


MOD_TL3_HU_HOLDING_REGISTERS: tuple[GrowattDeviceRegisters, ...] = (
    GrowattDeviceRegisters(
        name=ATTR_INVERTER_ENABLED,
        register=0,
        value_type=int
    ),
    FIRMWARE_REGISTER,
    SERIAL_NUMBER_REGISTER,
    GrowattDeviceRegisters(
        name=ATTR_INVERTER_MODEL,
        register=28,
        value_type=custom_function,
        length=2,
        function=model
    ),
    GrowattDeviceRegisters(
        name=ATTR_SERIAL_NUMBER,
        register=3001,
        value_type=str,
        length=15
    ),
    DEVICE_TYPE_CODE_REGISTER,
    NUMBER_OF_TRACKERS_AND_PHASES_REGISTER,
    GrowattDeviceRegisters(
        name=ATTR_MODBUS_VERSION,
        register=88,
        value_type=float,
        scale=100
    ),
    GrowattDeviceRegisters(
        name=ATTR_AC_CHARGE_ENABLED,
        register=3049,
        value_type=int,
        length=1
    )
)

MOD_TL3_HU_INPUT_REGISTERS: tuple[GrowattDeviceRegisters, ...] = (
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_REACTIVE_POWER, register=234, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_REACTIVE_ENERGY_TOTAL, register=236, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_STATUS_CODE, register=3000, value_type=int
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_POWER, register=3001, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_VOLTAGE, register=3003, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_AMPERAGE, register=3004, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_POWER, register=3005, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_VOLTAGE, register=3007, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_AMPERAGE, register=3008, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_POWER, register=3009, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_VOLTAGE, register=30011, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_AMPERAGE, register=30012, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_POWER, register=30013, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_POWER, register=35, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_GRID_FREQUENCY, register=37, value_type=float, scale=100
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_VOLTAGE, register=38, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_AMPERAGE, register=39, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_POWER, register=40, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_VOLTAGE, register=42, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_AMPERAGE, register=43, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_POWER, register=44, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_VOLTAGE, register=46, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_AMPERAGE, register=47, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_POWER, register=48, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OPERATION_HOURS, register=30047, value_type=float, length=2, scale=7200,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_ENERGY_TODAY, register=30049, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_ENERGY_TOTAL, register=30051, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_ENERGY_TOTAL, register=30053, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TODAY, register=30055, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TOTAL, register=30057, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TODAY, register=30059, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TOTAL, register=30061, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TODAY, register=30063, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TOTAL, register=30065, value_type=float, length=2
    ),
    GrowattDeviceRegisters(name=ATTR_DERATING_MODE, register=3086, value_type=int),
    GrowattDeviceRegisters(name=ATTR_TEMPERATURE, register=93, value_type=float),
    GrowattDeviceRegisters(name=ATTR_IPM_TEMPERATURE, register=94, value_type=float),
    GrowattDeviceRegisters(name=ATTR_BOOST_TEMPERATURE, register=95, value_type=float),
    GrowattDeviceRegisters(name=ATTR_P_BUS_VOLTAGE, register=30098, value_type=float),
    GrowattDeviceRegisters(name=ATTR_N_BUS_VOLTAGE, register=30099, value_type=float),
    GrowattDeviceRegisters(name=ATTR_OUTPUT_PERCENTAGE, register=3101, value_type=int),

    GrowattDeviceRegisters(name=ATTR_FAULT_CODE, register=3105, value_type=int),
    GrowattDeviceRegisters(
        name=ATTR_PAC_TO_USER_TOTAL, register=1021, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_PAC_TO_GRID_TOTAL, register=1029, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_WARNING_CODE, register=3110, value_type=int, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_SOC_PERCENTAGE, register=3171, value_type=int
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_POWER, register=3178, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_POWER, register=3180, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_POWER_TO_USER, register=1015, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_POWER_TO_GRID, register=1023, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_POWER_USER_LOAD, register=1031, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_USER_TODAY, register=3067, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_USER_TOTAL, register=3069, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_GRID_TODAY, register=3071, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_GRID_TOTAL, register=3073, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_ENERGY_TODAY, register=3125, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_ENERGY_TOTAL, register=3127, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_ENERGY_TODAY, register=3129, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_ENERGY_TOTAL, register=3131, value_type=float, length=2
    ),
)
