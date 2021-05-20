# constants.py/Open GoPro, Version 1.0 (C) Copyright 2021 GoPro, Inc. (http://gopro.com/OpenGoPro).
# This copyright was auto-generated on Thu, May  6, 2021 11:38:31 AM

"""Constant numbers shared across the GoPro module."""

import enum
from typing import Union, Tuple

import construct

GOPRO_BASE_UUID = "b5f9{}-aa8d-11e3-9046-0002a5d5c51b"


class ErrorCode(enum.Enum):
    """Status Codes."""

    SUCCESS = 0
    ERROR = 1
    INVALID_PARAM = 2


class UUID(enum.Enum):
    """BLE UUID."""

    # Generic Attribute Service
    S_GENERIC_ATT = "00001801-0000-1000-8000-00805f9b34fb"

    # Generic Access Service
    S_GENERIC_ACCESS = "00001800-0000-1000-8000-00805f9b34fb"
    ACC_DEVICE_NAME = "00002a00-0000-1000-8000-00805f9b34fb"
    ACC_APPEARANCE = "00002a01-0000-1000-8000-00805f9b34fb"
    ACC_PREF_CONN_PARAMS = "00002a04-0000-1000-8000-00805f9b34fb"
    ACC_CENTRAL_ADDR_RES = "00002aa6-0000-1000-8000-00805f9b34fb"

    # Tx Power
    S_TX_POWER = "00001804-0000-1000-8000-00805f9b34fb"
    TX_POWER_LEVEL = "00002a07-0000-1000-8000-00805f9b34fb"

    # Battery Service
    S_BATTERY = "0000180f-0000-1000-8000-00805f9b34fb"
    BATT_LEVEL = "00002a19-0000-1000-8000-00805f9b34fb"

    # Device Information Service
    S_DEV_INFO = "0000180a-0000-1000-8000-00805f9b34fb"
    INF_MAN_NAME = "00002a29-0000-1000-8000-00805f9b34fb"
    INF_MODEL_NUM = "00002a24-0000-1000-8000-00805f9b34fb"
    INF_SERIAL_NUM = "00002a25-0000-1000-8000-00805f9b34fb"
    INF_FW_REV = "00002a26-0000-1000-8000-00805f9b34fb"
    INF_HW_REV = "00002a27-0000-1000-8000-00805f9b34fb"
    INF_SW_REV = "00002a28-0000-1000-8000-00805f9b34fb"
    INF_SYS_ID = "00002a23-0000-1000-8000-00805f9b34fb"
    INF_CERT_DATA = "00002a2a-0000-1000-8000-00805f9b34fb"
    INF_PNP_ID = "00002a50-0000-1000-8000-00805f9b34fb"

    # GoPro Wifi Access Point Service
    S_WIFI_ACCESS_POINT = GOPRO_BASE_UUID.format("0001")
    WAP_SSID = GOPRO_BASE_UUID.format("0002")
    WAP_PASSWORD = GOPRO_BASE_UUID.format("0003")
    WAP_POWER = GOPRO_BASE_UUID.format("0004")
    WAP_STATE = GOPRO_BASE_UUID.format("0005")
    WAP_CSI_PASSWORD = GOPRO_BASE_UUID.format("0006")

    # GoPro Control & Query Service
    S_CONTROL_QUERY = "0000fea6-0000-1000-8000-00805f9b34fb"
    CQ_COMMAND = GOPRO_BASE_UUID.format("0072")
    CQ_COMMAND_RESP = GOPRO_BASE_UUID.format("0073")
    CQ_SETTINGS = GOPRO_BASE_UUID.format("0074")
    CQ_SETTINGS_RESP = GOPRO_BASE_UUID.format("0075")
    CQ_QUERY = GOPRO_BASE_UUID.format("0076")
    CQ_QUERY_RESP = GOPRO_BASE_UUID.format("0077")
    CQ_SENSOR = GOPRO_BASE_UUID.format("0078")
    CQ_SENSOR_RESP = GOPRO_BASE_UUID.format("0079")

    # GoPro Camera Management Service
    S_CAMERA_MANAGEMENT = GOPRO_BASE_UUID.format("0090")
    CM_NET_MGMT_COMM = GOPRO_BASE_UUID.format("0091")
    CN_NET_MGMT_RESP = GOPRO_BASE_UUID.format("0092")

    # Unknown
    S_UNKNOWN = GOPRO_BASE_UUID.format("0080")
    INTERNAL_81 = GOPRO_BASE_UUID.format("0081")
    INTERNAL_82 = GOPRO_BASE_UUID.format("0082")
    INTERNAL_83 = GOPRO_BASE_UUID.format("0083")
    INTERNAL_84 = GOPRO_BASE_UUID.format("0084")


class CmdId(enum.Enum):
    """Command ID's that are written to UUID.CQ_COMMAND."""

    SET_SHUTTER = 0x01
    SET_PAIRING_COMPLETE = 0x03
    GET_CAMERA_STATUS = 0x13
    SET_WIFI = 0x17
    GET_SETTINGS_JSON = 0x3B
    GET_HW_INFO = 0x3C
    LOAD_PRESET = 0x40
    SET_THIRD_PARTY_CLIENT_INFO = 0x50
    GET_THIRD_PARTY_API_VERSION = 0x51
    SET_TURBO_MODE = 0xF1
    GET_PRESET_STATUS = 0xF5


class ActionId(enum.Enum):
    """Action ID's that identify a protobuf command."""

    SET_TURBO_MODE = 0x6B
    GET_PRESET_STATUS = 0x02


class SettingId(enum.Enum):
    """Setting ID's that identify settings and are written to UUID.CQ_SETTINGS."""

    RESOLUTION = 2
    FPS = 3
    INTERNAL_5 = 5
    INTERNAL_6 = 6
    INTERNAL_13 = 13
    INTERNAL_19 = 19
    INTERNAL_24 = 24
    INTERNAL_30 = 30
    INTERNAL_31 = 31
    INTERNAL_32 = 32
    INTERNAL_37 = 37
    INTERNAL_41 = 41
    INTERNAL_42 = 42
    INTERNAL_43 = 43
    INTERNAL_44 = 44
    INTERNAL_45 = 45
    INTERNAL_47 = 47
    INTERNAL_48 = 48
    INTERNAL_54 = 54
    INTERNAL_59 = 59
    INTERNAL_60 = 60
    INTERNAL_61 = 61
    INTERNAL_62 = 62
    INTERNAL_64 = 64
    INTERNAL_65 = 65
    INTERNAL_66 = 66
    INTERNAL_67 = 67
    INTERNAL_75 = 75
    INTERNAL_76 = 76
    INTERNAL_79 = 79
    INTERNAL_83 = 83
    INTERNAL_84 = 84
    INTERNAL_85 = 85
    INTERNAL_86 = 86
    INTERNAL_87 = 87
    INTERNAL_88 = 88
    LED = 91
    INTERNAL_96 = 96
    INTERNAL_102 = 102
    INTERNAL_103 = 103
    INTERNAL_104 = 104
    INTERNAL_105 = 105
    INTERNAL_106 = 106
    INTERNAL_111 = 111
    INTERNAL_112 = 112
    INTERNAL_114 = 114
    INTERNAL_115 = 115
    INTERNAL_116 = 116
    INTERNAL_117 = 117
    INTERNAL_118 = 118
    VIDEO_FOV = 121
    PHOTO_FOV = 122
    MULTI_SHOT_FOV = 123
    INTERNAL_124 = 124
    INTERNAL_125 = 125
    INTERNAL_126 = 126
    INTERNAL_128 = 128
    SHORTCUT_LOWER_LEFT = 129
    SHORTCUT_LOWER_RIGHT = 130
    SHORTCUT_UPPER_LEFT = 131
    SHORTCUT_UPPER_RIGHT = 132
    INTERNAL_133 = 133
    INTERNAL_134 = 134
    INTERNAL_135 = 135
    INTERNAL_139 = 139
    FLATMODE = 144
    INTERNAL_145 = 145
    INTERNAL_146 = 146
    INTERNAL_147 = 147
    INTERNAL_148 = 148
    INTERNAL_149 = 149
    INTERNAL_153 = 153
    INTERNAL_154 = 154
    INTERNAL_155 = 155
    INTERNAL_156 = 156
    INTERNAL_157 = 157
    INTERNAL_158 = 158
    INTERNAL_159 = 159
    INTERNAL_160 = 160
    INTERNAL_161 = 161
    MAX_LENS_MOD = 162
    INTERNAL_163 = 163
    INTERNAL_164 = 164
    INTERNAL_165 = 165
    INTERNAL_166 = 166
    INTERNAL_167 = 167
    INTERNAL_168 = 168
    INTERNAL_169 = 169
    INVALID_FOR_TESTING = 0xFF


class QueryCmdId(enum.Enum):
    """Command ID that is written to UUID.CQ_QUERY."""

    GET_SETTING_VAL = 0x12
    GET_STATUS_VAL = 0x13
    GET_SETTING_NAME = 0x22
    GET_CAPABILITIES_VAL = 0x32
    GET_CAPABILITIES_NAME = 0x42
    REG_SETTING_VAL_UPDATE = 0x52
    REG_STATUS_VAL_UPDATE = 0x53
    REG_CAPABILITIES_UPDATE = 0x62
    UNREG_SETTING_VAL_UPDATE = 0x72
    UNREG_STATUS_VAL_UPDATE = 0x73
    UNREG_CAPABILITIES_UPDATE = 0x82
    SETTING_VAL_PUSH = 0x92
    STATUS_VAL_PUSH = 0x93
    SETTING_CAPABILITY_PUSH = 0xA2
    INVALID_FOR_TESTING = 0xFF


class StatusId(enum.Enum):
    """Status ID to identify statuses sent to UUID.CQ_QUERY or received from UUID.CQ_QUERY_RESP."""

    BATT_PRESENT = 1
    BATT_LEVEL = 2
    EXT_BATT_PRESENT = 3
    EXT_BATT_LEVEL = 4
    SYSTEM_HOT = 6
    SYSTEM_BUSY = 8
    QUICK_CAPTURE = 9
    ENCODING = 10
    LCD_LOCK_ACTIVE = 11
    VIDEO_PROGRESS = 13
    INTERNAL_14 = 14
    WIRELESS_ENABLED = 17
    PAIR_STATE = 19
    PAIR_TYPE = 20
    PAIR_TIME = 21
    WAP_SCAN_STATE = 22
    WAP_SCAN_TIME = 23
    WAP_PROV_STAT = 24
    REMOTE_CTRL_VER = 26
    REMOTE_CTRL_CONN = 27
    PAIR_STATE2 = 28
    WLAN_SSID = 29
    AP_SSID = 30
    APP_COUNT = 31
    PREVIEW_ENABLED = 32
    SD_STATUS = 33
    PHOTOS_REM = 34
    VIDEO_REM = 35
    NUM_GROUP_PHOTO = 36
    NUM_GROUP_VIDEO = 37
    NUM_TOTAL_PHOTO = 38
    NUM_TOTAL_VIDEO = 39
    DATE_TIME = 40
    OTA_STAT = 41
    DOWNLAD_CANCEL_PEND = 42
    MODE_GROUP = 43
    LOCATE_ACTIVE = 45
    INTERNAL_46 = 46
    INTERNAL_47 = 47
    INTERNAL_48 = 48
    MULTI_COUNT_DOWN = 49
    SPACE_REM = 54
    STREAMING_SUPP = 55
    WIFI_BARS = 56
    CURRENT_TIME_MS = 57
    NUM_HILIGHTS = 58
    LAST_HILIGHT = 59
    NEXT_POLL = 60
    ANALYTICS_RDY = 61
    ANALYTICS_SIZE = 62
    IN_CONTEXT_MENU = 63
    TIMELAPSE_REM = 64
    EXPOSURE_TYPE = 65
    EXPOSURE_X = 66
    EXPOSURE_Y = 67
    GPS_STAT = 68
    AP_STATE = 69
    INT_BATT_PER = 70
    ACC_MIC_STAT = 74
    DIGITAL_ZOOM = 75
    WIRELESS_BAND = 76
    DIG_ZOOM_ACTIVE = 77
    MOBILE_VIDEO = 78
    FIRST_TIME = 79
    SEC_SD_STAT = 80
    BAND_5GHZ_AVAIL = 81
    SYSTEM_READY = 82
    BATT_OK_OTA = 83
    CAPTURE_DELAY = 84
    VIDEO_LOW_TEMP = 85
    ORIENTATION = 86
    THERMAL_MIT_MODE = 87
    ZOOM_ENCODING = 88
    FLATMODE_ID = 89
    INTERNAL_90 = 90
    LOGS_READY = 91
    TIMEWARP_1X_ACTIVE = 92
    VIDEO_PRESETS = 93
    PHOTO_PRESETS = 94
    TIMELAPSE_PRESETS = 95
    PRESETS_GROUP = 96
    ACTIVE_PRESET = 97
    PRESET_MODIFIED = 98
    LIVE_BURST_REM = 99
    LIVE_BURST_TOTAL = 100
    CAPT_DELAY_ACTIVE = 101
    MEDIA_MOD_MIC_STAT = 102
    TIMEWARP_SPEED_RAMP = 103
    LINUX_CORE_ACTIVE = 104
    CAMERA_LENS_TYPE = 105
    VIDEO_HINDSIGHT = 106
    SCHEDULED_PRESET = 107
    SCHEDULED_CAPTURE = 108
    CREATING_PRESET = 109
    MEDIA_MOD_STAT = 110
    TURBO_MODE = 113


ProducerType = Tuple[QueryCmdId, Union[SettingId, StatusId]]
"""Types that can be registered for."""

CmdType = Union[CmdId, QueryCmdId, ActionId]
"""Types that identify a command."""

ResponseType = Union[CmdType, StatusId, SettingId, UUID, str, construct.Enum]
"""Types that are used to identify a response."""