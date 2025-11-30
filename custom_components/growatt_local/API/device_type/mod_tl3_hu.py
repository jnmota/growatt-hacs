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
    ATTR_FAULT_CODE,
    ATTR_WARNING_CODE,
    ATTR_INPUT_POWER,
    ATTR_INPUT_ENERGY_TOTAL,
    ATTR_INPUT_1_POWER,
    ATTR_INPUT_1_VOLTAGE,
    ATTR_INPUT_1_AMPERAGE,
    ATTR_INPUT_1_ENERGY_TODAY,
    ATTR_INPUT_1_ENERGY_TOTAL,
    ATTR_INPUT_2_POWER,
    ATTR_INPUT_2_VOLTAGE,
    ATTR_INPUT_2_AMPERAGE,
    ATTR_INPUT_2_ENERGY_TODAY,
    ATTR_INPUT_2_ENERGY_TOTAL,
    ATTR_INPUT_3_POWER,
    ATTR_INPUT_3_VOLTAGE,
    ATTR_INPUT_3_AMPERAGE,
    ATTR_INPUT_3_ENERGY_TODAY,
    ATTR_INPUT_3_ENERGY_TOTAL,
    ATTR_INPUT_ENERGY_TODAY,
    ATTR_OUTPUT_POWER,
    ATTR_SYSTEM_OUTPUT_POWER,
    ATTR_OUTPUT_REACTIVE_POWER,
    ATTR_OPERATION_HOURS,
    ATTR_TEMPERATURE,
    ATTR_IPM_TEMPERATURE,
    ATTR_BOOST_TEMPERATURE,
    ATTR_OUTPUT_PERCENTAGE,
    ATTR_SOC_PERCENTAGE,
    ATTR_DISCHARGE_POWER,
    ATTR_CHARGE_POWER,
    ATTR_POWER_TO_USER,
    ATTR_POWER_TO_GRID,
    ATTR_POWER_USER_LOAD,
    ATTR_POWER_USER_LOAD_TODAY,
    ATTR_POWER_USER_LOAD_TOTAL,
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
    ATTR_BATTERY_FIRST_ENABLED,
    ATTR_BATTERY_DISCHARGE_STOP_SOC
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
    ),
    GrowattDeviceRegisters(
        name=ATTR_BATTERY_DISCHARGE_STOP_SOC,
        register=3067,
        value_type=int,
        length=1
    ),
    GrowattDeviceRegisters(
        name=ATTR_BATTERY_FIRST_ENABLED,
        register=608,
        value_type=int,
        length=1
    )
)

MOD_TL3_HU_INPUT_REGISTERS: tuple[GrowattDeviceRegisters, ...] = (
    GrowattDeviceRegisters(
        name=ATTR_STATUS_CODE, register=3000, value_type=int, length=1
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_POWER, register=3001, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_VOLTAGE, register=3003, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_AMPERAGE, register=3004, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_POWER, register=3005, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_VOLTAGE, register=3007, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_AMPERAGE, register=3008, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_POWER, register=3009, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_VOLTAGE, register=3011, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_AMPERAGE, register=3012, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_POWER, register=3013, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_SYSTEM_OUTPUT_POWER, register=3019, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_REACTIVE_POWER, register=3021, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_POWER, register=3023, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_POWER_TO_USER, register=3041, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_POWER_TO_GRID, register=3043, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_POWER_USER_LOAD, register=3045, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OPERATION_HOURS, register=3047, value_type=float, length=2, scale=7200,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_ENERGY_TOTAL, register=3053, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TODAY, register=3055, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TOTAL, register=3057, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TODAY, register=3059, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TOTAL, register=3061, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TODAY, register=3063, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TOTAL, register=3065, value_type=float, length=2
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
        name=ATTR_POWER_USER_LOAD_TODAY, register=3075, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_POWER_USER_LOAD_TOTAL, register=3077, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_ENERGY_TODAY, register=3083, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_TEMPERATURE, register=3093, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_IPM_TEMPERATURE, register=3094, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_BOOST_TEMPERATURE, register=3095, value_type=int, length=1, multiplier=0.1
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_PERCENTAGE, register=3101, value_type=int, length=1
    ),
    GrowattDeviceRegisters(
        name=ATTR_FAULT_CODE, register=3105, value_type=int, length=1
    ),
    GrowattDeviceRegisters(
        name=ATTR_WARNING_CODE, register=3106, value_type=int, length=1
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
    GrowattDeviceRegisters(
        name=ATTR_SOC_PERCENTAGE, register=3171, value_type=int, length=1
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_POWER, register=3178, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_POWER, register=3180, value_type=float, length=2
    )
)
